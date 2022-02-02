# OrangePi Zero (H2+ H3) Hardware PWM-Fan control #
How to control a PWM fan depending on CPU temperature on a OrangePi Zero (H2+ / H3)

This solution requires Python - best with V 3.x or later. All examples are done with V 3.10

This was developed and tested on an OrangePi Zero. Most likely it will work on any H2+ and H3 chip solutions. The only thing to bare in mind is that you need to use PWM0 pin. On the OPi Zero (or on PC+) board this is **the middle pin** of the Debug TTL UART pins (the tree pins that stand alone). 

### Step 1: Make sure you run the most recent software ###

```# sudo apt-get update && sudo apt-get dist-upgrade -y```

### Step 2: Install or update Python 3.7 or later ###

```# python3 --version``` -->shows actual installed version(s)

```# sudo apt-get install python3.7``` -->installs Python3.7

The two most crucial third-party Python packages are setuptools and pip.

```# command -v pip3``` -->see if PIP for Python3 is installed

### Step 3: Actiate HW pwm on your OrangePi ###

Edit /boot/armbianEnv.txt and add new line: overlays=pwm

```# cd /boot```

```# nano armbianEnv.txt``` --> insert new line with ___overlays=pwm___

Exit Nano with <kbd>ControlX</kbd>, <kbd>y</kbd> and <kbd>Enter</kbd>

### Step 4: Install OpiGPIO

