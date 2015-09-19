# coding: utf-8
import re
from nltk.corpus import gutenberg


# -----------------------------------------
# 38
# トークン化に関する興味深い課題の1つに、改行によって分割された単語がある。たとえば「long-term」という単語が分割されれば、long-\ntermという文字列となる。
#   a. 改行を挟んでハイフンでつながっている単語を識別する正規表現を書いてみよう。この正規表現では\n文字を使う必要があるだろう。
#   b. re.sub()を用いて、それらの単語から\n文字を削除してみよう。
#   c. 'encyclo-\npedia'のように、改行を削除した後にハイフンを削除しなければならない単語を識別するにはどうすれば良いだろうか。
def isHyphenated(word):
    pattern = re.compile('-\n')
    if pattern.findall(word):
        return True
    else:
        return False


def removeBreak(word):
    pattern = re.compile('-\n')
    repl = '-'
    return re.sub(pattern, repl, word)


def getCorrectWord(word):
    str = re.sub(re.compile('-\n'), '', word)
    words = gutenberg.words('austen-emma.txt')
    # print sorted(set([w.lower() for w in words]))
    # print len(sorted(set([w.lower() for w in words])))
    isExist = False
    for w in words:
        # print '...' + str + '...', w
        if str == w:
            return w
        # break
    # print ' all done.'
    if isExist is False:
        return removeBreak(word)


def main():
    # a.
    # word = 'long-\nterm'
    # print isHyphenated(word)

    # b.
    # word = 'long-\nterm'
    # print removeBreak(word)

    # c.
    # word = 'wretch-\nedest'
    word = 'encyclo-\npedia'
    print getCorrectWord(word)


main()
