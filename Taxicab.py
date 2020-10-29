# Dan Wu
# 10/28/2020
# Write a class named Taxicab that has three private data members,the class have an init method, get method and move x method.

class Taxicab:
    """
    Represents Taxicab shift left or right, up or down and its distance
    """

    def __init__(self,x_coordinate ,y_coordinate):
        """Take two parameters to initialize the coordinates, and also initializes the odometer to zero."""
        self._x_coordinate = x_coordinate
        self._y_coordinate = y_coordinate
        self._odometer = 0

    def get_x_coord(self):
          """Returns the x_coordinate."""
          return self._x_coordinate

    def get_y_coord(self):
          """Returns the y_coordinate."""
          return self._y_coordinate

    def  get_odometer(self):
          """Returns the odometer distance"""
          return self._odometer


    def move_x(self , distance) :
        """Returns the left and right moving distance"""
        self._x_coordinate += distance
        self._odometer += abs ( distance )


    def move_y(self , distance) :
        """Returns the up and down moving distance"""
        self._y_coordinate += distance
        self._odometer += abs ( distance )
