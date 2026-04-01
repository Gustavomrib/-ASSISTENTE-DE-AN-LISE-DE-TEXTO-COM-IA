"""
models.py
---------
Define as estruturas de dados utilizadas no projeto.
Utiliza dataclasses para melhor organização e tipagem.
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class AnalysisResult:
    """
    Classe que representa o resultado da análise de um texto.
    
    Atributos:
        original_text (str): Texto original fornecido pelo usuário
        summary (str): Resumo inteligente do texto
        key_points (List[str]): Lista de pontos-chave extraídos
        action_suggestions (List[str]): Sugestões de ações baseadas no texto
        text_stats (dict): Estatísticas do texto (palavras, caracteres, etc)
        language_tone (str): Tom/sentimento do texto (positivo, neutro, negativo)
        complexity_score (float): Pontuação de complexidade (0-1)
    """
    original_text: str
    summary: str
    key_points: List[str]
    action_suggestions: List[str]
    text_stats: dict = field(default_factory=dict)
    language_tone: str = "neutro"
    complexity_score: float = 0.5
    
    def to_dict(self) -> dict:
        """Converte o resultado para um dicionário."""
        return {
            "sumário": self.summary,
            "pontos_chave": self.key_points,
            "sugestões_ações": self.action_suggestions,
            "estatísticas": self.text_stats,
            "tom_linguagem": self.language_tone,
            "complexidade": f"{self.complexity_score * 100:.1f}%"
        }
    
    def __str__(self) -> str:
        """Representação em string formatada do resultado."""
        return f"AnalysisResult(sumário={len(self.summary)} chars, pontos={len(self.key_points)}, tom={self.language_tone})"
