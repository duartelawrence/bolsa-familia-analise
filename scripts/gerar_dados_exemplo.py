"""
Gera dados de amostra realistas do Bolsa Família para demonstração.
Valores baseados em estatísticas públicas do Portal da Transparência e IBGE.
Execute: python scripts/gerar_dados_exemplo.py
"""
import pandas as pd
import numpy as np
from pathlib import Path

np.random.seed(42)
OUT = Path("data/sample")
OUT.mkdir(parents=True, exist_ok=True)

# ── Perfil de cada estado ─────────────────────────────────────────────────────
ESTADOS = {
    "AC": {"regiao": "Norte",        "benef_2023": 95_000,    "idh": 0.663, "pobreza": 32.7, "pop": 906_876},
    "AL": {"regiao": "Nordeste",     "benef_2023": 650_000,   "idh": 0.649, "pobreza": 48.1, "pop": 3_351_543},
    "AM": {"regiao": "Norte",        "benef_2023": 420_000,   "idh": 0.674, "pobreza": 33.4, "pop": 4_269_995},
    "AP": {"regiao": "Norte",        "benef_2023": 105_000,   "idh": 0.686, "pobreza": 40.3, "pop": 877_613},
    "BA": {"regiao": "Nordeste",     "benef_2023": 2_800_000, "idh": 0.660, "pobreza": 43.2, "pop": 14_873_064},
    "CE": {"regiao": "Nordeste",     "benef_2023": 1_380_000, "idh": 0.682, "pobreza": 40.8, "pop": 9_187_103},
    "DF": {"regiao": "Centro-Oeste", "benef_2023": 145_000,   "idh": 0.824, "pobreza": 10.2, "pop": 3_094_325},
    "ES": {"regiao": "Sudeste",      "benef_2023": 350_000,   "idh": 0.740, "pobreza": 22.4, "pop": 4_108_508},
    "GO": {"regiao": "Centro-Oeste", "benef_2023": 410_000,   "idh": 0.735, "pobreza": 21.3, "pop": 7_206_589},
    "MA": {"regiao": "Nordeste",     "benef_2023": 1_780_000, "idh": 0.637, "pobreza": 53.1, "pop": 7_153_262},
    "MG": {"regiao": "Sudeste",      "benef_2023": 1_380_000, "idh": 0.731, "pobreza": 23.5, "pop": 21_411_923},
    "MS": {"regiao": "Centro-Oeste", "benef_2023": 215_000,   "idh": 0.729, "pobreza": 23.7, "pop": 2_833_742},
    "MT": {"regiao": "Centro-Oeste", "benef_2023": 220_000,   "idh": 0.725, "pobreza": 23.1, "pop": 3_658_813},
    "PA": {"regiao": "Norte",        "benef_2023": 1_490_000, "idh": 0.646, "pobreza": 46.3, "pop": 8_777_124},
    "PB": {"regiao": "Nordeste",     "benef_2023": 720_000,   "idh": 0.673, "pobreza": 42.6, "pop": 4_059_905},
    "PE": {"regiao": "Nordeste",     "benef_2023": 1_300_000, "idh": 0.673, "pobreza": 40.3, "pop": 9_674_793},
    "PI": {"regiao": "Nordeste",     "benef_2023": 680_000,   "idh": 0.655, "pobreza": 48.9, "pop": 3_289_290},
    "PR": {"regiao": "Sul",          "benef_2023": 480_000,   "idh": 0.749, "pobreza": 17.3, "pop": 11_516_840},
    "RJ": {"regiao": "Sudeste",      "benef_2023": 910_000,   "idh": 0.761, "pobreza": 27.8, "pop": 17_463_349},
    "RN": {"regiao": "Nordeste",     "benef_2023": 490_000,   "idh": 0.684, "pobreza": 36.9, "pop": 3_560_903},
    "RO": {"regiao": "Norte",        "benef_2023": 175_000,   "idh": 0.690, "pobreza": 30.2, "pop": 1_815_278},
    "RR": {"regiao": "Norte",        "benef_2023": 70_000,    "idh": 0.707, "pobreza": 31.5, "pop": 652_713},
    "RS": {"regiao": "Sul",          "benef_2023": 530_000,   "idh": 0.769, "pobreza": 15.8, "pop": 11_466_630},
    "SC": {"regiao": "Sul",          "benef_2023": 250_000,   "idh": 0.774, "pobreza": 10.2, "pop": 7_762_154},
    "SE": {"regiao": "Nordeste",     "benef_2023": 310_000,   "idh": 0.678, "pobreza": 39.4, "pop": 2_338_474},
    "SP": {"regiao": "Sudeste",      "benef_2023": 1_720_000, "idh": 0.783, "pobreza": 19.8, "pop": 44_420_459},
    "TO": {"regiao": "Norte",        "benef_2023": 180_000,   "idh": 0.699, "pobreza": 34.1, "pop": 1_607_363},
}

