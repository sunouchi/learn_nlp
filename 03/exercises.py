# coding: utf-8
import nltk
import urllib
import urllib2
import lxml.html
import re
from bs4 import BeautifulSoup
from nltk.corpus import gutenberg


# ==================================================================================
# 難度1
# ==================================================================================
# -----------------------------------------
# 1
# def main():
#     s = 'colorless'
#     s = s[:4] + 'u' + s[4:]
#     print s


# -----------------------------------------
# 2
# def main():
#     print 'dishes'[:-2]
#     print 'running'[:-4]
#     print 'nationality'[:-5]
#     print 'undo'[:-2]
#     print 'preheat'[:-4]


# -----------------------------------------
# 6
# 以下の正規表現がどんな文字列にマッチするのかを説明してみよう。
# a. [a-zA-Z]+ // すべてのアルファベットにマッチする1つの文字
# b. [A-Za-z]*　// すべてのアルファベットにマッチする1つ以上の文字
# c. p[aeiou]{,2}t //pait, peet, poutなど
# d. \d+(\.\d+)? // 0.245, 0.1, 0.1873とか
# e. ([^aeiou][aeiou][^aeiou])* // 9a8, can, bo0とか
# f. \w+|[^\w\s]+ // 文字、あるいは文字とスペース以外のなにかの、1文字以上の文字列
# def main():
#     text = '01234567890789654312'
#     pattern = re.compile('^0.*?4')
#     matchObj = pattern.match(text)
#     if matchObj:
#         print matchObj.group()


# -----------------------------------------
# 10
# def main():
#     sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
#     result = []
#     for word in sent:
#         word_len = (word, len(word))
#         result.append(word_len)
#     print result

#     print [(w, len(w)) for w in sent]


# -----------------------------------------
# 11
# def main():
#     raw = 'I ate breads and chocolates this morning.'
#     words = []
#     last = 0
#     for i in range(len(raw)):
#         if raw[i] == 's':
#             words.append(raw[last:i+1])
#             last = i+1
#     words.append(raw[last:])
#     print words


# -----------------------------------------
# 14
# def main():
#     # sorted(words)はもとの配列がそのままであるのに対して、words.sort()は元の配列の順分が入れ替わる破壊的メソッドである
#     words = ['shibuya', 'akasaka', 'roppongi', 'ebisu', 'shinjuku', 'tokyo', 'ueno']
#     sorted(words)
#     print words

#     words.sort()
#     print words


# ==================================================================================
# 難度2
# ==================================================================================
# -----------------------------------------
# 18
# def main():
#     words = gutenberg.raw('austen-emma.txt')
#     words_tokenize = nltk.word_tokenize(words)
#     print sorted(set([w for w in words_tokenize if w.startswith('wh')]))


# -----------------------------------------
# 19
# def main():
#     lines = open('exercises.txt', 'r').readlines()
#     array = []
#     last = 0
#     for i, line in enumerate(lines):
#         array.append([])
#         for j in range(len(line)):
#             if line[j] == ' ' or line[j] == '\n' or line[j] == '\r\n':
#                 array[i].append(line[last:j])
#                 last = j+1
#         last = 0
#     print array


# -----------------------------------------
# 23
# 「don't」が「do」と「n't」にトークン化できる正規表現が書けるだろうか。また、<<n't|\w+>>という正規表現は正しく動作しないのだが、それはなぜだろうか。理由を説明してみよう。
# def main():


main()
