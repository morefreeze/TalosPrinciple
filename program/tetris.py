import sys
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

class T(Tetrimino):

    """Generate shape T"""

    def __init__(self):
        self.title = 'T'
        self.grids = [
            [
                "111",
                "010",
            ],
            [
                "01",
                "11",
                "01",
            ],
            [
                "010",
                "111",
            ],
            [
                "10",
                "11",
                "10",
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

class TetriminoFactory(object):

    """Generate each tetrimino."""

    @staticmethod
    def make(type):
        """Generate all shape of type.

        :type: TSZILJO
        :returns: One of Tetrimino

        """
        if (type == 'T'):
            return T()
        elif (type == 'O'):
            return O()
        else:
            raise Exception("No such shape %s" %(type))

TYPE_SET = "TSZILJO"

def print_board(b):
    """print board

    :b: board string
    :returns: None

    """
    if (len(b) == 0): print "(empty)"
    print '-'*(len(b[0])+2)
    for i in range(len(b)):
        print '|'+''.join(b[i])+'|'
    print '-'*(len(b[0])+2)

def print_path(path):
    """print path

    :path: path array
    :returns: None

    """
    for i in range(len(path)):
        print i, path[i][0]
        for row in path[i][1]:
            print row

def dfs(b, pics, path):
    """DFS in b with pics
    1. find most lest-upper empty grid
    2. try each pics place into board
    3. if success dfs next

    :b: board
    :pics: pieces
    :returns: boolean

    """
    # if len(filter(lambda c: c == 'X', pics)) == 4:
        # print '='*20
        # print_board(b)
        # print pics
    found = False
    next_x, next_y = 0,0
    for i in range(len(b)):
        if found:
            break
        for j in range(len(b[i])):
            if b[i][j] == ' ':
                next_x = i
                next_y = j
                found = True
                break
    if not found: return True
    tried = {}
    for i in range(len(pics)):
        pic = pics[i]
        # have tried or before tried
        if pic == 'X' or pic in tried:
            continue
        tried[pic] = 1
        tetrimino = TetriminoFactory.make(pic)
        for j in range(len(tetrimino.arr)):
            arr = tetrimino.arr[j]
            pics[i] = 'X'
            if try_place(b, next_x, next_y, arr, pic):
                path.append((pic, tetrimino.grids[j]))
                if dfs(b, pics, path):
                    return True
                path.pop()
                restore_place(b, next_x, next_y, arr)
            pics[i] = pic
    return False

def try_place(b, x, y, arr, pic):
    """Try to place tetrimino with each rotate into board.
    This function only try to fill (x,y) valid, don't care other things.

    :b: board
    :x: want to fill grid
    :y: same as x
    :arr: array of type
    :pic: title of tetrimino
    :returns: boolean

    """
    h = len(b)
    if h == 0: return False
    w = len(b[0])
    # boundary check
    for (dx,dy) in arr:
        if not(0 <= x+dx and x+dx < h and 0 <= y+dy and y+dy < w and b[x+dx][y+dy] == ' '):
            return False
    for (dx,dy) in arr:
        b[x+dx][y+dy] = pic
    return True

def restore_place(b, x, y, arr):
    """restore of placing, this function will only check boundary

    :b: board
    :x: want to fill grid
    :y: same as x
    :arr: array of type
    :returns: None

    """
    for (dx, dy) in arr:
        try:
            b[x+dx][y+dy] = ' '
        except:
            pass

def make_board(h, w):
    """make board with height * width
    """
    return [[' ']*w for i in range(h)]

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print """Usage: %s height width type_string
type set is [%s]""" %(sys.argv[0], TYPE_SET)
        exit(1)
    height = int(sys.argv[1])
    width = int(sys.argv[2])
    if height <= 0 or width <= 0:
        print "height and width must >= 0"
        exit(2)
    b = make_board(height, width)

    pics = [c for c in sys.argv[3]]
    cnt = 0
    for c in pics:
        if c in TYPE_SET:
            cnt += 4

    if height*width != cnt:
        print "this set [%s] can't be solved in %d x %d" %(pics, height, width)

    path = []
    if dfs(b, pics, path):
        print 'Solution is:'
        print_board(b)
        print_path(path)
    else:
        print "No solution!"
