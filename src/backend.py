import pandas as pd
from contrato import Vendas


def process_excel(uploaded_file):
    try:
        df = pd.read_excel(uploaded_file)
        erros = []

        # verifica se há colunas extras no Dataframe
        extra_cols = set(df.columns) - set(Vendas.model_fields.keys())
        if extra_cols:
            return False, f"Colunas extras no arquivo: {', '.join(extra_cols)}"
        
        for index, row in df.iterrows():
            try:
                _ =Vendas(**row.to_dict())
            except Exception as e:
                erros.append(f"Erro na linha {index + 2}: {str(e)}")

        # retornando os erros encontrados
        return True, None
    
    except Exception as e:
        # se houver excessão ao processar o arquivo retorna erro e df vazio
        return pd.DataFrame(),  f"Erro ao processar o arquivo: {str(e)}"
