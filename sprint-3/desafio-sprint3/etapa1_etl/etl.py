import pandas as pd
import numpy as np

def clean_data(input_file='concert_tours_by_women.csv', output_file='csv_limpo.csv'):
    """
    Limpa os dados do arquivo CSV de turnês, adaptado para a estrutura
    com a coluna 'Year(s)' e o nome 'Adjustedgross'.
    """
    try:
        # Carrega o dataset
        df = pd.read_csv(input_file)

        # --- Etapa de Limpeza e Transformação Adaptada ---

        # 1. Corrigir o nome da coluna 'Adjustedgross...'
        df.rename(columns={
            'Adjustedgross (in 2022 dollars)': 'Adjusted gross (in 2022 dollars)'
        }, inplace=True)

        # 2. Processar a coluna 'Year(s)' para criar 'Start year' e 'End year'
        df['Year(s)'] = df['Year(s)'].astype(str)
        split_years = df['Year(s)'].str.split('-')
        df['Start year'] = split_years.str[0]
        df['End year'] = split_years.str[-1]

        # 3. Limpar e converter colunas monetárias para tipo numérico (float)
        money_columns = ['Actual gross', 'Adjusted gross (in 2022 dollars)', 'Average gross']
        for col in money_columns:
            df[col] = df[col].astype(str).str.replace(r'[$,]', '', regex=True)
            df[col] = pd.to_numeric(df[col], errors='coerce')

        # 4. Converter outras colunas para os tipos de dados corretos
        df['Shows'] = pd.to_numeric(df['Shows'], errors='coerce')
        df['Start year'] = pd.to_numeric(df['Start year'], errors='coerce')
        df['End year'] = pd.to_numeric(df['End year'], errors='coerce')

        # 5. Remover linhas com valores nulos que possam ter surgido durante a conversão
        df.dropna(inplace=True)
        
        # 6. Garantir que os tipos de dados inteiros sejam corretos
        int_columns = ['Shows', 'Start year', 'End year']
        for col in int_columns:
            df[col] = df[col].astype(np.int64)

        # --- Etapa de Finalização (COM A CORREÇÃO) ---

        # 7. Ordenar os dados pela coluna 'Adjusted gross (in 2022 dollars)'
        df = df.sort_values(by='Adjusted gross (in 2022 dollars)', ascending=False)

        # 8. (NOVA LINHA) Remover a coluna 'Rank' original do CSV para evitar conflito.
        if 'Rank' in df.columns:
            df = df.drop(columns=['Rank'])

        # 9. Criar a nova coluna 'Rank' recalculada e na primeira posição
        df.insert(0, 'Rank', range(1, len(df) + 1))
        
        # 10. Selecionar e reordenar as colunas finais
        final_columns_order = [
            'Rank',
            'Actual gross',
            'Adjusted gross (in 2022 dollars)',
            'Artist',
            'Tour title',
            'Shows',
            'Average gross',
            'Start year',
            'End year'
        ]
        df = df[final_columns_order]

        # 11. Salvar o DataFrame limpo em um novo arquivo CSV
        df.to_csv(output_file, index=False)

        print(f"Limpeza de dados concluída. Arquivo salvo como '{output_file}'")

    except FileNotFoundError:
        print(f"Erro: O arquivo de entrada '{input_file}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == '__main__':
    clean_data()