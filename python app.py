from flask import Flask, render_template, request
import edge_tts
import asyncio
import os

app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/voice", methods=["POST"])
def voice():
    text = request.form["text"]
    lang = request.form["lang"]
    
    if lang == "hi":
        voice = "hi-IN-SwaraNeural"
    elif lang == "en":
        voice = "en-US-JennyNeural"
    else:
        voice = "en-IN-NeerjaNeural"
    
    async def make_voice():
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save("static/output.mp3")
    
    asyncio.run(make_voice())
    
    return render_template("index.html", done=True)

if __name__ == "__main__":
    app.run(debug=True)