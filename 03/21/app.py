# coding: utf-8
import nltk
import urllib2
import re
from bs4 import BeautifulSoup


# -----------------------------------------
# 21
# URLを引数に取り、そのウェブページ上に存在する未知の単語のリストを返す関数unknown()を書いてみよう。この処理を行うには、ページ上の部分文字列をすべて取り出して（re.findall()を用いて）小文字に変換し、語彙リストコーパス（nltk.corpus.words）に現れるすべてのものをリストから削除する。取り出した結果について、手動で分類を行い、調査結果について議論してみよう。
def unknown(url):
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')
    # text = soup.find('p', {'class': 'lead'}).string.lower()
    text = soup.get_text().lower()
    words_text = sorted(set(nltk.word_tokenize(text)))
    # words_corpus = nltk.corpus.gutenberg.words('austen-persuasion.txt')
    # words_corpus = nltk.corpus.gutenberg.words('melville-moby_dick.txt')
    words_corpus = nltk.corpus.gutenberg.words('shakespeare-hamlet.txt')
    # print sorted(set([w.lower() for w in words_corpus]))
    # return
    words_unknown = []
    is_known = False
    # 走査する
    for word in words_text:
        for word_corpus in words_corpus:
            if word == word_corpus:
                is_known = True
                # print 'hoge'
        if is_known is False:
            words_unknown.append(word)
        print word, ':', is_known
        is_known = False
    return words_unknown


def main():
    print unknown('http://sfpc.io/mission/')

    # # 'austen-persuasion.txt'
    # words1 = [u'10002', u'155', u'@', u'aesthetic', u'aims', u'analytical', u'approaches', u'art-making', u'artists', u'blog', u'bootcamp', u'building', u'classes', u'classmates', u'code', u'coding', u'colleagues', u'community', u'computation', u'computational', u'conventions', u'craft', u'creating', u'creative', u'demystification', u'dreams', u'electricity', u'email', u'employers', u'experimentation', u'expertise', u'explore', u'exploring', u'faculty', u'faq', u'flickr', u'focusing', u'forpoetic', u'goal', u'hacking', u'hardware', u'haven', u'hone', u'info', u'initiated', u'intensively', u'job', u'june', u'learners', u'logic', u'math', u'mechanics', u'meets', u'mission', u'ny', u'organized', u'outreach', u'participate', u'poetic', u'poetics', u'portfolio', u'program', u'programming', u'programs', u'realize', u'recognizing', u'rivington', u'search', u'session', u'sfpc.io', u'skills', u'software', u'sorts', u'st.', u'student', u'students', u'subscribe', u'teaching', u'technical', u'technology', u'thinkers', u'tools', u'trade', u'twitter', u'unsubscribe', u'vocational', u'whimsical', u'workshops', u'writer', u'york', u'|', u'\u2013', u'\u2014']
    # # 'melville-moby_dick.txt'
    # words2 = [u'10002', u'155', u'@', u'aesthetic', u'aims', u'analytical', u'appreciate', u'art-making', u'blog', u'bootcamp', u'classes', u'classmates', u'coding', u'colleagues', u'computation', u'computational', u'conventions', u'conversations', u'demystification', u'email', u'employers', u'experimentation', u'expertise', u'explore', u'exploring', u'faculty', u'faq', u'finances', u'flickr', u'focusing', u'forpoetic', u'hardware', u'info', u'intensively', u'june', u'learners', u'logic', u'math', u'mechanics', u'ny', u'outreach', u'participate', u'poetics', u'portfolio', u'program', u'programming', u'programs', u'promote', u'recognizing', u'rivington', u'session', u'sfpc.io', u'skills', u'software', u'st.', u'subscribe', u'teaching', u'technology', u'twitter', u'unsubscribe', u'vocational', u'whimsical', u'workshops', u'york', u'|', u'\u2013', u'\u2014']
    # # 'shakespeare-hamlet.txt'
    # words3 = [u'10002', u'155', u'21', u'4', u'@', u'acquainted', u'aesthetic', u'aims', u'also', u'analytical', u'apply', u'appreciate', u'approaches', u'around', u'art-making', u'artists', u'asked', u'beautiful', u'between', u'blog', u'bootcamp', u'building', u'classes', u'classmates', u'code', u'coding', u'colleagues', u'community', u'completely', u'computation', u'computational', u'conventions', u'conversations', u'creating', u'creative', u'critical', u'degree', u'demystification', u'design', u'dreams', u'electricity', u'email', u'employers', u'every', u'experimentation', u'expertise', u'explore', u'exploring', u'expressive', u'faq', u'finances', u'flickr', u'floor', u'focusing', u'form', u'forpoetic', u'goal', u'greater', u'group', u'hacking', u'hardware', u'haven', u'help', u'hone', u'however', u'idea', u'info', u'initiated', u'intensively', u'investigate', u'job', u'join', u'june', u'kind', u'language', u'large', u'learners', u'logic', u'looking', u'math', u'mechanics', u'meets', u'mission', u'ny', u'opportunity', u'organized', u'outreach', u'participate', u'poetic', u'poetics', u'portfolio', u'possibilities', u'press', u'process', u'program', u'programming', u'programs', u'promote', u'provide', u'questions', u'realize', u'recognizing', u'rivington', u'school', u'self', u'session', u'sfpc.io', u'skills', u'software', u'st.', u'student', u'students', u'subscribe', u'summer', u'surprise', u'teaching', u'technical', u'technology', u'than', u'thinkers', u'tools', u'trade', u'twitter', u'unsubscribe', u'us', u'used', u'useful', u'value', u'vocational', u'whimsical', u'workshops', u'writer', u'writing', u'york', u'|', u'\u2013', u'\u2014']


main()
