# Python program to translate
# speech to text and text to speech

import socket
import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()
buf = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8820))
#signUpOrLogIn = input("type-0 to sign up \n type-1 to log in")
#if signUpOrLogIn == "0":
 #   firstname = input("enter your first name")
  #  lastname = input("enter your last name")
   # name = input("enter username")
   # s.send(("username: " + name).encode())
   # data = s.recv(1024).decode()
   # print(data)
   # while "taken" in data:
   #     name = input("username taken, enter  new username")
   #     s.send(("username: " + name).encode())
    #    data = s.recv(1024).decode()
   # password = input("enter password")
   # s.send(name, firstname, lastname, password)
#elif signUpOrLogIn == "1":
 #   name = input("enter username")
  #  s.send(("usernameold:" + name).encode())
  #  data = s.recv(1024).decode()
   # while "found." in data:
    #    name = input("user not found, enter  new username")
     #   s.send(("username:" + name).encode())
      #  data = s.recv(1024).decode()
   # password = input("enter password")
   # s.send(("password:" + password).encode())
   # while "wrong:" in data:
   #     password = input("password is wrong, enter  new password")
    #    s.send(("password:" + password).encode())
     #   data = s.recv(1024).decode()


# Function to convert text to
# speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


# Loop infinitely for user to
# speak

while (1):

    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input
            audio2 = r.listen(source2)

            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            print(MyText)
            s.send(MyText.encode())
            ans = s.recv(buf).decode()
            print(ans)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")