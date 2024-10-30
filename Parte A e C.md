# Atividade de Lógica - Tabela Verdade

## Parte A – Construção Manual da Tabela Verdade

### Proposições

- **P**: Ana vai à festa.
- **Q**: Bruno vai à festa.
- **M**: Bruno traz música.
- **R**: A festa é animada.

### Condições Lógicas

1. Se Ana vai, Bruno vai: \( P \rightarrow Q \)
2. Se Ana ou Bruno for, a festa é animada: \( P \lor Q \rightarrow R \)
3. Se Ana não vai, a festa depende da música de Bruno: \( \neg P \rightarrow (M \rightarrow R) \)

### Tabela Verdade

| Ana (P) | Bruno (Q) | Música (M) | Festa (R) |
|---------|-----------|------------|-----------|
|   T     |     T     |     T      |     T     |
|   T     |     T     |     F      |     T     |
|   T     |     F     |     T      |     F     |
|   T     |     F     |     F      |     F     |
|   F     |     T     |     T      |     T     |
|   F     |     T     |     F      |     F     |
|   F     |     F     |     T      |     F     |
|   F     |     F     |     F      |     F     |

## Parte C – Explicação da Lógica do Algoritmo

1. **Combinações**: O algoritmo lista todas as combinações possíveis de P, Q e M.
2. **Avaliação Lógica**: As proposições são avaliadas usando os operadores lógicos em Python.
3. **Exibição**: O resultado é exibido em uma tabela que mostra se a festa é animada com base nas condições dadas.
