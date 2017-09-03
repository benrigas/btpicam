#!/usr/bin/env python

from flask import Flask
from flask import request
from flask import send_file
from picamera import PiCamera
from time import sleep

camera = PiCamera()
app = Flask(__name__)

#camera.resolution = (2592, 1944)
#camera.framerate = 15
#camera.rotation = 180
#camera.exposure_mode = "sports"
camera.awb_mode = "incandescent"
camera.shutter_speed = 11000
#camera.brightness = 50
camera.start_preview()

@app.route("/") 
def hello():
  return "Hello World!"

@app.route("/takePhotoNow")
def takePhotoNow():
  delay = float(request.args.get('delay'))
  filePath = '/home/pi/image.jpg'

  if (delay):
    sleep(delay)
  camera.capture(filePath)
  return send_file(filePath, mimetype='image/jpeg')

if __name__ == "__main__":
  app.run(host='0.0.0.0')
