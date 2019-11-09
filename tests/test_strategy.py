import unittest
from 2048-Project.Projet2048 import Carlo

class Test2048(unittest.TestCase):
    
    def test_Carlo(self):
        elt = 2048
        matrice = Carlo(300)
        p = 0
        for i in range(4):
            for j in range(4):
                if M[i][j] >= elt:
                    p += 1
        self.assertTrue(p >= 1)
        
    if __name__ == '__main__':
        unittest.main()
