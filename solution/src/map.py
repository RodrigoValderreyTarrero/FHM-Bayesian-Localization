
class Map:
    def __init__(self, dimension: tuple, criterio: callable):
        #dimension = NxM touple
        self.dimension = dimension
        #P(of being a reflecting cell)
        self.p_reflecting = 0.15
        self.create_map(criterio)

    def create_map(self, criterio):
        self.map = criterio(self.dimension)
  
    def get_dimensions(self):
        return self.dimension
    
    def __str__(self):
        res = "MAPA: \n"

        for n in range(len(self.map)):
            for m in range(len(self.map[n])):
               res += str(self.map[n][m]) + " "
            res += "\n" 
        return res
    