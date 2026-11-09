
from map import Map
from robot import Robot
import random as rn
from map_criterio import *
class Simulator:
    def __init__(self, dim: tuple):
        self.robot = Robot(dim)
        self.map = Map(dim, binary_criteria)
        self.robot_position = [rn.randint(0,dim[0]-1),rn.randint(0,dim[1]-1)]

        self.robot.mv_matrix.merge_with_map(self.map, [1,1])