import speech_recognition as speech_recog
import re
import datetime


now = datetime.datetime.now()

#open an read file with control words
wordslist = []
with open('words.txt', 'r', encoding='utf-8') as wordfile:
    for line in wordfile:
        wordslist.append(line)

recog = speech_recog.Recognizer()
# source
mic = speech_recog.Microphone()

while True:
    with mic as audio_file:
        print("Speak Please")

        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)

        print("Converting Speech to Text...")

        voicestr = ""
        try:
            voicestr = recog.recognize_google(audio, language="ru_RU")
            # in low register
            voicestr = voicestr.lower()
            # We need letters only
            voicestr = re.sub(r'\W+', '', voicestr)
     #     print("You said: " + recog.recognize_google(audio, language="ru_RU"))
        except Exception as e:
            print("No voce recognition")
     #       print("Error: " + str(e))

    for oneword in wordslist:

        # in low register
        oneword = oneword.lower()
        # We need letters only
        oneword = re.sub(r'\W+', '', oneword)
        print(voicestr)
        # if word is in phrase
        if oneword in voicestr:
            print('Find')
            # write audiofile
            with open(oneword + str(now.microsecond) + '.wav', 'wb') as soundfile:
                soundfile.write(audio.get_wav_data())