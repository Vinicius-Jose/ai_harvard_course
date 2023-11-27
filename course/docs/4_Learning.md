# Learning 
## Supervised Learning: 
- Dado um conjunto de pares de entrada e saida a IA aprende uma funçao para mapear as entradas com as saidas
    - Classification: tarefa de aprendizagem de uma funçao mapeando uma entrada para um categoria discreta
    - Nearest-Neighbor Classification: algoritimo que dado um input escolhe a classe mais proxima dos dados semelhantes aquele input
    - K-Nearest-Neighbor Classification: semelhante ao Nearest-Neighbor Classification mas olha mais de um ponto proximo
    - Perceptron learning rule: dado um ponto (x,y) atualizar cada weight de acordo com wi = wi + a(y-hw(X)) x Xi , o a na funçao normalmente é chamado de learning_rate, o valor no qual irá atualizar o weight
    - Support Vector Machine: utiliza um vetor adicional proximo a barreira para tomar a melhor decisão
    - Maximum Margin Separator: fronteira que maximiza a distancia ente qualquer um dos pontos de dados
    - Regression: tarefa do aprendizado supervisionado para aprender uma funçao para mapear uma entrada dentro de um valor continuo
- Loss Function: função que expressa o quao ruim foi uma hipotese gerada pela IA
- Overfitting: um modelo de IA aceita apeanas valores muito proximos dos dados treinados , falhando em generalizar dados futuros 
- Regularization: penalizar uma hipotese que é mais complexa no calculo de perda, e favorecer hipoteses mais simples
- Holdout Cross-Validation: dividir os dados entre dados de treino e dados de validaçao para validar se as hipoteses geradas pelo treinamento funcionaram corretamente
- K-Fold Cross-Validation: dividir os dados em k grupos, experimentando K vezes usando cada um dos grupos como teste uma vez e utilizando os demais como dados de teste

## Reinforcement Learning: 
- Aprendizado por reforço: onde a IA aprende por tentativa e erro recebendo recompensas ou puniçoes
- Markov Decision Process: modelo de decisão-ação representando estados, ações e suas recompensas
    - Define os estados S
    - Define as ações Actions(s)
    - Modelos de transiçoes P(s'|s,a)
    - Reward function R(s, a, s')
- Q-learning: método de aprendizado onde uma funçao Q(s,a) estima se a combinaraçao irá performar em uma açao a dentro de um estado s
    - Inicia com Q(s,a) = 0 para todo s,a
    - Quando tomamos uma ação e recebemos uma recompensa:
        - Estimamos que o valor de Q(s,a) baseado na recompensa atual e pelas recompensas futuras esperadas 
        - Atualizamos Q(s,a) para receber a conta do valor estimado anteriormente comparado com a nova estimativa
- Greedy Decision-Making: quando em um estado s ecolher a ação com o maior valor de Q(s,a)
- E-greedy:
    - Definir E igual a o quanto é desejavel que a IA explore algum movimento aleatoriamente
    - Com a probabilidade de 1-E escolha o melhor movimento possivel
    - Com a probabilidade de E escolha um movimento aleatorio
- Function Approximation: approximating Q(s,a) razoavelmente por uma funçao combinando varios fatores, outros do que armazenar apenas um valor para cada par de estado-ação

## Unsupervised Learning:
- Dado uma entrada de dados sem nenhum feedback adicional, a IA aprende o padrão desses dados
- Clustering: organizar um dado numero de objetos em grupos de forma que  objetos similares estejam dentro do mesmo grupo
- K-Means Clustering: algoritimo para clusterizar dados baseado em repetidamente definir pontos para os clusters e atualizar o centro de cada cluster