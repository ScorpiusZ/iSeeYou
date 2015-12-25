#! /usr/bin/env python
#coding:utf8
from sentence import Sentence
from tornado.options import options
from os.path import join,exists,dirname
from os import makedirs

#ml
from sklearn.externals import joblib
from sklearn.naive_bayes import BernoulliNB

class ClassifierNotExist(Exception):
    def __init__(self,nameSpace,name):
        self.error_msg = 'classifier {0}/{1} not exists, you shold train first'.format(nameSpace,name)

class SvmClassifier():
    def __init__(self,nameSpace,name):
        self.nameSpace = nameSpace
        self.name = name

    def check(self):
        if not self.classifier_exist():
            raise ClassifierNotExist(self.nameSpace,self.name)

    def predict(self,X):
        self.check()
        return self.load().predict(X)

    def classifier_exist(self):
        file_name = self.file_name()
        return exists(file_name)

    def train(self,X,y,persistence=False):
        clf = BernoulliNB()
        clf.fit(X,y)
        if persistence:
            self.save(clf)

    def file_name(self):
        root_path = options.classifier_path
        return join(root_path,self.nameSpace,self.name+'.pkl')

    def save(self,clf):
        path = dirname(self.file_name())
        print path
        if not exists(path):
            makedirs(path)
        joblib.dump(clf,self.file_name(),compress = 3)

    def partial_fit(self,X,y):
        clf = self.load().partial_fit(X,y)
        self.save(clf)

    def load(self):
        return joblib.load(self.file_name())

def predict_data_list(clf,datas):
    result = []
    X = map(lambda x: Sentence(x).calcutive_array,datas)
    y = clf.predict(X)
    for s,p in zip(datas,y):
        result.append({'data':s,'prediction':p})
    return result

def predict(datas,nameSpace,name):
    try:
        clf = SvmClassifier(nameSpace,name)
        clf.check()
        result =  predict_data_list(clf,datas)
        return {'results':result,'msg':'success'}
    except ClassifierNotExist as e:
        print e.error_msg
        return {'result':[],'msg':e.error_msg}

def train_data_list(clf,datas,targets):
    try:
        X = map(lambda x: Sentence(x).calcutive_array,datas)
        clf.partial_fit(X,targets)
        return True
    except Exception,e:
        return False

def train(datas,targets,nameSpace,name):
    clf = SvmClassifier(nameSpace,name)
    if train_data_list(clf,datas,targets):
        return 'success'
    else:
        return 'failed'


def demo():
    import numpy as np
    size = 500
    clf = SvmClassifier('test','spam1')
    X = (np.random.ranf(size*Sentence.offset)*256).reshape(-1,Sentence.offset)
    y = np.random.choice([0,1],size)
    clf.train(X,y,True)

