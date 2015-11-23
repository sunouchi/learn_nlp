# coding: utf-8
import nltk
import random
"""
参考にした:
https://stephenholiday.com/articles/2011/gender-prediction-with-python/
"""


class GenderPredictor():
    def get_featureset(self):
        male_names = [(name, 'Male') for name in nltk.corpus.names.words('male.txt')]
        female_names = [(name, 'Female') for name in nltk.corpus.names.words('female.txt')]
        names = male_names + female_names

        featureset = [(self.name_features(n), g) for (n,g) in names]
        return featureset


    def train_and_test(self):
        featureset = self.get_featureset()
        random.shuffle(featureset)

        test_set = featureset[:500]
        devtest_set = featureset[500:1000]
        train_set = featureset[1000:]

        self.train(train_set)

        print 'Accuracy(train_set):', self.get_train_accuracy(train_set)
        print 'Accuracy(devtest_set):', self.get_train_accuracy(devtest_set)
        print 'Accuracy(test_set):', self.get_testAccuracy(test_set)
        print self.get_most_informative_features(10)

        return self.test(test_set)


    def train(self, train_set):
        self.classifier = nltk.NaiveBayesClassifier.train(train_set)
        return self.classifier


    def test(self, test_set):
        self.classifier = nltk.NaiveBayesClassifier.train(test_set)
        return self.classifier


    def devtest(self, devtest_set):
        self.classifier = nltk.NaiveBayesClassifier.train(devtest_set)
        return self.classifier


    def get_testAccuracy(self, test_set):
        return nltk.classify.accuracy(self.test(test_set), test_set)


    def getDevtestAccuracy(self, devtest_set):
        return nltk.classify.accuracy(self.devtest(devtest_set), devtest_set)


    def get_train_accuracy(self, train_set):
        return nltk.classify.accuracy(self.train(train_set), train_set)


    def get_most_informative_features(self, num=5):
        return self.classifier.show_most_informative_features(num)


    def get_accuracy(self, set):
        return nltk.classify.accuracy(self.classifier, set)


    def name_features(self, name):
        return {
            'last_letter': name[-1],
            'last_two_letters': name[-2:],
            'last_is_vowel': (name[-1] in 'aiueoy')
        }


gp = GenderPredictor()
gp.train_and_test()
