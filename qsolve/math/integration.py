""" The purpose of this module is to provide 
specific integtration methods

"""

###########
# Imports #
###########

import numpy

#####################
# Class definitions #
#####################

class IntegrationMethod(object):
    """ This is an abstract class
    that will only be inherited from

    """
    def __init__(self):
        """ There is no initialization 
        for this class

        """
        pass

    def integrate(cls):
        """ This method will be overridden 
        by subclasses
        
        """
        pass

class RungeKutta(IntegrationMethod):
    """ This class will implement a Runge Kutta 
    method of integration

    """

    def __init__(self):
        """ No initialization

        """
        pass

    def integrate(cls):
        pass

class RiemanSum(IntegrationMethod):
    """ This class allows integration by
    the Rieman Sum method

    """
    def __init__(self):
        pass

    def integrate(cls):
        pass

class MonteCarlo(IntegrationMethod):
    """ This allows integration by Monte Carlo simulation

    """
    def __init__(self):
        pass

    def integrate(cls):
        pass
