import random
import unittest

from main import shipDetectorIterativo, shipDetectorRecursivo, image_generator


class MyTestCase(unittest.TestCase):

    def test_something(self):
        image = [[29, 150, 22],
                 [244, 71, 21],
                 [226, 229, 223]]
        your_solution = shipDetectorIterativo(image)
        solution = [[1, 0]]

        self.assertListEqual(your_solution, solution)

    def test_practice_validator_2_x_2_iterativo(self):
        image = image_generator(2)
        your_solution = shipDetectorIterativo(image['image'])

        self.assertListEqual(your_solution, image['solution'])

    def test_practice_validator_3_x_3_iterativo(self):
        image = image_generator(3)
        your_solution = shipDetectorIterativo(image['image'])
        print(image['image'])
        print(your_solution)
        print(image['solution'])

        self.assertListEqual(your_solution, image['solution'])

    def test_practice_validator_4_x_4_iterativo(self):
        image = image_generator(4)
        your_solution = shipDetectorIterativo(image['image'])
        print(image['image'])
        print(your_solution)
        print(image['solution'])
        self.assertListEqual(your_solution, image['solution'])

    def test_practice_validator_5_x_5_iterativo(self):
        image = image_generator(5)
        your_solution = shipDetectorIterativo(image['image'])
        print(image['image'])
        print(your_solution)
        print(image['solution'])
        self.assertListEqual(your_solution, image['solution'])

    def test_practice_validator_10_x_10_iterativo(self):
        image = image_generator(10)
        your_solution = shipDetectorIterativo(image['image'])
        print(image['image'])
        print(your_solution)
        print(image['solution'])
        self.assertListEqual(your_solution, image['solution'])

    def test_practice_validator_n_x_n_iterativo(self):
        image = image_generator(random.randint(10, 100))
        your_solution = shipDetectorIterativo(image['image'])
        print(image['image'])
        print(your_solution)
        print(image['solution'])
        self.assertListEqual(your_solution, image['solution'])

    def test_practice_validator_2_x_2_recursivo(self):
        image = image_generator(2)
        your_solution = shipDetectorRecursivo(image['image'])

        self.assertListEqual(your_solution, image['solution'])

    def test_practice_validator_3_x_3_recursivo(self):
        image = image_generator(3)
        your_solution = shipDetectorRecursivo(image['image'])
        print(image['image'])
        print(your_solution)
        print(image['solution'])

        self.assertListEqual(your_solution, image['solution'])

    def test_practice_validator_4_x_4_recursivo(self):
        image = image_generator(4)
        your_solution = shipDetectorRecursivo(image['image'])
        print(image['image'])
        print(your_solution)
        print(image['solution'])
        self.assertListEqual(your_solution, image['solution'])

    def test_practice_validator_5_x_5_recursivo(self):
        image = image_generator(5)
        your_solution = shipDetectorRecursivo(image['image'])
        print(image['image'])
        print(your_solution)
        print(image['solution'])
        self.assertListEqual(your_solution, image['solution'])

    def test_practice_validator_10_x_10_recursivo(self):
        image = image_generator(10)
        your_solution = shipDetectorRecursivo(image['image'])
        print(image['image'])
        print(your_solution)
        print(image['solution'])
        self.assertListEqual(your_solution, image['solution'])

if __name__ == '__main__':
    unittest.main()
