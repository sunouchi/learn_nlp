# coding: utf-8
# 代名詞と名詞の素性をみて、一致するかを判定する
import nltk


pronouns = {
    'i'    : {'PER': 1, 'NUM': 'SG'},
    'you'  : {'PER': 2, 'NUM': 'SG'},
    'he'   : {'PER': 3, 'NUM': 'SG'},
    'she'  : {'PER': 3, 'NUM': 'SG'},
    'it'   : {'PER': 3, 'NUM': 'SG'},
    'we'   : {'PER': 1, 'NUM': 'PL'},
    'they' : {'PER': 3, 'NUM': 'PL'}
}
beverbs = {
    'am'   : {'TENSE': 'pres', 'AGR': {'PER': 1, 'NUM': 'SG'}},
    'is'   : {'TENSE': 'pres', 'AGR': {'PER': 3, 'NUM': 'SG'}},
    'are'  : {'TENSE': 'pres', 'AGR': {'PER': 2, 'NUM': 'SG'}},
    'are'  : {'TENSE': 'pres', 'AGR': {'PER': 3, 'NUM': 'PL'}}
}


def is_grammatical(sent):
    tokens = sent.split()
    subj = tokens[0].lower()
    bev  = tokens[1].lower()
    is_grammatical = False
    if beverbs.has_key(bev):
        for key in beverbs:
            if pronouns[subj]['PER'] == beverbs[bev]['AGR']['PER'] and \
               pronouns[subj]['NUM'] == beverbs[bev]['AGR']['NUM']:
                is_grammatical = True
    return is_grammatical


# Usage
# print is_grammatical('I am happy')
# print is_grammatical('He is happy')
# print is_grammatical('They are happy')
# print is_grammatical('I is happy')
# print is_grammatical('They am happy')
