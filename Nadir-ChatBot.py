from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
chatbot = ChatBot('ChatBot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")
while True:
    user_input = input("You: ")
    response = chatbot.get_response(user_input)
    print("Bot:", response)
    from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))

if __name__ == "__main__":
    app.run()