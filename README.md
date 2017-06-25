# Twitter-Robot-Detection

Politicians around the world inflates their popularity by social media metrics, to give an example
let's say we have a politician that we'll call Napoleon and other one we refer as Squealer (the names
were randomly assigned), Napoleon and Squealer both have an account on Twitter, they talk about really
important things on their tweets, but the impact they cause in the people is directly proportional to the
popularity of their tweets. What would happend if Napoleon wrote lies in his tweets? What will happend if some
untruthful tweet gain popularity in the network and many people see it, maybe the audience will believe blindly in
this information.

Napoleon and Squealer both have a way to inflate their tweets popularity by creating fake accounts on the 
network, and making this fake accounts to retweet or like their tweets. This project is an attempt to find 
who Napoleon or Squealer have created more fake accounts.

## The Robot Search Process

What do you need to know:

* [MongoDb](https://www.mongodb.com/)
* [Python](https://www.python.org/)
* A [Twitter](https://twitter.com/) account

### The Components

* **tweet_retriever.py** is a python script that reads a file called properties.json (see below for details),
this scripts searches for tweets with specific characteristics as mentions for some accounts and some keywords in the tweet content, it use the [Twitter Search API](https://dev.twitter.com/rest/public/search). In order to use the script you must generate your own bearer token, [here](https://dev.twitter.com/oauth/application-only) you can find the instructions, possible (as it happend to me) you will face a common problem obtaining the token, so here i let a useful [link](https://stackoverflow.com/questions/23183050/twitter-1-1-oauth-authenticity-token-error99).

* **properties.json** is a file readed by the previous script, is a json structure to define the search parameters or the script, it contains a list of **characters**, each character has three properties: **account** where you must put the twitter account you are interested; **sinceId** which represent a tweet id to begin the search, each tweet is identified by this id, so when you perform a search the script will retrieve all the tweets whose id is bigger than sinceId, you must set this property to 0 and don't worry about several executions, the script will update this field automatically. Finally the **subject** is a string to define the keywords that you want to be present in the tweets, see the twitter api documentation to learn how to create more advanced queries. I provide a properties_bk.json file that you can modify according to your needs, remember to rename it to **properties.json** and place it in the same path as the tweet_retriever.py.

* **tweetLoader.py** is a python script to insert your tweets in a MongoDb collection.

### Execution

Once you configure your properties.json you must run the tweet_retriever.py script, you may face some troubles for missing python modules, remember to use pip or your favourite package manager to install the missing modules. The script will create one file per character in the properties.json, each file stores the retrieved tweets. I recommend to run the script periodically, maybe one time per hour will be okey, remember you have some restrictions for the use of the api, and if you perform two search within a small window of time, the chance of find new tweets will be minimal.

When you finished the process of tweets recolection, it's time to load the tweets on a MongoDb collection, the easiest way is to use the [Mongo Shell](https://docs.mongodb.com/getting-started/shell/client/), first you need to create a database and then a collection inside the new database. Then, use the tweetLoader.py to load the tweets, you need to specify the file path and the run the script, one time per file created by the tweet_retriever.py.

I wanted to find those account with little number of followers but great number of favourites tweets, so i use the following Mongo query:



