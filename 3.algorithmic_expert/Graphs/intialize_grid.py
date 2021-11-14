# itialize 6x6 grid with 0s dynamically

class Grid:
    def __init__(self, n):
        self.n = n
        self.grid = [[0 for i in range(n)] for j in range(n)]

    def grid_print(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.grid[i][j], end=" ")
            print()

def main():
    n = int(6) # 6x6 grid
    grid = Grid(n)
    grid.grid_print()


if __name__ == "__main__":
    main()