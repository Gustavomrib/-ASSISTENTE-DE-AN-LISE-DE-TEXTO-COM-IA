#!/usr/bin/env python3
"""
gui.py
------
Interface gráfica com Tkinter para o Text Analysis Assistant.

Uso:
    python gui.py
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import sys
import os

# Adiciona o diretório src ao path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.analyzer import TextAnalyzer
from src.utils import format_result_for_display


class TextAnalysisGUI:
    """Interface gráfica para o Text Analysis Assistant."""
    
    def __init__(self, root):
        """Inicializa a interface gráfica."""
        self.root = root
        self.root.title("🤖 Text Analysis Assistant - Interface Gráfica")
        self.root.geometry("1000x700")
        self.root.resizable(True, True)
        
        # Configurar estilo
        self.root.configure(bg="#1a1a1a")
        style = ttk.Style()
        style.theme_use('clam')
        
        # Cores personalizadas
        self.bg_color = "#1a1a1a"
        self.fg_color = "#ffffff"
        self.accent_color = "#0d47a1"
        
        self.analyzer = TextAnalyzer(verbose=False)
        self.setup_ui()
    
    def setup_ui(self):
        """Configura os elementos da interface."""
        # Header
        header_frame = tk.Frame(self.root, bg=self.accent_color)
        header_frame.pack(fill=tk.X, padx=0, pady=0)
        
        title_label = tk.Label(
            header_frame,
            text="🤖 ASSISTENTE DE ANÁLISE DE TEXTO COM IA",
            font=("Arial", 16, "bold"),
            bg=self.accent_color,
            fg=self.fg_color
        )
        title_label.pack(pady=10)
        
        # Main content frame
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left panel - Input
        left_panel = tk.Frame(main_frame, bg=self.bg_color)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        # Input label
        tk.Label(
            left_panel,
            text="📝 TEXTO PARA ANÁLISE",
            font=("Arial", 11, "bold"),
            bg=self.bg_color,
            fg=self.fg_color
        ).pack(anchor=tk.W, pady=(0, 5))
        
        # Text input area
        self.text_input = scrolledtext.ScrolledText(
            left_panel,
            height=15,
            width=40,
            wrap=tk.WORD,
            bg="#2a2a2a",
            fg=self.fg_color,
            font=("Courier", 10),
            insertbackground=self.fg_color
        )
        self.text_input.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Buttons frame
        buttons_frame = tk.Frame(left_panel, bg=self.bg_color)
        buttons_frame.pack(fill=tk.X)
        
        # Analyze button
        analyze_btn = tk.Button(
            buttons_frame,
            text="🔍 ANALISAR",
            command=self.analyze_text,
            bg=self.accent_color,
            fg=self.fg_color,
            font=("Arial", 10, "bold"),
            padx=20,
            pady=8,
            cursor="hand2"
        )
        analyze_btn.pack(side=tk.LEFT, padx=5)
        
        # Clear button
        clear_btn = tk.Button(
            buttons_frame,
            text="🗑️ LIMPAR",
            command=self.clear_text,
            bg="#666666",
            fg=self.fg_color,
            font=("Arial", 10, "bold"),
            padx=15,
            pady=8,
            cursor="hand2"
        )
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Load file button
        load_btn = tk.Button(
            buttons_frame,
            text="📂 CARREGAR",
            command=self.load_file,
            bg="#666666",
            fg=self.fg_color,
            font=("Arial", 10, "bold"),
            padx=15,
            pady=8,
            cursor="hand2"
        )
        load_btn.pack(side=tk.LEFT, padx=5)
        
        # Right panel - Results
        right_panel = tk.Frame(main_frame, bg=self.bg_color)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)
        
        tk.Label(
            right_panel,
            text="📊 RESULTADOS DA ANÁLISE",
            font=("Arial", 11, "bold"),
            bg=self.bg_color,
            fg=self.fg_color
        ).pack(anchor=tk.W, pady=(0, 5))
        
        # Results text area
        self.results_output = scrolledtext.ScrolledText(
            right_panel,
            height=15,
            width=40,
            wrap=tk.WORD,
            bg="#2a2a2a",
            fg=self.fg_color,
            font=("Courier", 9),
            state=tk.DISABLED
        )
        self.results_output.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Export button
        export_btn = tk.Button(
            right_panel,
            text="💾 EXPORTAR",
            command=self.export_results,
            bg=self.accent_color,
            fg=self.fg_color,
            font=("Arial", 10, "bold"),
            padx=15,
            pady=8,
            cursor="hand2"
        )
        export_btn.pack(fill=tk.X, padx=0)
    
    def analyze_text(self):
        """Analisa o texto inserido."""
        text = self.text_input.get("1.0", tk.END).strip()
        
        if not text:
            messagebox.showwarning("Aviso", "Por favor, insira um texto para análise!")
            return
        
        if len(text) < 20:
            messagebox.showwarning("Aviso", "O texto deve ter pelo menos 20 caracteres!")
            return
        
        try:
            # Desabilitar botão durante análise
            self.root.config(cursor="wait")
            self.root.update()
            
            # Perform analysis
            resultado = self.analyzer.analyze(text)
            
            # Format results for display
            output = format_result_for_display(resultado)
            
            # Update results area
            self.results_output.config(state=tk.NORMAL)
            self.results_output.delete("1.0", tk.END)
            self.results_output.insert("1.0", output)
            self.results_output.config(state=tk.DISABLED)
            
            # Store results for export
            self.last_results = output
            
            messagebox.showinfo("Sucesso", "Análise concluída com sucesso!")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro durante análise: {str(e)}")
        
        finally:
            self.root.config(cursor="arrow")
    
    def clear_text(self):
        """Limpa o texto de entrada."""
        self.text_input.delete("1.0", tk.END)
        self.results_output.config(state=tk.NORMAL)
        self.results_output.delete("1.0", tk.END)
        self.results_output.config(state=tk.DISABLED)
    
    def load_file(self):
        """Carrega texto de um arquivo."""
        file_path = filedialog.askopenfilename(
            filetypes=[
                ("Arquivos de texto", "*.txt"),
                ("Todos os arquivos", "*.*")
            ]
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                self.text_input.delete("1.0", tk.END)
                self.text_input.insert("1.0", content)
                messagebox.showinfo("Sucesso", "Arquivo carregado com sucesso!")
            
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao carregar arquivo: {str(e)}")
    
    def export_results(self):
        """Exporta os resultados para um arquivo."""
        if not hasattr(self, 'last_results'):
            messagebox.showwarning("Aviso", "Nenhuma análise para exportar!")
            return
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[
                ("Arquivos de texto", "*.txt"),
                ("Todos os arquivos", "*.*")
            ]
        )
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(self.last_results)
                
                messagebox.showinfo("Sucesso", f"Resultados exportados para:\n{file_path}")
            
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao exportar: {str(e)}")


def main():
    """Função principal."""
    root = tk.Tk()
    app = TextAnalysisGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
