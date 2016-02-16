# coding: utf-8
import nltk
import random
from nltk.corpus import names
from nltk.corpus import movie_reviews
from nltk.corpus import brown
import pprint

pp = pprint.PrettyPrinter(indent=4)


# -----------------------------------------
# 6.1.1 性別の決定
"""
def gender_features(word):
    return {'last_letter': word[-1]}

# print gender_features('Sherk')

_names = (
        [(name, 'male') for name in names.words('male.txt')] +
        [(name, 'female') for name in names.words('female.txt')]
    )
random.shuffle(_names)
# print _names[:10]

featuresets = [(gender_features(n), g) for (n, g) in _names]
train_set, test_set = featuresets[:500], featuresets[500:]
classifier = nltk.NaiveBayesClassifier.train(train_set)

# print classifier.classify(gender_features('Neo'))
# print classifier.classify(gender_features('Trinity'))
print nltk.classify.accuracy(classifier, test_set)
"""


# -----------------------------------------
# 6.1.3 文書の分類
# 例6-2
# 例6-3
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
        features['contains(%s)' % word] = (word in document_words) # TODO: この文法がよく分からない
    return features

# print document_features(movie_reviews.words('pos/cv957_8737.txt'))

featuresets = [(document_features(d), c) for (d, c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print nltk.classify.accuracy(classifier, test_set) # TODO:実行される度にこの結果がかわるのはなぜか
classifier.show_most_informative_features(5)
"""


# -----------------------------------------
# 6.1.4 品詞のタグ付け
"""
suffix_fdist = nltk.FreqDist()
for word in brown.words():
    word = word.lower()
    suffix_fdist.inc(word[-1:])
    suffix_fdist.inc(word[-2:])
    suffix_fdist.inc(word[-3:])

common_suffixes = suffix_fdist.keys()[:100]
print common_suffixes

def pos_features(word):
    features = {}
    for suffix in common_suffixes:
        features['endswith(%s)' % suffix] = word.lower().endswith(suffix)

tagged_words = brown.tagged_words(categories='news')
featuresets = [(pos_features(n), g) for (n, g) in tagged_words]

size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]

classifier = nltk.DecisionTreeClassifier.train(train_set)
nltk.classify.accuracy(classifier, test_set)
"""


# -----------------------------------------
# 6.1.5 品詞のタグ付け
"""
def pos_features(sentence, i):
    features = {
        "suffix(1)": sentence[i][-1:],
        "suffix(2)": sentence[i][-2:],
        "suffix(3)": sentence[i][-3:]
    }
    if i == 0:
        features['prev-word'] = '<START>'
    else:
        features['prev-word'] = sentence[i-1]
    return features

pp.pprint(pos_features(brown.sents()[0], 8))
tagged_sents = brown.tagged_sents(categories='news')
featuresets = []
for tagged_sent in tagged_sents:
    untagged_sent = nltk.tag.untag(tagged_sent)
    for i, (word, tag) in enumerate(tagged_sent):
        featuresets.append( (pos_features(untagged_sent, i), tag) )

size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print nltk.classify.accuracy(classifier, test_set)
"""



# -----------------------------------------
# 6.2.1 文分割
"""
    sents = nltk.corpus.treebank_raw.sents()
    tokens = []
    boundaries = set()
    offset = 0
    for sent in sents:
        tokens.extend(sent)
        offset += len(sent)
        boundaries.add(offset-1)

    def punct_features(token, i):
        return { 'next-word-capidalized': tokens[i+1][0].isupper(),
                'prevword': tokens[i-1].lower(),
                'punct': tokens[i],
                'prev-word-is-one-char': len(tokens[i-1]) == 1 }

        featuresets = [(punct_features(tokens, i), (i in boundaries))
                for i in range (1, len(tokens)-1)
                if tokens[i] in '.?!']

        size = int(len(featuresets) * 0.1)
    train_set, test_set = featuresets[:size], featuresets[size:]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print nltk.classify.accuracy(classifier, test_set)

    def segment_sentences(words):
        start = 0
        sents = []
        for i, word in enumerate(words):
            if word in '.?!' and classifier.classify(punct_features(word, i) == True):
                sents.append(words[start:i+1])
                start = i+1
        if start < len(words):
            sents.append(words[start:])
        return
"""




# -----------------------------------------
# 
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
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print nltk.classify.accuracy(classifier, test_set) # TODO:実行される度にこの結果がかわるのはなぜか
classifier.show_most_informative_features(5)
