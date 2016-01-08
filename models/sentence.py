#! /usr/bin/env python
#coding:utf8

class Sentence():
    offset = 255
    scale = 9
    def __init__(self,data):
        self.data = data.strip()
        self.calcutive_array = self.str_to_calcutive_array(data)

    def str_to_calcutive_array(self,data):
        data = [ord(c)*self.scale for c in data]
        result = data[0:self.offset] if len(data) >=self.offset else data + [0]*(self.offset-len(data))
        return result

    def to_json(self):
        return {'data':self.data,'calcutive_array':self.calcutive_array}


