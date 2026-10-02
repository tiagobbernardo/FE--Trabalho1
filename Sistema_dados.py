import numpy as np
import matplotlib.pyplot as plt

def simular_boltzmann(energia_media: int, n_dados: int, faces: int, n_configs: int) -> np.ndarray:
    """Executa a simulação de Monte Carlo para um sistema de N dados."""
    dados = np.full(n_dados, energia_media)
    contagem_total = np.zeros(faces)

    for _ in range(n_configs):
        for _ in range(n_dados):
            i, j = np.random.choice(n_dados, 2, replace=False)
            soma = dados[i] + dados[j]
            
            lim_inf = max(1, soma - faces)
            lim_sup = min(faces, soma - 1)
            
            if lim_inf <= lim_sup:
                dados[i] = np.random.randint(lim_inf, lim_sup + 1)
                dados[j] = soma - dados[i]
                
        contagem_total += np.bincount(dados, minlength=faces + 1)[1:]
        
    return contagem_total / (n_configs * n_dados)

def calcular_beta(energias: np.ndarray, probabilidades: np.ndarray) -> float:
    """Extrai o parâmetro beta através da regressão linear do logaritmo das probabilidades."""
    indices_validos = probabilidades > 0
    x = energias[indices_validos]
    y = np.log(probabilidades[indices_validos])
    
    declive, _ = np.polyfit(x, y, 1)
    return -declive

def gerar_graficos(resultados: dict, energias: np.ndarray, config_estilos: dict):
    """Gera e exporta os gráficos individuais e a sobreposição global."""
    
    # Configuração global dos tamanhos de letra
    plt.rcParams.update({
        'axes.titlesize': 28,    # Títulos dos gráficos
        'axes.labelsize': 24,    # Rótulos dos eixos X e Y
        'legend.fontsize': 18,   # Texto da legenda
        'xtick.labelsize': 15,   # eixo X
        'ytick.labelsize': 15    # eixo Y
    })

    fig_sobre, (ax1_sobre, ax2_sobre) = plt.subplots(1, 2, figsize=(14, 6))

    for e_med, probs in resultados.items():
        cor, marcador = config_estilos[e_med]
        probs_validas = np.where(probs > 0, probs, np.nan)
        log_probs = np.log(probs_validas)

        # Gráficos individuais
        fig_indiv, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        ax1.plot(energias, probs, marker=marcador, linestyle='-', color=cor)
        ax1.set(xlabel=r'Energia $\epsilon$', ylabel=r'$p(\epsilon)$', 
                title=rf'Distribuição de Probabilidade ($\bar{{\epsilon}} = {e_med}$)')
        ax1.grid(True, linestyle='--', alpha=0.6)
        
        ax2.plot(energias, log_probs, marker=marcador, linestyle='-', color=cor)
        ax2.set(xlabel=r'Energia $\epsilon$', ylabel=r'$\ln p(\epsilon)$', 
                title=rf'Logaritmo da Distribuição ($\bar{{\epsilon}} = {e_med}$)')
        ax2.grid(True, linestyle='--', alpha=0.6)
        
        fig_indiv.tight_layout()
        fig_indiv.savefig(f'distribuicao_boltzmann_energia_{e_med}.png', dpi=300)
        plt.close(fig_indiv)

        # Atualização dos gráficos sobrepostos
        label = rf'$\bar{{\epsilon}} = {e_med}$'
        ax1_sobre.plot(energias, probs, marker=marcador, linestyle='-', color=cor, label=label)
        ax2_sobre.plot(energias, log_probs, marker=marcador, linestyle='--', color=cor, label=label)

    # Formatação final da sobreposição
    ax1_sobre.set(xlabel=r'Energia $\epsilon$', ylabel=r'$p(\epsilon)$', title='Distribuições Sobrepostas')
    ax1_sobre.legend()
    ax1_sobre.grid(True, linestyle='--', alpha=0.6)

    ax2_sobre.set(xlabel=r'Energia $\epsilon$', ylabel=r'$\ln p(\epsilon)$', title='Logaritmo das Distribuições')
    ax2_sobre.legend()
    ax2_sobre.grid(True, linestyle='--', alpha=0.6)

    fig_sobre.tight_layout()
    fig_sobre.savefig('distribuicao_boltzmann_todas_sobrepostas.png', dpi=300)
    plt.close(fig_sobre)

def main():
    N = 4
    K = 6
    NC = 10000
    ENERGIAS_MEDIAS = [2, 3, 4, 5]
    
    energias = np.arange(1, K + 1)
    resultados = {}
    estilos = {
        2: ('blue', 'o'), 
        3: ('orange', 's'), 
        4: ('green', '^'), 
        5: ('red', 'd')
    }

    print("A executar simulações numéricas...")
    for e_med in ENERGIAS_MEDIAS:
        resultados[e_med] = simular_boltzmann(e_med, N, K, NC)

    print("A exportar gráficos...")
    gerar_graficos(resultados, energias, estilos)

    print("\n--- Resultados Analíticos (Parâmetro Beta) ---")
    for e_med, probs in resultados.items():
        beta = calcular_beta(energias, probs)
        print(f"Energia Média = {e_med}  ->  Beta = {beta:.4f}")

if __name__ == "__main__":
    main()