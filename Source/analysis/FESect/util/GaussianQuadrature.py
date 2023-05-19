import numpy as np


def GaussPointsTri(Num):
    if Num == 1:
        GPs = np.array([[1 / 3, 1 / 3]])
        Wts = [1]
    elif Num == 3:
        GPs = np.array([[1 / 6, 1 / 6],
                        [1 / 6, 2 / 3],
                        [2 / 3, 1 / 6]])
        Wts = np.full(3, 1 / 3)
    elif Num == 4:
        GPs = np.array([[1 / 3, 1 / 3],
                        [1 / 5, 3 / 5],
                        [1 / 5, 1 / 5],
                        [3 / 5, 1 / 5]])
        Wts = np.array([-27 / 48, 25 / 48, 25 / 48, 25 / 48])
    elif Num == 7:
        GPs = np.array([[0.1012865073235, 0.1012865073235],
                        [0.1012865073235, 0.7974269853531],
                        [0.7974269853531, 0.1012865073235],
                        [0.0597158717898, 0.4701420641051],
                        [0.4701420641051, 0.4701420641051],
                        [0.4701420641051, 0.0597158717898],
                        [0.3333333333333, 0.3333333333333]])
        Wts = np.array([0.1259391805448, 0.1259391805448, 0.1259391805448, 0.1323941527885, 0.1323941527885, 0.1323941527885, 0.225])
    return GPs, Wts


def GaussPointsQuad(Num):
    if Num == 1:
        GPs = np.array([[0, 0]])
        Wts = [4]
    elif Num == 4:
        GPs = np.array([[-1 / np.sqrt(3), -1 / np.sqrt(3)], [1 / np.sqrt(3), -1 / np.sqrt(3)],
                        [-1 / np.sqrt(3), 1 / np.sqrt(3)], [1 / np.sqrt(3), 1 / np.sqrt(3)]])
        Wts = np.full(4, 1)
    elif Num == 9:
        GPs = np.array([[-np.sqrt(3 / 5), -np.sqrt(3 / 5)], [0, -np.sqrt(3 / 5)], [np.sqrt(3 / 5), -np.sqrt(3 / 5)],
                        [-np.sqrt(3 / 5), 0], [0, 0], [np.sqrt(3 / 5), 0],
                        [-np.sqrt(3 / 5), np.sqrt(3 / 5)], [0, np.sqrt(3 / 5)], [np.sqrt(3 / 5), np.sqrt(3 / 5)]])
        Wts = np.array([25 / 81, 40 / 81, 25 / 81,
                        40 / 81, 64 / 81, 40 / 81,
                        25 / 81, 40 / 81, 25 / 81])
    return GPs, Wts