- **Capitulo 2.2**

- Exercício 1

  <p align="justify"><i>Utilizando o programa "exemplos/pixels.cpp" como referência, implemente um programa "regions.cpp". Esse programa deverá solicitar ao usuário as coordenadas de dois pontos P1 e P2 localizados dentro dos limites do tamanho da imagem e exibir que lhe for fornecida. Entretanto, a região definida pelo retângulo de vértices opostos definidos pelos pontos P1 e P2 será exibida com o negativo da imagem na região correspondente.<i></p>
  
  ***[Solução](#)*** <br>
  <p>Inicialmente abrimos a imagem em escala de cinza e atribuimos a variavel "imagem" :</p>

   ```Python
  imagem = cv2.imread('C:\\Users\\Matuzo\\Desktop\\PDI\\Python\\Opencv\\Imagens\\biel.png', cv2.IMREAD_GRAYSCALE)
  ```
  
  <p>Recebemos as coordenadas dos pontos via terminal. Consideramos que cada ponto será representado como uma lista com duas posições representando respectivamente a coordenada horizontal e vertical do pixel :</p>
  
  ```Python
  P1 = []
  P2 = []

  P1.append(int(input("Digite a coordenada horizontal do primeiro ponto : ")))
  P1.append(int(input("Digite a coordenada vertical do primeiro ponto : ")))

  P2.append(int(input("Digite a coordenada horizontal do segundo ponto : ")))
  P2.append(int(input("Digite a coordenada vertical do segundo ponto : ")))
  ```
  
  <p>Exibimos a imagem original:</p>
  
  ```Python 
  cv2.imshow("Original", imagem)
  ```
  
  <p>Definimos a função "PreenchimentoInvertido" que recebe os vertices da região para ser invertida. Nessa função, varremos todos os pixels da imagem e caso o pixel atual pertença a região, invertemos o valor do tom de cinza do mesmo. Essa nova image sobrescreve a imagem original:</p>
  
  ```Python
  def PreenchimentoInvertido(P1, P2):
    for j in range(min([P1[0], P2[0]]), max([P1[0], P2[0]])+1):
        for i in range(min([P1[1], P2[1]]), max([P1[1], P2[1]])+1):
            imagem[j][i] = abs(255-imagem[j][i])
  ```
  
  <p>Invocamos a função criada e exibimos novamente a imagem :</p>
  
  ```Python
  PreenchimentoInvertido(P1, P2)
  cv2.imshow("Modificada", imagem)
  cv2.waitKey(0)
  ```
  
  <p>Exemplo de saida :</p>
  <p align="center">
    <img alt="Biel" src="https://github.com/AugustMatt/PDI/blob/main/Exercicios/2.%20Manipulando%20pixels%20em%20uma%20imagem/2.21.PNG">
    <img alt="Saída" src="https://github.com/AugustMatt/PDI/blob/main/Exercicios/2.%20Manipulando%20pixels%20em%20uma%20imagem/2.22.PNG">
    <br>
    <em>Figura de entrada (Biel.png)&emsp;&emsp;&emsp;&emsp;Figura de saída (Saída.png)</em>
  </p>
  
  
  - Exercício 2
  
  <p align="justify"><i>Utilizando o programa exemplos/pixels.cpp como referência, implemente um programa trocaregioes.cpp. Seu programa deverá trocar os quadrantes em diagonal   na imagem. Explore o uso da classe Mat e seus construtores para criar as regiões que serão trocadas.<i></p>
  
  ***[Solução](#)*** <br>
 


