class TV:
   def __init__(self, power, volume, size):
       self.power = power
       self.volume = volume
       self.sie = size
   def switch(self, on_off):
       self.power = on_off
   def set_volume(self, vol):
       self.volume = vol
   def watch(self):
       str = "have fun!" if self.power else "switch on"
       print(str)

obj = TV(True, 14, 40)
obj.switch(True)
obj.watch()