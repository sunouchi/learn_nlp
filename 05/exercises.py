# coding: utf-8
import nltk
import re
from bs4 import BeautifulSoup
from nltk.corpus import brown

"""
ëy¶È1
"""
# -----------------------------------------
# def main():
#     """
#     3
#     """
#     text = "The wind back the clock, while we chase after the wind"
#     token = nltk.word_tokenize(text)
#     print nltk.pos_tag(token)

# -----------------------------------------
# def main():
#     """
#     5
#     """
#     d = {
#         'banana': 'yellow',
#         'lime': 'green',
#         'grape': 'purple',
#         'apple': 'red'
#     }
#     print d['banana']
#     print d['xyz']

# -----------------------------------------
# def main():
#     """
#     10
#     """
#     text = "The wind back the clock, while we chase after the wind"
#     token = nltk.word_tokenize(text)
#     tagger = nltk.UnigramTagger(brown.tagged_sents(categories='news'))
#     print tagger.tag(token)

# -----------------------------------------
# def main():
#     """
#     12
#     """
#     brown_tagged_sents = brown.tagged_sents(categories='news')
#     brown_sents = brown.sents(categories='news')
#     size = int(len(brown_tagged_sents) * .9)
#     train_sents = brown_tagged_sents[:size]
#     test_sents = brown_tagged_sents[size:]
#     bigram_tagger = nltk.BigramTagger(train_sents)
#     print bigram_tagger.evaluate(test_sents)

# -----------------------------------------
def main():
    """
    14
    """
    brown_tagged_words = brown.tagged_words()
    print sorted(set([tag for (word, tag) in brown_tagged_words]))


main()
