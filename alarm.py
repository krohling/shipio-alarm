#Import Libraries
import urllib2
import json
import time
import RPi.GPIO as GPIO

#Initialize our API URL (http://ship.io/api)
JOB_ID = "<YOUR JOB ID>"
API_TOKEN = "<YOUR API TOKEN>"
url = "https://ship.io/jobs/" + JOB_ID + "/builds.json?access_token=" + API_TOKEN

#Initialize our output pin
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, False)

#Check every 30 seconds
while True:
  response = urllib2.urlopen(url)
  data = json.load(response)
  print data
  if data[0]['successful']:
    print '***Passing Build***'
    GPIO.output(22, False)
  else:
    print '***Broken Build***'
    GPIO.output(22, True)

  time.sleep(30)
