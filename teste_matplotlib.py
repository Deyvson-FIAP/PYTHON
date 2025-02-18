#importação das bibliotecas de visualização de gráficos.
import matplotlib.pyplot as plt 
import numpy as np

#Exemplo 1: Seno Simples

x = np.arange(0, 3 * np.pi, 0.1) #criar array(vetor) X
y = np.sin(x) #Calcula o Seno de cada valor de X

plt.plot(x,y) #Plotar o gráfico com as coordenadas informadas
plt.show() #Mostrar o gráfico


#Exemplo 2: Gráfico de Seno e Cosseno (dois valores) detalhado
x = np.arange(0, 3 * np.pi, 0.1) #Criar o array(vetor) X
y_sin = np.sin(x) #Calcular o seno de cada valor de X (Primeiro valor)
y_cos = np.cos(x) #Calcular o cosseno de cada valor de X (Segundo valor)


plt.plot(x,y_sin) #Plotar o Gráfico do Seno
plt.plot(x, y_cos) #Plotar o Gráfico do Cosseno
plt.xlabel('Eixo X') #Nomear o eixo X do gráfico
plt.ylabel('Eixo Y') #Nomear o eixo Y do gráfico
plt.title('exemplo seno e cosseno') #Nomear titulo do gráfico
plt.legend(['seno','cosseno']) #Nomear Legenda para os valores informados na tabela
plt.show()

#Forma alternativa de adicionar legenda no plot usando função LABEL


x = np.arange(0, 3 * np.pi, 0.1) #Criar o array(vetor) X
y_sin = np.sin(x) #Calcular o seno de cada valor de X (Primeiro valor)
y_cos = np.cos(x) #Calcular o cosseno de cada valor de X (Segundo valor)
plt.plot(x, y_sin, label='Seno')
plt.plot(x, y_cos, label='Cosseno')
plt.legend()
plt.show()