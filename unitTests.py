import unittest
import eight_queens as qu

class TestEightSquare(unittest.TestCase):
    def test_queen_attacks_one_queen(self):
        board={}
        qu.init_board(board)
        board[0][0]=True
        board [0][1]=True
        attacks= qu.attacks(0, 0, board)
        self.assertEqual(attacks, 1)

    def test_queen_attacks_two_queen(self):
        board={}
        qu.init_board(board)
        board[4][1]=True
        board [4][3]=True
        board [7][1]=True
        attacks= qu.attacks(4, 1, board)
        self.assertEqual(attacks, 2)

#   def test_upper(self):
#       self.assertEqual('foo'.upper(), 'FOO')

#   def test_isupper(self):
#       self.assertTrue('FOO'.isupper())
#       self.assertFalse('Foo'.isupper())

#   def test_split(self):
#       s = 'hello world'
#       self.assertEqual(s.split(), ['hello', 'world'])
#       
#       # check that s.split fails when the separator is not a string
#       with self.assertRaises(TypeError):
#           s.split(2)

#   def test_swap_tiles(self):
#       board={}
#       rowMax=3
#       columnMax=3
#       pz.init_board(board, rowMax, columnMax)
#       pz.fill_one_to_eight(board)
#       pz.swap_tiles(board, (0,0), (0,1))
#       self.assertEqual(board[0][0], 2)
#       self.assertEqual(board[0][1], 1)

if __name__ == '__main__':
    unittest.main()