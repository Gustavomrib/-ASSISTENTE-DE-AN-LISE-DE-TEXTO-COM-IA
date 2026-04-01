# GETTING_STARTED.md

## 🚀 Guia Rápido de Início

### 5 Minutos para Começar

#### 1️⃣ Verifique Python

```bash
python --version
# Necessário: Python 3.8+
```

#### 2️⃣ Execute o Programa

```bash
python main.py
```

#### 3️⃣ Escolha uma Opção

```
[1] Analisar texto personalizado
[2] Usar texto de exemplo
[3] Ver informações do projeto
[4] Sair
```

#### 4️⃣ Veja os Resultados

Você receberá:

- 📝 Resumo automático
- ⭐ Pontos-chave
- 💡 Sugestões de ação
- 📊 Estatísticas e análise detalhada

---

## 📝 Exemplos de Uso

### Opção 1: Interface Interativa (Recomendado para primeiro uso)

```bash
python main.py
# Digite [1] para análise personalizada
# Cole seu texto (mínimo 20 caracteres)
# Digite "FIM" em uma linha vazia quando terminar
```

### Opção 2: Usar Exemplos Pré-carregados

```bash
python main.py
# Digite [2] para exemplos
# Escolha: [1] Email de Projeto, [2] Relatório, etc
```

### Opção 3: Ver Exemplos de Código

```bash
python examples.py
# Executa 5 exemplos de uso programático
# Veja como usar como módulo Python
```

### Opção 4: Usar como Biblioteca

```python
from src.analyzer import TextAnalyzer

# Criar analisador
analyzer = TextAnalyzer()

# Analisar texto
texto = "Sua análise de IA é excelente!"
resultado = analyzer.analyze(texto)

# Acessar dados
print(resultado.summary)          # Resumo
print(resultado.key_points)       # Pontos-chave
print(resultado.action_suggestions)  # Sugestões
print(resultado.language_tone)    # Tom
print(resultado.complexity_score) # Complexidade 0-1
```

---

## 🔧 Instalação

### Windows

Double-click:

```
install-windows.bat
```

Ou manual:

```bash
# Criar ambiente virtual
python -m venv venv
venv\Scripts\activate

# Instalar dependências (opcionais)
pip install -r requirements.txt

# Executar
python main.py
```

### Linux/Mac

```bash
# Dar permissão de execução
chmod +x install-linux-mac.sh

# Executar
./install-linux-mac.sh
```

Ou manual:

```bash
# Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependências (opcionais)
pip install -r requirements.txt

# Executar
python3 main.py
```

---

## 📊 Entendendo a Saída

### Estrutura dos Resultados

```
📝 SUMÁRIO
└─ Versão condensada do texto principal

⭐ PONTOS-CHAVE
└─ 3-5 frases mais importantes

💡 SUGESTÕES DE AÇÃO
└─ Recomendações baseadas no conteúdo

📈 ANÁLISE AVANÇADA
├─ Tom: positivo/negativo/neutro
├─ Complexidade: 0-100%
└─ Palavras-chave mais frequentes

📊 ESTATÍSTICAS
├─ Total de caracteres
├─ Total de palavras
├─ Palavras únicas
├─ Frases
└─ Palavras-chave mais comuns
```

---

## 💡 Dicas de Uso

### ✅ Textos que funcionam bem:

- Emails profissionais
- Relatórios de negócios
- Comunicados internos
- Documentos estruturados
- Notícias
- Descrições de projetos

### ⚠️ Limitações conhecidas:

- Textos muito curtos (< 20 chars)
- Textos em outros idiomas
- Código ou dados estruturados
- Poesia ou textos muito criativos

---

## 🎯 Casos de Uso

### 1. **Análise de Emails**

```
Email da empresa → Extrair ações necessárias → Dashboard
```

### 2. **Resumo de Documentos**

```
Relatório longo → Sumário automático → Apresentação
```

### 3. **Detecção de Sentimento**

```
Feedback do cliente → Classificar tom → Priorizar resposta
```

### 4. **Extração de Informações**

```
Texto → Pontos-chave → Banco de dados
```

---

## 🐛 Resolução de Problemas

### "Python não encontrado"

```bash
# Windows
python --version
# Se não funcionar, instale de: https://www.python.org

# Linux/Mac
python3 --version
# Se não funcionar: sudo apt install python3 (Linux) ou brew install python (Mac)
```

### "Erro ao importar módulos"

```bash
# Certifique-se que está no diretório correto
cd text-analysis-assistant

# Verifique estrutura
src/
  __init__.py
  analyzer.py
  processor.py
  models.py
  utils.py
main.py
```

### "Texto muito curto"

```
Insira pelo menos 20 caracteres. Exemplo:
"IA é o futuro da tecnologia e negócios."
```

---

## 📚 Próximas Etapas

### Aprender a Usar

1. Comece com exemplos pré-carregados
2. Teste com seus próprios textos
3. Explore results diferentes (tom, complexidade)
4. Exporte resultados em arquivo

### Desenvolver Conhecimento

1. Leia os comentários no código
2. Entenda os algoritmos (veja README.md)
3. Modifique o código (ex: altere stopwords)
4. Crie seus próprios algoritmos

### Expandir o Projeto

1. Adicionar suporte a múltiplos idiomas
2. Integrar com APIs de IA
3. Criar interface web
4. Adicionar testes unitários

---

## 📖 Documentação Completa

Para mais detalhes, veja:

- **README.md** - Visão geral do projeto
- **PRESENTATION.md** - Como apresentar em entrevistas
- **analyzer.py** - Documentação dos algoritmos
- **processor.py** - Detalhes de processamento
- **examples.py** - Exemplos de código

---

## ✨ Conclusão

Você está pronto! Execute `python main.py` e comece a explorar.

**Dúvidas?** Leia os arquivos `.py` com comentários detalhados.

**Boa sorte! 🚀**
