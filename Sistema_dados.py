import numpy as np
import matplotlib.pyplot as plt

def simular_boltzmann(energia_media, N, k, Nc):
    """
    Simula o sistema de N dados para uma dada energia média e 
    devolve a distribuição de probabilidades.
    """
    dados = np.full(N, energia_media)
    contagem_total = np.zeros(k)

    for _ in range(Nc):
        for _ in range(N):
            i, j = np.random.choice(N, 2, replace=False)
            soma = dados[i] + dados[j]
            
            lim_inf = max(1, soma - k)
            lim_sup = min(k, soma - 1)
            
            if lim_inf <= lim_sup:
                dados[i] = np.random.randint(lim_inf, lim_sup + 1)
                dados[j] = soma - dados[i]
                
        contagem_total += np.bincount(dados, minlength=k+1)[1:]
        
    return contagem_total / (Nc * N)

# 1. Definição de parâmetros principais
N = 200
k = 6
Nc = 10000
energias_medias = [2, 3, 4, 5]
energias = np.arange(1, k + 1)

resultados = {}
cores = {2: 'blue', 3: 'orange', 4: 'green', 5: 'red'}
marcadores = {2: 'o', 3: 's', 4: '^', 5: 'd'}

# 2. Executar simulações para cada energia média
print("A iniciar as simulações. Aguarde um momento...")
for e_med in energias_medias:
    print(f"A simular para energia média = {e_med}...")
    resultados[e_med] = simular_boltzmann(e_med, N, k, Nc)

# 3. Gerar e guardar os gráficos INDIVIDUAIS
for e_med in energias_medias:
    probs = resultados[e_med]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Gráfico da distribuição p(e) individual
    ax1.plot(energias, probs, marker=marcadores[e_med], linestyle='-', color=cores[e_med])
    ax1.set_xlabel(r'Energia $\epsilon$')
    ax1.set_ylabel(r'$p(\epsilon)$')
    ax1.set_title(rf'Distribuição de Probabilidade ($\bar{{\epsilon}} = {e_med}$)')
    ax1.grid(True, linestyle='--', alpha=0.6)
    
    # Gráfico do logaritmo ln(p(e)) individual
    probs_validas = np.where(probs > 0, probs, np.nan)
    ax2.plot(energias, np.log(probs_validas), marker=marcadores[e_med], linestyle='-', color=cores[e_med])
    ax2.set_xlabel(r'Energia $\epsilon$')
    ax2.set_ylabel(r'$\ln p(\epsilon)$')
    ax2.set_title(rf'Logaritmo da Distribuição ($\bar{{\epsilon}} = {e_med}$)')
    ax2.grid(True, linestyle='--', alpha=0.6)
    
    plt.tight_layout()
    nome_ficheiro = f'distribuicao_boltzmann_energia_{e_med}.png'
    plt.savefig(nome_ficheiro, dpi=300)
    plt.close(fig) # Fecha a figura para não misturar com as seguintes
    print(f"Gráfico individual guardado: '{nome_ficheiro}'")

# 4. Gerar e guardar o gráfico com todas as curvas SOBREPOSTAS
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

for e_med in energias_medias:
    probs = resultados[e_med]
    
    # Gráfico da distribuição p(e)
    ax1.plot(energias, probs, marker=marcadores[e_med], linestyle='-', 
             color=cores[e_med], label=rf'$\bar{{\epsilon}} = {e_med}$')
    
    # Gráfico do logaritmo ln(p(e))
    probs_validas = np.where(probs > 0, probs, np.nan)
    ax2.plot(energias, np.log(probs_validas), marker=marcadores[e_med], linestyle='--', 
             color=cores[e_med], label=rf'$\bar{{\epsilon}} = {e_med}$')

ax1.set_xlabel(r'Energia $\epsilon$')
ax1.set_ylabel(r'$p(\epsilon)$')
ax1.set_title('Distribuições de Probabilidade Sobrepostas')
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.6)

ax2.set_xlabel(r'Energia $\epsilon$')
ax2.set_ylabel(r'$\ln p(\epsilon)$')
ax2.set_title('Logaritmo das Distribuições')
ax2.legend()
ax2.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
nome_ficheiro_sobrepostas = 'distribuicao_boltzmann_todas_sobrepostas.png'
plt.savefig(nome_ficheiro_sobrepostas, dpi=300)
plt.close(fig)
print(f"Gráfico com todas as curvas sobrepostas guardado: '{nome_ficheiro_sobrepostas}'")