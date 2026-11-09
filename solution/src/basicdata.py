
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
    
