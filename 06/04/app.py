# coding: utf-8
import nltk
import random
from nltk.corpus import movie_reviews
from nltk.corpus import brown
import pprint

pp = pprint.PrettyPrinter(indent=4)

"""
documents = [(list(movie_reviews.words(fileid)), category)
            for category in movie_reviews.categories()
            for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = all_words.keys()[:2000]

def document_features(document):
    document_words = set(document)
    features = {}        
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words) 
        # features['contains(%s)' % word] = (word in document_words) # TODO: この文法がよく分からない
    return features

# print document_features(movie_reviews.words('pos/cv957_8737.txt'))

featuresets = [(document_features(d), c) for (d, c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print nltk.classify.accuracy(classifier, test_set) # TODO:実行される度にこの結果がかわるのはなぜか
classifier.show_most_informative_features(30)
"""

# print nltk.classify.accuracy(classifier, test_set)



documents = [(list(movie_reviews.words(fileid)), category)
            for category in movie_reviews.categories()
            for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = all_words.keys()[:2000]

def document_features(document):
    document_words = set(document)
    features = {}        
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words) # TODO: この文法がよく分からない
    return features

# print document_features(movie_reviews.words('pos/cv957_8737.txt'))

featuresets = [(document_features(d), c) for (d, c) in documents]
print len(featuresets)
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)

# import pdb; pdb.set_trace()

print nltk.classify.accuracy(classifier, test_set) # TODO:実行される度にこの結果がかわるのはなぜか
classifier.show_most_informative_features(30)
