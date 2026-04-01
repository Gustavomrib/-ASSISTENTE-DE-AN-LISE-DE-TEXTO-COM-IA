"""
Text Analysis Assistant - Assistente inteligente de análise de texto
Desenvolvido como projeto de IA aplicada a negócios para apresentação em entrevista.
"""

__version__ = "1.0.0"
__author__ = "Gustavo Marques Lopes Ribeiro"
__description__ = "Assistente de Análise de Texto com IA aplicada"

from .models import AnalysisResult
from .analyzer import TextAnalyzer
from .processor import TextProcessor

__all__ = ["AnalysisResult", "TextAnalyzer", "TextProcessor"]
