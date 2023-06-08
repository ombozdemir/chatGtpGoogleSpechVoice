import openai
import speech_recognition as sr
import json
from gtts import gTTS
import os

r = sr.Recognizer()

openai.api_key = 'sk-****'


r = sr.Recognizer()

while True:  # sürekli dinlemek için bir while döngüsü
    with sr.Microphone() as source:
        print("Bir şeyler söyleyin!")
        # mikrofondan sesi yakalar
        audio = r.listen(source)

        try:
            # Google'ın ses tanıma servisini kullanarak sesi metne çevir
            soz = r.recognize_google(audio, language='en-EN')
            print("Ben:"+soz)
            if soz is not '':
              response = openai.Completion.create(
                model="text-davinci-003",
                prompt=soz,
                temperature=0.9,
                max_tokens=10,
                top_p=1,
                frequency_penalty=0.0,
                presence_penalty=0.6,
                stop=[" Human:", " AI:"]
              )
              sozResponse = response['choices'][0]['text']
              print("Aı response: " + sozResponse)
              myobj = gTTS(text=sozResponse, lang='en', slow=False)

              # Saving the converted audio in a mp3 file named
              # welcome
              myobj.save("welcome.mp3")
              os.system("mpg321 welcome.mp3")
        except sr.UnknownValueError:
            print("Google Speech Recognition söylediğinizi anlamadı")
        except sr.RequestError as e:
            print(f"Google Speech Recognition servisi talebe yanıt veremedi; {e}")



