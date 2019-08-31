'''
Whodis-
Final App made during TAMU Hack, Uses Google voice analytics,
Tried Microsoft Azure as a substitute to Google but stuck with google because of better accuracy
App successfuly sent sms to user with keyword which when said aloud successfully authenticated
'''

import speech_recognition as sr
import pyaudio
import wave
import random
from twilio.rest import Client

import time
#####################################
def record_try():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    ########################################

    r = sr.Recognizer()
    harvard = sr.AudioFile('output.wav')
    with harvard as source:
        audio_play = r.record(source)
        type(audio_play)
    transcript = r.recognize_google(audio_play)
    print(transcript)
    return transcript

def send_sms():
    # Your Account Sid and Auth Token from twilio.com/console
    account_sid = *******
    auth_token = ******
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Press enter and say " + passphrase_str.upper() + " out loud",
        from_='+12099893521',
        to='+19797399252'
    )

    # print(message.sid)


word_list =['hello','big','how','yellow','apple','super','bottle','cat','dog']
passphrase_list =[]
for words in range(3):
    x = random.choice(word_list)
    passphrase_list.append(x)
print(passphrase_list)

passphrase_str= passphrase_list[0]+' '+passphrase_list[1]+' '+passphrase_list[2]


#####################################

otptrial=0
send_sms()
for trial in range(3):
    dummy = input('press enter to continue or enter * if u did not recieve ur otp')
    if( dummy=='*' and otptrial<2):
        print("retrying")
        send_sms()
    elif(otptrial==3):
        print("out of otp tries")
        break
    else:
        out=record_try().lower()
        if(out==passphrase_str):
            print("AUTHENTICATED!!")
            break
        print('wrong ', 2-trial,' tries left')
