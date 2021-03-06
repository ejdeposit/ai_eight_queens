import unittest
import eight_queens as qu

class TestEightSquare(unittest.TestCase):
    def test_init_board(self):
        board= qu.init_board()
        rows =  board.keys()
        #rows = [0,1,2,3,4,5,6,7]
        for i in range(0,8):
            self.assertIn(i, rows)

        for i in range(0,8):
            columns= board[i].keys()
            for j in range(0,8):
                self.assertIn(j, columns)
                
    def test_queen_attacks_one_queen(self):
        board = qu.init_board()
        board[0][0]=True
        board [0][1]=True

        expected=set()
        expected.add('00-01')

        attacks= qu.attacked_by(0, 0, board)
        self.assertEqual(attacks, expected)

    def test_attacked_by_two_pairs(self):
        """
        00000000
        00000000
        00000000
        00000000
        0x0x0000
        00000000
        00000000
        0x000000
        """
        board = qu.init_board()
        board[4][1]=True
        board[4][3]=True
        board[7][1]=True

        expected=set()
        expected.add('41-43')
        expected.add('41-71')

        attacks= qu.attacked_by(4, 1, board)
        self.assertEqual(attacks, expected)
        
    def test_attacked_by_one_diagnol_pair(self):
        board = qu.init_board()
        board[0][0]=True
        board [5][5]=True

        expected=set()
        expected.add('00-55')

        attacks= qu.attacked_by(0, 0, board)
        print('')
        for item in attacks:
            print(item)
        print('')
        self.assertEqual(attacks, expected)

    def test_attacking_queens_all_on_diagonals(self):
        config='01234567'
        board=qu.to_board(config)
        self.assertEqual(qu.attacking_queens(board), 28)
        
    def test_attacking_queens_all_on_row(self):
        config='11111111'
        board=qu.to_board(config)
        self.assertEqual(qu.attacking_queens(board), 28)

    def test_attacking_queens_all_on_col(self):
        board=qu.init_board()
        for i in range(0,8):
            board[i][1]=True
        self.assertEqual(qu.attacking_queens(board), 28)

    def test_to_board(self):
        board = qu.to_board('01234567')
        row = 0
        for col in range(0,8):
            self.assertTrue(board[row][col])
            row += 1

    def test_crossover(self):
        parent1='01234567'
        parent2='76543210'
        crossOverPoint=4
        expChild='01233210'
        child=qu.cross_over(parent1, parent2, crossOverPoint)
        self.assertEqual(child, expChild)

    def test_mutation(self):
        pass

    def test_fitness_of_sub_optimal_solution(self):
        fitness = qu.fitness('75316420')
        self.assertEqual(fitness, 27)

        
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