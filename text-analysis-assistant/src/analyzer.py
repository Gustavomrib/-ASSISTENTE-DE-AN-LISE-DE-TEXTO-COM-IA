"""
analyzer.py
-----------
Módulo principal de análise de texto com IA aplicada.
Implementa algoritmos de resumição, extração de pontos-chave e sugestões.
"""

from typing import List, Tuple
from .models import AnalysisResult
from .processor import TextProcessor


class TextAnalyzer:
    """
    Classe principal do assistente de análise de texto.
    Implementa algoritmos de IA para análise semântica.
    
    Métodos:
        analyze: Realiza análise completa do texto
        extract_summary: Extrai resumo automático
        extract_key_points: Extrai pontos principais
        suggest_actions: Sugere ações baseadas no texto
    """
    
    def __init__(self, verbose: bool = False):
        """
        Inicializa o analisador.
        
        Args:
            verbose: Se True, exibe logs detalhados do processo
        """
        self.processor = TextProcessor()
        self.verbose = verbose
        self._log("Analisador de Texto inicializado (v1.0)")
    
    def _log(self, message: str) -> None:
        """Exibe log se verbose está ativado."""
        if self.verbose:
            print(f"[LOG] {message}")
    
    def analyze(self, text: str) -> AnalysisResult:
        """
        Realiza análise completa do texto fornecido.
        
        Args:
            text: Texto a ser analisado
            
        Returns:
            AnalysisResult com todos os dados da análise
            
        Raises:
            ValueError: Se o texto estiver vazio
        """
        if not text or not text.strip():
            raise ValueError("Texto não pode estar vazio!")
        
        self._log(f"Iniciando análise de texto ({len(text)} caracteres)")
        
        # Etapa 1: Pré-processamento
        cleaned_text = self.processor.clean_text(text)
        normalized_text = self.processor.normalize(cleaned_text)
        tokens = self.processor.tokenize(normalized_text)
        sentences = self.processor.extract_sentences(cleaned_text)
        
        self._log(f"Tokens extraídos: {len(tokens)}")
        self._log(f"Frases extraídas: {len(sentences)}")
        
        # Etapa 2: Análise estatística
        statistics = self.processor.count_statistics(cleaned_text, tokens)
        tone = self.processor.identify_tone(cleaned_text)
        complexity = self.processor.calculate_complexity(tokens, sentences)
        
        self._log(f"Tom identificado: {tone}")
        self._log(f"Complexidade: {complexity:.2%}")
        
        # Etapa 3: Extração de insights
        summary = self.extract_summary(sentences, tokens)
        key_points = self.extract_key_points(sentences, tokens)
        action_suggestions = self.suggest_actions(summary, key_points, cleaned_text)
        
        self._log("Análise concluída com sucesso")
        
        # Etapa 4: Retorno do resultado
        return AnalysisResult(
            original_text=text,
            summary=summary,
            key_points=key_points,
            action_suggestions=action_suggestions,
            text_stats=statistics,
            language_tone=tone,
            complexity_score=complexity
        )
    
    def extract_summary(self, sentences: List[str], tokens: List[str]) -> str:
        """
        Extrai um resumo automático do texto usando algoritmo de Pontuação de Frases.
        
        Algoritmo: TF-IDF simplificado
        - Calcula peso de cada frase baseado em frequência de palavras importantes
        - Seleciona as frases com maior peso
        - Retorna resumo ordenado por ordem de aparição
        
        Args:
            sentences: Lista de frases do texto
            tokens: Lista de tokens do texto
            
        Returns:
            Resumo do texto
        """
        if not sentences:
            return "Não foi possível gerar resumo."
        
        if len(sentences) <= 2:
            # Se tem poucas frases, retorna o texto original
            return sentences[0] if sentences else "Sem conteúdo"
        
        # Calcula frequência de palavras significativas
        meaningful_tokens = [
            t for t in tokens 
            if t not in self.processor.STOPWORDS and len(t) > 2
        ]
        
        word_freq = {}
        for word in meaningful_tokens:
            word_freq[word] = word_freq.get(word, 0) + 1
        
        # Normaliza frequências
        if word_freq:
            max_freq = max(word_freq.values())
            for word in word_freq:
                word_freq[word] = word_freq[word] / max_freq
        
        # Calcula score de cada frase
        sentence_scores = {}
        for i, sentence in enumerate(sentences):
            words = self.processor.tokenize(sentence)
            score = sum(word_freq.get(word, 0) for word in words)
            sentence_scores[i] = score
        
        # Seleciona 30-40% das frases com maior score
        num_sentences = max(1, int(len(sentences) * 0.35))
        top_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)[:num_sentences]
        
        # Retorna frases em ordem de aparição
        top_indices = sorted([idx for idx, _ in top_sentences])
        summary = " ".join([sentences[i].strip() for i in top_indices])
        
        return summary
    
    def extract_key_points(self, sentences: List[str], tokens: List[str]) -> List[str]:
        """
        Extrai os pontos-chave do texto.
        
        Algoritmo: Detecção de tópicos e entidades
        - Identifica palavras mais frequentes (por TF)
        - Agrupa frases por relevância
        - Extrai frases que contêm as palavras mais importantes
        
        Args:
            sentences: Lista de frases
            tokens: Lista de tokens
            
        Returns:
            Lista de pontos-chave (máximo 5)
        """
        if not sentences:
            return []
        
        # Encontra palavras mais frequentes
        meaningful_tokens = [
            t for t in tokens 
            if t not in self.processor.STOPWORDS and len(t) > 2
        ]
        
        from collections import Counter
        word_freq = Counter(meaningful_tokens)
        top_words = [word for word, _ in word_freq.most_common(6)]
        
        # Encontra frases que contêm essas palavras
        key_sentences = []
        for sentence in sentences:
            sentence_lower = sentence.lower()
            matches = sum(1 for word in top_words if word in sentence_lower)
            if matches >= 2:
                key_sentences.append((sentence.strip(), matches))
        
        # Ordena por relevância e pega os melhores
        key_sentences.sort(key=lambda x: x[1], reverse=True)
        
        # Formata e retorna (máximo 5 pontos)
        key_points = []
        for sentence, _ in key_sentences[:5]:
            if len(sentence) > 10:  # Filtra frases muito curtas
                # Limita tamanho de cada ponto
                if len(sentence) > 100:
                    sentence = sentence[:100] + "..."
                key_points.append("• " + sentence)
        
        return key_points if key_points else ["Sem pontos-chave identificados"]
    
    def suggest_actions(self, summary: str, key_points: List[str], text: str) -> List[str]:
        """
        Sugere ações baseadas na análise do texto.
        
        Algoritmo: Detecção de padrões e palavras-chave de ação
        - Detecta palavras relacionadas a ações (verbos, problemas, oportunidades)
        - Gera sugestões contextualizadas
        
        Args:
            summary: Resumo do texto
            key_points: Pontos-chave extraídos
            text: Texto original
            
        Returns:
            Lista de sugestões de ação
        """
        suggestions = []
        text_lower = text.lower()
        
        # Mapa de palavras-chave para ações sugeridas
        action_mappings = {
            # Problemas detectados
            ('problem', 'erro', 'falha', 'não funciona'): [
                "🔧 Investigar e documentar o tipo de problema",
                "📋 Criar plano de ação para resolução"
            ],
            
            # Oportunidades de melhoria
            ('melhorar', 'aumentar', 'expandir', 'otimizar'): [
                "✨ Planejar implementação de melhorias identificadas",
                "📊 Estabelecer KPIs para medir progresso"
            ],
            
            # Questões de análise/pesquisa
            ('análise', 'pesquisa', 'estudar', 'investigar', 'dados'): [
                "🔍 Conduzir análise mais profunda do tema",
                "💾 Consolidar dados em relatório estruturado"
            ],
            
            # Comunicação/Alinhamento
            ('comunicar', 'alinhar', 'discutir', 'reunião', 'stakeholder'): [
                "👥 Agendar reunião com stakeholders relevantes",
                "📢 Preparar apresentação dos resultados"
            ],
            
            # Execução/Implementação
            ('implementar', 'executar', 'iniciar', 'começar', 'projeto'): [
                "⏰ Definir cronograma de implementação",
                "👤 Designar responsáveis e recursos"
            ],
            
            # Monitoramento/Follow-up
            ('acompanhar', 'monitorar', 'controlar', 'revisão', 'status'): [
                "📅 Estabelecer ciclo de revisões periódicas",
                "✅ Criar checklist de validação"
            ]
        }
        
        # Verifica quais ações são aplicáveis
        for keywords, actions in action_mappings.items():
            if any(keyword in text_lower for keyword in keywords):
                suggestions.extend(actions)
        
        # Se nenhuma ação específica foi encontrada, gera sugestões genéricas
        if not suggestions:
            suggestions.extend([
                "📝 Documentar os aprendizados principais",
                "💡 Identificar próximos passos com base nos insights",
                "📊 Criar métrica para acompanhar progresso"
            ])
        
        # Remove duplicatas mantendo ordem
        seen = set()
        unique_suggestions = []
        for s in suggestions:
            # Remove emoji para comparação
            s_clean = s.replace('🔧', '').replace('📋', '').replace('✨', '').replace('📊', '')
            s_clean = s_clean.replace('🔍', '').replace('💾', '').replace('👥', '').replace('📢', '')
            s_clean = s_clean.replace('⏰', '').replace('👤', '').replace('📅', '').replace('✅', '')
            s_clean = s_clean.replace('📝', '').replace('💡', '').strip()
            
            if s_clean not in seen:
                seen.add(s_clean)
                unique_suggestions.append(s)
        
        return unique_suggestions[:5]  # Retorna no máximo 5 sugestões
