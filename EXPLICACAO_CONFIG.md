### 📘 Guia Detalhado do `config.json`

Este guia explica cada linha do arquivo de configuração para que você saiba exatamente o que mudar em cada novo projeto.

#### **1. Identificação e Contexto**
*   **`"advertiser_name": "Generic Advertiser"`**
    *   **Descrição:** O nome do cliente ou projeto.
    *   **Por que alterar?** Este nome será usado para criar as pastas de resultados em `outputs/`. Altere para cada novo cliente para não sobrescrever os dados de outros.
*   **`"client_industry": "Retail"`**
    *   **Descrição:** O setor de atuação do cliente (Varejo, Tech, Educação, etc).
    *   **Por que alterar?** A inteligência artificial (Gemini) usa isso para entender a sazonalidade e os desafios típicos do setor ao escrever o relatório.
*   **`"client_business_goal": "increase online sales."`**
    *   **Descrição:** O objetivo principal do negócio.
    *   **Por que alterar?** Orienta o "tom" do relatório da IA. Se o foco for "Market Share" ou "ROI", o texto final será diferente.
*   **`"primary_business_metric_name": "Conversions"`**
    *   **Descrição:** O nome amigável do seu KPI (ex: "Compras", "Leads").
    *   **Por que alterar?** É o nome que aparecerá nos eixos dos gráficos e nos títulos dos relatórios.

#### **2. Caminhos de Arquivos (Inputs)**
*   **`"investment_file_path": "..."`**
    *   **Descrição:** Onde está o arquivo com os custos diários por canal.
*   **`"performance_file_path": "..."`**
    *   **Descrição:** Onde está o arquivo com os resultados diários (KPI).
*   **`"generic_trends_file_path": "..."`**
    *   **Descrição:** Opcional. Dados de mercado (ex: Google Trends).
    *   **Por que alterar?** Para cada projeto, seus dados estarão em pastas diferentes. Garanta que o caminho aponte para o arquivo correto.

#### **3. Parâmetros de Negócio**
*   **`"performance_kpi_column": "Sessions"`**
    *   **Descrição:** O nome exato da coluna de resultado no seu arquivo CSV de performance.
    *   **Por que alterar?** Se no seu CSV a coluna se chama "Vendas" e aqui estiver "Sessions", o motor vai dar erro.
*   **`"average_ticket": 100`**
    *   **Descrição:** O valor médio (em R$) de cada conversão.
    *   **Por que alterar?** Essencial para calcular o **ROI** e a **Receita Projetada**. Se o cliente vende carros, aqui seria 50.000; se vende meias, seria 20.
*   **`"conversion_rate_from_kpi_to_bo": 0.05`**
    *   **Descrição:** Taxa de conversão do seu KPI para venda real (0.05 = 5%).
    *   **Por que alterar?** Use se o seu KPI for algo intermediário (ex: Sessões ou Cliques). Se o seu KPI já for a venda final, deixe como `1.0`.

#### **4. Metas Financeiras (Guardrails)**
*   **`"target_cpa": 25.0`**
    *   **Descrição:** Custo por Aquisição (CPA) máximo desejado.
    *   **Por que alterar?** O motor usará isso para dizer se um canal está "dentro da meta" ou "caro demais".
*   **`"target_roas": 4.0`**
    *   **Descrição:** Retorno sobre Investimento (ROAS) mínimo desejado.
    *   **Por que alterar?** Se o ROAS real for menor que este, o motor sugerirá reduzir investimento nesse canal.

#### **5. Rigor e Thresholds do Modelo**
*   **`"p_value_threshold": 0.1`**
    *   **Descrição:** Nível de confiança estatística (0.1 = 90% de confiança).
    *   **Por que alterar?** Diminua (ex: 0.05) para ser mais rigoroso. Se os dados forem muito ruidosos, você pode aumentar para 0.15 para "encontrar" mais tendências.
*   **`"r_squared_threshold": 0.6`**
    *   **Descrição:** Quão bem o modelo explica os dados (0 a 1).
    *   **Por que alterar?** Se os resultados do dashboard não aparecerem, pode ser que o R² esteja abaixo deste valor. Tente baixar para 0.5 se os dados forem difíceis de modelar.
*   **`"increase_threshold_percent": 50`**
    *   **Descrição:** O quanto o investimento deve subir para ser considerado um "evento" de análise.
    *   **Por que alterar?** Em contas que oscilam muito naturalmente, use valores altos (50%). Em contas estáveis, use valores menores (20%).

#### **6. Mapeamento de Colunas (CSV Mapping)**
Esta seção diz ao script como ler os seus CSVs, independente do nome que as colunas tenham.
*   **`"date_col": "dates"`**: Qual coluna no CSV tem a data.
*   **`"channel_col": "product_group"`**: Qual coluna tem o nome do canal (Google, FB).
*   **`"investment_col": "total_revenue"`**: Qual coluna tem o valor investido (custo).

---

### 💡 Como usar este guia:
Sempre que você pegar um CSV novo de um cliente, abra este guia, compare com os cabeçalhos do CSV e preencha o seu `config.json` seguindo estas regras. Isso garante que o motor rode de primeira sem erros de "Coluna não encontrada"!
