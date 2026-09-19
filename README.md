# Distribuição de Probabilidades: Sistema de N Dados com Energia Constante

## 📖 Sobre o Projeto
Este repositório contém o programa numérico desenvolvido para o 1º Trabalho da unidade curricular de Física Estatística (3º ano, 5º semestre) da Licenciatura em Física Aplicada no ISEL. 

O objetivo principal é calcular numericamente a distribuição de probabilidades do número obtido por cada dado num sistema com $N$ dados e energia total constante, focando a simulação para as energias médias $\bar{\epsilon} \in \{2, 3, 4, 5\}$, conforme descrito na secção 1.2 da sebenta da disciplina. Os resultados demonstram, através de um algoritmo numérico simples, que a função de probabilidade do sistema segue a **Distribuição de Boltzmann**.

## ⚙️ O Algoritmo
O modelo numérico utiliza um método iterativo de Monte Carlo com as seguintes regras:
1. **Inicialização:** A energia total do sistema é fixada atribuindo o valor da energia média desejada a todos os $N$ dados.
2. **Evolução (Balanço Energético):** Em cada passo, dois dados são selecionados aleatoriamente. As suas energias são alteradas através da definição de limites ($max(1, s-k)$ e $min(k, s-1)$), garantindo que a soma de ambos e a conservação da energia total do sistema permanecem inalteradas.
3. **Descorrelação:** O passo anterior é repetido $N$ vezes iterativas para garantir que a nova configuração gerada seja suficientemente descorrelacionada e válida como amostra estatística representativa para a recolha de dados.

## 🛠️ Tecnologias Utilizadas
* **Python 3.x**
* **NumPy:** Para manipulação eficiente de vetores e geração de números aleatórios.
* **Matplotlib:** Para a visualização dos resultados estatísticos e exportação automática dos gráficos.

## 🚀 Como Executar

1. Clona este repositório para a tua máquina local:
   ```bash
   git clone [https://github.com/teu-utilizador/nome-do-repositorio.git](https://github.com/teu-utilizador/nome-do-repositorio.git)