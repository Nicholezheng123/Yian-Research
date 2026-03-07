import requests
from bs4 import BeautifulSoup
import csv

import requests
from bs4 import BeautifulSoup
import csv

# Function to extract references for a given RFC ID
def extract_references(rfc_id):
    url = f"https://datatracker.ietf.org/doc/rfc{rfc_id}/references/"
    print(f"Processing rfc{rfc_id}...")
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to fetch rfc{rfc_id}: HTTP {response.status_code}")
            return None

        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find reference table
        references_table = soup.find('table', class_='table')
        if not references_table:
            print(f"No references table found for rfc{rfc_id}.")
            return None

        # Extract the references
        urls = []
        types = []
        for row in references_table.find_all('tr')[1:]:  # Skip the header row
            cols = row.find_all('td')
            if len(cols) > 0:  # Ensure there are columns in the row
                link_tag = cols[0].find('a')  # Find the hyperlink in the first column
                if link_tag and link_tag['href']:
                    ref_url = link_tag['href']
                    ref_type = cols[0].get_text(strip=True)  # Get the reference type text
                    urls.append(ref_url)
                    types.append(ref_type)

        # Combine all URLs and types into single strings with semicolons
        combined_urls = "; ".join(urls) if urls else "N/A"
        combined_types = "; ".join(types) if types else "N/A"

        return combined_urls, combined_types

    except Exception as e:
        print(f"Error processing rfc{rfc_id}: {e}")
        return None

# List of RFC IDs to process
rfc_ids = range(1,9672)

# List to store all RFC data
all_rfc_data = []

# Process each RFC ID
for rfc_id in rfc_ids:
    result = extract_references(rfc_id)
    if result is not None:
        combined_urls, combined_types = result
        all_rfc_data.append({
            'rfcID': f"rfc{rfc_id}",
            'url': combined_urls,
            'type': combined_types
        })
    else:
        # Add the RFC ID with N/A for URLs and types if processing fails
        all_rfc_data.append({
            'rfcID': f"rfc{rfc_id}",
            'url': 'N/A',
            'type': 'N/A'
        })

# Write all data to a single CSV file
output_file = "all_references.csv"
with open(output_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['rfcID', 'url', 'type'])
    writer.writeheader()
    writer.writerows(all_rfc_data)

print(f"All references have been saved to '{output_file}'.")
print("Processing complete.")