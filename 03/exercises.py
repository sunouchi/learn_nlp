# coding: utf-8
import nltk
import urllib
import urllib2
import lxml.html
import re
from bs4 import BeautifulSoup
from nltk.corpus import gutenberg


# ==================================================================================
# �y��1
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
# ���¤���Ҏ��F���ɤ�������Ф˥ޥå�����Τ����h�����Ƥߤ褦��
# a. [a-zA-Z]+ // ���٤ƤΥ���ե��٥åȤ˥ޥå�����1�Ĥ�����
# b. [A-Za-z]*��// ���٤ƤΥ���ե��٥åȤ˥ޥå�����1�����Ϥ�����
# c. p[aeiou]{,2}t //pait, peet, pout�ʤ�
# d. \d+(\.\d+)? // 0.245, 0.1, 0.1873�Ȥ�
# e. ([^aeiou][aeiou][^aeiou])* // 9a8, can, bo0�Ȥ�
# f. \w+|[^\w\s]+ // ���֡����뤤�����֤ȥ��ک`������Τʤˤ��Ρ�1�������Ϥ�������
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
#     # sorted(words)�Ϥ�Ȥ����Ф����ΤޤޤǤ���Τˌ����ơ�words.sort()��Ԫ�����Ф�혷֤���������Ɖ��ĥ᥽�åɤǤ���
#     words = ['shibuya', 'akasaka', 'roppongi', 'ebisu', 'shinjuku', 'tokyo', 'ueno']
#     sorted(words)
#     print words

#     words.sort()
#     print words


# ==================================================================================
# �y��2
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
# ��don't������do���ȡ�n't���˥ȩ`���󻯤Ǥ�����Ҏ��F����������������ޤ���<<n't|\w+>>�Ȥ�����Ҏ��F���������������ʤ��Τ���������Ϥʤ������������ɤ��h�����Ƥߤ褦��
# def main():


main()
