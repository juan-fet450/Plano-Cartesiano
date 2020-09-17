import math

class punto:
    def __init__(self, corX, corY):
        self.corX1 = corX
        self.corY1 = corY

    def distancia(self, corX2, corY2):
        ans = math.sqrt(math.pow((corX2 - self.corX1), 2) + math.pow((corY2 - self.corY1), 2))
        return ans

class circulo:
    def __init__(self, corX1, corY1, corX2, corY2):
        self.corX1 = corX1
        self.corY1 = corY1
        self.corX2 = corX2
        self.corY2 = corY2

    def punto_adentro(self, rX1, rY1):
        ans = math.sqrt(math.pow((self.corX2 - self.corX1), 2) + math.pow((self.corY2 - self.corY1), 2))
        ans2 = math.sqrt(math.pow((rX1 - self.corX1), 2) + math.pow((rY1 - self.corY1), 2))
        if ans >= ans2:
            return True
        else:
            return False

