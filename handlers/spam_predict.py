from handlers.base import BaseHandler
from models.classifier import predict,train,init

import time

default_nameSpace = 'test'
default_name = 'spam'

class SpamPredictHandler(BaseHandler):
    def post(self):
        result = {}
        datas = self.get_json_argument('datas')
        nameSpace = self.get_json_argument('namespace',[default_nameSpace])[0]
        name = self.get_json_argument('name',[default_name])[0]
        result.update(predict(datas,nameSpace,name))
        self.write(result)

class SpamTrainHandler(BaseHandler):
    def post(self):
        datas = self.get_json_argument('datas')
        nameSpace = self.get_json_argument('namespace',[default_nameSpace])[0]
        name = self.get_json_argument('name',[default_name])[0]
        targets = self.get_json_argument('targets')
        result_msg = train(datas,targets,nameSpace,name)
        self.write({'msg':result_msg})

class SpamInitHandler(BaseHandler):
    def get(self):
        nameSpace = self.get_json_argument('namespace',[default_nameSpace])[0]
        name = self.get_json_argument('name',[default_name])[0]
        init(nameSpace,name)
        self.write('success')

