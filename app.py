from search import search
import sys
import os
import streamlit as st
import pandas as pd
import time

from download_documents import download_pubmed_articles
from build_index import build_index

st.set_page_config(
    page_title="medSearch",
    page_icon="🩺",
    layout="wide",
)

st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 1rem 0 0.5rem 0;
    }
    .main-header h1 {
        font-size: 2.8rem;
        background: linear-gradient(90deg, #1e88e5, #43a047);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .main-header p {
        color: #666;
        font-size: 1.05rem;
    }
    .result-card {
        background: #f8f9fa;
        border-left: 4px solid #1e88e5;
        border-radius: 8px;
        padding: 1.2rem 1.5rem;
        margin-bottom: 1rem;
    }
    .result-card h3 {
        margin: 0 0 0.5rem 0;
        color: #1a1a2e;
    }
    .result-meta {
        color: #555;
        font-size: 0.9rem;
        margin-bottom: 0.4rem;
    }
    .result-abstract {
        color: #333;
        font-size: 0.92rem;
        line-height: 1.5;
        margin-top: 0.5rem;
    }
    .score-badge {
        display: inline-block;
        background: #1e88e5;
        color: white;
        padding: 2px 10px;
        border-radius: 12px;
        font-size: 0.85rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

CORPUS_PATH = "data/raw/respiratory_corpus.json"
INDEX_PATH = "data/processed/inverted_index.json"

if not os.path.exists(CORPUS_PATH):
    with st.spinner("Downloading PubMed articles..."):
        download_pubmed_articles()

if not os.path.exists(INDEX_PATH):
    with st.spinner("Building search index..."):
        build_index()

st.markdown("""
<div class="main-header">
    <h1>🩺 medSearch</h1>
    <p>Biomedical Information Retrieval System for Respiratory Disease Literature</p>
    <p style="font-size: 0.85rem; color: #999;">Built using TF-IDF · Inverted Indexing · Cosine Similarity · scispaCy NLP</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

with st.sidebar:
    st.markdown("### ⚙️ Corpus Settings")
    corpus_size = st.number_input("Number of PubMed documents:", min_value=10, max_value=5000, value=1000, step=100)
    if st.button("Rebuild Corpus & Index", use_container_width=True):
        with st.spinner(f"Downloading {corpus_size} articles..."):
            download_pubmed_articles(retmax=corpus_size)
        with st.spinner("Rebuilding search index..."):
            build_index()
        st.session_state.results = []
        st.session_state.last_query = ""
        st.success(f"Corpus rebuilt with {corpus_size} documents.")

    st.markdown("---")
    st.markdown("### 🧑‍🔬👩‍🔬👨‍🔬 Team")
    st.markdown("Yasmeen Wood, Aksheytha Chelikavada, and Naga Harivadana Kalapatapu")

col1, col2 = st.columns([4, 1])

with col1:
    user = st.text_input("🔍 Enter symptom query:", placeholder="e.g. shortness of breath, persistent cough wheezing")

with col2:
    viewResults = st.selectbox("Results:", [3, 6, 9, 12], index=1)

if "results" not in st.session_state:
    st.session_state.results = []
    st.session_state.last_query = ""

if st.button("Search", type="primary", use_container_width=True):

    if not user.strip():
        st.warning("Please enter a query to search.")
    else:
        bar = st.progress(0)
        for i in range(0, 100, 10):
            bar.progress(i + 1)
            time.sleep(0.05)

        st.session_state.results = search(user, viewResults)
        st.session_state.last_query = user

        bar.progress(100)
        time.sleep(0.2)
        bar.empty()

if not st.session_state.results and st.session_state.last_query:
    st.info("No results found. Try a different query.")
elif st.session_state.results:
    st.markdown(f"**{len(st.session_state.results)} results** for *\"{st.session_state.last_query}\"*")
    st.markdown("")

    for i, r in enumerate(st.session_state.results):
        score_val = r['score']
        st.markdown(f"""
        <div class="result-card">
            <h3>{i + 1}. {r['title']}</h3>
            <div class="result-meta">
                <span class="score-badge">Score: {score_val:.4f}</span>
                &nbsp;&nbsp;📖 {r['journal']} &nbsp;&nbsp;📅 {r['year']} &nbsp;&nbsp;🆔 PMID: {r['pmid']}
            </div>
            <div class="result-meta">
                🔗 <a href="{r['url']}" target="_blank">{r['url']}</a>
            </div>
            <div class="result-abstract">
                {r['abstract'][:500]}...
            </div>
        </div>
        """, unsafe_allow_html=True)
