# Distribuição de Probabilidades: Sistema de N Dados com Energia Constante

## 📖 Sobre o Projeto
Este repositório contém o programa computacional desenvolvido para o 1º Trabalho da unidade curricular de **Física Estatística** (3º ano, 5º semestre) da Licenciatura em Engenharia Física Aplicada no **Instituto Superior de Engenharia de Lisboa (ISEL)**. 

O objetivo principal é calcular numericamente a distribuição de probabilidades do número obtido por cada dado num sistema com $N$ dados e energia total constante, focando a simulação para as energias médias $\bar{\epsilon} \in \{2, 3, 4, 5\}$. Os resultados demonstram, através de um algoritmo numérico simples, que a função de probabilidade do sistema converge para a **Distribuição de Boltzmann** no limite termodinâmico.

**Autores:**
* Tiago Bernardo (53117)
* Gabriel Marques (53087)

## ⚙️ O Algoritmo
O modelo numérico utiliza uma amostragem baseada no método de Monte Carlo com as seguintes regras fundamentais:
1. **Inicialização:** A energia total do sistema é fixada atribuindo o valor da energia média desejada a todos os $N$ dados simultaneamente.
2. **Evolução (Balanço Energético):** Em cada passo, dois dados são selecionados aleatoriamente. As suas energias são alteradas através da definição de limites rígidos ($\max(1, s-k)$ e $\min(k, s-1)$), garantindo que a soma de ambos ($s$) e a energia total do sistema permanecem inalteradas.
3. **Descorrelação:** O passo de perturbação anterior é repetido $N$ vezes iterativas (uma varredura completa) para garantir que a nova configuração gerada seja suficientemente descorrelacionada e válida como amostra estatística independente para a recolha de dados.

## 🛠️ Tecnologias Utilizadas
* **Python 3.x**
* **NumPy:** Para manipulação eficiente de matrizes, vetores e geração de números aleatórios.
* **Matplotlib:** Para a visualização dos resultados estatísticos e exportação automática dos gráficos (com formatação otimizada para relatórios académicos).