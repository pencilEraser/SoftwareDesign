# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 16:20:23 2014

PROVIDED UNDER NO LICENSE.  NO WARRANTY PROVIDED OR IMPLIED.
USE AT YOUR OWN RISK.

Pie chart code modified from example at http://matplotlib.org/examples/pie_and_polar_charts/pie_demo_features.html
Bar plot code modified from example at http://wiki.scipy.org/Cookbook/Matplotlib/BarCharts

@author: neal
"""

from pattern.web import Twitter
import pickle
from pattern.web.locale import geocode 
from pattern.en import *
import matplotlib.pyplot as plt



def automate_data_collection():
    """
    Automatically collects data for the listed cities and Twitter search terms.
    Inputs: none, but uses the lists cities and search_terms to automatically run
    the function search_with_language_in_region().
    
    Outputs: the collected data, saved to disk as pickle files of the format
    city_searchterm_secondTermIfApplicable.pickle.
    """
    
    cities = ['Paris', 'Brussels', 'Berlin', 'Kiev', 'Moscow']
    search_terms = ['obama', 'putin', ['obama', 'crimea'], ['putin', 'crimea']]
    for city in cities:
        for term in search_terms:        
            search_with_language_in_region('en', city, term, city + '_' + term)



def automate_sentiment_analysis():
    """
    Automatically does sentiment analysis of data
    Inputs: none, but assumes that data has already been collected and saved to disk for
    the cities and search terms below

    Outputs: a dictionary of of data for the cities and search terms.  Dictionary 
    key is city_searchTerm_secondTermIfApplicable
    See semantic_analysis() for further details.
    
    """
    
    cities = ['Paris', 'Brussels', 'Berlin', 'Kiev', 'Moscow']
    search_terms = ['obama', 'putin', ['obama', 'crimea'], ['putin', 'crimea']]
    city_tweet_data = {}    
    
    for city in cities:
        for term in search_terms:        
            city_tweet_data[city + '_' + term] = semantic_analysis(city + '_' + term)    
    return city_tweet_data



def search_with_language_in_region(lang, capital_city, search_terms, file_name):
    """
    Does a twitter search in the specified language in the area of a given capital city
    e.g. search_with_language_in_region('en', 'Paris', '#yoloswag', 'Paris_yoloswag')
    
    Inputs: expects strings for everything.
        lang: the language you want to search in [string], e.g. 'en'
        capital_city: the city you want to search around, found 
        through pattern's geocode function,  e.g. 'Paris'
        search_terms: duh. e.g. ['crimea','putin']
        file_name: the file name you want to save the tweets as, will come out as e.g. nealiscool.pickle
    
    Outputs: a pickled dictionary of the tweets, which are saved on disk as tweets_gathered.pickle.
    The keys of the dicitonary are the unique tweet IDs.
    """
    t = Twitter(language=lang)
    tweets_gathered = {}
    i = None
    for j in range(2):
        for tweet in t.search(search_terms, start=i, count=10,geo=geocode(capital_city)[:2]):
            print tweet.text
            print
            i = tweet.id
            tweets_gathered[tweet.id] = tweet.text
    f = open(file_name,'w')   
    pickle.dump(tweets_gathered,f)
    f.close()
    
    
    
def semantic_analysis(pickled_tweet_data_filename):
    """
    Does semantic analysis (using pattern's built-in semantic analysis tools) of the data provided to it.
    
    Inputs: pickled_tweet_data_filename
    Expects pickled_tweet_data_filename to be a string,
    and assumes the data at that filename is a pickled dict.
    
    Outputs a list of [number of positive tweets, number of negative tweets]
    
    """
    input_file = open(pickled_tweet_data_filename,'r')
    tweet_dict = pickle.load(input_file)
    input_file.close()
    running_count = 0.0
    average_polarity = 0.0
    average_subjectivity = 0.0
    neg_count = 0
    pos_count = 0
    for tweet_id in tweet_dict.keys():
        average_polarity += sentiment(tweet_dict[tweet_id])[0]
        average_subjectivity += sentiment(tweet_dict[tweet_id])[1]
        running_count += 1        
        print sentiment(tweet_dict[tweet_id])
        if sentiment(tweet_dict[tweet_id])[0] > 0.0 or sentiment(tweet_dict[tweet_id])[0] < 0.0:
            if sentiment(tweet_dict[tweet_id])[0] < 0.3:
                neg_count += 1
            else:
                pos_count += 1
    #print running_count
    #print average_polarity / running_count   
    #print average_subjectivity / running_count       
    print    
    print pickled_tweet_data_filename, ":"
    print "pos count: " 
    print pos_count 
    print "neg count: " 
    print neg_count
    print "-----------"
    print
    return [pos_count, neg_count]




#### Globally define the font for use in the plotting functions below ####
font = {'family' : 'serif',
        'color'  : 'darkblue',
        'weight' : 'normal',
        'size'   : 16,
        }



def make_pie_chart_putin(city_tweet_data_dict):
    """
    Creates a pie chart which shows the relative percentages of positive tweets
    for each city, with respect to the search term "Putin."
    Inputs: a dictionary containing the tweet data by city and topic 
    
    Outputs: displays a pie chart of the data.
    
    """    
    cities = ['Paris', 'Brussels', 'Berlin', 'Kiev', 'Moscow']
    positive_tweets_total = 0
    positive_paris = city_tweet_data_dict['Paris_putin'][0]
    positive_brussels  = city_tweet_data_dict['Brussels_putin'][0]
    positive_berlin  = city_tweet_data_dict['Berlin_putin'][0]
    positive_kiev  = city_tweet_data_dict['Kiev_putin'][0]
    positive_moscow  = city_tweet_data_dict['Moscow_putin'][0]
    
    for city in cities:
        positive_tweets_total += city_tweet_data_dict[city + '_putin'][0]

    # The slices will be ordered and plotted counter-clockwise.
    labels = 'Paris', 'Brussels', 'Berlin', 'Kiev', 'Moscow'
    sizes = [positive_paris, positive_brussels, positive_berlin, positive_kiev, positive_moscow]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'red']
    explode = (0.1, 0, 0, 0, 0) # only "explode" the 1st slice (i.e. 'Paris')
    
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.text(0.3, 1.3, r'Total positive tweets: ' + str(positive_tweets_total), fontdict=font)
    plt.title('Cities with most positive attitude towards Putin', fontdict=font)
    #plt.subplots_adjust(right=0.15)
    plt.axis('equal')
    plt.show()



def make_pie_chart_obama(city_tweet_data_dict):
    """
    Creates a pie chart which shows the relative percentages of positive tweets
    for each city, with respect to the search term "Obama."
    Inputs: a dictionary containing the tweet data by city and topic 
    
    Outputs: displays a pie chart of the data.
    
    """    
    cities = ['Paris', 'Brussels', 'Berlin', 'Kiev', 'Moscow']
    positive_tweets_total = 0
    positive_paris = city_tweet_data_dict['Paris_obama'][0]
    positive_brussels  = city_tweet_data_dict['Brussels_obama'][0]
    positive_berlin  = city_tweet_data_dict['Berlin_obama'][0]
    positive_kiev  = city_tweet_data_dict['Kiev_obama'][0]
    positive_moscow  = city_tweet_data_dict['Moscow_obama'][0]
    
    for city in cities:
        positive_tweets_total += city_tweet_data_dict[city + '_obama'][0]

    # The slices will be ordered and plotted counter-clockwise.
    labels = 'Paris', 'Brussels', 'Berlin', 'Kiev', 'Moscow'
    sizes = [positive_paris, positive_brussels, positive_berlin, positive_kiev, positive_moscow]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'red']
    explode = (0.1, 0, 0, 0, 0) # only "explode" the 1st slice (i.e. 'Paris')
    
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.text(0.3, 1.1, r'Total positive tweets: ' + str(positive_tweets_total), fontdict=font)
    plt.title('Cities with most positive attitude towards Obama', fontdict=font)
    plt.subplots_adjust(left=0.2)
    plt.axis('equal')
    plt.show()



def barplot_obama_crimea(city_tweet_data_dict):
    """
    Creates a bar plot which shows the number of positive and negative tweets
    for each city, with respect to the search term "Obama Crimea."
    Inputs: a dictionary containing the tweet data by city and topic 
    
    Outputs: displays a plot of the data.
    
    """        
    
    N = 5
    
    positive_tweets = []
    negative_tweets = []
    cities = ['Paris', 'Brussels', 'Berlin', 'Kiev', 'Moscow']
    i = 0
    for i in range(len(cities)):
        positive_tweets.append( city_tweet_data_dict[cities[i] + '_obama_crimea'][0])
        negative_tweets.append(-1*city_tweet_data_dict[cities[i] + '_obama_crimea'][1])

    ind = np.arange(N)    # the x locations for the groups
    width = 0.35       # the width of the bars: can also be len(x) sequence
    
    p1 = plt.bar(ind, positive_tweets,   width, color='b')
    p2 = plt.bar(ind, negative_tweets, width, color='r')
    
    plt.ylabel('No. of Tweets for each sentiment (pos/neg)')
    plt.title('Data per city for terms "Obama Crimea"')
    plt.xticks(ind+width/2., cities )
    plt.yticks(np.arange(-13,10,2))
    plt.legend( (p1[0], p2[0]), ('Positive', 'Negative') )
    
    plt.show()



def barplot_putin_crimea(city_tweet_data_dict):
    """
    Creates a bar plot which shows the number of positive and negative tweets
    for each city, with respect to the search term "Putin Crimea."
    Inputs: a dictionary containing the tweet data by city and topic 
    
    Outputs: displays a plot of the data.
    
    """    
    
    N = 5
    
    positive_tweets = []
    negative_tweets = []
    cities = ['Paris', 'Brussels', 'Berlin', 'Kiev', 'Moscow']
    i = 0
    for i in range(len(cities)):
        positive_tweets.append( city_tweet_data_dict[cities[i] + '_putin_crimea'][0])
        negative_tweets.append(-1*city_tweet_data_dict[cities[i] + '_putin_crimea'][1])
    
    ind = np.arange(N)    # the x locations for the groups
    width = 0.35       # the width of the bars: can also be len(x) sequence
    
    p1 = plt.bar(ind, positive_tweets,   width, color='b')
    p2 = plt.bar(ind, negative_tweets, width, color='r')
    
    plt.ylabel('No. of Tweets for each sentiment (pos/neg)')
    plt.title('Data per city for terms "Putin Crimea"')
    plt.xticks(ind+width/2., cities )
    plt.yticks(np.arange(-13,10,2))
    plt.legend( (p1[0], p2[0]), ('Positive', 'Negative') )
    
    plt.show()



