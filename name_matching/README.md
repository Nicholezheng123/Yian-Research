# Fellowship–Dimensions Name Matching Pipeline

## Overview
This project builds a **name-matching pipeline** to accurately link **Schmidt Science fellowship researcher names** to author records in the **Dimensions database**. The goal is to ensure reliable identity matching before downstream analysis of AI influence on research papers.

Because name inconsistencies (e.g., abbreviations, formatting differences, missing middle names) can lead to incorrect matches, this pipeline focuses on validating and improving name alignment between datasets.

---

## Research Context
**Organization:** Schmidt Science  
**Dataset Focus:** Fellowship researcher names vs. Dimensions author database

Accurate name matching is a critical preprocessing step for analyzing how AI has influenced research outputs associated with fellowship recipients.

---

## Objectives
- Verify that fellowship names correctly correspond to authors in the Dimensions database
- Reduce false matches caused by name ambiguity
- Create a reproducible and auditable matching process

---

## What I Did
- Designed an algorithm to **check name consistency** between fellowship and database records
- Built a **matching pipeline** linking fellowship names to Dimensions author names
- Implemented validation logic to flag mismatches and ambiguous cases
- Prepared clean, matched identifiers for downstream AI-ness analysis

---

## Matching Approach
The pipeline follows this process:
1. Standardize name formats across datasets
2. Match fellowship names to candidate database names
3. Apply rule-based checks to confirm valid matches
4. Flag uncertain or conflicting matches for review

This ensures that later analyses are based on **correct author identity resolution**, not name coincidences.

---

## Why This Matters
Accurate author matching is foundational for:
- Studying AI’s influence on individual researchers
- Linking publication behavior to fellowship participation
- Preventing downstream bias in AI-ness metrics and trend analyses

Errors at this stage would propagate through all later results.

---

## Learn More
For implementation details and code, see the accompanying notebook:  
👉 **`dimensions_name_matcher.ipynb`**

---

## Author
**Nichole Zheng**  
