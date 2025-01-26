# OrangePi Zero (H2+, H3) Hardware PWM-Fan control #
How to control a PWM fan depending on CPU temperature on a OrangePi Zero (H2+ / H3) directly from the harware pwm pin (without a transistor, diode and resistor)? The current settings keeps the temperature below 50 degrees Celsius.

![OrangePi Zero](https://github.com/3KUdelta/Orange-Pi-H2-H3-Hardware-PWM-Fan/blob/main/pics/PWM_FAN_1.jpg "")

This solution requires Python - best with V 3.x or later. All examples are done with V 3.7

This was developed and tested on an OrangePi Zero. Most likely it will work on any H2+ and H3 chip solutions. The only thing to bare in mind is that you need to use PWM0 pin. On the OPi Zero (or on PC+) board this is **the middle pin** of the Debug TTL UART pins (the tree pins that stand alone next to the ethernet port). 

### Step 1: Make sure you run the most recent software ###

```# sudo apt-get update && sudo apt-get dist-upgrade -y```

### Step 2: Install or update Python 3.7 or later ###

```# python3 --version``` -->shows actual installed version(s)

```# sudo apt-get install python3.7``` -->installs Python3.7

The two most crucial third-party Python packages are setuptools and pip.

```# command -v pip3``` -->see if PIP for Python3 is installed

if not, install it: ```# sudo apt install python3-pip```

### Step 3: Activate HW pwm on your OPi Zero ###

Edit /boot/armbianEnv.txt and add new line: overlays=pwm

```# cd /boot```

```# nano armbianEnv.txt``` --> insert new line with ___overlays=pwm___

Exit Nano with <kbd>ControlX</kbd>, <kbd>y</kbd> and <kbd>Enter</kbd>

```# sudo reboot```-->reboot the OPi

### Step 4: Install OpiGPIO ###

```# sudo pip3 install --upgrade OPi.GPIO```

If you get the following error: externally-managed-environment, use this prompt:

```#sudo pip3 install --upgrade OPi.GPIO --break-system-packages``` and ignore the permission warning

More info about OPi.GPIO is here: [https://opi-gpio.readthedocs.io](https://opi-gpio.readthedocs.io/ "OPi.GPIO Reference") and here: [https://github.com/rm-hull/OPi.GPIO](https://github.com/rm-hull/OPi.GPIO/ "OPi.GPIO Reference")

### Step 5: Install WiringOP-Zero ###

```# cd /root```

```# git clone https://github.com/xpertsavenue/WiringOP-Zero.git``` (if git is not installed do this first: ```#sudo apt-get install git```)

```# cd WiringOP-Zero```

```# chmod +x ./build```

```# sudo ./build``` (if you get error make: not found, install GCC first: ```#sudo apt install build-essential```

Test if successful:

```# gpio readall```

```
+-----+-----+----------+------+--Orange Pi Zero--+------+----------+-----+-----+
| H2+ | wPi |   Name   | Mode | V | Physical | V | Mode | Name     | wPi | H2+ |
+-----+-----+----------+------+---+----++----+---+------+----------+-----+-----+
|     |     |     3.3v |      |   |  1 || 2  |   |      | 5v       |     |     |
|  12 |   8 |    SDA.0 | ALT3 | 0 |  3 || 4  |   |      | 5V       |     |     |
|  11 |   9 |    SCL.0 | ALT3 | 0 |  5 || 6  |   |      | 0v       |     |     |
|   6 |   7 |   GPIO.7 | ALT3 | 0 |  7 || 8  | 0 | ALT3 | TxD3     | 15  | 198 |
|     |     |       0v |      |   |  9 || 10 | 0 | ALT3 | RxD3     | 16  | 199 |
|   1 |   0 |     RxD2 | ALT3 | 0 | 11 || 12 | 0 | ALT3 | GPIO.1   | 1   | 7   |
|   0 |   2 |     TxD2 | ALT3 | 0 | 13 || 14 |   |      | 0v       |     |     |
|   3 |   3 |     CTS2 | ALT3 | 0 | 15 || 16 | 0 | ALT3 | GPIO.4   | 4   | 19  |
|     |     |     3.3v |      |   | 17 || 18 | 0 | ALT3 | GPIO.5   | 5   | 18  |
|  15 |  12 |     MOSI | ALT3 | 0 | 19 || 20 |   |      | 0v       |     |     |
|  16 |  13 |     MISO | ALT3 | 0 | 21 || 22 | 0 | ALT3 | RTS2     | 6   | 2   |
|  14 |  14 |     SCLK | ALT3 | 0 | 23 || 24 | 0 | ALT3 | CE0      | 10  | 13  |
|     |     |       0v |      |   | 25 || 26 | 0 | ALT3 | GPIO.11  | 11  | 10  |
+-----+-----+----------+------+---+---LEDs---+---+------+----------+-----+-----+
|  17 |  30 | STAT-LED |  OUT | 0 | 27 || 28 |   |      | PWR-LED  |     |     |
+-----+-----+----------+------+---+-----+----+---+------+----------+-----+-----+
| H2+ | wPi |   Name   | Mode | V | Physical | V | Mode | Name     | wPi | H2+ |
+-----+-----+----------+------+--Orange Pi Zero--+---+------+---------+-----+--+
```

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

Credits for this goes to [https://www.instructables.com/PWM-Regulated-Fan-Based-on-CPU-Temperature-for-Ras/](https://www.instructables.com/PWM-Regulated-Fan-Based-on-CPU-Temperature-for-Ras/ ""). To run the program automatically at startup, just use the bash script and autolaunch this bash script at startup within rc.local.

Copy ___launch_fan_ctrl.sh___ and ___fan_ctrl.py___ into ___/home___ (use FileZilla or similar)

Edit the /etc/rc.local file and add a new line before the "exit 0": sudo sh '/home/launch_fan_ctrl.sh':

```# nano /etc/rc.local```

add ___sudo sh '/home/launch_fan_ctrl.sh'___ as a new line before exit 0

Exit Nano with <kbd>ControlX</kbd>, <kbd>y</kbd> and <kbd>Enter</kbd>

```# sudo reboot```

You might to check the actual temperature: ```# armbianmonitor -m```

## done! :smile: ##
