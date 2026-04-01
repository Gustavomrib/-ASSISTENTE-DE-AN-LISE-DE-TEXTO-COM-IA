"""
examples.py
-----------
Script com exemplos de uso programático do analisador.

Este arquivo demonstra como usar a biblioteca TextAnalyzer
sem a interface de linha de comando.
"""

import sys
import os

# Adiciona o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.analyzer import TextAnalyzer
from src.utils import format_result_for_display


def example_1_simple_analysis():
    """
    Exemplo 1: Análise simples de um texto curto.
    """
    print("\n" + "=" * 70)
    print("EXEMPLO 1: Análise Simples")
    print("=" * 70 + "\n")
    
    analyzer = TextAnalyzer()
    
    text = """
    A inteligência artificial está transformando a forma como fazemos negócios.
    Empresas usam IA para otimizar processos, melhorar atendimento e tomar
    decisões mais inteligentes. É essencial que profissionais entendam IA.
    O futuro pertence a quem domina essa tecnologia.
    """
    
    result = analyzer.analyze(text)
    print(format_result_for_display(result))


def example_2_verbose_analysis():
    """
    Exemplo 2: Análise com modo verbose (mostra logs).
    """
    print("\n" + "=" * 70)
    print("EXEMPLO 2: Análise com Logs Detalhados")
    print("=" * 70 + "\n")
    
    analyzer = TextAnalyzer(verbose=True)
    
    text = """
    O projeto de transformação digital enfrentou desafios significativos.
    Problemas de integração ocorreram na primeira fase. Precisamos investigar
    todas as falhas e criar um plano detalhado de ação para o futuro.
    A experiência aprendida será crítica para próximos projetos.
    """
    
    result = analyzer.analyze(text)
    print(format_result_for_display(result))


def example_3_programmatic_access():
    """
    Exemplo 3: Acesso programático aos dados (sem formatação).
    """
    print("\n" + "=" * 70)
    print("EXEMPLO 3: Acesso Programático aos Dados")
    print("=" * 70 + "\n")
    
    analyzer = TextAnalyzer()
    
    text = """
    Expandir para novos mercados é uma excelente oportunidade de crescimento.
    Os dados mostram alta demanda nessas regiões. Recomendamos aumentar
    investimento em marketing e abrir novos centros de distribuição.
    """
    
    result = analyzer.analyze(text)
    
    # Acesso aos dados via dicionário
    data = result.to_dict()
    
    print("Dados estruturados em dicionário:")
    for key, value in data.items():
        print(f"  {key}: {value}")


def example_4_batch_analysis():
    """
    Exemplo 4: Análise em lote de múltiplos textos.
    """
    print("\n" + "=" * 70)
    print("EXEMPLO 4: Análise em Lote")
    print("=" * 70 + "\n")
    
    analyzer = TextAnalyzer()
    
    textos = [
        "Ótimo resultado! Superamos todas as metas do trimestre.",
        "Terrível falha no sistema. Perdemos dados críticos.",
        "O projeto está em andamento conforme o planejado."
    ]
    
    for i, text in enumerate(textos, 1):
        print(f"\n--- Texto {i} ---")
        result = analyzer.analyze(text)
        print(f"Sumário: {result.summary}")
        print(f"Tom: {result.language_tone}")
        print(f"Complexidade: {result.complexity_score * 100:.1f}%")


def example_5_filter_and_analyze():
    """
    Exemplo 5: Filtrar e processar textos por ton.
    """
    print("\n" + "=" * 70)
    print("EXEMPLO 5: Análise Filtrada por Tom")
    print("=" * 70 + "\n")
    
    analyzer = TextAnalyzer()
    
    textos = {
        "email1": "Excelente desempenho! Os resultados foram incríveis e superaram expectativas!",
        "email2": "Erro grave em produção. Sistema fora do ar. Situação crítica.",
        "email3": "Reunião marcada para amanhã às 10h. Agenda normal.",
        "email4": "Maravilhoso! Conseguimos fechar a maior parceria da história!",
    }
    
    # Analisa todos
    resultados = {}
    for nome, texto in textos.items():
        result = analyzer.analyze(texto)
        resultados[nome] = result
    
    # Filtra por tom
    print("\n✅ Textos com tom POSITIVO:")
    for nome, result in resultados.items():
        if result.language_tone == "positivo":
            print(f"  • {nome}: {result.summary[:50]}...")
    
    print("\n❌ Textos com tom NEGATIVO:")
    for nome, result in resultados.items():
        if result.language_tone == "negativo":
            print(f"  • {nome}: {result.summary[:50]}...")
    
    print("\n⚪ Textos com tom NEUTRO:")
    for nome, result in resultados.items():
        if result.language_tone == "neutro":
            print(f"  • {nome}: {result.summary[:50]}...")


def main():
    """
    Executa todos os exemplos.
    """
    print("\n🚀 EXEMPLOS DE USO DO ANALISADOR DE TEXTO\n")
    
    try:
        example_1_simple_analysis()
        example_2_verbose_analysis()
        example_3_programmatic_access()
        example_4_batch_analysis()
        example_5_filter_and_analyze()
        
        print("\n" + "=" * 70)
        print("✅ Todos os exemplos executados com sucesso!")
        print("=" * 70 + "\n")
        
    except Exception as e:
        print(f"\n❌ Erro ao executar exemplos: {e}")


if __name__ == "__main__":
    main()
