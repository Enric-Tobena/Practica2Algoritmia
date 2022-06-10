import random
import unittest

from main import shipDetectorIterativo, shipDetectorRecursivo, image_generator


class MyTestCase(unittest.TestCase):

    def test_something(self):
        image = [[29, 150, 22],
                 [244, 71, 21],
                 [226, 229, 223]]
        your_solution = shipDetectorIterativo(image)
        solution = [[0, 1], [1, 0], [2, 1]]

        self.assertListEqual(your_solution, solution)

    def test_practice_validator_2_x_2_iterativo(self):
        image = [[3, 6],
                 [2, 11]]
        your_solution = shipDetectorIterativo(image)
        solution = [[1, 1]]

        self.assertListEqual(your_solution, solution)

    def test_practice_validator_3_x_3_iterativo(self):
        image = [[24, 54, 32],
                 [12, 25, 18],
                 [30, 40, 11]]
        your_solution = shipDetectorIterativo(image)
        solution = [[0, 1], [2, 1]]

        self.assertListEqual(your_solution, solution)

    def test_practice_validator_4_x_4_iterativo(self):
        image = [[15, 12, 25, 9],
                 [24, 32, 12, 4],
                 [18, 42, 35, 52],
                 [30, 68, 112, 39]]
        your_solution = shipDetectorIterativo(image)
        solution = [[0, 2], [2, 3], [3, 2]]

        self.assertListEqual(your_solution, solution)

    def test_practice_validator_5_x_5_iterativo(self):
        image = [[15, 13, 40, 25, 41],
                 [32, 18, 36, 27, 19],
                 [10, 8, 38, 52, 116],
                 [60, 34, 16, 38, 55],
                 [39, 70, 17, 54, 33]]
        your_solution = shipDetectorIterativo(image)
        solution = [[0, 2], [0, 4], [1, 0], [2, 4], [3, 0], [4, 1], [4, 3]]

        self.assertListEqual(your_solution, solution)

    def test_practice_validator_2_x_2_recursivo(self):
        image = [[3, 6],
                 [2, 11]]
        your_solution = shipDetectorRecursivo(image)
        solution = [[1, 1]]

        self.assertListEqual(your_solution, solution)

    def test_practice_validator_3_x_3_recursivo(self):
        image = [[24, 54, 32],
                 [12, 25, 18],
                 [30, 40, 11]]
        your_solution = shipDetectorIterativo(image)
        solution = [[0, 1], [2, 1]]

        self.assertListEqual(your_solution, solution)

    def test_practice_validator_4_x_4_recursivo(self):
        image = [[15, 12, 25, 9],
                 [24, 32, 12, 4],
                 [18, 42, 35, 52],
                 [30, 68, 112, 39]]
        your_solution = shipDetectorIterativo(image)
        solution = [[0, 2], [2, 3], [3, 2]]

        self.assertListEqual(your_solution, solution)

    def test_practice_validator_5_x_5_recursivo(self):
        image = [[15, 13, 40, 25, 41],
                 [32, 18, 36, 27, 19],
                 [10, 8, 38, 52, 116],
                 [60, 34, 16, 38, 55],
                 [39, 70, 17, 54, 33]]
        your_solution = shipDetectorIterativo(image)
        solution = [[0, 2], [0, 4], [1, 0], [2, 4], [3, 0], [4, 1], [4, 3]]

        self.assertListEqual(your_solution, solution)

    def test_practice_validator_10_x_10(self):
        image = image_generator(10)
        iter_solution = shipDetectorIterativo(image['image'])
        rec_solution = shipDetectorRecursivo(image['image'])

        self.assertListEqual(iter_solution, rec_solution)


if __name__ == '__main__':
    unittest.main()
