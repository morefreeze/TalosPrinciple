import unittest
import program.tetris

class TestTetriminos(unittest.TestCase):

    """Test Tetriminos."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_t(self):
        t = program.tetris.TetriminoFactory.make('T')
        self.assertEqual(t.title, 'T')
        self.assertEqual(4, len(t.arr))
        arr = [
        # downward
            [ (0,0), (0,1), (0,2), (1,1) ],
        # left
            [ (0,0), (1,-1), (1,0), (2,0) ],
        # upward
            [ (0,0), (1,-1), (1,0), (1,1) ],
        # right
            [ (0,0), (1,0), (1,1), (2,0) ],
        ]
        self.assertEqual(t.arr, arr)

    def test_o(self):
        o = program.tetris.TetriminoFactory.make('O')
        self.assertEqual(o.title, 'O')
        self.assertEqual(1, len(o.arr))
        arr = [
            [ (0,0), (0,1), (1,0), (1,1) ],
        ]
        self.assertEqual(o.arr, arr)

class TestBoard(unittest.TestCase):

    """Test board"""

    def setUp(self):
        self.b = program.tetris.make_board(5, 5)

    def tearDown(self):
        pass

    def test_try_place(self):
        # this will modify self.b
        b = self.b
        o = program.tetris.TetriminoFactory.make('O')
        self.assertTrue(program.tetris.try_place(b, 0, 0, o.arr[0], o.title))
        b0 = [
            [c for c in "OO   "],
            [c for c in "OO   "],
            [" "]*5,
            [" "]*5,
            [" "]*5,
        ]
        self.assertEqual(b0, b)

    def test_restore_place(self):
        b = self.b
        o = program.tetris.TetriminoFactory.make('O')
        self.assertTrue(program.tetris.try_place(b, 0, 0, o.arr[0], o.title))
        program.tetris.restore_place(b, 0, 0, o.arr[0])
        ori_b = program.tetris.make_board(5, 5)
        self.assertEqual(ori_b, b)

if __name__ == "__main__":
    unittest.main()
