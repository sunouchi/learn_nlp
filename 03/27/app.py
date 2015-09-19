# coding: utf-8
import re
import random


# -----------------------------------------
# 27
# Pythonのrandomモジュールには、シーケンスから無作為にアイテムを1つ選択する関数choice()が含まれている。たとえばchoice('aehh ')は、4文字のうちの1つを返すが、文字hがほかの文字の2倍の頻度で選択される。文字列'aehh 'から作成された、無作為に選ばれた500文字からなる文字のシーケンスを生成する式を書き、そしてそれを1つの長い文字列に連結するために''.join()関数の引数としてその式を与えてみよう。結果得られる文字列は、「a ee heheeh eha」などまるでくしゃみが出そうか、おかしな笑い方をしてえるような文字列になるはずだ。最後にsplit()とjoin()を利用して、この文字列の空白文字を正規化してみよう。
def main():
    letters = 'aehh '
    strList = []
    for i in range(500):
        strList.append(random.choice(letters))
    raw = ''.join(strList)
    text = ''.join(re.findall('\S', raw))
    print text


main()
