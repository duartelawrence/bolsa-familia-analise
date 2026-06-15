# Bolsa Família — Beneficiários, Valor e Desigualdade Social no Brasil

Análise exploratória dos dados do maior programa de transferência de renda do Brasil, cobrindo o período 2019–2024 e as transições entre Bolsa Família, Auxílio Brasil e Bolsa Família (novo).

---

## Perguntas respondidas

1. Como evoluiu o número de famílias beneficiárias entre 2019 e 2024?
2. O valor médio do benefício é suficiente para superar a linha de pobreza?
3. Quais estados e regiões concentram mais beneficiários?
4. Existe correlação entre IDH e dependência do programa?
5. Qual foi o impacto real da transição Bolsa Família → Auxílio Brasil → Bolsa Família (novo)?

---

## Principais achados

- Em 2023, o programa atingiu **21 milhões de famílias** — maior patamar histórico
- O valor médio triplicou entre 2019 (R$186) e 2023 (R$680)
- Mesmo com o aumento, o benefício médio cobre ~87% da linha de pobreza familiar
- O **Nordeste** concentra ~45% dos beneficiários, reflexo da pobreza histórica da região
- Correlação de ~-0,75 entre IDH estadual e beneficiários per capita

---

## Estrutura

```
bolsa-familia-analise/
├── data/
│   ├── raw/                        # Dados brutos do Portal da Transparência (gitignored)
│   └── sample/                     # Dados de amostra para demo imediata
├── notebooks/
│   └── analise_bolsa_familia.ipynb # Análise completa com narrativa
├── outputs/
│   └── figures/                    # Gráficos gerados
├── scripts/
│   └── gerar_dados_exemplo.py      # Gera data/sample/ com valores realistas
└── src/
    └── loader.py                   # Funções de carga de dados
```

---

## Como reproduzir

**Com dados de amostra (imediato):**
```bash
pip install -r requirements.txt
python scripts/gerar_dados_exemplo.py
jupyter notebook notebooks/analise_bolsa_familia.ipynb
```

**Com dados reais:**

Baixe os dados mensais em [portaldatransparencia.gov.br](https://portaldatransparencia.gov.br/download-de-dados/bolsa-familia-pagamentos) e coloque os CSVs em `data/raw/`.

---

## Fonte dos dados

Portal da Transparência do Governo Federal — dados públicos, sem restrição de uso.  
IBGE — IDH e indicadores socioeconômicos estaduais.
