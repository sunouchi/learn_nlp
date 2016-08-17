# coding: utf-8
from pyknp import KNP

sent = '先生は自転車で学校に行った。'
knp = KNP()
result = knp.parse(sent)

# 文節
for bnst in result.bnst_list():
    midasi = ''.join(mrph.midasi for mrph in bnst.mrph_list())
    print(bnst.bnst_id, midasi, bnst.dpndtype, bnst.parent_id, bnst.fstring)

# タグ
print('-----------------------------------')
for tag in result.tag_list():
    midasi = ''.join(mrph.midasi for mrph in bnst.mrph_list())
    print(tag.tag_id, midasi, tag.dpndtype, tag.parent_id, tag.fstring)

# 形態素
print('-----------------------------------')
for mrph in result.mrph_list():
    midasi = ''.join(mrph.midasi for mrph in bnst.mrph_list())
    print(mrph.midasi, mrph.yomi, mrph.genkei, mrph.hinsi, mrph.bunrui, mrph.katuyou1, mrph.katuyou2, mrph.imis, mrph.repname)


