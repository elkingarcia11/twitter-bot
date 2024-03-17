from twitter_client import TwitterClient
from firestore_helper import FirestoreHelper


def main():
    # Configure Database details:
    credentials_file_path = 'credentials.json'
    collection_name = 'verses'
    document_field_name = 'text'
    count_collection_name = 'count'
    count_document_field_name = 'count'

    # Initialize Firestore connection with configuration
    firestore_helper = FirestoreHelper(credentials_file_path, collection_name,
                                       document_field_name, count_collection_name, count_document_field_name)

    # Get random document from firestore database
    random_document = firestore_helper.get_random_document()

    # Twitter client
    client = TwitterClient()

    # If random document exists, print and tweet it
    if random_document:
        print("Randomly selected document:", random_document)
        # Assuming tweet_text is the method to post a tweet
        client.tweet_text(random_document)
    else:
        print("No document available in the collection.")


if __name__ == "__main__":
    main()