# Fator de escala por ano (relativo a 2023)
ESCALA_BENEF = {2019: 0.62, 2020: 0.68, 2021: 0.70, 2022: 0.87, 2023: 1.00, 2024: 0.99}
VALOR_MEDIO  = {2019: 186,  2020: 190,  2021: 197,  2022: 408,  2023: 680,  2024: 682}
PROGRAMA     = {
    2019: "Bolsa Família",
    2020: "Bolsa Família",
    2021: "Bolsa Família / Auxílio Brasil",
    2022: "Auxílio Brasil",
    2023: "Bolsa Família (novo)",
    2024: "Bolsa Família (novo)",
}
ANOS = [2019, 2020, 2021, 2022, 2023, 2024]


# ── 1. resumo_por_estado.csv ──────────────────────────────────────────────────
rows = []
for ano in ANOS:
    for uf, info in ESTADOS.items():
        b = int(info["benef_2023"] * ESCALA_BENEF[ano] * np.random.uniform(0.97, 1.03))
        vm = round(VALOR_MEDIO[ano] * np.random.uniform(0.95, 1.05), 2)
        rows.append({
            "ANO": ano, "UF": uf, "REGIAO": info["regiao"],
            "BENEFICIARIOS": b, "VALOR_MEDIO": vm,
            "VALOR_TOTAL": round(b * vm / 1e6, 2),  # em milhões R$
        })
df_estados = pd.DataFrame(rows)
df_estados.to_csv(OUT / "resumo_por_estado.csv", index=False, encoding="utf-8-sig")
print(f"  resumo_por_estado.csv  ({len(df_estados)} linhas)")


# ── 2. resumo_por_regiao.csv ──────────────────────────────────────────────────
df_reg = (
    df_estados.groupby(["ANO", "REGIAO"])
    .agg(BENEFICIARIOS=("BENEFICIARIOS", "sum"),
         VALOR_TOTAL=("VALOR_TOTAL", "sum"))
    .reset_index()
)
df_reg["VALOR_MEDIO"] = (df_reg["VALOR_TOTAL"] * 1e6 / df_reg["BENEFICIARIOS"]).round(2)
df_reg.to_csv(OUT / "resumo_por_regiao.csv", index=False, encoding="utf-8-sig")
print(f"  resumo_por_regiao.csv  ({len(df_reg)} linhas)")


# ── 3. resumo_nacional_mensal.csv ─────────────────────────────────────────────
rows = []
for ano in ANOS:
    total_base = df_estados[df_estados["ANO"] == ano]["BENEFICIARIOS"].sum()
    for mes in range(1, 13):
        # Leve sazonalidade — pico em dez/jan
        sazon = 1.0 + 0.02 * np.sin((mes - 1) * np.pi / 6)
        b = int(total_base * sazon * np.random.uniform(0.99, 1.01))
        vm = round(VALOR_MEDIO[ano] * np.random.uniform(0.98, 1.02), 2)

        # Transição brusca em nov/2021 (Auxílio Brasil) e jan/2023 (novo BF)
        prog = PROGRAMA[ano]
        if ano == 2021 and mes >= 11:
            b   = int(b * 1.22)
            vm  = round(vm * 1.15, 2)
            prog = "Auxílio Brasil"

        rows.append({
            "ANO": ano, "MES": mes,
            "DATA": f"{ano}-{mes:02d}-01",
            "PROGRAMA": prog,
            "BENEFICIARIOS": b,
            "VALOR_MEDIO": vm,
            "VALOR_TOTAL_MM": round(b * vm / 1e9, 3),  # bilhões R$
        })
df_nac = pd.DataFrame(rows)
df_nac.to_csv(OUT / "resumo_nacional_mensal.csv", index=False, encoding="utf-8-sig")
print(f"  resumo_nacional_mensal.csv  ({len(df_nac)} linhas)")


# ── 4. perfil_estados.csv ─────────────────────────────────────────────────────
rows = []
for uf, info in ESTADOS.items():
    b23 = df_estados[(df_estados["ANO"] == 2023) & (df_estados["UF"] == uf)]["BENEFICIARIOS"].values[0]
    rows.append({
        "UF": uf, "REGIAO": info["regiao"],
        "BENEFICIARIOS_2023": b23,
        "POPULACAO": info["pop"],
        "BENEF_PER_100K": round(b23 / info["pop"] * 100_000, 1),
        "IDH": info["idh"],
        "POBREZA_PCT": info["pobreza"],
    })
df_perf = pd.DataFrame(rows)
df_perf.to_csv(OUT / "perfil_estados.csv", index=False, encoding="utf-8-sig")
print(f"  perfil_estados.csv  ({len(df_perf)} linhas)")

print("\nDados de amostra gerados em data/sample/")
