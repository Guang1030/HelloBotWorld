#coding:utf-8
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
wukong=ChatBot("wukong")
wukong.set_trainer(ChatterBotCorpusTrainer)
wukong.train("chatterbot.corpus.chinese")
questions = ["晚上好","很高兴认识你","你是谁？","你是机器人么","机器人吃饭么","你骗人把"]
for q in questions:
    print '问：%s'%q
    print '答：%s'%(wukong.get_response(q.decode('utf-8')).text.encode('utf-8'))
    print
