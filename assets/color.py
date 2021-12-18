
import random

# retorna uma cor
def getColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    cor = f'rgba({r}, {g}, {b}, 0.5)'
    return cor
