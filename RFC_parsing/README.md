# RFC Data Collection Scripts

## Overview

This project contains Python scripts used to collect and extract information from RFC (Request for Comments) documents available online. The scripts automate downloading RFC HTML files and extracting structured metadata such as:

- Author names
- Author emails
- Reference links
- Reference types

The data is saved into CSV files for further analysis.

The scripts interact with publicly available RFC data from:

- IETF Datatracker
- RFC Editor website

---

## Files in this Project

### 1. download.py

This script downloads HTML files for a range of RFC documents from the RFC Editor website.

The script loops through RFC numbers and saves each RFC as an HTML file locally.

#### Purpose

This provides **local copies of RFC documents**, which can later be parsed or analyzed.

---
### 2. authors.py

This script extracts **author names and email addresses** for each RFC document from the IETF Datatracker website.

It accesses each page and for each RFC:

1. The webpage is downloaded
2. The author metadata section is parsed using BeautifulSoup
3. Author names and emails are extracted
4. The results are stored in a CSV file

The script can be altered to process RFC documents from **0 to 9671**.
However, this script chooses to process RFC documents by increments of 1000 for convenience. 

#### Output

The results are saved to a csv file with the following columns:
| Column | Description |
|------|------|
| rfcID | RFC identifier |
| author | Author name(s) |
| email | Author email address(es) |

Multiple authors or emails are separated using semicolons.

---
### 3. reference.py

This script extracts **references cited within RFC documents**.


The script:

1. Downloads the reference page
2. Locates the reference table
3. Extracts:
   - Reference URLs
   - Reference types
4. Saves the results into a CSV file

The script processes RFC IDs from **1 to 9671**.

#### Output

The results are saved to a csv file with the following columns:

| Column | Description |
|------|------|
| rfcID | RFC identifier |
| url | Reference URLs |
| type | Reference types |

Multiple references are separated with semicolons.

---

## Dependencies

These scripts require the following Python packages:
- requests
- beautifulsoup4




