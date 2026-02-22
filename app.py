from flask import Flask, render_template, request
from chatbot import get_response
from datetime import datetime

app = Flask(__name__)

chat_history = []

@app.route("/", methods=["GET", "POST"])
def home():
    global chat_history

    if request.method == "POST":
        user_input = request.form.get("message")

        if user_input and user_input.strip() != "":
            bot_response, confidence = get_response(user_input)

            current_time = datetime.now().strftime("%I:%M %p")

            chat_history.append({
                "user": user_input,
                "bot": bot_response,
                "time": current_time,
                "confidence": round(float(confidence), 2)
             })
            
            with open("chat_log.txt", "a", encoding="utf-8") as log:
                 log.write(f"[{current_time}] USER: {user_input}\n")
                 log.write(f"[{current_time}] BOT: {bot_response}\n\n")

    return render_template("index.html", chat_history=chat_history)

@app.route("/clear")
def clear():
    global chat_history
    chat_history = []
    return render_template("index.html", chat_history=chat_history)

if __name__ == "__main__":
    app.run(debug=True)