# coding: utf-8
import nltk
from nltk import load_parser

sents = [
    # a. If Angus sings, it is not the case that Bertie sulks.
    'sing(Angus) -> -sulk(Bertie)',
    # b. Cyril runs and barks.
    'run(Cyril) & bark(Cyril)',
    # c. It will snow if it doesn't rain.
    '-rain(it) -> snow(it)',
    # d. It's not the case that Irene will be happy if Olive or Tofu comes.
    '(come(Olive) | come(Tofu)) -> -happy(Irene)',
    # e. Pat didn't cough or sneeze.
    '-cough(Pat) | -sneeze(Pat)'
    # f. If you don't come if I call, I won't come if you call.
    '(call(I) -> -come(you)) -> (call(you) -> -come(I))'
]


lp = nltk.sem.logic.LogicParser()
for s in sents:
    print lp.parse(s)

