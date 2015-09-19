# coding: utf-8
import nltk
import pprint
from nltk.corpus import brown


# -----------------------------------------
# 3.6.1 ステマー
# 例3-1 ステマーを用いたテキストのインデックス構築
class IndexedText(object):
    def __init__(self, stemmer, text):
        self._text = text
        self._stemmer = stemmer
        self._index = nltk.Index((self._stem(word), i)
                      for i, word in enumerate(text))
    def concordance(self, word, width=40):
        key = self._stem(word)
        wc = word / 4   # word of context
        for i in self_index[key]:
            lcontext = ' '.join(self._text[i-wc:i])
            rcontext = ' '.join(self._text[i:i+wc])
            ldisplay = '%*s' % (width, lcontext[-width:])
            rdisplay = '%-*s' % (width, rcontext[:width])
            print ldisplay, rdisplay
    def _stem(self, word):
        return self._stemmer.stem(word).lower()


# -----------------------------------------
# 3.7.2 NLTKの正規表現トークナイザ
# def main():
#     text  = 'That U.S.A poster-print costs $12.40...'
#     pattern = r'''(?x)
#         ([A-Z]\.)+
#         | |w+(-\w+)*
#         | \$?\d+(\.\d+)?%?
#         | \.\.\.
#         | [][.,;"'?():-_`]
#         '''
#     print nltk.regexp_tokenize(text, pattern)


# -----------------------------------------
# 3.8.1
# def main():
#     sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
#     text = nltk.corpus.gutenberg.raw('chesterton-thursday.txt')
#     sents = sent_tokenizer.tokenize(text)
#     pprint.pprint(sents[171:181])
#     print(sents[171:181])


# -----------------------------------------
# 3.8.2
# 単語の境界を取り除いたテキストから単語ごとに分割されたデータを再構築する
# def segment(text, segs):
#     words = []
#     last = 0
#     for i in range(len(segs)):
#         if segs[i] == '1':
#             words.append(text[last:i+1])
#             last = i+1
#     words.append(text[last:])
#     return words


# # 語彙目録の保存と再構築のコストの計算
# def evaluate(text, segs):
#     words = segment(text, segs)
#     text_size = len(words)
#     lexicon_size = len(' '.join(list(set(words))))
#     return text_size + lexicon_size


# def main():
#     text = 'doyouseethekittyseethedoggydoyoulikethekittylikethedoggy'
#     seg1 = '0000000000000001000000000010000000000000000100000000000'
#     seg2 = '0100100100100001001001000010100100010010000100010010000'
#     seg3 = '0000100100000011001000000110000100010000001100010000001'
#     # print segment(text, seg1)
#     # print segment(text, seg2)
#     print segment(text, seg3)
#     print evaluate(text, seg3)
#     print evaluate(text, seg2)
#     print evaluate(text, seg1)


# -----------------------------------------
# 3.9.3
# ブラウンコーパスの各セクションでの法助動詞の頻度
# def tabulate(cfdist, words, categories):
#     print '%-16s' % 'Category',
#     for word in words:
#         print '%6s' % word,
#     print
#     for category in categories:
#         print '%-16s' % category,
#         for word in words:
#             print '%6s' % cfdist[category][word],
#         print


# def main():
#     cfd = nltk.ConditionalFreqDist(
#             (genre, word)
#             for genre in brown.categories()
#             for word in brown.words(categories=genre))
#     genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
#     modals = ['can', 'could', 'may', 'might', 'must', 'will']
#     tabulate(cfd, modals, genres)


# -----------------------------------------
# 3.9.4
# def main():
#     output_file = open('output.txt', 'w')
#     words = set(nltk.corpus.genesis.words('english-kjv.txt'))
#     # for word in words:
#     #     output_file.write(word+'\n')

#     # output_file.write(len(words) + '\n')
#     output_file.write(str(len(words)) + '\n')
#     output_file.close()


# -----------------------------------------
# 3.9.5
def main():
    saying = ['After', 'all', 'is', 'said', 'and', 'done', ',', 'more', 'is', 'said', 'than', 'done', '.']
    for word in saying:
        print word, '(' + str(len(word)) + ')',


main()
