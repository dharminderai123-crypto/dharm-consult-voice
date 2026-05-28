from gtts import gTTS
import os

def voice_banao():
    print("=========================")
    print("  dharm.consult Voice AI")
    print("=========================")
    
    text = input("Kya bolwana hai AI se? ")
    
    print("⏳ AI voice bana raha hai...")
    
    voice = gTTS(text=text, lang='hi', slow=False)
    voice.save("output.mp3")
    
    print("✅ Voice ready hai!")
    os.system("start output.mp3")

voice_banao()