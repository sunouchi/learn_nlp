# coding: utf-8
import nltk
import re
from nltk.corpus import brown


brown_tagged_words = brown.tagged_words(categories='humor')

def main():
    print get_largest_tag()


# def a():
    # words = [word for (word, tag) in brown_tagged_words if tag=='NN']
    # result = sorted(set([w for w in words if w.endswith('s')]))
    # print result
    # print len(result)


def get_largest_tag():
    """
    b
    """
    # fd = nltk.FreqDist(brown_tagged_words)
    # return fd.max()
    # max = fd.max()
    # print fd.keys()[:10]
    # print fd.keys()

    # def findtags(tag_prefix, tagged_text):
    #     cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text
    #                                    if tag.startswith(tag_prefix))
    #     print cfd.conditions()
    #     return dict((tag, cfd[tag].keys()[:5]) for tag in cfd.conditions())

    # tagdict = findtags('NN', nltk.corpus.brown.tagged_words(categories='news'))
    # for tag in sorted(tagdict):
    #     print tag, tagdict[tag]


main()
