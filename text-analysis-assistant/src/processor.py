"""
processor.py
-----------
Modulo de processamento de texto.
Realiza operações de limpeza, tokenização e análise estatística do texto.
"""

import re
from typing import List, Tuple, Dict
from collections import Counter


class TextProcessor:
    """
    Classe responsável pelo processamento e análise estatística de textos.
    
    Métodos:
        clean_text: Remove caracteres especiais e normaliza
        tokenize: Divide o texto em palavras
        count_statistics: Calcula estatísticas (palavras, caracteres, etc)
        extract_sentences: Extrai frases do texto
        normalize: Normaliza o texto (lowercase, espaços extras)
    """
    
    # Palavras comuns que não agregam muito significado (stopwords)
    STOPWORDS = {
        'o', 'a', 'os', 'as', 'um', 'uma', 'uns', 'umas',
        'e', 'ou', 'de', 'para', 'com', 'sem', 'por',
        'foi', 'é', 'são', 'ser', 'está', 'estão',
        'em', 'ao', 'à', 'nas', 'dos', 'das', 'do', 'da',
        'que', 'se', 'não', 'mais', 'como', 'tem', 'havia',
        'mas', 'porque', 'seu', 'sua', 'seus', 'suas'
    }
    
    @staticmethod
    def normalize(text: str) -> str:
        """
        Normaliza o texto removendo espaços extras e convertendo para minúsculas.
        
        Args:
            text: Texto a ser normalizado
            
        Returns:
            Texto normalizado
        """
        # Remove espaços extras
        text = re.sub(r'\s+', ' ', text)
        return text.strip().lower()
    
    @staticmethod
    def clean_text(text: str) -> str:
        """
        Remove caracteres especiais e símbolos desnecessários do texto.
        
        Args:
            text: Texto a ser limpo
            
        Returns:
            Texto limpo
        """
        # Remove URLs
        text = re.sub(r'http\S+|www\S+', '', text)
        # Remove emails
        text = re.sub(r'\S+@\S+', '', text)
        # Remove caracteres especiais mantendo pontuação básica (incluindo MAIÚSCULAS)
        text = re.sub(r'[^a-zA-ZáéíóúâêôãõçñÁÉÍÓÚÂÊÔÃÕÇÑ\s.!?,;:\'-]', '', text)
        return text
    
    @staticmethod
    def tokenize(text: str) -> List[str]:
        """
        Divide o texto em palavras (tokens).
        
        Args:
            text: Texto a ser tokenizado
            
        Returns:
            Lista de palavras
        """
        # Divide por espaços e remove palavras vazias
        tokens = text.lower().split()
        # Remove pontuação das palavras
        tokens = [re.sub(r'[.,!?;:\'\"-]', '', token) for token in tokens]
        # Filtra tokens vazios
        return [token for token in tokens if token]
    
    @staticmethod
    def extract_sentences(text: str) -> List[str]:
        """
        Extrai as frases do texto.
        
        Args:
            text: Texto para extração
            
        Returns:
            Lista de frases
        """
        # Divide por pontos, exclamações e interrogações
        sentences = re.split(r'[.!?]+', text)
        # Remove espaços e filtra vazias
        sentences = [s.strip() for s in sentences if s.strip()]
        return sentences
    
    @staticmethod
    def count_statistics(text: str, tokens: List[str]) -> Dict:
        """
        Calcula estatísticas sobre o texto.
        
        Args:
            text: Texto original
            tokens: Tokens do texto
            
        Returns:
            Dicionário com estatísticas
        """
        sentences = TextProcessor.extract_sentences(text)
        
        # Filtra stopwords para análise
        meaningful_tokens = [
            t for t in tokens 
            if t not in TextProcessor.STOPWORDS and len(t) > 2
        ]
        
        return {
            "total_caracteres": len(text),
            "total_palavras": len(tokens),
            "palavras_unicas": len(set(tokens)),
            "total_frases": len(sentences),
            "palavras_significativas": len(meaningful_tokens),
            "media_palavras_por_frase": round(len(tokens) / len(sentences), 2) if sentences else 0,
            "palavras_mais_frequentes": dict(Counter(meaningful_tokens).most_common(5))
        }
    
    @staticmethod
    def identify_tone(text: str) -> str:
        """
        Identifica o tom/sentimento do texto (simulando IA).
        
        Args:
            text: Texto para análise
            
        Returns:
            Tom identificado: 'positivo', 'negativo' ou 'neutro'
        """
        text_lower = text.lower()
        
        # Palavras-chave positivas
        positive_keywords = {
            'excelente', 'ótimo', 'maravilhoso', 'incrível', 'perfeito',
            'adorei', 'amei', 'feliz', 'alegre', 'sucesso', 'ganho',
            'melhor', 'fantástico', 'legal', 'bom', 'boa', 'positivo'
        }
        
        # Palavras-chave negativas
        negative_keywords = {
            'terrível', 'horrível', 'pior', 'ruim', 'fracasso', 'perda',
            'problem', 'erro', 'falha', 'infeliz', 'triste', 'decepcionante',
            'negativo', 'péssimo', 'desastre', 'crítica', 'crítico'
        }
        
        # Conta ocorrências
        positive_count = sum(1 for word in positive_keywords if word in text_lower)
        negative_count = sum(1 for word in negative_keywords if word in text_lower)
        
        if positive_count > negative_count:
            return "positivo"
        elif negative_count > positive_count:
            return "negativo"
        else:
            return "neutro"
    
    @staticmethod
    def calculate_complexity(tokens: List[str], sentences: List[str]) -> float:
        """
        Calcula a complexidade do texto (0-1).
        Baseado na média de palavras por frase e variação vocabulário.
        
        Args:
            tokens: Lista de tokens
            sentences: Lista de frases
            
        Returns:
            Score de complexidade entre 0 e 1
        """
        if not sentences or not tokens:
            return 0.0
        
        # Média de palavras por frase
        avg_words_per_sentence = len(tokens) / len(sentences)
        
        # Razão de palavras únicas
        unique_ratio = len(set(tokens)) / len(tokens) if tokens else 0
        
        # Calcula complexidade (0-1)
        # Textos com mais palavras por frase e maior vocabulário são mais complexos
        complexity = (min(avg_words_per_sentence / 30, 1.0) + unique_ratio) / 2
        
        return min(complexity, 1.0)
