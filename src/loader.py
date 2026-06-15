"""
Funções utilitárias para carga dos dados do Bolsa Família.
Fonte: Portal da Transparência — dados.gov.br
"""
import pandas as pd
from pathlib import Path

_BASE      = Path(__file__).parent.parent   # raiz do projeto
RAW_DIR    = _BASE / "data" / "raw"
SAMPLE_DIR = _BASE / "data" / "sample"

REGIOES = {
    "AC": "Norte", "AM": "Norte", "AP": "Norte", "PA": "Norte",
    "RO": "Norte", "RR": "Norte", "TO": "Norte",
    "AL": "Nordeste", "BA": "Nordeste", "CE": "Nordeste", "MA": "Nordeste",
    "PB": "Nordeste", "PE": "Nordeste", "PI": "Nordeste", "RN": "Nordeste", "SE": "Nordeste",
    "DF": "Centro-Oeste", "GO": "Centro-Oeste", "MS": "Centro-Oeste", "MT": "Centro-Oeste",
    "ES": "Sudeste", "MG": "Sudeste", "RJ": "Sudeste", "SP": "Sudeste",
    "PR": "Sul", "RS": "Sul", "SC": "Sul",
}

PROGRAMA_NOME = {
    2019: "Bolsa Família",
    2020: "Bolsa Família",
    2021: "Bolsa Família / Auxílio Brasil",
    2022: "Auxílio Brasil",
    2023: "Bolsa Família (novo)",
    2024: "Bolsa Família (novo)",
}


def _ler(nome: str) -> pd.DataFrame:
    for d in [RAW_DIR, SAMPLE_DIR]:
        p = d / nome
        if p.exists():
            return pd.read_csv(p)
    raise FileNotFoundError(
        f"{nome} não encontrado. Execute: python scripts/gerar_dados_exemplo.py"
    )


def load_nacional() -> pd.DataFrame:
    return _ler("resumo_nacional_mensal.csv")


def load_estados() -> pd.DataFrame:
    return _ler("resumo_por_estado.csv")


def load_regioes() -> pd.DataFrame:
    return _ler("resumo_por_regiao.csv")


def load_perfil_estados() -> pd.DataFrame:
    return _ler("perfil_estados.csv")
