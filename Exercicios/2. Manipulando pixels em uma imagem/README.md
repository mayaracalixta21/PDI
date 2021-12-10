- **2.2 Exercício 1**

  <p align="justify"><i>Utilizando o programa "exemplos/pixels.cpp" como referência, implemente um programa "regions.cpp". Esse programa deverá solicitar ao usuário as coordenadas de dois pontos P1 e P2 localizados dentro dos limites do tamanho da imagem e exibir que lhe for fornecida. Entretanto, a região definida pelo retângulo de vértices opostos definidos pelos pontos P1 e P2 será exibida com o negativo da imagem na região correspondente.<i></p>
  
  ***[Solução](#)***
  <p>Inicialmente abrimos a imagem em escala de cinza e atribuimos a variavel "imagem" :</p>

   <code>imagem = cv2.imread('C:\\Users\\Matuzo\\Desktop\\PDI\\Python\\Opencv\\Imagens\\biel.png', cv2.IMREAD_GRAYSCALE)</code>
  
  <p>Recebemos as coordenadas dos pontos via terminal. Consideramos que cada ponto será representado como uma lista com duas posições representando respectivamente a coordenada horizontal e vertical do pixel :</p>
  
  <code>P1 = []</code><br>
  <code>P2 = []</code><br>
  <code>P1.append(int(input("Digite a coordenada horizontal do primeiro ponto : ")))</code><br>
  <code>P1.append(int(input("Digite a coordenada vertical do primeiro ponto : ")))</code><br>
  <code>P2.append(int(input("Digite a coordenada horizontal do segundo ponto : ")))</code><br>
  <code>P2.append(int(input("Digite a coordenada vertical do segundo ponto : ")))</code>
  
  <p>Exibimos a imagem original:</p>
  
  <code>cv2.imshow("Original", imagem)</code>
  
  <p>Definimos a função "Preenchimento Invertido"
  
  
  
