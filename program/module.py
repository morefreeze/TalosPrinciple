class Tetrimino(object):

    """Describe each tetrimino."""
    title = 'X'
    grids = [[]]
    arr = []

    def __init__(self):
        from operator import sub
        self.arr = []
        for i in range(len(self.grids)):
            arr = []
            for x in range(len(self.grids[i])):
                for y in range(len(self.grids[i][x])):
                    if self.grids[i][x][y] == '1':
                        arr.append((x,y))
            # convert first element as (0,0)
            (dx, dy) = arr[0]
            for i in range(len(arr)):
                arr[i] = tuple(map(sub, arr[i], (dx, dy)))
            self.arr.append(arr)

class TetriminoFactory(object):

    """Generate each tetrimino."""

    @staticmethod
    def make(type):
        """Generate all shape of type.

        :type: TSZILJO
        :returns: One of Tetrimino

        """
        type = type.upper()
        if (type == 'T'):
            return T()
        elif (type == 'S'):
            return S()
        elif (type == 'Z'):
            return Z()
        elif (type == 'I'):
            return I()
        elif (type == 'L'):
            return L()
        elif (type == 'J'):
            return J()
        elif (type == 'O'):
            return O()
        else:
            raise Exception("No such shape %s" %(type))

class T(Tetrimino):

    """Generate shape T"""

    def __init__(self):
        self.title = 'T'
        self.grids = [
            [
                "111",
                " 1",
            ],
            [
                " 1",
                "11",
                " 1",
            ],
            [
                " 1",
                "111",
            ],
            [
                "1",
                "11",
                "1",
            ],
        ]
        Tetrimino.__init__(self)

class S(Tetrimino):

    """Generate shape S"""

    def __init__(self):
        self.title = 'S'
        self.grids = [
            [
                " 11",
                "11",
            ],
            [
                "1",
                "11",
                " 1",
            ],
        ]
        Tetrimino.__init__(self)

class Z(Tetrimino):

    """Generate shape Z"""

    def __init__(self):
        self.title = 'Z'
        self.grids = [
            [
                "11",
                " 11",
            ],
            [
                " 1",
                "11",
                "1 ",
            ],
        ]
        Tetrimino.__init__(self)

class I(Tetrimino):

    """Generate shape I"""

    def __init__(self):
        self.title = 'I'
        self.grids = [
            [
                "1111",
            ],
            [
                "1",
                "1",
                "1",
                "1",
            ],
        ]
        Tetrimino.__init__(self)

class L(Tetrimino):

    """Generate shape L"""

    def __init__(self):
        self.title = 'L'
        self.grids = [
            [
                "1",
                "1",
                "11",
            ],
            [
                "111",
                "1",
            ],
        ]
        Tetrimino.__init__(self)

class J(Tetrimino):

    """Generate shape J"""

    def __init__(self):
        self.title = 'J'
        self.grids = [
            [
                " 1",
                " 1",
                "11",
            ],
            [
                "111",
                "  1",
            ],
        ]
        Tetrimino.__init__(self)

class O(Tetrimino):

    """Generate shape O"""

    def __init__(self):
        self.title = 'O'
        self.grids = [
            [
                "11",
                "11",
            ],
        ]
        Tetrimino.__init__(self)


TYPE_SET = "TSZILJO"


