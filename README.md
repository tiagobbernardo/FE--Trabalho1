# Distribuição de Probabilidades: Sistema de N Dados com Energia Constante

## 📖 Sobre o Projeto
Este repositório contém o programa numérico desenvolvido para o 1º Trabalho da unidade curricular de Física Estatística (3º ano, 5º semestre) da licenciatura em Física Aplicada no ISEL. 

O objetivo principal é calcular numericamente a distribuição de probabilidades do número obtido por cada dado num sistema com $N$ dados e energia total constante, conforme descrito na secção 1.2 da sebenta da disciplina. O resultado demonstra, através de um algoritmo numérico simples, que a função de probabilidade do sistema segue a **Distribuição de Boltzmann**[cite: 1].

## ⚙️ O Algoritmo
O modelo numérico utiliza um método iterativo com as seguintes regras:
1. **Inicialização:** A energia total do sistema é fixada atribuindo o valor da energia média desejada (ex: $\bar{\epsilon} = 2$) a todos os $N$ dados[cite: 1].
2. **Evolução:** Em cada passo, dois dados são selecionados aleatoriamente. As suas energias são alteradas, garantindo que a soma de ambos permanece inalterada (conservando assim a energia total do sistema)[cite: 1].
3. **Descorrelação:** O passo anterior é repetido um número de vezes pelo menos igual a $N$ para garantir que a nova configuração gerada seja suficientemente descorrelacionada e válida como amostra estatística representativa[cite: 1].

## 🛠️ Tecnologias Utilizadas
* **Python 3.x**
* **NumPy:** Para manipulação eficiente de vetores e geração de números aleatórios.
* **Matplotlib:** Para a visualização dos resultados estatísticos através de gráficos.

## 🚀 Como Executar

1. Clona este repositório para a tua máquina local:
   ```bash
   git clone [https://github.com/teu-utilizador/nome-do-repositorio.git](https://github.com/teu-utilizador/nome-do-repositorio.git)