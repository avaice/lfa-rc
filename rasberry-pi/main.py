from machine import Pin
from secrets import WIFI_SSID, WIFI_PASS
from wifi import start_ap
from melody import Tones, tone
from motor import Motor
import time

led = Pin("LED", Pin.OUT)
speaker_gpio = 15
MTR_STBY = 22
MTR_AIN1 = 16
MTR_AIN2 = 17
MTR_PWMA = 18

tones = Tones()

ip = start_ap(WIFI_SSID, WIFI_PASS)

if ip is None: 
    tone(speaker_gpio, tones.C, 50)
    time.sleep(0.1)
    tone(speaker_gpio, tones.C, 500)
    raise RuntimeError("Wi-Fi connect timeout")

tone(speaker_gpio, tones.C, 100)
tone(speaker_gpio, tones.G, 100)
tone(speaker_gpio, tones.HiC, 200)

led.on()

time.sleep(0.5)

motor = Motor(MTR_STBY, MTR_AIN1, MTR_AIN2, MTR_PWMA)

motor.drive(0.2)

time.sleep(1)

motor.stop()
led.off()