<p align="center">

  <img src="https://img.shields.io/badge/Biomedical-Information%20Retrieval-blue?style=for-the-badge" />

  <img src="https://img.shields.io/badge/Python-IR%20System-green?style=for-the-badge" />

  <img src="https://img.shields.io/badge/scispaCy-Biomedical%20NLP-orange?style=for-the-badge" />

</p>

<h1 align="center">

🩺 medSearch

</h1>

<p align="center">

Biomedical Information Retrieval System for Respiratory Disease Literature

</p>

<p align="center">

Built using TF-IDF, Inverted Indexing, Cosine Similarity, and Biomedical NLP

</p>

# Biomedical Information Retrieval System for Respiratory Disease Literature

**Biomedical Literature Search Engine Using TF-IDF, BM25, Query Expansion, Inverted Indexing, Cosine Similarity, and Biomedical NLP**

## Overview

medSearch is a biomedical information retrieval (IR) system designed for searching and retrieving respiratory disease literature from PubMed abstracts. The system enables symptom-oriented and concept-based search using classical information retrieval techniques enhanced with biomedical natural language processing.

The project explores how biomedical entity extraction, query expansion, and advanced retrieval models can improve the discovery of relevant medical literature for respiratory diseases such as asthma, COPD, pulmonary fibrosis, pneumonia, and chronic bronchitis.

**Note:** This project is intended for biomedical literature retrieval and research purposes only. It is not designed to provide medical advice, diagnosis, or treatment recommendations.

---

## Features

* PubMed biomedical corpus construction
* Respiratory disease literature retrieval
* NLTK-based preprocessing and normalization
* Biomedical entity extraction using scispaCy
* Inverted index generation
* TF-IDF document weighting
* Cosine similarity ranking
* BM25 retrieval model
* Query expansion for improved recall
* Symptom-based medical document search
* Retrieval evaluation using Precision, MAP, and NDCG
* PubMedBERT-assisted semantic evaluation
* Biomedical NLP pipeline for concept preservation

---

## Dataset

**Source:** PubMed

**Domain:** Respiratory Diseases

Example topics include:

* Asthma
* Chronic Obstructive Pulmonary Disease (COPD)
* Pulmonary Fibrosis
* Pneumonia
* Chronic Bronchitis
* Respiratory Infections
* Lung Inflammation
* Shortness of Breath Disorders

**Document Type:**

* PubMed abstracts
* Article metadata
* Biomedical literature records

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/harivadana/medsearch_indexninjas.git
cd medsearch_indexninjas
```

### 2. Create Virtual Environment

#### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Upgrade pip

```bash
python -m pip install --upgrade pip setuptools wheel
```

### 4. Install scispaCy Biomedical Model

```bash
python -m pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.5/en_core_sci_sm-0.5.5-py3-none-any.whl
```

### 5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

## Building the Biomedical Corpus

Download respiratory disease literature from PubMed:

```bash
python download_documents.py
```

Output:

```text
data/raw/respiratory_corpus.json
```

---

## Building the Inverted Index

Configure indexing options inside:

```python
USE_BIOMEDICAL_ENTITIES = True
```

Then build the index:

```bash
python build_index.py
```

Generated files:

```text
data/processed/
├── inverted_index.json
├── idf.json
├── doc_metadata.json
└── doc_lengths.json
```

---

## Retrieval Models

### TF-IDF + Cosine Similarity

Classical vector-space retrieval model using term frequency and inverse document frequency weighting.

Run:

```bash
python search.py
```

---

### BM25 Retrieval

BM25 is a probabilistic retrieval model that improves ranking quality by accounting for document length normalization and term frequency saturation.

Run:

```bash
python bm25_search.py
```

---

### Query Expansion

Expands user queries with related biomedical terminology to improve retrieval recall.

Run:

```bash
python query_expansion.py
```

---

### Expanded Search

Combines query expansion with retrieval models to improve biomedical document discovery.

Run:

```bash
python expanded_search.py
```

---

## Example Queries

```text
shortness of breath

persistent cough wheezing

pulmonary fibrosis chest tightness

asthma inflammation

copd chronic bronchitis
```

---

## Biomedical Entity Extraction

The system uses scispaCy biomedical entity extraction to preserve important medical concepts during indexing and retrieval.

Example transformations:

```text
shortness of breath
→ ENTITY_shortness_breath

pulmonary fibrosis
→ ENTITY_pulmonary_fibrosis

chronic obstructive pulmonary disease
→ ENTITY_chronic_obstructive_pulmonary_disease
```

This helps maintain the meaning of multi-word biomedical concepts and improves retrieval quality.

---

## Retrieval Pipeline

```text
PubMed Documents
        ↓
Preprocessing
        ↓
Tokenization
        ↓
Stop-word Removal
        ↓
Biomedical Entity Extraction
        ↓
Inverted Index Construction
        ↓
TF-IDF Index
        ↓
BM25 Index
        ↓
Query Expansion
        ↓
Document Retrieval
        ↓
Ranking
        ↓
Evaluation
```

---

## Evaluating the Retrieval System

### Generate Retrieval Results

Create ranked retrieval outputs for relevance assessment:

```bash
python evaluate_retrieval.py
```

Output:

```text
retrieval_results_for_judging.csv
```

---

### Manual Relevance Judgments

Assign relevance labels:

```text
0 = Not Relevant
1 = Somewhat Relevant
2 = Highly Relevant
```

---

### Compute Retrieval Metrics

Run:

```bash
python compute_metrics.py
```

Metrics:

* Precision@10
* Mean Average Precision (MAP)
* NDCG@10

---

## Semantic Evaluation with PubMedBERT

The project also supports semantic relevance evaluation using PubMedBERT.

Run:

```bash
python pubmedbert_llm_evaluation.py
```

Output:

```text
llm_assisted_evaluation_results.csv
```

Semantic evaluation helps assess retrieval quality beyond exact keyword matching by considering biomedical context and meaning.

---

## Technologies Used

* Python
* NLTK
* scispaCy
* PubMed API
* NumPy
* Pandas
* TF-IDF
* BM25
* Inverted Indexing
* Cosine Similarity
* Biomedical NLP
* Information Retrieval
* PubMedBERT

---

## Research Contributions

This project investigates how biomedical NLP techniques can improve symptom-oriented medical literature retrieval.

Research areas explored include:

* Biomedical entity extraction using scispaCy
* TF-IDF versus BM25 retrieval effectiveness
* Query expansion for improved recall
* Symptom-based biomedical search
* Semantic evaluation using PubMedBERT
* Biomedical concept preservation during indexing
* Retrieval effectiveness in medical literature search

---

## Future Work

Potential extensions include:

* Dense vector retrieval
* Transformer-based retrieval models
* Retrieval-Augmented Generation (RAG)
* Hybrid TF-IDF + Embedding retrieval
* Clinical question answering
* Biomedical knowledge graph integration
* Multi-modal biomedical search
* Advanced semantic reranking

---

## References

1. PubMed – https://pubmed.ncbi.nlm.nih.gov/
2. scispaCy – https://allenai.github.io/scispacy/
3. Robertson, S., & Zaragoza, H. (2009). The Probabilistic Relevance Framework: BM25 and Beyond.
4. Lee et al. (2020). BioBERT: A Pre-trained Biomedical Language Representation Model.
5. Gu et al. (2021). PubMedBERT: Domain-Specific Language Models for Biomedical NLP.
