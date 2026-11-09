import csv
from pathlib import Path
from map_criterio import *
from map import Map
from basicdata import BasicMatrix3D

csv_path = Path(__file__).resolve().parent.parent / "mv_function.csv"

class MvMatrix:
    def __init__(self, mv_function_file_name):
        # mv matrix 
        self.mv_function_file_name = mv_function_file_name
        self.prepare_mv_function()
    def initMvMatrix(self):
        self.matrix = [[BasicMatrix3D() for col in range(3)] for row in range(3)]

    def prepare_mv_function(self):
            self.initMvMatrix()            
            #used: https://docs.python.org/es/3.9/library/csv.html
            with open(self.mv_function_file_name) as csvfile:
                spamreader = csv.reader(csvfile, delimiter=",",quotechar='"')
                next(spamreader)
                for row in spamreader:
                    # read a line
                    for i in range(len(row)):
                        if i == 0 or i == 1:
                            row[i]= int(row[i])
                        else:     
                            row[i]= float(row[i])
                    self.matrix[row[0]][row[1]].fulfill(row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])
    
    def merge_with_map(self, map, position:tuple):
        pos_x =  position[0] #index (0, len-1)
        pos_y =  position[1]  #index (0, len-1)
        len_col = map.get_dimensions()[0] #longitude of a col = how many rows
        len_row = map.get_dimensions()[1]
        matrix = self.matrix
        if pos_x <=0:
            #we are left
            matrix[0][0] = matrix[1][0] = matrix[2][0] = 0
        if pos_x >= len_row -1:
            # we are right
            matrix[0][2] = matrix[1][2] = matrix[2][2] = 0
        if pos_y <=0:
            # we are up
            matrix[0][0] = matrix[0][1] = matrix[0][2]= 0
        if pos_y >= len_col -1:
            # we are down
            matrix[2][0] = matrix[2][1] = matrix[2][2] = 0
        print(matrix)
        return matrix
        
class Sensor():
    def __init__(self):
        pass
    def probability_function(real_situation: int):
        """P(obseving a mark)"""
        if real_situation == 1:
            return 0.85
        return 0.15

class Robot():
    def __init__(self, map_dimensions: tuple):
        self.mv_matrix = MvMatrix(csv_path)
        self.internal_probaility_map = Map(map_dimensions, prob_criteria)
        self.internal_real_map = Map(map_dimensions, binary_criteria)
        self.sensor = Sensor()

    def get_next_mov(self):
        return rn.randint(-1,1), rn.randint(-1,1)

    def move(self):
        mov_x, mov_y = self.get_next_mov()

    def get_intention_possibiltiies(self, start_pos:tuple, intention: tuple):
        
        
        deltaX = start_pos[0]-intention[0]
        deltaY = start_pos[1]-intention[1]

        #key = deltaX, deltaY. Value=pos in mv_matrix [[][][]]
        intention_to_pos_mapper = {(-1,-1):(0,0),
                                   (0,-1):(1,0),
                                   (1,-1):(0,2),
                                   (0,-1):(1,0),
                                   (-1,-1):(0,0),
                                   (-1,-1):(0,0),
                                   (-1,-1):(0,0)}
                                   
        


    def prediction_step(self):
        tmp_prob_map = self.internal_probaility_map
        #1 take all position possibilities

        for n in range(len(self.internal_probaility_map)-1):
            for m in range(len(n)-1):
                # we are evaluating in n,m 
                


                b_t_minus_1 = tmp_prob_map[n][m]
             