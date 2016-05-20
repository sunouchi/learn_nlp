# coding: utf-8
# 問題：「I am happy」や「She is happy」などの文は正しく構文解析でき、「*you is happy」や「*they am happy」などの文を正しくないと判断できるようにするためには、どのような制約が必要だろうか。英語の動詞「be」の現在形変化に対する2つの解放を実装してみよう。1つは文法(8)を利用する方法であり、もう1つは文法(20)を利用する方法である。
# 
# 代名詞の素性のみで判定する
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


def is_grammatical(sent):
    tokens = sent.split()
    subj = tokens[0].lower()
    per = pronouns[subj]['PER']
    num = pronouns[subj]['NUM']
    beverb= ''
    if per == 1 and num == 'SG':
        beverb = 'am'
    elif per == 3 and num == 'SG':
         beverb = 'is'
    else:
         beverb = 'are'
    return tokens[1] == beverb


# Usage
print is_grammatical('I am happy')
print is_grammatical('He is happy')
print is_grammatical('They are happy')
print is_grammatical('I is happy')
print is_grammatical('They am happy')
