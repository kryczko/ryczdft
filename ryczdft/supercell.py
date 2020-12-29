
from ase.io import read, write
import numpy as np

class Supercell:
    def __init__(self, config):
        self.config = config
        self.init()

    def init(self):
        self.atoms = read(self.config['ions'])
        self.cell = self.atoms.cell
        self.recip_cell = self.cell.reciprocal()
        self.X, self.Y, self.Z = self.rGrid()
    
    def getCellVolume(self):
        return self.cell.volume

    def getCell(self):
        return self.cell

    def getReciprocalCell(self):
        """
        Does not include factor of 2 * pi
        """
        return self.recip_cell

    def getRGrid(self):
        return self.X, self.Y, self.Z

    def rGrid(self):
        grid = self.config['grid']
        cell = self.getCell()

        a0xgrid = np.linspace(0, cell[0][0], grid[0], endpoint=False)
        a0ygrid = np.linspace(0, cell[0][1], grid[0], endpoint=False)
        a0zgrid = np.linspace(0, cell[0][2], grid[0], endpoint=False)

        a1xgrid = np.linspace(0, cell[1][0], grid[1], endpoint=False)
        a1ygrid = np.linspace(0, cell[1][1], grid[1], endpoint=False)
        a1zgrid = np.linspace(0, cell[1][2], grid[1], endpoint=False)

        a2xgrid = np.linspace(0, cell[2][0], grid[2], endpoint=False)
        a2ygrid = np.linspace(0, cell[2][1], grid[2], endpoint=False)
        a2zgrid = np.linspace(0, cell[2][2], grid[2], endpoint=False)


        X_flat = np.empty(np.prod(grid))
        Y_flat = np.empty(np.prod(grid))
        Z_flat = np.empty(np.prod(grid))
        counter = 0
        for i in range(grid[0]):
            for j in range(grid[1]):
                for k in range(grid[2]):
                    X[counter] = a0xgrid[i] + a1xgrid[j] + a2xgrid[k]
                    Y[counter] = a0ygrid[i] + a1ygrid[j] + a2ygrid[k]
                    Z[counter] = a0zgrid[i] + a1zgrid[j] + a2zgrid[k]
                    counter += 1
                    
        X = X_flat.reshape(grid)   
        Y = Y_flat.reshape(grid)
        Z = Z_flat.reshape(grid)
        return X, Y, Z