"""
app.py
------
Interface web com Streamlit para o Text Analysis Assistant.

Execucao:
    streamlit run app.py
"""

from __future__ import annotations

from typing import Dict

import streamlit as st

from src.analyzer import TextAnalyzer
from src.models import AnalysisResult
from src.utils import format_result_for_display, load_sample_texts, validate_text_input


def get_analyzer() -> TextAnalyzer:
    """Cria (uma vez por sessao) o analisador principal."""
    if "analyzer" not in st.session_state:
        st.session_state.analyzer = TextAnalyzer(verbose=False)
    return st.session_state.analyzer


def get_samples() -> Dict[str, Dict[str, str]]:
    """Retorna os textos de exemplo existentes no projeto."""
    return load_sample_texts()


def apply_custom_css() -> None:
    """Aplica ajustes visuais leves para melhorar legibilidade e espacamento."""
    st.markdown(
        """
        <style>
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2.5rem;
        }
        .hero-card {
            border: 1px solid rgba(49, 51, 63, 0.2);
            border-radius: 16px;
            padding: 1.1rem 1.2rem;
            background: rgba(240, 242, 246, 0.35);
            margin-bottom: 1rem;
        }
        .section-card {
            border: 1px solid rgba(49, 51, 63, 0.15);
            border-radius: 14px;
            padding: 1rem 1rem 0.6rem 1rem;
            background: rgba(250, 250, 252, 0.25);
            margin-bottom: 1rem;
        }
        .small-muted {
            color: #6b7280;
            font-size: 0.94rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_header() -> None:
    """Renderiza topo da pagina com titulo, subtitulo e descricao curta."""
    st.markdown(
        """
        <div class="hero-card">
            <h1 style="margin:0 0 0.2rem 0;">Text Analysis Assistant</h1>
            <p style="margin:0; font-size:1.05rem;">
                Analise de texto com NLP para extrair insights acionaveis.
            </p>
            <p class="small-muted" style="margin:0.45rem 0 0 0;">
                Gere resumo, pontos-chave, sugestoes, tom e estatisticas em uma unica analise.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_metrics(result: AnalysisResult) -> None:
    """Mostra os principais indicadores em cards."""
    stats = result.text_stats
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Tom", result.language_tone.capitalize())
    col2.metric("Complexidade", f"{result.complexity_score * 100:.1f}%")
    col3.metric("Palavras", stats.get("total_palavras", 0))
    col4.metric("Frases", stats.get("total_frases", 0))


def render_stats(result: AnalysisResult) -> None:
    """Renderiza estatisticas detalhadas e frequencia de termos."""
    stats = result.text_stats

    st.subheader("Estatisticas do texto")
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"Total de caracteres: {stats.get('total_caracteres', 0)}")
        st.write(f"Palavras unicas: {stats.get('palavras_unicas', 0)}")
        st.write(
            "Media de palavras por frase: "
            f"{stats.get('media_palavras_por_frase', 0)}"
        )
    with col2:
        st.write(
            "Palavras significativas: "
            f"{stats.get('palavras_significativas', 0)}"
        )
        st.write(
            "Palavras mais frequentes: "
            f"{len(stats.get('palavras_mais_frequentes', {}))}"
        )

    frequent_words = stats.get("palavras_mais_frequentes", {})
    if frequent_words:
        st.subheader("Palavras mais frequentes")
        st.bar_chart(frequent_words)


