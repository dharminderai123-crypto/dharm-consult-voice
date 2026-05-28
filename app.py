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

    voices = {
        "hi-female": "hi-IN-SwaraNeural",
        "hi-male":   "hi-IN-MadhurNeural",
        "en-female": "en-US-JennyNeural",
        "en-male":   "en-US-GuyNeural",
        "in-female": "en-IN-NeerjaNeural",
        "in-male":   "en-IN-PrabhatNeural",
    }

    selected_voice = voices.get(lang, "hi-IN-SwaraNeural")
    os.makedirs("static", exist_ok=True)

    async def make_voice():
        communicate = edge_tts.Communicate(text, selected_voice)
        await communicate.save("static/output.mp3")

    asyncio.run(make_voice())
    return render_template("index.html", done=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)