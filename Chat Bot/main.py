from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("E-Commerce Bot")
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations")

while True:
    request = input("You: ")
    response = chatbot.get_response(request)
    print("Bot: ", response)
