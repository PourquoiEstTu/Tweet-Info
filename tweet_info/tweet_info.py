import json
from string import punctuation

#all functions take at the very least a json file as input

#counts the amount of tweets sent on every day of the month 
def tweets_per_day(jsonurl):
    tweetDict = {}
    with open(jsonurl, 'r', encoding = 'utf-8') as fh :
        #s = fh.read()
        content = json.loads(fh.read()) 

        #print(content) 
        for subDict in content :
            if int(subDict["Tweet Posted Time (UTC)"][:2]) in tweetDict :
                tweetDict[int(subDict["Tweet Posted Time (UTC)"][:2])] += 1
            else :
                tweetDict[int(subDict["Tweet Posted Time (UTC)"][:2])] = 1
        
        return tweetDict

#counts the number of times an inputted word appears in given tweets
def count_occurences(jsonurl, word):
    with open(jsonurl, 'r', encoding="utf-8") as fh :
        content = json.loads(fh.read())

        
        for subDict in content :
            for char in subDict["Tweet Content"] :
                for punc in punctuation :
                    if char == punc :
                        subDict["Tweet Content"] = subDict["Tweet Content"].replace(char, '')
        #             elif char == '\n' :
        #                 subDict["Tweet Content"] = subDict["Tweet Content"].replace(char, 'n')
        #             elif char == '\t' :
        #                 subDict["Tweet Content"] = subDict["Tweet Content"].replace(char, 't')

        count = 0
        for subDict in content :
            subDict["Tweet Content"] = subDict["Tweet Content"].split(' ')
            for item in subDict["Tweet Content"] :
                if (' ' + word.lower() + ' ') in (' ' + item.lower() + ' ') :
                    count += 1

    return count  


#counts the number of times a word is tweeted vs. the day of the month
#function is like a combination of the previous two functions
def words_per_day(jsonurl, word):
    tweetDict = {}
    with open(jsonurl, 'r', encoding = 'utf-8') as fh :
        #s = fh.read()
        content = json.loads(fh.read()) 

        for subDict in content :
            for char in subDict["Tweet Content"] :
                for punc in punctuation :
                    if char == punc :
                        subDict["Tweet Content"] = subDict["Tweet Content"].replace(char, '')
        #             elif char == '\n' :
        #                 subDict["Tweet Content"] = subDict["Tweet Content"].replace(char, 'n')
        #             elif char == '\t' :
        #                 subDict["Tweet Content"] = subDict["Tweet Content"].replace(char, 't')
        # #print(content) 
        
        for subDict in content :
            if int(subDict["Tweet Posted Time (UTC)"][:2]) not in tweetDict :
                tweetDict[int(subDict["Tweet Posted Time (UTC)"][:2])] = 0
        #print(tweetDict)

        for subDict in content :
            subDict["Tweet Content"] = subDict["Tweet Content"].split(' ')
            for item in subDict["Tweet Content"] :
                if (' ' + word.lower() + ' ') in (' ' + item.lower() + ' ') :
                    #print(item)
                    tweetDict[int(subDict["Tweet Posted Time (UTC)"][:2])] += 1

    return tweetDict

#print(tweets_per_day("sample_tweets.json"))
#print(count_occurences("sample_tweets.json", "you"))
#print(words_per_day("sample_tweets.json", "you"))