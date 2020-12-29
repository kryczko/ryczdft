

class Operator:
    def __init__(self, config, dim=3):
        pass

class Kinetic(Operator):
    def __init__(self, config, dim=3):
        super().__init__(config, dim)


class Hartree(Operator):
    def __init__(self, config, dim=3):
        super().__init__(config, dim)

class Pseudo(Operator):
    def __init__(self, config, dim=3):
        super().__init__(config, dim)

class XC(Operator):
    def __init__(self, config, dim=3):
        super().__init__(config, dim)

