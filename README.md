# Bible Twitter Bot

The Bible Twitter Bot is designed to select a random verse from my Google Cloud database of Bible verses and post them to Twitter using the Twitter API every hour.

## Table of Contents

1. [Installation](#installation)
2. [Configuration](#configuration)
3. [Prerequisites](#prerequisites)
4. [Usage](#usage)
5. [Features](#features)
6. [Production Link](#production-link)
7. [Contact](#contact)
8. [Acknowledgments](#acknowledgments)

## Installation

To set up and utilize the Bible Twitter Bot, follow these steps:

- Install [Python3](https://www.python.org/downloads/)
- Install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- Clone the repository: `git clone https://github.com/elkingarcia11/bible_twitter_bot.git `
- Install dependencies using pip: `pip install -r requirements.txt`

## Configuration

- Configure the environment variables for the project by creating a `.env` file and adding your Twitter API credentials
- Add your Service Account credentials to the `credentials.json` file to connect to Cloud Firestore Database

## Prerequisites

Before running the project, ensure you have the following prerequisites:

- [ ] Python3 installed
- [ ] Git installed
- [ ] Repository cloned
- [ ] Dependencies installed
- [ ] `.env` file created & configured
- [ ] `credentials.json` file created & configured

## Usage

### Development
1. Run the program in the development environment: `python3 main.py`
2. Check the Bot's Twitter Page to verify if a tweet has been posted.
   
### Production

For enhanced stability, deploy this Python program on the Cloud by following these steps:

1. Install Docker on your machine: [Docker Installation](https://docs.docker.com/engine/install/)
2. Build the Docker image of the application.
3. Tag the image with the name of your Artifact Registry project.
4. Push the project image to the Artifact Registry or Container Registry.
5. Deploy an instance of the image using Cloud Run, configured to listen on port 80.
6. Monitor the Bot's Twitter Page for to verify if tweets are posting.

To implement scheduled Tweets:


1. Move Python code to a Cloud Function environment 
2. Create a Pub/Sub topic to send data and trigger the Cloud Function
3. Set the trigger to be the Pub/Sub Topic you created
4. Create a Cloud Scheduler job to post a message to the Pub/Sub Topic you created every X unit of time
5. Monitor the Bot's Twitter Page for to verify if tweets are posting.

## Features

- Posts tweets to the Bot's Twitter Page using Tweepy API (a Python library for interacting with the Twitter API).
- Implements waiting periods to adhere to Twitter rate limits.
- Accesses the Cloud Firestore database (a NoSQL database service provided by Google Cloud).
- Provides functionality to add, delete, and update posts in the database.

### Upcoming Features

- Auto-follow new followers.

### Production Link

Visit [@bible_bihourly](https://twitter.com/bible_bihourly) on Twitter to interact with the bot's posts and page.

## Contact

For questions, feedback, or inquiries, feel free to contact me via email at elkingarcia.11@gmail.com or connect with me on [LinkedIn](https://www.linkedin.com/in/elkingarcia11/)

## Acknowledgments

- Special thanks to Tweepy for providing an accessible Python library for interacting with the Twitter API.
- Gratitude to the [King JSON Bible](https://github.com/brendancol/king-json-bible) repository for providing the collection of verses used in this project. JSON files for specific books, verses, chapters, and texts were sourced from this repository.
