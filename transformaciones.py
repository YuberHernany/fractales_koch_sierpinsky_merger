















from sets_base import escenario
from sets_base import CUADRADO, SEGMENTO, CUBO
import numpy as np
import matplotlib.pyplot as plt

def rotation_matrix(theta):
    """
    Input: float angle of rotation
    Output: array 2D matrix
    """
    R = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta),  np.cos(theta)]])
    return R

def similitud(s=1, theta=0, vec=np.array([0, 0]).reshape(1, -1)):
    """
    Input: s float, theta float, vec np.array
    Output: funct
    """
    def trans_similitud(puntos):
        R = rotation_matrix(theta)
        nueva_R = s * R
        nuevos_puntos = np.dot(puntos, nueva_R) + vec
        return nuevos_puntos
    return trans_similitud

def koch():
    v0 = np.array([0, 0]).reshape(1, -1)
    v1 = np.array([1./3, 0]).reshape(1, -1)
    v2 = np.array([1./2, np.sqrt(3)/6]).reshape(1, -1)
    v3 = np.array([2./3, 0]).reshape(1, -1)
    s0 = similitud(s=1./3, theta=0, vec=v0)
    s1 = similitud(s=1./3, theta=-np.pi/3, vec=v1)
    s2 = similitud(s=1./3, theta=np.pi/3, vec=v2)
    s3 = similitud(s=1./3, theta=0, vec=v3)
    return s0, s1, s2, s3

def merger():
    ORIGIN = np.zeros(3).reshape(1, -1)
    e1, e2, e3 = np.eye(3)[0].reshape(1, -1), np.eye(3)[1].reshape(1, -1), np.eye(3)[2].reshape(1, -1)
    capa1 = np.vstack([ORIGIN, e1, 2*e1, 2*e1+e2, 2*e1+2*e2, e1+2*e2, 2*e2, e2, ORIGIN]).reshape(-1, 3)
    capa2 = np.vstack([e3, e3+2*e1, e3+2*e1+2*e2, e3+2*e2, e3]).reshape(-1, 3)
    capa3 = (capa1 + 2*e3).reshape(-1, 3)
    desplazamientos = (1./3) * np.vstack([capa1, capa2, capa3]).reshape(-1, 3)
    return desplazamientos

def merger_sobre(vertices):
    r = 1./3
    desplazamientos = merger()
    partes = (r*vertices + desp for desp in desplazamientos)
    todo = np.vstack([parte for parte in partes])
    return todo

def itera_merger(n_iter, vertices_iniciales):
    vertices = merger_sobre(vertices_iniciales)
    for _ in range(n_iter):
        vertices = merger_sobre(vertices)
    return vertices

def sierpinski_carpet():
    desplazamientos = np.array([[0, 0], [1./3, 0], [2./3, 0], [2./3, 1./3],
                                [2./3, 2./3], [1./3, 2./3], [0, 2./3], [0, 1./3], [0, 0]])
    similitudes = (similitud(s=1./3, theta=0, vec=desp) for desp in desplazamientos)
    return similitudes

def sierpinski_carpet_sobre(vertices):
    similitudes = sierpinski_carpet()
    partes = (sim(vertices) for sim in similitudes)
    todo = np.vstack([parte for parte in partes])
    return todo

def itera_sierpinski_carpet(n_iter, vertices_iniciales):
    vertices = sierpinski_carpet_sobre(vertices_iniciales)
    for _ in range(n_iter):
        vertices = sierpinski_carpet_sobre(vertices)
    return vertices

def dibuja_linea_polig(vertices):
    """
    Input: np.array 2D shape N, 2
    Output: plt. plot
    """
    ax = plt.gca()
    ax.plot(vertices[:, 0], vertices[:, 1], "w-")

def dibuja_linea_polig_3d(vertices):
    """
    Input: np.array 3D shape N, 3
    Output: plt. plot
    """
    ax = plt.gca()
    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], s=1)

def koch_sobre(vertices):

    s0, s1, s2, s3 = koch()
    ver0, ver1, ver2, ver3 = s0(vertices), s1(vertices), s2(vertices), s3(vertices)
    vertices = np.vstack([ver0, ver1, ver2, ver3])
    return vertices

def itera_koch(n_iter, vertices_iniciales):
    vertices = koch_sobre(vertices_iniciales)
    for _ in range(n_iter):
        vertices = koch_sobre(vertices)
    return vertices


if __name__ == '__main__':



    ############## sierpinski_carpet ##############
    # escenario()
    # fig, ax = plt.subplots()
    # for iter in range(4):
    #     vertices_iniciales = itera_sierpinski_carpet(iter, CUADRADO)
    #     dibuja_linea_polig(vertices_iniciales)
    #     plt.axis('equal')
    #     plt.pause(1)
    #     plt.cla()
    # vertices_iniciales = itera_sierpinski_carpet(5, CUADRADO)
    # dibuja_linea_polig(vertices_iniciales)
    # plt.show()

    ############# koch ##############
    escenario()
    fig, ax = plt.subplots()
    for iter in range(5):
        vertices_iniciales = itera_koch(iter, SEGMENTO)
        dibuja_linea_polig(vertices_iniciales)
        plt.axis('equal')
        plt.pause(1)
        plt.cla()
    vertices_iniciales = itera_koch(7, SEGMENTO)
    dibuja_linea_polig(vertices_iniciales)
    plt.show()


    # ############## merger ##############
    # ############## se logra solo un scatter ##############
    # escenario()
    # fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
    # ax.grid(False)
    # ax.axis('off')
    # ax.xaxis.pane.fill = False
    # ax.yaxis.pane.fill = False
    # ax.zaxis.pane.fill = False
    # # dibuja_linea_polig_3d(CUBO)
    #
    # vertices = itera_merger(1, CUBO)
    # dibuja_linea_polig_3d(vertices)
    # plt.show()
