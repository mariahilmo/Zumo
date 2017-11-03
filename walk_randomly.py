from behavior import Behavior
import random

class search_for_garbage(behavior):

    def __init__(self,sensob,bbcon):
        super.__init__(sensob,bbcon)

    def consider_deactivation(self):
        return False

    def consider_activation(self):
        return True

    def update(self):
        self.sense_and_act()

    def sense_and_act(self):

        directions = ['L','R','F','B']
        direct_int = random.randint(0,4)
        direction = directions(direct_int)
        duration = round(random.random(),2)
        speed = round(random.random(),2)

        self.motor_recommendations = [direction,speed,duration]


