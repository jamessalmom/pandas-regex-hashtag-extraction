# Extração de hashtags

Método pandas + regex usando `str.findall` para extrair TODAS as
ocorrências de um padrão em cada linha (diferente de `str.extract`,
que pega só a primeira).

## Uso
```python
import pandas as pd
from extrair_hashtags import extrair_hashtags

df = pd.DataFrame({"post": ["Ótimo dia! #python #pandas #dados"]})
df = extrair_hashtags(df, "post")
```
