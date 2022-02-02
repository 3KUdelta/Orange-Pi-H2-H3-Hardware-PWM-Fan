#!/usr/bin/python
# -*- coding: utf-8 -*-

import OPi.GPIO as GPIO 
import time
import sys

PWM_chip = 0
PWM_pin = 0
frequency_Hz = 3800
Duty_Cycle_Percent = 100

fan = GPIO.PWM(PWM_chip, PWM_pin, frequency_Hz, Duty_Cycle_Percent)

#stop fan
fan.stop_pwm()

# Configurable temperature and fan speed steps
tempSteps = [40, 70]   # [°C]
speedSteps = [0, 100]  # [%]

# Fan speed will change only of the difference of temperature is higher than hysteresis
hyst = 1

i = 0
cpuTemp = 0
fanSpeed = 0
cpuTempOld = 0
fanSpeedOld = 0

# We must set a speed value for each temperature step
if len(speedSteps) != len(tempSteps):
    print("Numbers of temp steps and speed steps are different")
    exit(0)

try:
    while 1:
        # Read CPU temperature
        cpuTempFile = open("/sys/class/thermal/thermal_zone0/temp", "r")
        cpuTemp = float(cpuTempFile.read()) / 1000
        cpuTempFile.close()

        # Calculate desired fan speed
        if abs(cpuTemp - cpuTempOld) > hyst:
            # Below first value, fan will run at min speed.
            if cpuTemp < tempSteps[0]:
                fanSpeed = speedSteps[0]
            # Above last value, fan will run at max speed
            elif cpuTemp >= tempSteps[len(tempSteps) - 1]:
                fanSpeed = speedSteps[len(tempSteps) - 1]
            # If temperature is between 2 steps, fan speed is calculated by linear interpolation
            else:
                for i in range(0, len(tempSteps) - 1):
                    if (cpuTemp >= tempSteps[i]) and (cpuTemp < tempSteps[i + 1]):
                        fanSpeed = round((speedSteps[i + 1] - speedSteps[i])
                                         / (tempSteps[i + 1] - tempSteps[i])
                                         * (cpuTemp - tempSteps[i])
                                         + speedSteps[i], 0)

            if fanSpeed != fanSpeedOld:
                if (fanSpeed != fanSpeedOld or fanSpeed == 0):
                    fan.duty_cycle(fanSpeed)
                    fanSpeedOld = fanSpeed
            cpuTempOld = cpuTemp

        # print(fanSpeed)

        # Wait until next refresh
        time.sleep(30)  # frefresh all 30 seconds


# If a keyboard interrupt occurs (ctrl + c), the GPIO is set to 0 and the program exits.
except KeyboardInterrupt:
    print(" Fan ctrl interrupted by keyboard - PWM to 0, resetting GPIO - mod mst22")
    fan.duty_cycle(0)
    fan.pwm_close()
    del fan    #delete the class
    sys.exit()
