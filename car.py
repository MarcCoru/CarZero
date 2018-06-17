from gpiozero import Motor, OutputDevice
from time import sleep

class Car():
    def __init__(self):
        self.motorright = Motor(24, 27)
        self.motorright_enable = OutputDevice(5, initial_value=1)
        self.motorleft = Motor(6, 22)
        self.motorleft_enable = OutputDevice(17, initial_value=1)

    def forward(self):
        self.motorleft.backward()
        self.motorright.backward()

    def backward(self):
        self.motorleft.forward()
        self.motorright.forward()

    def left(self):
        self.motorleft.forward()
        self.motorright.backward()

    def right(self):
        self.motorleft.backward()
        self.motorright.forward()

    def stop(self):
        self.motorleft.stop()
        self.motorright.stop()

    def test(self):
        self.forward()
        sleep(1)
        self.backward()
        sleep(1)
        self.left()
        sleep(1)
        self.right()
        sleep(1)
        self.stop()
