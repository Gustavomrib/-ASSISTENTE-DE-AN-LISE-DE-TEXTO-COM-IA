# Text Analysis Assistant

Assistente inteligente de análise de texto com IA aplicada, desenvolvido como projeto de portfólio para entrevistas de estágio em IA.

## 📋 Sobre o Projeto

Um assistente que analisa textos e extrai insights usando algoritmos de processamento natural de linguagem (NLP), **sem dependência de APIs externas**. Este projeto demonstra conhecimento em:

- ✅ Algoritmos de NLP (TF-IDF, Tokenização, Análise de Sentimento)
- ✅ Estrutura profissional de código Python
- ✅ Boas práticas de engenharia de software
- ✅ Análise e processamento de dados
- ✅ Arquitetura modular e escalável

## 🎯 Funcionalidades

O assistente recebe um texto e retorna:

1. **📝 Resumo Automático**: Síntese inteligente do conteúdo principal
2. **⭐ Pontos-Chave**: Tópicos e informações mais relevantes
3. **💡 Sugestões de Ação**: Recomendações contextualizadas
4. **📊 Análise de Tom**: Detecção de sentimento (positivo/negativo/neutro)
5. **📈 Complexidade**: Score de dificuldade do texto
6. **📋 Estatísticas**: Palavras, frases, frequência, etc.

## 🏗️ Estrutura do Projeto

```
text-analysis-assistant/
├── src/
│   ├── __init__.py          # Inicialização do módulo
│   ├── models.py            # Estruturas de dados (dataclasses)
│   ├── analyzer.py          # Lógica principal de análise
│   ├── processor.py         # Processamento de texto
│   └── utils.py             # Utilitários e formatação
├── main.py                  # Interface principal (CLI)
├── examples.py              # Exemplos de uso programático
├── README.md                # Este arquivo
├── PRESENTATION.md          # Guia de apresentação em entrevista
├── requirements.txt         # Dependências
└── setup.py                 # Script de instalação
```

## ⚙️ Arquitetura

### Camada de Processamento (`processor.py`)

- Limpeza e normalização de texto
- Tokenização (divisão em palavras)
- Extração de frases
- Cálculo de estatísticas
- Análise de sentimento por palavras-chave

### Camada de Análise (`analyzer.py`)

- Algoritmo TF-IDF para extração de frases importantes
- Pontuação de relevância
- Sugestões baseadas em padrões
- Orquestração do pipeline de análise

### Modelos e Dados (`models.py`)

- `AnalysisResult`: Resultado estruturado da análise
- Uso de dataclasses para type-safety
- Métodos de serialização

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8 ou superior
- Nenhuma dependência externa (usa apenas stdlib)

### Instalação

```bash
# Clone ou baixe o projeto
cd text-analysis-assistant

# Não é necessário instalar dependências
# (excepto se usar requirements.txt para ambiente virtual)
```

### Uso - Opção 1: Interface Interativa

```bash
python main.py
```

Menu interativo com opções:

```
1. Análise de texto personalizado
2. Usar texto de exemplo
3. Ver informações do projeto
4. Sair
```

### Uso - Opção 2: Exemplos Programáticos

```bash
python examples.py
```

Demonstra 5 casos de uso diferentes:

1. Análise simples
2. Análise com logs detalhados
3. Acesso programático
4. Análise em lote
5. Filtragem por tom

### Uso - Opção 3: Importar como Módulo

```python
from src.analyzer import TextAnalyzer

analyzer = TextAnalyzer()
resultado = analyzer.analyze("Seu texto aqui...")

print(f"Sumário: {resultado.summary}")
print(f"Tom: {resultado.language_tone}")
print(f"Pontos-chave: {resultado.key_points}")
```

## 📊 Algoritmos Implementados

### 1. **TF-IDF Simplificado** (Extração de Frases)

```
- Calcula frequência de termo (TF) para palavras significativas
- Seleciona 30-40% das frases com maior score
- Retorna em ordem de aparição original
```

### 2. **Tokenização e Normalizaçãõ**

```
- Remove URLs, emails, caracteres especiais
- Converte para minúsculas
- Remove espaços extras
- Divide em palavras (tokens)
```

### 3. **Análise de Sentimento**

```
- Conta palavras-chave positivas vs. negativas
- Classifica como: positivo, negativo ou neutro
- Mapeia palavras para emoções/temas
```

