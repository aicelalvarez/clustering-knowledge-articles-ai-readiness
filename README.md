# Clustering Knowledge Articles for AI-Readiness Assessment

This capstone project applies an end-to-end machine learning lifecycle to group knowledge-article-like content into structural archetypes that support AI-readiness assessment for enterprise AI assistants (Retrieval-Augmented Generation context).

## Project Objectives
- Build an unsupervised clustering pipeline to identify structural archetypes of knowledge articles
- Engineer interpretable features aligned with AI-ready knowledge principles
- Evaluate multiple clustering methods and justify model selection
- Provide explainability (surrogate model + SHAP) and ethical/bias analysis

## Dataset
Source: Stack Exchange public data dump (Archive.org).  
Raw archives and XML files are not included in this repository due to size.  
See `data/README.md` for reproduction steps.

## Repository Structure
- `notebooks/` Colab notebook (end-to-end pipeline)
- `src/` helper scripts (preprocessing, features, clustering, evaluation)
- `data/` dataset instructions (raw data excluded)
- `models/` saved artifacts (optional) + documentation
- `appendix/` exported CSV artifacts (data dictionary, missingness, outliers)
- `slides/` technical and business presentations
- `reports/` final report (Markdown/PDF)

## How to Reproduce
1. Create a Python environment and install requirements:
   ```bash
   pip install -r requirements.txt
