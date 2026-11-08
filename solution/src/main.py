import csv
from pathlib import Path
import random as rn
class Simulator:
    def __init__(self):
        self.robot = Robot(mv_matrix)
        self.map = Map(dim)

class Point2D:
    def __init__(self, x, y, value):
        self.x
        self.y
        self.value 

class BasicMatrix3D:
    def __init__(self):
        self.value = [
                [0,0,0],
                [0,0,0],
                [0,0,0]
                ]
    def getValue(self,i,j):
        return self.value[i,j]

    def setValue(self,i,j,val):
            self.value[i,j] = val

    def fulfill(self, pos_1, pos_2, pos_3, pos_4, pos_5, pos_6, pos_7, pos_8, pos_9):
            self.value = [
                [pos_1, pos_2, pos_3],
                [pos_4, pos_5, pos_6],
                [pos_7, pos_8, pos_9]
            ]



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

            

    
    
    

class Robot():
    def __init__(self, ):
        pass

    

class Map:
    def __init__(self, dimension: tuple):
        #dimension = NxM touple
        self.dimension = dimension
        self.p_reflecting = 0.05

    def create_map(self):
        self.map = [[0 for _ in range(self.dimension[1])] for row in range(self.dimension[0])]
        for n in self.map:
             for m in n:
                  rnd = rn.randrange(0, 1)
                  if rnd < self.p_reflecting:
                    m = 1
        

if __name__ == "main":
    csv_path = Path(__file__).resolve().parent.parent / "mv_function.csv"

    a = MvMatrix(csv_path)
    print(a.matrix[0][0].value)