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

### Step 3: Actiate HW pwm on your OPi Zero ###

Edit /boot/armbianEnv.txt and add new line: overlays=pwm

```# cd /boot```

```# nano armbianEnv.txt``` --> insert new line with ___overlays=pwm___

Exit Nano with <kbd>ControlX</kbd>, <kbd>y</kbd> and <kbd>Enter</kbd>

```# sudo reboot```-->reboot the OPi

### Step 4: Install OpiGPIO ###

```# sudo pip3 install --upgrade OPi.GPIO```

More info about OPi.GPIO is here: [https://opi-gpio.readthedocs.io](https://opi-gpio.readthedocs.io/ "OPi.GPIO Reference").

### Step 5: Install WiringOP-Zero ###

```# cd /root```
```# git clone https://github.com/xpertsavenue/WiringOP-Zero.git```

```# cd WiringOP-Zero```

```# chmod +x ./build```

```# sudo ./build```

Test if successful:

```# gpio readall```

More info about WiringOP-Zero is here: [https://github.com/xpertsavenue/WiringOP-Zero](https://github.com/xpertsavenue/WiringOP-Zero/ "WiringOP-Zero Reference").

### Step 6: Test ###

