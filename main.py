from twitter_client import TwitterClient
from firestore_helper import FirestoreHelper


def main():
    # Get random document from firestore database
    firestore_helper = FirestoreHelper()
    random_document = firestore_helper.get_random_document()

    # Twitter client
    #client = TwitterClient()

    # If random document exists, print and tweet it
    if random_document:

        sentence = f"\"{random_document['text']}\" - {random_document['source']}"
        print("Randomly selected document:", sentence)
        # Assuming tweet_text is the method to post a tweet
        #client.tweet_text(random_document)
    else:
        print("No document available in the collection.")

if __name__ == "__main__":
    main()
