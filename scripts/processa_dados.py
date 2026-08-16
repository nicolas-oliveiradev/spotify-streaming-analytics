import glob
import json
import sqlite3
import pandas as pd

# 1. Unificar arquivos JSON do Spotify
arquivos_json = glob.glob("StreamingHistory_music_*.json")
dados_completos = []

for arquivo in arquivos_json:
    with open(arquivo, encoding="utf-8") as f:
        dados = json.load(f)
        dados_completos.extend(dados)

print(
    f"✅ Unificados {len(arquivos_json)} arquivos do Spotify! Total: {len(dados_completos)} linhas."
)

# 2. Criar DataFrame do Pandas
df = pd.DataFrame(dados_completos)

# 3. Renomear colunas (CORRIGIDO: 'artista' com 'a')
df = df.rename(
    columns={
        "endTime": "data_reproducao",
        "artistName": "artista",
        "trackName": "musica",
    }
)

# 4. Tratamento de Tempo
df["tempo_minutos"] = df["msPlayed"] / 60000
df["tempo_horas"] = df["tempo_minutos"] / 60

# 5. Criar chave unificada para o Top N do Power BI
df["musica_artista"] = df["musica"] + " - " + df["artista"]

# 6. Filtrar e ordenar colunas finais
colunas_finais = [
    "data_reproducao",
    "artista",
    "musica",
    "musica_artista",
    "msPlayed",
    "tempo_minutos",
    "tempo_horas",
]

df_limpo = df[colunas_finais].copy()

# Forçar tipos numéricos explícitos
df_limpo["tempo_minutos"] = df_limpo["tempo_minutos"].astype(float)
df_limpo["tempo_horas"] = df_limpo["tempo_horas"].astype(float)

# Tratamento de Tempo (Arredondado para 2 casas decimais)
df["tempo_minutos"] = (df["msPlayed"] / 60000).round(2)
df["tempo_horas"] = (df["tempo_minutos"] / 60).round(2)

# 7. Exportar para SQLite e CSV
conexao = sqlite3.connect("spotify_analytics.db")
df_limpo.to_sql("historico_musica", conexao, if_exists="replace", index=False)
conexao.close()

df_limpo.to_csv("spotify_limpo.csv", index=False, decimal=",", encoding="utf-8-sig")

print("🚀 Processamento e exportação concluídos com sucesso!")