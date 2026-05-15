# Max Impact Engine
** THIS IS NOT A GOOGLE OFFICIAL TOOL.**
This Python application automates a comprehensive marketing analytics workflow. It begins by analyzing historical data to find and validate the impact of specific marketing campaigns, then performs a holistic **Global Saturation Analysis** to provide strategic, forward-looking budget recommendations based on diminishing returns.

## Features

*   **Interactive Dashboard UI:** Run analyses seamlessly via a complete, interactive Streamlit frontend with a secure Google Login and visual file uploaders.
*   **Configuration Driven:** All parameters and file paths can also be managed in central `config.json` files for CLI execution.
*   **Automated Event Detection:** Scans investment data to automatically find and validate periods of significant budget changes.
*   **Causal Impact Analysis:** Uses `statsmodels` to build a time-series model that isolates the incremental impact of past marketing campaigns.
*   **Global Elasticity Analysis:** After analyzing individual events, the script runs a holistic analysis on the entire dataset to model long-term channel contributions and diminishing returns.
*   **Dynamic Financial Guardrails:** Strictly bounds investment recommendations based on real-world business constraints like Target CPA and Target ROAS.
*   **Automated Reporting:** Generates detailed HTML reports with strategic narratives powered by the Gemini API, alongside clean offline CSV and Markdown fallbacks.
*   **Usage Tracking:** Automatically logs execution statistics to stdout for organizational tracking.

---
## Guia de Uso da Interface (Streamlit)

A interface do **Max Impact Engine** foi projetada para ser intuitiva. Abaixo, detalhamos como preencher cada campo na aba **Setup (Nova Otimização)**:

### 1. Informações do Projeto
*   **Nome do Anunciante:** O nome da empresa ou projeto (ex: "E-commerce_Demo").
*   **Setor do Cliente:** O mercado de atuação (ex: "Varejo", "Tecnologia").
*   **Objetivo de Negócio:** Uma breve descrição do que se busca (ex: "Maximizar vendas com ROI acima de 2.0").

### 2. Configuração de KPI e Financeiro
*   **Nome do KPI de Negócio:** Como você chama sua conversão (ex: "Compras", "Leads").
*   **Nome da Coluna do KPI:** O nome exato da coluna no seu arquivo de performance. 
    *   *Dica: O motor agora tenta detectar automaticamente se você deixar como "Sessions" e seu arquivo tiver colunas como "Purchases" ou "Vendas".*
*   **Ticket Médio (R$):** Valor médio de cada conversão. Se for 0, o motor focará em volume (CPA).
*   **Taxa de Conversão (KPI -> BO):** Se o seu KPI for algo intermediário (ex: cliques ou sessões), qual a taxa que vira venda final? (ex: 0.01 para 1%).

### 3. Upload de Arquivos (CSV)
*   **Arquivo de Investimento (Obrigatório):** Deve conter as colunas de data e investimento por canal.
*   **Arquivo de Performance (Obrigatório):** Deve conter a data e o volume do KPI escolhido.
*   **Arquivo de Tendências (Opcional):** Dados de mercado (ex: Google Trends) para ajudar o modelo a isolar sazonalidade.

### 4. Limites Estratégicos (Financial Guardrails)
*   **Target CPA / ROAS:** Defina seus limites de eficiência. O motor não recomendará investimentos que ultrapassem esses custos.
*   **P-Value Threshold:** Sensibilidade estatística (padrão 0.1). Quanto menor, mais rigoroso o modelo é para validar um "sucesso".

---

## Como a Análise Funciona

O script é um motor que executa a análise em duas etapas distintas:

### Estágio 1: Análise Causal de Eventos (Isolamento de Impacto)

1.  **Detecção de Eventos:** O script analisa o histórico de investimentos para encontrar mudanças significativas de verba (aumentos ou reduções bruscas).
2.  **Modelagem de Impacto Causal:** Para cada evento, ele constrói um modelo de séries temporais que prevê o que teria acontecido *sem* aquela mudança de investimento. A diferença entre o real e o previsto é o **Lift Incremental**.
3.  **Validação Estatística:** Apenas eventos com significância estatística (p-value baixo) são validados como sucessos ou falhas estratégicas.

### Estágio 2: Análise de Saturação Global (Estratégia de Longo Prazo)

1.  **Modelagem de Elasticidade:** O motor analisa todo o período histórico para entender a contribuição de cada canal, considerando efeitos de **Adstock** (memória do marketing) e **Saturação** (rendimentos decrescentes).
2.  **Otimização de Portfólio:** Com base nas curvas de resposta de cada canal, o sistema redistribui a verba para encontrar o ponto de **Máxima Eficiência** e o **Limite Estratégico** de investimento.
3.  **Relatórios com Gemini:** Os achados são compilados em relatórios HTML com uma narrativa estratégica gerada pela IA do Gemini.

---

## Começando

### 1. Pré-requisitos
- Python 3.9+ (Testado na versão 3.9.6)
- `venv` para gerenciamento de ambiente virtual

### 2. Instalação

**a. Clone o repositório:**
```bash
git clone <url-do-repositorio>
cd opportunity-engine-hervas
```

**b. Crie e ative o ambiente virtual:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**c. Instale as dependências:**
```bash
pip install -r requirements.txt
```

### 3. Execução via Dashboard (Recomendado)

```bash
streamlit run scripts/streamlit_app.py
```

1. Acesse `http://localhost:8501`.
2. Vá na aba **Setup (Nova Otimização)**.
3. Faça o upload dos arquivos e insira sua **Gemini API Key**.
4. Clique em **"Construir Motor de Oportunidades"**.

---

## Saídas (Outputs)

Os resultados são organizados na pasta `outputs/` por nome do anunciante:

### 1. Relatório Estratégico Global
- **Local:** `outputs/<anunciante>/global_saturation_analysis/`
- **Destaque:** `global_report.html` (Relatório completo com insights do Gemini).

### 2. Relatórios de Eventos Específicos
- **Local:** `outputs/<anunciante>/<canal>/<data_do_evento>/`
- **Destaque:** `gemini_report_... .html` (Análise detalhada daquele investimento específico).
