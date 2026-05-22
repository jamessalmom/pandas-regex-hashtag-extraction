"""
Extração de múltiplas ocorrências com str.findall.

Diferente de str.extract (que pega só o primeiro match), findall retorna
uma lista com todas as ocorrências do padrão em cada linha.
"""
import pandas as pd


def extrair_hashtags(df: pd.DataFrame, coluna: str) -> pd.DataFrame:
    """
    Extrai todas as hashtags de um texto, retornando uma lista por linha,
    além da contagem de hashtags encontradas.

    Exemplo:
        df = extrair_hashtags(df, 'post')
    """
    df[f'{coluna}_hashtags'] = df[coluna].astype(str).str.findall(r'#(\w+)')
    df[f'{coluna}_qtd_hashtags'] = df[f'{coluna}_hashtags'].str.len()
    return df


if __name__ == "__main__":
    df = pd.DataFrame({"post": ["Ótimo dia! #python #pandas #dados", "sem hashtag"]})
    print(extrair_hashtags(df, "post"))
