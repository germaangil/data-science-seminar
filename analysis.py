# Script de ejemplo para el Seminario SPF
import math

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

if __name__ == "__main__":
    r = 5
    print(f"El área de un círculo con radio {r} es {calcular_area_circulo(r)}")