'''
Get tweets based on Ids

version 1.0
'''



import tweepy
#nesseracy API tokens
API_key = "XXXX"
API_key_secret = "XXX"
bearer_token = "XXX"

client = tweepy.Client(bearer_token=bearer_token)

file_name = 'tweets.txt'

#this could be given as an argument in a CLI, or imported as an excel file or whatever
id_list = ["1562422383612669952", "1562420114930241536"]

with open(file_name, 'a+', encoding="utf-8") as filehandle:
    #call the get tweets method
    response = client.get_tweets(id_list)
    #write each tweet nicely in a .txt file, could be CSV file instead
    for tweet in response.data:
        filehandle.write('%s\t%s\n\n' % (tweet.id, tweet.text))