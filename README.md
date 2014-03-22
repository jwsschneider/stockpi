stockpi
=======

A Raspberry Pi-powered stock checker with LED indicators


**About:**

I built this project to continue my exploration of Python, Raspberry Pi, and embedded-systems programming. The result is a device that checks your stock portfolio and lets you know via LED indication whether you are up or down on the day.

The project utilizes the Raspberry Pi's GIPO pins to power three LEDs: blue, green, and red. The LEDs indicate process status (blue) and whether a stock portfolio has a total gain (green) or loss (red) on the day.


**Setup:**

I built stockpi on a Raspberry Pi (Model B, 512 MB RAM) running Raspian (wheezy) 3.10. The code is written in Python. It relies on the Beautiful Soup Python library (http://www.crummy.com/software/BeautifulSoup/). Because stockpi uses the Raspberry Pi's GPIO pins, you have to import the RPi.GPIO library. RPi.GPIO is included in the latest versions of Raspian, but there are instructions to download it here (http://makezine.com/projects/tutorial-raspberry-pi-gpio-pins-and-python/) if you don't already have the library.

I have the code executing according to a cron job (run as sudo):

```
00,30 9-17 * * 1-5 //home/pi/stockpi/stockpi.sh
```

This cronjob runs once every 30 minutes from 9 a.m. to 5 p.m. each business day (when the markets are open on the east coast).

The LED wiring is simple, and I'll describe it in detail in the stockpi wiki (https://github.com/jwsschneider/stockpi/wiki).


**License:**

All of the code and supporting files in the stockpi git repository are licensed under the Creative Commons Attribution-ShareAlike 4.0 International Public License (https://creativecommons.org/licenses/by-sa/4.0/legalcode and https://creativecommons.org/licenses/by-sa/4.0/). Anyone is free to take and modify the files as long as the attribution to its original author is maintained and the modifier agrees to, in turn, license his/her modified files under the Creative Commons Attribution-ShareAlike 4.0 International Public License, too.
