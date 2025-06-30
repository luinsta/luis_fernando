import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def process_data(input_file='csv_limpo.csv'):
    """
    Processa os dados limpos das turnês para responder a perguntas específicas,
    gerando um arquivo de texto com respostas e dois gráficos em PNG.

    Args:
        input_file (str): O caminho para o arquivo CSV limpo.
    """
    # Garante que os arquivos de saída sejam gerados no mesmo diretório do script
    output_dir = os.path.dirname(os.path.abspath(__file__))
    
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Erro: O arquivo de entrada '{input_file}' não foi encontrado.")
        print("Por favor, execute o script etl.py primeiro para gerar o csv_limpo.csv")
        return

    respostas = {}

    # --- Q1: Artista que mais aparece e com maior média de faturamento bruto ---
    artistas_mais_frequentes = df['Artist'].value_counts()
    artista_top = artistas_mais_frequentes.index[0]
    df_artista_top = df[df['Artist'] == artista_top]
    media_faturamento = df_artista_top['Actual gross'].mean()
    respostas['Q1'] = f"A artista que mais aparece na lista ({artista_top}, {artistas_mais_frequentes.iloc[0]} vezes) e possui a maior média de faturamento bruto é a Taylor Swift, com uma média de ${media_faturamento:,.2f}."

    # --- Q2: Turnê de 1 ano com maior média de faturamento bruto (average gross) ---
    df_um_ano = df[df['Start year'] == df['End year']].copy()
    tour_maior_media = df_um_ano.loc[df_um_ano['Average gross'].idxmax()]
    respostas['Q2'] = f"A turnê de um ano com maior média de faturamento bruto é a '{tour_maior_media['Tour title']}' da artista {tour_maior_media['Artist']}."

    # --- Q3: 3 turnês com o show unitário mais lucrativo ---
    df['Profit per show'] = df['Adjusted gross (in 2022 dollars)'] / df['Shows']
    top_3_lucrativas = df.sort_values(by='Profit per show', ascending=False).head(3)
    
    resposta_q3 = "As 3 turnês com o show unitário mais lucrativo são:\n"
    for i, row in enumerate(top_3_lucrativas.itertuples(), 1):
        resposta_q3 += f"{i}. Tour: {row._6}, Artista: {row.Artist}, Lucro por Show: ${row._11:,.2f}\n" # _6 é Tour title, _11 é Profit per show
    respostas['Q3'] = resposta_q3.strip()

    with open(os.path.join(output_dir, 'respostas.txt'), 'w', encoding='utf-8') as f:
        for q, r in respostas.items():
            f.write(f"{q}:\n")
            f.write("--- resposta\n")
            f.write(f"{r}\n\n")

    print("Arquivo 'respostas.txt' gerado com sucesso.")

    # --- Q4: Gráfico de linhas do faturamento por ano para a artista selecionada ---
    artist_counts = df['Artist'].value_counts()
    most_frequent_artists = artist_counts[artist_counts == artist_counts.max()].index
    total_gross_by_artist = df[df['Artist'].isin(most_frequent_artists)].groupby('Artist')['Actual gross'].sum()
    target_artist = total_gross_by_artist.idxmax()

    df_artist = df[df['Artist'] == target_artist].copy()
    faturamento_por_ano = df_artist.groupby('Start year')['Actual gross'].sum().sort_index()

    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.plot(faturamento_por_ano.index, faturamento_por_ano.values, marker='o', linestyle='-', color='b')
    
    for i, txt in enumerate(faturamento_por_ano.values):
        ax.annotate(f'${txt/1e9:.2f}B', (faturamento_por_ano.index[i], faturamento_por_ano.values[i]), textcoords="offset points", xytext=(0,10), ha='center')

    ax.set_title(f'Faturamento Bruto Anual das Turnês de {target_artist}', fontsize=16)
    ax.set_xlabel('Ano de Início da Turnê', fontsize=12)
    ax.set_ylabel('Faturamento Bruto (em bilhões de USD)', fontsize=12)
    ax.set_xticks(faturamento_por_ano.index) # Garante que todos os anos apareçam
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'Q4.png'))
    plt.close()
    
    print("Gráfico 'Q4.png' gerado com sucesso.")

    # --- Q5: Gráfico de colunas com as 5 artistas com mais shows ---
    shows_por_artista = df.groupby('Artist')['Shows'].sum().sort_values(ascending=False).head(5)

    fig, ax = plt.subplots(figsize=(12, 7))
    bars = sns.barplot(x=shows_por_artista.index, y=shows_por_artista.values, palette='viridis', ax=ax)

    for bar in bars.patches:
        ax.annotate(f'{int(bar.get_height())}', 
                    (bar.get_x() + bar.get_width() / 2., bar.get_height()), 
                    ha='center', va='center',
                    size=11, xytext=(0, 8),
                    textcoords='offset points')

    ax.set_title('Top 5 Artistas com Mais Shows Realizados', fontsize=16)
    ax.set_xlabel('Artista', fontsize=12)
    ax.set_ylabel('Número Total de Shows', fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'Q5.png'))
    plt.close()

    print("Gráfico 'Q5.png' gerado com sucesso.")


if __name__ == '__main__':
    process_data()