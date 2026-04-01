#!/usr/bin/env python3
"""
main.py
-------
Arquivo principal - Interface do usuário e orquestração da aplicação.

Este é o ponto de entrada do programa. Gerencia a interação com o usuário
através da linha de comando e coordena a análise de texto.

Uso:
    python main.py
"""

import sys
import os

# Adiciona o diretório src ao path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.analyzer import TextAnalyzer
from src.utils import (
    format_result_for_display,
    validate_text_input,
    save_analysis_to_file,
    load_sample_texts,
    display_menu,
    display_options
)


class TextAnalysisApp:
    """
    Classe principal da aplicação.
    Gerencia o fluxo de interação com o usuário.
    """
    
    def __init__(self):
        """Inicializa a aplicação."""
        self.analyzer = TextAnalyzer(verbose=False)
        self.running = True
    
    def run(self) -> None:
        """Executa o loop principal da aplicação."""
        display_menu()
        
        while self.running:
            display_options()
            choice = input("Escolha uma opção: ").strip()
            
            try:
                if choice == "1":
                    self.analyze_custom_text()
                elif choice == "2":
                    self.analyze_sample_text()
                elif choice == "3":
                    self.show_project_info()
                elif choice == "4":
                    self.exit_app()
                else:
                    print("❌ Opção inválida! Tente novamente.")
            except KeyboardInterrupt:
                print("\n⚠️  Operação cancelada pelo usuário.")
                self.exit_app()
            except Exception as e:
                print(f"❌ Erro: {e}")
    
    def analyze_custom_text(self) -> None:
        """
        Permite que o usuário insira um texto personalizado para análise.
        """
        print("\n" + "=" * 70)
        print("📝 ANALISAR TEXTO PERSONALIZADO")
        print("=" * 70)
        print("Digite seu texto (mínimo 20 caracteres):")
        print("(Digite 'FIM' em uma linha vazia para finalizar)\n")
        
        lines = []
        while True:
            line = input()
            if line.strip().upper() == "FIM":
                break
            lines.append(line)
        
        text = "\n".join(lines)
        
        # Valida o texto
        is_valid, message = validate_text_input(text)
        print(message)
        
        if not is_valid:
            return
        
        # Realiza análise
        self._perform_analysis(text)
    
    def analyze_sample_text(self) -> None:
        """
        Permite que o usuário escolha um texto de exemplo para análise.
        """
        print("\n" + "=" * 70)
        print("📚 ANALISAR TEXTO DE EXEMPLO")
        print("=" * 70)
        
        samples = load_sample_texts()
        
        # Exibe opções
        for key, sample in samples.items():
            print(f"  [{key}] {sample['titulo']}")
        print("  [0] Voltar")
        
        choice = input("\nEscolha um exemplo: ").strip()
        
        if choice == "0":
            return
        
        if choice not in samples:
            print("❌ Opção inválida!")
            return
        
        text = samples[choice]["texto"]
        print(f"\n✓ Analisando: {samples[choice]['titulo']}\n")
        self._perform_analysis(text)
    
    def _perform_analysis(self, text: str) -> None:
        """
        Realiza a análise do texto e exibe os resultados.
        
        Args:
            text: Texto a ser analisado
        """
        try:
            print("\n⏳ Analisando texto...")
            result = self.analyzer.analyze(text)
            
            # Exibe resultado
            print(format_result_for_display(result))
            
            # Pergunta se quer salvar
            save = input("Deseja salvar este resultado em um arquivo? (s/n): ").strip().lower()
            if save == 's':
                filename = input("Nome do arquivo (sem extensão): ").strip()
                if filename:
                    filename = f"{filename}.txt"
                    if save_analysis_to_file(result, filename):
                        print(f"✅ Arquivo salvo como '{filename}'")
                    else:
                        print("❌ Erro ao salvar arquivo")
        
        except ValueError as e:
            print(f"❌ Erro de validação: {e}")
        except Exception as e:
            print(f"❌ Erro na análise: {e}")
    
    def show_project_info(self) -> None:
        """
        Exibe informações sobre o projeto.
        """
        print("\n" + "=" * 70)
        print("ℹ️  INFORMAÇÕES DO PROJETO")
        print("=" * 70 + "\n")
        
        info = """
📌 NOME:
   Assistente de Análise de Texto com IA

🎯 OBJETIVO:
   Analisar textos e extrair insights usando algoritmos de processamento
   natural de linguagem (NLP) sem dependência de APIs externas.

🔧 TECNOLOGIAS:
   • Python 3.8+
   • Algoritmos de NLP: TF-IDF, Tokenização, Extração de Entidades
   • Dataclasses para estrutura de dados
   • Processamento de texto com Regex

💡 FUNCIONALIDADES:
   ✓ Resumo automático de textos
   ✓ Extração de pontos-chave
   ✓ Sugestões de ações baseadas em análise
   ✓ Detecção de tom (positivo/negativo/neutro)
   ✓ Cálculo de complexidade do texto
   ✓ Estatísticas detalhadas
   ✓ Exportação de resultados

📊 ALGORITMOS UTILIZADOS:
   1. TF-IDF Simplificado: Pontuação de frases baseada em frequência
   2. Tokenização: Divisão em palavras e frases
   3. Análise de Sentimento: Detecção de tom por palavras-chave
   4. Detecção de Tópicos: Identificação de temas principais
   5. Cálculo de Complexidade: Baseado em estrutura e vocabulário

🚀 COMO USAR:
   1. Execute: python main.py
   2. Escolha uma opção no menu
   3. Insira ou selecione um texto
   4. Analise os resultados
   5. Exporte se desejar

📈 POSSÍVEIS MELHORIAS:
   • Integração com OpenAI GPT (resumos IA real)
   • Integração com Google Gemini
   • Análise de Sentimento com ML (transformers)
   • Interface web com Flask/FastAPI
   • Banco de dados para histórico
   • Geração de relatórios em PDF
   • Análise de entidades nomeadas (NER)
   • Suporte multilíngue

👨‍💼 APRESENTAÇÃO EM ENTREVISTA:
   Ver arquivo PRESENTATION.md para dicas de apresentação.

📝 VERSÃO: 1.0.0
📧 CÓDIGO: Disponível no repositório
"""
        print(info)
        input("\nPressione ENTER para voltar ao menu...")
    
    def exit_app(self) -> None:
        """Encerra a aplicação."""
        print("\n👋 Obrigado por usar o Assistente de Análise de Texto!")
        print("   Até logo! 🚀\n")
        self.running = False
        sys.exit(0)


def main() -> None:
    """
    Função principal do programa.
    Instancia e executa a aplicação.
    """
    try:
        app = TextAnalysisApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\n⚠️  Programa interrompido pelo usuário.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Erro crítico: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
