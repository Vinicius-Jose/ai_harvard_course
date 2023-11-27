## Knowledge
- Knowledge-based agents : agentes onde a razão é operarem internamente para representaçoes do conhecimento
- Sentence: uma assertiva sobre o mundo em uma representação do conhecimento em linguagem natural
- Propositional logic: logica baseada em proposiçoes, sentenças
- Proposition symbols:
    - P, Q, R
    - Temos os seguintes simbolos:
        - And, or e not
        - Implication: Se a entao b. Se nao a entao nao b
        - Biconditional: apenas se a e b forem iguais
- Knowledge base (KB): uma serie de sentenças que a IA irá conhecer para tirar conclusões
- Entailment: significa que em qualquer modelo no qual a sentença A é verdadeira entao B também será verdadeira
- Inference: derivar novas sentencias baseado nas ja existentes, definir conclusões
- Model checking: enumerar todas as possibilidades e qual a unica que bate com a base de conhecimento, (se voce tem N proposiçoes o model checking ira validar 2^n de probailidades tornando o algoritimo mt lento)
- Clause: Uma disjunçao de literais ex: P v Q v R
- Conjunctive normal form (CNF): sentença logica que é uma conjunçao de clauses: ex (A v B v C) ^(d v ~E) ^(FvG)

## Knowlegde Enginerring:
- Codificar uma base de conhecimento para que uma maquina possa interpretar com logica boleana
- Inference Rules: Transformar as regras atuais em novas baseado em inferencia, para reduzir a lentidão do model checking
    - Modus Pones: você usa a implicação para provar que a consequência é verdadeira ao demonstrar que a premissa é verdadeira.
        - Ex:      Se hoje é terça, então João vai ao trabalho.Hoje é terça.Então, João vai ao trabalho.
    - And elimination(Conjuction elimination ou Eliminaçao da conjunçao): estabelece que se A e B é verdadeira entao A é verdadeiro e B também:
        - Ex: Harry é amigo da Hermione e do Ron. Harry é amigo do Ron
    - Double Negation Elimination(Dupla Negação): Se uma declaração é verdadeira, então não é o caso que a declaração não é verdadeira
        - Ex: Não é verdade que Harry não passou no teste. Entao Harry passou no teste
    - Implication Elimination: Uma forma de passar uma sentença de if/then para uma de or:
        - Ex: Se estiver chovendo, entao Harry estará dentro. Não está chovendo ou Harry está dentro
    - Biconditional Elimination: quando a proposiçao vale para os dois lados da sentenca:
        - Ex: Está chovendo se e apenas se Harry estiver dentro. Se estiver chovendo, entao Harry esta dentro. Se Harry estiver dentro entao está chovendo
    - De Morgan's Law (Teorema de De Morgan): 
        - Ex: Não é verdade que ambos Harry e Ron passaram no teste. Harry nao passou no teste ou Ron nao passou no teste
    - Distributive Property: Possibilidade de distribuir a preposiçao por ex: (a^(BvY)) == (a^B) v (a^Y)
    

## Theorem Proving (Search problem)
- Aplicar os itens do problema de busca para gerar a base de conhecimento
    - Initial state: começando a base de conhecimento
    - Actions: Inference rules
    - Transition models: nova base de conhecimento após a actions
    - Goal test: checar se a preposiçao que estamos tentando provar
    - Path cost function: numeros de passos necessarios até validar a questão, ou ainda o numero de inference rules que precisamos passar para chegar a resposta

# Conversion to CNF (COnversão de uma proposiçao para CNF)
- Eliminar bicondicionais
- Eliminar implications
- Mover negativas para frente utilizando De Morgan's Laws
- Usar a regra distributiva para distribuir o v(and) onde for possivel
- Ex:
    - Original: (P v Q) -> R 
    - Eliminar implications: ~(P v Q) v R
    - De Morgan's Laws: (~P ^ ~Q) v R
    - Distributive Property: (~P v R) ^(~Q v R)

## Inference by Resolution
- Baseado em duas preposiçoes uma elimina parte da outra
- Determinar que na base de conhecimento A será verdadeiro
    - Checar se (KB ^ ~A) é uma contradiçao
- Converter a KB ^ -a para CNF

## First-Order Logic
- Melhor que Propositional Logic
- Separaçao em grupos 
- Possui Constant Symbols e Predicate Symbols - Quase uma relaçao de OOp
    - Ex da casa de harry potter:
        - Constant Symbols: Grifinoria, Minerva, Harry etc
        - Predicate Symbols: People, House, Belongsto
    - Declaraçao Person(Minverva), House(Grifinoria), ~House(Minerva)
    - Universal Quantification: uma forma de classificar, permite definir que uma regra vale para todos  A.xBelongsTo(x, Grifinoria) -> ~BelongsTo(x,Hufflepuff)
    - Existencial Quantification: define que uma sentenca so sera verdadeira para um valor especifico