# coding: utf-8
import CaboCha

sent = '先生は自転車で学校に行った。'
c = CaboCha.Parser()
tree = c.parse(sent).toString(CaboCha.FORMAT_XML)
print(tree)
