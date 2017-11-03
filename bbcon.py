from time import sleep
import random
import imager2 as IMR
from reflectance_sensors import ReflectanceSensors
from camera import Camera
from motors import Motors
from ultrasonic import Ultrasonic
from zumo_button import ZumoButton
from arbitrator import Arbitrator
from sensob import Sensob
from motob import Motob


def Class BBCON:
    def __init__():
        self.behaviors = []
        self.active_behaviors = []
        self.sensobs = []
        self.motobs = []
        self.arbitrator = Arbitrator()

    def add_behavior(self,behavior):
        self.behaviors.append(behavior)

    def add_sensob(self,sensob):
        self.sensobs.append(sensob)

    def activate_behavior(self,behavior):
        if behavior not in self.active_behaviors:
            self.active_behaviors.append(behavior)

    def deactivate_behavior(self,behavior):
        if behavior in self.active_behaviors:
            self.active_behaviors.remove(behavior)
    
