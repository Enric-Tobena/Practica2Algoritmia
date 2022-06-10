import sys
from findpeaks import findpeaks
import random
import numpy as np
from matplotlib import pyplot as plt


def image_generator(n_size=10):
    img = [[random.randint(0, 255) for i in range(n_size)] for j in range(n_size)]
    fp = findpeaks(method='mask', whitelist='peak', scale=False, denoise=None, verbose=0)
    result = fp.fit(img)
    solution = np.argwhere(result['Xdetect'] == True)
    return {
        "image": img,
        "solution": solution.tolist()
    }


# TODO: Realizar cada una de vuestras funciones para detectar barcos dentro de la imagen de entrada que se encuentra en la variable "image2D".
def shipDetectorIterativo(image):
    imageToAnalyze = setupBorders(image)
    positions = []
    for i in range(1, len(imageToAnalyze) - 1):
        for j in range(1, len(imageToAnalyze) - 1):
            if smallerSides(i, j, imageToAnalyze):
                positions.append([i - 1, j - 1])

    return positions


def shipDetectorRecursivo(image):
    imageToAnalyze = setupBorders(image)
    positions = []

    return analizarEntornoRecursivo(imageToAnalyze, positions, 1, 1)


def analizarEntornoRecursivo(imageToAnalyze, positions, i, j):
    if i == len(imageToAnalyze) - 2 and j == len(imageToAnalyze) - 1:
        return positions
    if j == len(imageToAnalyze) - 1:
        return analizarEntornoRecursivo(imageToAnalyze, positions, i + 1, 1)

    if smallerSides(i, j, imageToAnalyze):
        positions.append([i - 1, j - 1])

    return analizarEntornoRecursivo(imageToAnalyze, positions, i, j + 1)


def setupBorders(image):
    newImage = [[-1 for i in range(len(image) + 2)] for j in range(len(image) + 2)]

    for i in range(1, len(image) + 1):
        for j in range(1, len(image) + 1):
            newImage[i][j] = image[i - 1][j - 1]

    return newImage


def smallerSides(i, j, image):
    num = image[i][j]
    return num >= image[i + 1][j] and num >= image[i - 1][j] and num >= image[i][j + 1] and num >= image[i][j - 1]


# TODO: En este programa, debereis generar las imagenes de costos correspondientes tal y como hicimos en laboratorios y en la práctica 1.

def calcularTiempoIterativo():
    import timeit
    times = []
    for x in range(4, 200, 4):
        print("n =", x)
        provImg = image_generator(x)['image']
        times.append((x, timeit.timeit("shipDetectorIterativo(" + str(provImg) + ")",
                                       setup="from __main__ import shipDetectorIterativo", number=100)))
    return times


def calcularTiempoRecursivo():
    import timeit
    times = []
    for x in range(2, 32, 1):
        print("n =", x)
        provImg = image_generator(x)['image']
        times.append((x, timeit.timeit("shipDetectorRecursivo(" + str(provImg) + ")",
                                       setup="from __main__ import shipDetectorRecursivo", number=100)))
    return times


def setupGraphs(x_list, y_list):
    print(x_list)
    print(y_list)
    plt.scatter(x_list, y_list)
    plt.show()


def empiricalTimes():
    iterativeTime = calcularTiempoIterativo()
    setupGraphs(*map(list, zip(*iterativeTime)))

    recursiveTime = calcularTiempoRecursivo()
    setupGraphs(*map(list, zip(*recursiveTime)))

    return 0


# Programa principal para la generación de las matrices 2D y la identificación de barcos.
if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit('Usage: ' + sys.argv[0] + ' <matrix_size_number>')

    image2D = image_generator(int(sys.argv[1]))
    print(shipDetectorIterativo(image2D['image']))

    empiricalTimes()
