import os
import eel

from engin.features import *
from engin.command import *
from engin.auth import recoganize

def start():
    
    eel.init("www")
    
    playAssistantSound()
    @eel.expose
    def init():    
      eel.hideLoader() 
      speak("Ready for Face Authentication")
      flag=recoganize.AuthenticateFace()
      if flag==1:
          eel.hideFaceAuth()
          speak("Face Authentication Successfull")
          eel.hideFaceAuthSuccess()
          speak("Hello,Welcome Sir,How can i Help You")
          eel.hideStart()
          playAssistantSound()
      else:
          speak("Face Authentication Fail")    


    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    eel.start('index.html', mode=None, host='localhost', block=True)
        

 