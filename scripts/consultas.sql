-- 1. Visão Geral: Quantas reproduções totais e tempo total em horas?
SELECT 
    COUNT(*) AS total_reproducoes,
    ROUND(SUM(tempo_horas), 2) AS total_horas_ouvidas
FROM historico_musica;


-- 2. O seu TOP 10 Artistas mais ouvidos (por tempo em horas)
SELECT 
    artista,
    ROUND(SUM(tempo_horas), 2) AS horas_tocadas,
    COUNT(*) AS quantidade_músicas
FROM historico_musica
GROUP BY artista
ORDER BY horas_tocadas DESC
LIMIT 10;


-- 3. O seu TOP 10 Músicas mais ouvidas
SELECT 
    musica,
    artista,
    ROUND(SUM(tempo_minutos), 2) AS minutos_totais,
    COUNT(*) AS vezes_tocada
FROM historico_musica
GROUP BY musica, artista
ORDER BY vezes_tocada DESC
LIMIT 10;

--- Use CTRL + SHIFT + P para Query!
