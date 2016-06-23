# coding: utf-8
import nltk

# 2項述語としてラムダ抽出化をする
logics = [
    # exists y.love(pat, y)
    r'\x.(exists y.(love(x, y)))',
    # exists y.(love(pat, y) | love(y, pat))
    r'\x.(exists y.((love(x, y) | love(y, x))))',
    # walk(fido)
    r'\x.(walk(fido))',
]

lp = nltk.sem.logic.LogicParser()
for l in logics:
    e1 = lp.parse(l)
    e2 = lp.parse('pat')
    e3 = nltk.sem.ApplicationExpression(e1, e2)
    print e3.simplify()