def render_result(result: AnalysisResult) -> None:
    """Exibe o resultado da analise em tabs."""
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("Indicadores principais")
    render_metrics(result)
    st.markdown("</div>", unsafe_allow_html=True)

    tab_summary, tab_key_points, tab_actions, tab_stats = st.tabs(
        ["Resumo", "Pontos-chave", "Sugestoes", "Estatisticas"]
    )

    with tab_summary:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.write(result.summary if result.summary else "Resumo indisponivel para este texto.")
        st.markdown("</div>", unsafe_allow_html=True)

    with tab_key_points:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        if result.key_points:
            for point in result.key_points:
                clean_point = point.lstrip("•").strip()
                st.write(f"- {clean_point}")
        else:
            st.info("Nenhum ponto-chave foi identificado para este texto.")
        st.markdown("</div>", unsafe_allow_html=True)

    with tab_actions:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        if result.action_suggestions:
            for idx, suggestion in enumerate(result.action_suggestions, start=1):
                st.write(f"{idx}. {suggestion}")
        else:
            st.info("Nenhuma sugestao de acao foi gerada para este texto.")
        st.markdown("</div>", unsafe_allow_html=True)

    with tab_stats:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        render_stats(result)
        st.markdown("</div>", unsafe_allow_html=True)


def main() -> None:
    """Ponto de entrada da interface Streamlit."""
    st.set_page_config(
        page_title="Text Analysis Assistant",
        page_icon="??",
        layout="wide",
    )

    apply_custom_css()
    render_header()

    analyzer = get_analyzer()
    samples = get_samples()

    if "last_result" not in st.session_state:
        st.session_state.last_result = None

    with st.sidebar:
        st.header("Configuracoes")
        mode = st.radio(
            "Origem do texto",
            options=["Texto livre", "Texto de exemplo"],
            index=0,
            help="Use texto livre para colar seu conteudo ou selecione um exemplo pronto.",
        )

        selected_sample = None
        if mode == "Texto de exemplo":
            option_map = {f"{k} - {v['titulo']}": k for k, v in samples.items()}
            selected_label = st.selectbox(
                "Escolha um exemplo",
                options=list(option_map.keys()),
                help="Exemplos pre-carregados para teste rapido.",
            )
            selected_sample = samples[option_map[selected_label]]

        min_chars = st.slider(
            "Tamanho minimo do texto",
            min_value=20,
            max_value=200,
            value=20,
            help="A analise exige uma quantidade minima de caracteres.",
        )
        st.caption("As configuracoes secundarias ficam aqui para manter a tela principal organizada.")

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("Entrada de texto")
    st.caption("Insira manualmente ou use um exemplo para gerar a analise.")

    if mode == "Texto de exemplo" and selected_sample:
        text_input = st.text_area(
            "Texto para analise",
            value=selected_sample["texto"],
            height=280,
            help="Voce pode editar o texto de exemplo antes de analisar.",
        )
    else:
        text_input = st.text_area(
            "Texto para analise",
            placeholder="Cole ou escreva aqui o texto que deseja analisar...",
            height=280,
            help="Textos maiores costumam gerar resumos e insights mais ricos.",
        )
    st.markdown("</div>", unsafe_allow_html=True)

    action_col1, action_col2 = st.columns([1, 3])
    with action_col1:
        analyze_clicked = st.button(
            "Analisar texto",
            type="primary",
            use_container_width=True,
            help="Executa o pipeline de analise no texto informado.",
        )
    with action_col2:
        st.caption("Dica: ajuste o tamanho minimo na sidebar para validar entradas mais curtas ou longas.")

    if analyze_clicked:
        is_valid, message = validate_text_input(text_input, min_length=min_chars)
        if not is_valid:
            st.error(message)
        else:
            with st.spinner("Processando analise..."):
                st.session_state.last_result = analyzer.analyze(text_input)
            st.success("Analise concluida com sucesso.")

    if st.session_state.last_result is None:
        st.info("Nenhuma analise executada ainda. Informe um texto e clique em 'Analisar texto'.")
    else:
        render_result(st.session_state.last_result)
        st.download_button(
            label="Baixar resultado em TXT",
            data=format_result_for_display(st.session_state.last_result),
            file_name="analise_texto.txt",
            mime="text/plain",
            use_container_width=False,
        )

    st.markdown("---")
    st.subheader("Sobre o projeto")
    st.write(
        "Este app faz parte de um projeto de analise de texto com IA/NLP, "
        "desenvolvido para extrair insights de forma rapida e objetiva sem depender de APIs externas."
    )


if __name__ == "__main__":
    main()

