from machine import Pin, PWM

class Motor:
    def __init__(self, stby, ain1, ain2, pwma):
        self.stby = Pin(stby, Pin.OUT)
        self.ain1 = Pin(ain1, Pin.OUT)
        self.ain2 = Pin(ain2, Pin.OUT)
        self.pwma = PWM(Pin(pwma))
        
        self.stby.on()
        self.pwma.freq(1000)

    def drive(self, power):
        if power > 0:
            self.ain1.on()
            self.ain2.off()
        elif power < 0:
            self.ain1.off()
            self.ain2.on()
        else:
            self.stop()
            return

        # 絶対値に変換し、0-65535の範囲にスケーリング
        duty = int(65535 * min(abs(power), 1.0))
        self.pwma.duty_u16(duty)

    def stop(self):
        self.pwma.duty_u16(0)
        self.ain1.off()
        self.ain2.off()