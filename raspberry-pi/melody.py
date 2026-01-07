from machine import Pin, PWM
import time

class Tones:
    def __init__(self, base_freq=440.0):
        # A4(69)を基準に各音の周波数を計算
        names = ['C', 'Cs', 'D', 'Ds', 'E', 'F', 'Fs', 'G', 'Gs', 'A', 'As', 'B', "HiC"]
        # C4はMIDI番号60
        for i, name in enumerate(names):
            # 基準のA4から見た半音の距離を計算
            freq = base_freq * (2 ** ((i - 9) / 12))
            setattr(self, name, int(round(freq, 2)))

pwm = None

def tone(pin, freq, ms, duty=20000):
    global pwm
    if pwm is None:
        pwm = PWM(Pin(pin))
    pwm.freq(freq)
    pwm.duty_u16(duty)
    time.sleep_ms(ms)
    silence(pin)

def silence(pin):
    global pwm
    if pwm is not None:
        pwm.duty_u16(0)
        pwm.deinit()
        pwm = None
    Pin(pin, Pin.OUT).value(0)
