class Robot:
    def __init__(self, grid):
        self.grid = grid
        self.r = len(grid)
        self.c = len(grid[0])
        self.path = []
        self.visited = set()

    def es_valido(self, x, y):
        return 0 <= x < self.r and 0 <= y < self.c and self.grid[x][y] == 0

    def encontrar_ruta(self):
        if not self.dfs(0, 0):
            return "No hay ruta disponible"
        return self.path

    def dfs(self, x, y):
        if not self.es_valido(x, y) or (x, y) in self.visited:
            return False

        self.path.append((x, y))
        self.visited.add((x, y))

        if x == self.r - 1 and y == self.c - 1:
            return True

        # Moverse a la derecha
        if self.dfs(x, y + 1):
            return True
        # Moverse hacia abajo
        if self.dfs(x + 1, y):
            return True

        # Si no se encuentra una ruta, retroceder
        self.path.pop()
        return False

def leer_mapa():
    r = int(input("Ingrese el número de filas: "))
    c = int(input("Ingrese el número de columnas: "))
    
    print("Ingrese la rejilla fila por fila (0 para celdas libres, 1 para celdas bloqueadas):")
    grid = []
    for i in range(r):
        fila = list(map(int, input().split()))
        grid.append(fila)
    
    return grid

def imprimir_ruta_en_rejilla(grid, ruta):
    ruta_set = set(ruta)  # Convertir la ruta a un conjunto para acceso rápido
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) in ruta_set:
                print("*", end=" ")
            else:
                print(grid[i][j], end=" ")
        print()

# Leer la rejilla desde la entrada del usuario
grid = leer_mapa()

# Crear una instancia del robot y encontrar la ruta
robot = Robot(grid)
ruta = robot.encontrar_ruta()

# Imprimir la ruta encontrada
if isinstance(ruta, str):
    print(ruta)
else:
    print("Ruta encontrada:")
    imprimir_ruta_en_rejilla(grid, ruta)
