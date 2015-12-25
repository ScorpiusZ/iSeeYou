from handlers.spam_predict import *

url_patterns = [
    (r"/spam/predict", SpamPredictHandler),
    (r"/spam/train", SpamTrainHandler),
    (r"/spam/init", SpamInitHandler),
]
