# AI Trends Analysis: General vs AI Tool Papers

This project analyzes how research papers evolve with respect to AI-related content, comparing trends between the general research population and Schmidt Fellows.

---

## Overview

The goal of this analysis is to understand how AI is diffusing into research over time and whether leading researchers adopt AI earlier than the broader community.

We compare two populations:
- General research papers  
- Schmidt Fellow papers (representing leading researchers)

We further categorize papers into:
- AI tool producers (build AI tools)
- AI tool consumers (use or reference AI tools)
- Papers with no AI involvement  

Using embedding-based similarity (L2 distance), we measure how closely each paper aligns with AI-related content.

---

## Research Questions

- How has the use of AI tools in research changed over time?
- Do Schmidt Fellows adopt AI tools earlier than the general population?
- How does similarity to AI-related content differ across paper types?
- Are non-AI papers becoming more “AI-like” over time?

---

## Methodology

### Data
- General research paper dataset  
- Schmidt Fellow dataset  
- Time range: 2012 – present  

---

### Key Variables
- `is_AITool` — whether the paper involves AI tools  
- `l2_normalized` — similarity to AI-related embeddings  
- `publication_year`  

---

### Approach
- Represent papers using vector embeddings  
- Compute L2 distance to AI reference embeddings  
- Compare:
  - Trends over time  
  - Differences between fellows vs general researchers  
  - Differences across AI usage categories  

---

## Key Findings

### 1. Rapid Growth of AI Tool Adoption
- AI-tool papers increase significantly after ~2016  
- Growth reflects widespread adoption of machine learning and AI tools  

---

### 2. Schmidt Fellows Adopt AI Earlier and More Frequently
- Fellows reach ~15–17% AI-tool usage  
- General population reaches ~8%  
- Fellows show faster adoption curves  

**Interpretation:**  
Leading researchers tend to adopt emerging technologies earlier, likely due to greater resources and involvement in cutting-edge work.

---

### 3. Clear Separation Between Paper Types

L2 similarity shows a consistent ordering:

- AI producers: ~0.43  
- AI consumers: ~0.47  
- No AI papers: ~0.51  

**Interpretation:**  
The embedding-based metric effectively distinguishes levels of AI involvement.

---

### 4. Stable Similarity Distributions
- AI-tool papers consistently cluster around 0.40–0.47  
- Distributions remain stable across years  

---

### 5. Diffusion of AI into General Research
- Even non-AI papers show decreasing L2 distance over time  
- Indicates increasing similarity to AI-related content  

**Interpretation:**  
AI is not confined to specialized papers — it is spreading across research fields.

---

### 6. AI Adoption Occurs Through Usage Before Creation
By 2025:
- ~17% of papers reference AI tools  
- ~8% produce AI tools  

**Interpretation:**  
Researchers are more likely to adopt existing tools before developing new ones.

---

## Tools and Techniques

- Python  
- Pandas, NumPy  
- Embedding-based similarity analysis  
- Data visualization  

---

## Files

- `general_vs_fellow_ai_tool_analysis.ipynb` — main analysis notebook  

---

## Additional Resources

For full methodology, visualizations, and detailed results, see the project slides:  
https://docs.google.com/presentation/d/16TIMsRiXdbt3YrXtm96XVCkUhd7_ceFhMNgHt5Er0ms/edit?slide=id.g395ddb12497_0_180#slide=id.g395ddb12497_0_180

---

## Summary

This project demonstrates how AI adoption differs between leading researchers and the broader academic community.

The results show that Schmidt Fellows adopt AI tools earlier and more intensively, while AI methods gradually diffuse into general research, making the boundary between AI and non-AI work increasingly blurred.