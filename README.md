# Yian-Research
# Yian Research

Research repository for projects conducted under Professor Yian Yin, focusing on large-scale data processing, entity resolution, and research analytics.

---

## Overview

This repository contains research projects related to:

- Author name disambiguation  
- Entity resolution and record linkage  
- Large-scale data pipelines for academic datasets  
- Measuring and analyzing AI-related research trends  

The work involves building scalable systems to clean, match, and analyze noisy real-world data from sources such as OpenAlex and Dimensions.

---

## Research Context

This work is part of ongoing research under Professor Yian Yin at Cornell University.

For more information on the broader research direction:  
[Professor Yian Yin – Research](https://www.yianyin.net/research.html)

---

## Projects

### 1. Name Matching Pipeline
Folder: `name_matching/`

Developed a multi-step pipeline for matching author names across datasets.

**Key components:**
- Data normalization (lowercasing, removing punctuation, handling accents)
- Name parsing (first, middle, last extraction)
- Fuzzy matching for approximate string similarity
- Nickname dictionary and handling cultural naming variations

**Outcome:**
- Automatically matched approximately 80–90% of records  
- Significantly reduced manual verification effort  

---

### 2. RFC Parsing
Folder: `RFC_parsing/`

Built tools to parse and structure unstructured text data.

**Key tasks:**
- Extract structured information from raw text  
- Clean and standardize formatting  
- Prepare datasets for downstream analysis  

---

### 3. AI-ness Metric (Research Trend Analysis)
Folder: `AI-ness/`

Analyzed how research papers evolve with respect to AI-related content.

**Key ideas:**
- Represent papers using vector embeddings  
- Measure similarity using L2 distance  
- Track how research topics shift toward AI over time  

---

## Methods and Tools

- Python  
- Pandas, NumPy  
- Scikit-learn  
- Fuzzy matching techniques  
- Data cleaning and preprocessing pipelines  

---

## Skills Demonstrated

- Large-scale data cleaning and preprocessing  
- Entity resolution and record linkage  
- Feature engineering and similarity metrics  
- Building end-to-end data pipelines  
- Research-oriented data analysis  

---

## Summary

This repository showcases research-focused data engineering and analysis work, with an emphasis on handling noisy real-world datasets and building scalable matching and analysis pipelines.

