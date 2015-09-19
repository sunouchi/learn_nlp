# coding: utf-8
import urllib2
import lxml.html


# -----------------------------------------
# 20
# 任意のウェブページにアクセスし、そこからテキストを抽出するコードを書いてみよう。たとえば、天気予報サイトへアクセスし、特定の都市や街の今日の予報最高気温を取得してみよう。
def main():
    html = urllib2.urlopen('http://weather.yahoo.co.jp/weather/13/4410.html').read()
    root = lxml.html.fromstring(html)
    lists = root.xpath('//li[@class="high"]/em')
    for (i, l) in enumerate(lists):
        if i == 0:
            temp = l.text
    print u'今日の最高気温は「%s度」です。' % temp


main()
