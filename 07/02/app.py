# coding: utf-8
import nltk


grammer = r"""
    NP: {<DT|PP\$|CD>?<JJ>*<NN.*>}
"""
cp = nltk.RegexpParser(grammer)
sentence1 = [("Rapunzel", "NNP"), ("let", "VBD"), ("down", "RP"), ("her", "PP$"), ("long", "JJ"), ("golden", "JJ"), ("hair", "NN")]
sentence2 = [("many", "JJ"), ("researches", "NNS"), ("two", "CD"), ("weeks", "NNS"), ("both", "DT"), ("new", "JJ"), ("positions", "NNS")]

print cp.parse(sentence1)
print cp.parse(sentence2)
