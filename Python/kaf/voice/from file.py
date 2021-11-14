import speech_recognition as speech_recog
import re
import datetime
import os


recog = speech_recog.Recognizer()


currentDirectory = os.path.join(os.getcwd(), 'vicedir')

# for each file in directory
#for currentFile in os.listdir(currentDirectory):
#currentFile = os.path.join(currentDirectory, currentFile)
#print(currentFile)

currentFile = 'C:\\Users\\Ika\\infa_2020_Maxim\\Python\\kaf\\voice\\vicedir\\2020-08-24-16-13-04.244764.+79674125077.f686ceff-32d5-4612-bed8-5690921ace15.wav'

# source
sample_audio = speech_recog.AudioFile(currentFile)

with sample_audio as audio_file:
#    print("Speak Please")


#    audio = recog.adjust_for_ambient_noise(audio_file, duration = 1)
    audio = recog.record(audio_file, offset=3, duration=60)

    print("Converting Speech to Text...")

    voicestr = ""

    voicestr = recog.recognize_att(audio, language="ru_RU", show_all=False)


    print(voicestr)
