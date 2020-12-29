
import numpy as np

class Operator:
    def __init__(self, config, supercell):
        self.config = config
        self.supercell = supercell
        self.field = None

class Kinetic(Operator):
    def __init__(self, config, supercell):
        super().__init__(config, supercell)
        self.config = config
        self.supercell = supercell
    
    def oneDimInit(self):
        grid = self.config['grid'][0]
        periodic = self.config['periodic'][0]
        field = np.zeros(grid)

        X, _, _ = self.supercell.getRGrid()
        a = X[1] - X[0]
        field += np.diag(-2 * np.ones(grid))
        field += np.diag(np.ones(grid - 1), k=1)
        field += np.diag(np.ones(grid - 1), k=-1)
    
        if periodic:
            field[0, -1] = 1
            field[-1, 0] = 1
    return -0.5 * field / a**2

    def twoDimInit(self):
        grid = self.config['grid'][:-1]
        periodic = self.config['periodic'][:-1]
        field = np.zeros(grid)

        X, Y, _ = self.supercell.getRGrid()
        field += np.diag(-4 * np.ones(np.prod(grid)))

    def threeDimInit(self):
        pass

    def init(self):
        if config['dim'] == 1:
            self.field = oneDimInit()
        if config['dim'] == 2:
            self.field = twoDimInit()
        if config['dim'] == 3:
            self.field = threeDimInit()

class Hartree(Operator):
    def __init__(self, config, supercell):
        super().__init__(config, supercell)

class Pseudo(Operator):
    def __init__(self, config, supercell):
        super().__init__(config, supercell)

class XC(Operator):
    def __init__(self, config, supercell):
        super().__init__(config, supercell)

