import random
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter


class FirestoreHelper:
    def __init__(self, credentials_file_path, collection_name, document_field_name, count_collection_name, count_document_field_name):
        """
        Initialize the FirestoreHelper.

        Args:
            credentials_file_path (str): The path to the Firebase credentials file.
            collection_name (str): The name of the collection to operate on.
            document_field_name (str): The name of the field containing document data.
            count_collection_name (str): The name of the collection containing count data.
            count_document_field_name (str): The name of the field containing the document count.

        Description:
            This class helps interact with Firestore database.
        """
        self.credentials_file_path = credentials_file_path
        self.collection_name = collection_name
        self.document_field_name = document_field_name
        self.count_collection_name = count_collection_name
        self.count_document_field_name = count_document_field_name
        self.db = self.initialize_firestore()

    def initialize_firestore(self):
        """
        Initialize Firestore client.

        Returns:
            firebase_admin.firestore.Client: The Firestore client instance.

        Description:
            This method initializes and returns the Firestore client using the provided credentials.
        """
        cred = credentials.Certificate(self.credentials_file_path)
        app = firebase_admin.initialize_app(cred)
        db = firestore.client(app=app)
        return db

    def get_random_document(self):
        """
        Retrieve a random document from the collection.

        Returns:
            dict: A dictionary representing the document.

        Description:
            This method fetches a random document from the collection based on document count.
        """
        count = self.get_document_count()
        random_number = random.randint(0, count - 1)
        documents = self.db.collection(self.collection_name).where(
            FieldFilter('index', '==', random_number)).stream()
        for document in documents:
            doc_dict = document.to_dict()
            return doc_dict[self.document_field_name]

    def get_document_count(self):
        """
        Get the count of documents in a collection.

        Returns:
            int: The count of documents.

        Description:
            This method retrieves the count of documents in a specified collection.
        """
        doc_ref = self.db.collection(self.count_collection_name).document(
            self.count_document_field_name)
        doc = doc_ref.get()
        if doc.exists:
            doc_dict = doc.to_dict()
            return doc_dict[self.count_document_field_name]
        else:
            print('No such document!')
            return 0

    def delete_document(self, document_content, collection_to_delete_from):
        """
        Delete a document from a collection.

        Args:
            document_content (str): The content of the document to delete.
            collection_to_delete_from (str): The name of the collection to delete from.

        Description:
            This method deletes a document from the specified collection based on its content.
        """
        document_id = self.get_document_id(document_content)
        if document_id:
            self.db.collection(collection_to_delete_from).document(
                document_id).delete()
        else:
            print("Document doesn't exist")

    def get_document_id(self, document_content):
        """
        Get the ID of a document based on its content.

        Args:
            document_content (str): The content of the document.

        Returns:
            str: The ID of the document.

        Description:
            This method retrieves the ID of a document based on its content. 
            You need to implement this function based on your document structure.
        """
        pass
