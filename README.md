## Installation Instructions

You can set up the Raspberry Pi by plugging in the HDMI cable into the Raspberry Pi and then into the monitor. Connect the micro-USB cable to the port in the Raspberry Pi, and then the USB on the other side to a power source. Connect the keyboard and mouse to the USB ports in the Raspberry Pi, and then start it up. Connect the button to the Raspberry Pi in the GPIO 25 and GND ports and the camera to the camera port. Also plug the earphones into the headphone jack.

You will need to install some software onto the Raspberry Pi for the program to work, type each of the following lines into the terminal, allowing each line to run before moving on.
```git clone https://github.com/simonmonk/squid.git
cd squid	
sudo python setup.py install
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install tesseract-ocr
sudo apt-get install python-imaging
sudo apt-get install python-imaging-tk
sudo pip install pyttsx
```

After you have done all this, you can the code from the file Readie.py. Then you are done and can use Readie.
