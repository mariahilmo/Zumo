
class Behavior():

    def __init__(self, sensob, bbcon, priority = 0):
        self.bbcon = bbcon
        self.sensob = sensob
        self.motor_recommendations = [] # list with tuples
        self.active_flag = False
        self.halt_request = False
        self.priority = priority
        self.match_degree = 0
        self.weight = 0

    # A test to see if the behavior should be deactivated
    def consider_deactivation(self):
        pass

    # A test to see if the behavior should be activated
    def consider_activation(self):
        pass

    """
    Purpose: The main interface between the bbcon and the behavior.
    Actions: Update the activity status
             Call sense_and_act
             Update the behavior's weight
    """
    def update(self):
        pass


    """
    The core computations performed by the behavior that use sensob readings to produce motor recommendations
    Gathering the values of its sensobs (and possibly checking for relevant posts on the bbcon), and using this
    information to determine the motor recommendations, and possibly a halt request. Also setting the match_degree
    """
    def sense_and_act(self):
        pass
