# Exercicio de programação 2.2
import cv2
import sys

imagem = cv2.imread('C:\\Users\\Matuzo\\Desktop\\PDI\\Python\\Opencv\\Imagens\\biel.png', cv2.IMREAD_GRAYSCALE)

print(imagem.shape)

P1 = []
P2 = []

P1.append(int(input("Digite a coordenada horizontal do primeiro ponto : ")))
P1.append(int(input("Digite a coordenada vertical do primeiro ponto : ")))

P2.append(int(input("Digite a coordenada horizontal do segundo ponto : ")))
P2.append(int(input("Digite a coordenada vertical do segundo ponto : ")))

cv2.imshow("Original", imagem)

def PreenchimentoInverido(P1, P2):

    for j in range(min([P1[0], P2[0]]), max([P1[0], P2[0]])+1):
        for i in range(min([P1[1], P2[1]]), max([P1[1], P2[1]])+1):
            imagem[j][i] = abs(255-imagem[j][i])
            

PreenchimentoInverido(P1, P2)
cv2.imshow("Modificada", imagem)
cv2.waitKey(0)