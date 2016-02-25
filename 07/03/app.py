# coding: utf-8
import nltk
import pprint
from nltk.corpus import conll2000

pp = pprint.PrettyPrinter(indent=4)

def evaluate_vp():
    print 'chunk_type: VP'
    grammer = r'VP: {<[V].*>+}'
    cp = nltk.RegexpParser(grammer)
    test_sents = conll2000.chunked_sents('test.txt', chunk_types=['VP'])
    print cp.evaluate(test_sents)
    # for i in range(15,30):
    #     print conll2000.chunked_sents('test.txt')[i]
# evaluate_vp()

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

test_sents = conll2000.chunked_sents('test.txt', chunk_types=['VP'])
train_sents = conll2000.chunked_sents('train.txt', chunk_types=['VP'])
unigram_chunker = UnigramChunker(train_sents)
print unigram_chunker.evaluate(test_sents)

postags = sorted(set(pos for sent in test_sents
                     for (word,pos) in sent.leaves()))
pp.pprint(unigram_chunker.tagger.tag(postags))

