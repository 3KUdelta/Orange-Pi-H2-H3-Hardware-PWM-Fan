# OrangePi Zero (H2+ H3) Hardware PWM-Fan control #
How to control a PWM fan depending on CPU temperature on a OrangePi Zero (H2+ / H3)

![OrangePi Zero](https://github.com/3KUdelta/Orange-Pi-H2-H3-Hardware-PWM-Fan/blob/main/pics/PWM_FAN_1.jpg "")

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

More info about OPi.GPIO is here: [https://opi-gpio.readthedocs.io](https://opi-gpio.readthedocs.io/ "OPi.GPIO Reference") and here: [https://github.com/rm-hull/OPi.GPIO](https://github.com/rm-hull/OPi.GPIO/ "OPi.GPIO Reference")

### Step 5: Install WiringOP-Zero ###

```# cd /root```

```# git clone https://github.com/xpertsavenue/WiringOP-Zero.git```

```# cd WiringOP-Zero```

```# chmod +x ./build```

```# sudo ./build```

Test if successful:

```# gpio readall```

More info about WiringOP-Zero is here: [https://github.com/xpertsavenue/WiringOP-Zero](https://github.com/xpertsavenue/WiringOP-Zero/ "WiringOP-Zero Reference").

### Step 6: Install PWM Fan ###

In my case I have bought a nocuta NF-A4x10 5V PWM fan [https://noctua.at/en/products/fan/nf-a4x10-5v-pwm](https://noctua.at/en/products/fan/nf-a4x10-5v-pwm/ "nocuta"). Excellent piece of work.

![OrangePi Zero](https://github.com/3KUdelta/Orange-Pi-H2-H3-Hardware-PWM-Fan/blob/main/pics/PWM_FAN_2.jpg "")

Connect: 

YELLOW (VIN) to physical pin 4 (5V)

BLACK (GND) to physical pin 6 (GND)

BLUE (PWM) to middle pin of Debug TTL UART pins (3 standalone pins next to the Ethernet plug)

GREEN (RPM) will NOT be connected

![OrangePi Zero](https://github.com/3KUdelta/Orange-Pi-H2-H3-Hardware-PWM-Fan/blob/main/pics/PWM_FAN_3.jpg "")

### Step 7: Python program and autostart ###

Credits for this goes to [https://www.instructables.com/PWM-Regulated-Fan-Based-on-CPU-Temperature-for-Ras/](https://www.instructables.com/PWM-Regulated-Fan-Based-on-CPU-Temperature-for-Ras/ "")

To run the program automatically at startup, I made a bash script where I put all the programs I want to launch, and then I launch this bash script at startup with rc.local.

Use FileZilla or similar to copy ___launch_fan_ctrl.sh___ and ___fan_ctrl.py___ into ___/home___

Edit the /etc/rc.local file and add a new line before the "exit 0": sudo sh '/home/launch_fan_ctrl.sh'

```# nano /etc/rc.local```

add ___sudo sh '/home/launch_fan_ctrl.sh'___ as a new line before exit 0

Exit Nano with <kbd>ControlX</kbd>, <kbd>y</kbd> and <kbd>Enter</kbd>

```# sudo reboot```

## done! ##
