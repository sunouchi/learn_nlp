# coding: utf-8
import nltk
import pprint
from nltk.corpus.reader import *
from nltk.corpus.reader.util import *
from nltk.text import Text

pp = pprint.PrettyPrinter(indent=4)


# -----------------------------------------
# 12.1.1 
jp_sent_tokenizer = nltk.RegexpTokenizer('[^　「」！？。]*[！？。]')
jp_chartype_tokenizer = nltk.RegexpTokenizer('([ぁ-んー]+|[ァ-ンー]+|[\u4e00-\u9FFF]+|[^ぁ-んァ-ンー\u4e00-\u9FFF]+)')
ginga = PlaintextCorpusReader('./corpora/', 'gingatetsudono_yoru.txt',
                              encoding='utf-8',
                              para_block_reader=read_line_block,
                              sent_tokenizer=jp_sent_tokenizer,
                              word_tokenizer=jp_chartype_tokenizer)
ginga_t = Text(w for w in ginga.words())
ginga_t.concordance('川')
