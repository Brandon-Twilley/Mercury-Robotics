#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
import sys

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
pwm = PWM(0x40, debug=True)
print "this is a test"
servoMin = 195   # Min pulse length out of 4096
servoMax = 573  # Max pulse length out of 4096

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
pwm_current = 200
pickup = "p"
place = "o"
while (True):
  # Change speed of continuous servo on channel O
  input_var = input(" << ")
  if (input_var == pickup):
	if pwm_current + 25 < servoMax:
		pwm_current +=25
	else:
		pwm_current = servoMax
  elif (input_var == place):
	if pwm_current - 25 > servoMin:
		pwm_current -= 25
	else:
		pwm_current = servoMin
  
  pwm.setPWM(0,0, pwm_current)
  time.sleep(.2)
