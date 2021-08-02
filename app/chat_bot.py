from chatterbot import Chatbot
from chatterbot.trainers import ListTrainer


small_talk = [
    'hi there!',
    'hi!',
    'how do you do?',
    'i\'m cool',
    'glad to hear that',
    'i\'m fine',
    'glad to hear that',
    'i feel awesome',
    'excellent',
    'glad to hear that'
    'not so good',
    'sorry to hear that',
    'what\'s your name',
    'i\'m your shop assistant ask me anything',
]

math_talk_1 = [
    'pythagorean theorem',
    'a squared plus b squared equals c squared'
]

math_talk_2 = [
    'law of cosines',
    'c**2 = a**2 + b**2 - 2*a*b*cos(gamma)'
]


chatbot = Chatbot("Shop Assistant")

trainer = ListTrainer(chatbot)
trainer.train(small_talk)

response = chatbot.get_response("good morning")
print(response)