class Audio:
    def __init__(self, power, volume):
        self.power = power
        self.volume = volume
    def switch(self, on_off):
        self.power = on_off
    def set_volume(self, vol):
        self.volume = vol
    def tune(self):
        str = "La la la..." if self.power else "turn it on"
        print(str)

mp3 = Audio(False, 8)
mp3.tune()
mp3.switch(True)
mp3.tune()