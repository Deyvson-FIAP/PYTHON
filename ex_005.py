import pandas as pd

# Dados base fictícios para machine learning
dados = {
    "idade": [20, 28, 35, 18, 45, 32, 22, 50, 27, 40],
    "tempo_livre": [15, 5, 10, 20, 2, 7, 12, 1, 8, 3],
    "renda": [1500, 3000, 5000, 800, 7000, 4000, 1800, 8500, 3500, 6000],
    "inscreveu": [1, 0, 1, 1, 0, 1, 1, 0, 1, 0]
}

# Criando o DataFrame
df = pd.DataFrame(dados)

# separando o X (features) e Y (targets)
x = df[['idade','tempo_livre', 'renda']]
y = df['inscreveu']

# importando do modelo de seleção do sklearn a ferramenta que divide os treinos e testes da maquina
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42) #random_state=42 usado para manter os dados de treinos iguais e deixar mais fiel o aprendizado.

# modelo de ML de classificação, na qual cria uma arvore de decisões para prever uma classe
from sklearn.tree import DecisionTreeClassifier

modelo = DecisionTreeClassifier()
modelo.fit(x_train, y_train)


# Import de accuracy e classification para avaliarmos o desempenho da maquina
from sklearn.metrics import accuracy_score, classification_report

previsoes = modelo.predict(x_test)

print('acurácia de:', accuracy_score(y_test, previsoes))
print(classification_report(y_test, previsoes, zero_division=1))


# Tabela de comparação dos dados reais com a previsão
comparacao = pd.DataFrame({
    'idade': x_test['idade'],
    'tempo_livre': x_test['tempo_livre'],
    'renda': x_test['renda'],
    'valor_real': y_test,
    'previsão': previsoes
})

print(comparacao)

