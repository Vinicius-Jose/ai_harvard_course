## Termos IA

- Agent : entidade presente em um ambiente e que atua dentro desse ambiente
    - Em uma IA para achar o melhor caminho de carro do ponto x ao y o agente é o carro
- State: configuração do agente no ambiente
- Initial state: estado inicial o state pode ser um step dentro das açoes da Ia, por exemplo o inital state pode ser a rua de saida e o state pode ser no meio do percurso etc
- Actions: as escolhas que a IA irá fazer no state, uma funçao que recebe o state e retornar as funçoes que podem ser executadas naquele estado (state)
- Transition model: descrição do state para cada ação aplicavel, uma funçao que recebe a açao  e o estado e retornar o estado apos a execução da açao
- State space: todas os estados alcançáveis a partir do estado inicial baseado em uma sequencia de ações
- Goal state: uma forma de determinar se um determinado estado é o objetivo
- Path Cost: um custo numerico associado a um caminho determinado
- Solution: sequencia de ações que vao do initial state até o goal state
- Optimal Solution: sequencia de ações que vao do initial state até o goal state com o menor custo possivel
- node : estrutura de dados que mantem:
    - o Estado atual, 
    - O estado anterior (parent)
    - A ação que resultou no estado atual
    - Custo até o momento

## Exemplos de abordagens 
### Approach (Abordagem):
    - Iniciando com uma fronteira que contem o estado inicial
    - Repetir:
        - Se a fronteira estiver vazia nao há solução
        - Remover um node da fronteira
        - Se o node removido é o goal state retornar a solução
        - Expandir o node adicionando nodes da fronteira


### Revised Approach (Abordagem revisada):
    - Iniciando com uma fronteira que contem o estado inicial
    - Inicair com uma lista(set) de exploraçao vazia
    - Repetir:
        - Se a fronteira estiver vazia nao há solução
        - Remover um node da fronteira
        - Se o node removido é o goal state retornar a solução
        - Adicionar o node removido a lista de exploraçao
        - Expandir o node adicionando nodes da fronteira caso os outros nós nao estejam na lista de exploração

# Algoritmos para utilizar na fronteira
- Stack : Last in First out
- Breadth-first: (buscas em largura)  expande o no mais raso na fronteira, em termo de codigo busca em uma arvore os itens que estao na mesma "linha" antes de partir para a proxima linha Utiliza o queue
- Queue: First in First out
- Depht-First: (busca em profundidade) pesquisa por profundidade vai ate o ultimo no de uma decisão antes de buscar o proximo item, utiliza o Stack

- Uninformed Search - estrategia que nao utilizia nenhuma conhecimento especifico do problema (Depht-First, Breadth-first)
- Informed Search - Utiliza estrategias especificas de um problema para encontrar a solução de uma forma mais eficiente 
    - Greedy best-first search (melhor primeiro): escolhe sempre o node que esta mais próximo do seu objetivo. Utiliza uma funçao heuristica h(n)
    - A* search (Algoritimo A*):  uma expansao do anterior buscando o node com o menor valor de g(n) + h(n) onde g é o custo para alcançar aquele node e o h é a funçao heuristica de distancia do objetivo
        - Pode ser otimizado se:
            - A funçao h(n) nao esta com valor acima do correto
            - Se cada no tem de fato um valor menor que o anterior (conforme vai se aproximando do objetivo)
    - Minimax: Define duas variaves/agentes um que sempre ira buscar alcançar o máximo e outro que sempre irá buscar o minimo
        - Dado um estado S:
            - Max escolhe a açao A in Actions(s) que tem o maior valor de Min-Value(Result(r,a))
            - Max escolhe a açao A in Actions(s) que tem o menor valor de Max-Value(Result(r,a))
    - Alpha Beta pruning: uma versão melhorada do minimax onde você elimina alguns nos dentro de uma seleçao visto que o anterior ja apresentou um valor menor do que as opçoes ja conhecidas
    - Depth-Limited Minimax: Ao contrário dos anterior que olhavam até a ultimo movimento possivel para tomar uma decisao, nesse limitamos a quantidade de "jogadas" previstas para podermos tomar uma decisa
        - Evaluation function: funçao para estimar a utilidade esperada de um jogo baseado em um estado