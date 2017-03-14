from picamera import PiCamera
from time import sleep
from gpiozero import Button
from datetime import datetime
import pytesseract
import Image
import pyttsx

button = Button(25)
camera = PiCamera()

camera.start_preview()
button.wait_for_press()
camera.capture('image.png')
camera.stop_preview()

engine = pyttsx.init()
engine.say(pytesseract.image_to_string(Image.open('image.png')))
engine.runAndWait()