### 4. **Extração de Tópicos**

```
- Identifica palavras mais frequentes
- Encontra frases contendo múltiplas palavras-chave
- Ordena por relevância
```

### 5. **Cálculo de Complexidade**

```
Complexidade = (média_palavras_por_frase / 30 + diversidade_vocabulário) / 2
```

## 💼 Apresentação em Entrevista

Ver arquivo [PRESENTATION.md](PRESENTATION.md) para dicas detalhadas de como apresentar este projeto em uma entrevista de IA.

### Pontos-chave a mencionar:

✅ **Sem APIs externas**: Totalmente implementado do zero
✅ **Profissional**: Código limpo, documentado e estruturado
✅ **Escalável**: Fácil adicionar novos algoritmos
✅ **Testável**: Cada módulo é independente
✅ **Educacional**: Demonstra compreensão de NLP

## 🔮 Possíveis Melhorias

### Curto Prazo

- [ ] Análise de Entidades Nomeadas (NER)
- [ ] Correção de ortografia
- [ ] Suporte a múltiplos idiomas
- [ ] Testes unitários com pytest

### Médio Prazo

- [ ] Interface web com Flask/FastAPI
- [ ] Integração com OpenAI GPT-3/4
- [ ] Integração com Google Gemini
- [ ] Banco de dados para histórico
- [ ] API REST completa

### Longo Prazo

- [ ] Análise de sentimento com transformers (BERT)
- [ ] Classificação de textos com ML
- [ ] Extração de relacionamentos entre entidades
- [ ] Geração de relatórios em PDF/Word
- [ ] Dashboard com visualizações
- [ ] Suporte a análise de documentos

## 📝 Exemplos de Saída

### Entrada:

```
"A empresa alcançou resultados excelentes no Q1. O projeto de transformação
digital superou todas as metas. Agora precisamos consolidar os aprendizados
e planejar a expansão para novas regiões."
```

### Saída:

```
📝 SUMÁRIO:
A empresa alcançou resultados excelentes. O projeto de transformação digital
superou metas. Agora consolidar aprendizados e planejar expansão para regiões.

⭐ PONTOS-CHAVE:
• A empresa alcançou resultados excelentes no Q1
• O projeto de transformação digital superou todas as metas
• Precisamos consolidar os aprendizados

💡 SUGESTÕES DE AÇÃO:
1. ✨ Planejar implementação de melhorias identificadas
2. 📊 Estabelecer KPIs para medir progresso
3. 👥 Agendar reunião com stakeholders relevantes

📈 ANÁLISE AVANÇADA:
Tom do texto: POSITIVO
Complexidade: 42.5%
Palavras-chave: empresa, resultados, projeto

📊 ESTATÍSTICAS:
Total de palavras: 35
Total de frases: 3
Média de palavras por frase: 11.67
```

## 🛠️ Desenvolvendo

### Estrutura de um novo algoritmo:

1. Adicionar método na classe `TextProcessor` ou `TextAnalyzer`
2. Criar testes no arquivo de testes
3. Integrar no pipeline principal
4. Documentar no README

Exemplo:

```python
def new_analysis_feature(self, text: str) -> str:
    """
    Descrição Clara

    Args:
        text: Descrição

    Returns:
        Descrição
    """
    # Implementação
    return resultado
```

## 📚 Referências

- Processamento de Linguagem Natural (NLP): https://pt.wikipedia.org/wiki/Processamento_de_linguagem_natural
- TF-IDF: https://pt.wikipedia.org/wiki/Tf%E2%80%93idf
- Análise de Sentimento: https://pt.wikipedia.org/wiki/An%C3%A1lise_de_sentimentos
- Python Best Practices: https://pep8.org/

## 📄 Licença

Este projeto é fornecido como exemplo educacional.

## 👤 Autor

Desenvolvido como projeto de portfólio para demonstrar competências em:

- Desenvolvimento Python
- Algoritmos de IA/NLP
- Engenharia de Software
- Apresentação profissional

---

**Versão**: 1.0.0  
**Última atualização**: 2024  
**Status**: ✅ Pronto para apresentação

## ?? Uso Web com Streamlit

```bash
pip install -r requirements.txt
streamlit run app.py
```

A interface web reaproveita a mesma logica de analise do modulo `src/`.
