"""
utils.py
--------
Funções utilitárias do projeto.
Inclui formatação, validação e utilitários gerais.
"""

from typing import List
from .models import AnalysisResult


def format_result_for_display(result: AnalysisResult) -> str:
    """
    Formata o resultado da análise para exibição ao usuário.
    
    Args:
        result: AnalysisResult com os dados da análise
        
    Returns:
        String formatada pronta para impressão
    """
    output = "\n"
    output += "=" * 70 + "\n"
    output += "📊 RESULTADO DA ANÁLISE DE TEXTO\n"
    output += "=" * 70 + "\n\n"
    
    # Sumário
    output += "📝 SUMÁRIO:\n"
    output += "-" * 70 + "\n"
    output += f"{result.summary}\n\n"
    
    # Pontos-chave
    output += "⭐ PONTOS-CHAVE:\n"
    output += "-" * 70 + "\n"
    for point in result.key_points:
        output += f"{point}\n"
    output += "\n"
    
    # Sugestões de ação
    output += "💡 SUGESTÕES DE AÇÃO:\n"
    output += "-" * 70 + "\n"
    for i, suggestion in enumerate(result.action_suggestions, 1):
        output += f"{i}. {suggestion}\n"
    output += "\n"
    
    # Análise avançada
    output += "📈 ANÁLISE AVANÇADA:\n"
    output += "-" * 70 + "\n"
    output += f"Tom do texto: {result.language_tone.upper()}\n"
    output += f"Complexidade: {result.complexity_score * 100:.1f}%\n"
    output += f"Palavras-chave mais frequentes: {', '.join(list(result.text_stats['palavras_mais_frequentes'].keys())[:3])}\n"
    output += "\n"
    
    # Estatísticas
    output += "📊 ESTATÍSTICAS:\n"
    output += "-" * 70 + "\n"
    output += f"Total de caracteres: {result.text_stats['total_caracteres']}\n"
    output += f"Total de palavras: {result.text_stats['total_palavras']}\n"
    output += f"Palavras únicas: {result.text_stats['palavras_unicas']}\n"
    output += f"Total de frases: {result.text_stats['total_frases']}\n"
    output += f"Média de palavras por frase: {result.text_stats['media_palavras_por_frase']}\n"
    output += "\n"
    
    output += "=" * 70 + "\n"
    
    return output


def validate_text_input(text: str, min_length: int = 20) -> tuple[bool, str]:
    """
    Valida o texto de entrada do usuário.
    
    Args:
        text: Texto a validar
        min_length: Comprimento mínimo do texto
        
    Returns:
        Tupla (é_válido, mensagem_erro)
    """
    if not text:
        return False, "❌ Texto não pode estar vazio!"
    
    if len(text.strip()) < min_length:
        return False, f"❌ Texto muito curto! Mínimo de {min_length} caracteres necessários."
    
    if len(text.strip()) > 10000:
        return False, "❌ Texto muito longo! Máximo de 10000 caracteres."
    
    return True, "✅ Texto válido"


def save_analysis_to_file(result: AnalysisResult, filename: str) -> bool:
    """
    Salva o resultado da análise em um arquivo de texto.
    
    Args:
        result: AnalysisResult com os dados
        filename: Nome do arquivo
        
    Returns:
        True se salvo com sucesso, False caso contrário
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(format_result_for_display(result))
        return True
    except IOError as e:
        print(f"❌ Erro ao salvar arquivo: {e}")
        return False


def load_sample_texts() -> dict:
    """
    Carrega textos de exemplo para demonstração.
    
    Returns:
        Dicionário com textos de exemplo
    """
    return {
        "1": {
            "titulo": "Email de Projeto",
            "texto": """Prezados,

Informo que o projeto de análise de dados teve uma falha crítica no servidor principal. 
O sistema parou de processar às 14:30 UTC. O time técnico está investigando e documentando 
o problema. Precisamos estabelecer um plano de ação para evitar isso no futuro. 
Sugiro que façamos uma reunião de alinhamento com todos os stakeholders amanhã às 10h.

Att,
João"""
        },
        "2": {
            "titulo": "Relatório de Performance",
            "texto": """Q1 2024 Performance Report

Excelentes resultados! A empresa alcançou 150% dos objetivos de vendas. 
O crescimento foi impulsionado por uma campanha de marketing inovadora e parcerias estratégicas. 
Todos os KPIs estão acima das metas. Recomendamos expandir o modelo para outras regiões. 
Aumentar investimento em tecnologia e recursos humanos será crítico para sustentar o crescimento."""
        },
        "3": {
            "titulo": "Análise de Mercado",
            "texto": """Estudo de Viabilidade - Novo Produto

A pesquisa indica forte demanda de mercado para solução inovadora. 
Competitors não cobrem completamente essa lacuna. Investigamos dados de 500 potenciais clientes 
e 87% demonstraram interesse. O investimento inicial será $250k. Esperamos ROI em 18 meses.
Próximos passos: finalizar design do produto e planejar beta testing com early adopters."""
        }
    }


def display_menu() -> None:
    """Exibe o menu principal de boas-vindas."""
    print("\n" + "=" * 70)
    print("🤖 BEM-VINDO AO ASSISTENTE DE ANÁLISE DE TEXTO COM IA")
    print("=" * 70)
    print("\nEste assistente foi desenvolvido como projeto de IA aplicada!")
    print("\nO que está ferramenta pode fazer:")
    print("  ✓ Gerar resumos automáticos")
    print("  ✓ Extrair pontos principais")
    print("  ✓ Sugerir ações")
    print("  ✓ Identificar tom do texto")
    print("  ✓ Calcular complexidade")
    print("  ✓ Fornecer análise detalhada")
    print("\n" + "-" * 70)


def display_options() -> None:
    """Exibe as opções disponíveis."""
    print("\nOpções disponíveis:")
    print("  [1] Analisar texto personalizado")
    print("  [2] Usar texto de exemplo")
    print("  [3] Ver informações do projeto")
    print("  [4] Sair")
    print()
