# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 09:31:06 2019

@author: pattn
"""

#import files
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

#bot = ChatBot("Pikachu")
bot = ChatBot(name='Pikachu', read_only=True,
                 logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                 'chatterbot.logic.BestMatch'])
trainer = ListTrainer(bot)
trainer.train(['What is your name?', 'My name is Pikachu'])
trainer.train(['How are you?', 'I am good' ])
trainer.train(['Bye?', 'Bye, see you later' ])


conversation = [
    "Hello",
    "Hello!!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer.train(conversation)
trainer.train(math_talk_1)
trainer.train(math_talk_2)

corpus_trainer = ChatterBotCorpusTrainer(bot)
corpus_trainer.train('chatterbot.corpus.english')

@app.route("/")
def home():    
    return render_template("home.html") 
@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')    
    return str(bot.get_response(userText)) 
if __name__ == "__main__":    
    app.run()