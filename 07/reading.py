# coding: utf-8
import nltk
import pprint
from nltk.corpus import conll2000

pp = pprint.PrettyPrinter(indent=4)


# -----------------------------------------
# 7.1.1 情報抽出アーキテクチャ
def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    

# -----------------------------------------
# 7.2.4 テキストコーパスの探索
# cp = nltk.RegexpParser('CHUNK: {<V.*> <TO> <V.*>}')
# brown = nltk.corpus.brown
# for sent in brown.tagged_sents():
#     tree = cp.parse(sent)
#     for subtree in tree.subtrees():
#         if subtree.label() == 'CHUNK': print subtree


# -----------------------------------------
# 7.3 チャンカの開発と評価
text = '''
he PRP B-NP
accepted VBD B-VP
the DT B-NP
position NN I-NP
of IN B-PP
vice NN B-NP
chairman NN I-NP
of IN B-PP
Carlyle NNP B-NP
Group NNP I-NP
, , O
a DT B-NP
merchant NN I-NP
banking NN I-NP
concern NN I-NP
. . O
'''
# nltk.chunk.conllstr2tree(text, chunk_types=['NP']).draw()

# print conll2000.chunked_sents('train.txt')[99]

cp = nltk.RegexpParser('')
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
print cp.evaluate(test_sents)
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['VP'])
print cp.evaluate(test_sents)
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['PP'])
print cp.evaluate(test_sents)


# -----------------------------------------
# 7.4 ユニグラムタガーを用いた名詞句チャンキング
class UnigramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents):
        train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)] for sent in train_sents]
        self.tagger = nltk.UnigramTagger(train_data)

    def parse(self, sentence):
        pos_tags = [pos for (word, pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word, pos), chunktag) in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)

