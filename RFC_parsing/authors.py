
import requests
from bs4 import BeautifulSoup
import csv
import urllib.parse
import time

# Function to process a single RFC ID
def process_rfc(rfc_id, data_list):
    url = f"https://datatracker.ietf.org/doc/rfc{rfc_id}/"
    print(f"Processing rfc{rfc_id}...")
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to fetch rfc{rfc_id}: HTTP {response.status_code}")
            # Add the RFC ID with N/A for author and email
            data_list.append({
                'rfcID': f"rfc{rfc_id}",
                'author': 'N/A',
                'email': 'N/A'
            })
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        authors_section = soup.find('tbody', class_='meta align-top border-top')
        authors = []
        if authors_section:
            for author_tag in authors_section.find_all('a', href=True):
                name = author_tag.get_text(strip=True)
                email_tag = author_tag.find_next_sibling('a', href=True)
                if email_tag and "mailto:" in email_tag['href']:
                    raw_email = email_tag['href'].replace("mailto:", "").strip()
                    decoded_email = urllib.parse.unquote(raw_email)
                    authors.append({'name': name, 'email': decoded_email})
        
        # If no authors are found, add N/A
        if not authors:
            authors = [{'name': 'N/A', 'email': 'N/A'}]

        # Combine all authors and emails into a single string
        author_names = "; ".join([author['name'] for author in authors])
        author_emails = "; ".join([author['email'] for author in authors])

        # Append the data to the list
        data_list.append({
            'rfcID': f"rfc{rfc_id}",
            'author': author_names,
            'email': author_emails
        })

    except Exception as e:
        print(f"Error processing rfc{rfc_id}: {e}")
        # Add the RFC ID with N/A for author and email in case of any other error
        data_list.append({
            'rfcID': f"rfc{rfc_id}",
            'author': 'N/A',
            'email': 'N/A'
        })

# List of RFC IDs to process (from 1 to 1000)
rfc_ids = range(8001, 9672)

# List to store all RFC data
all_rfc_data = []

for rfc_id in rfc_ids:
    process_rfc(rfc_id, all_rfc_data)
    time.sleep(1)  # Delay to avoid overloading the server

# Write all data to a single CSV file
output_file = "rfc_authors9671.csv"
with open(output_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['rfcID', 'author', 'email'])
    writer.writeheader()
    writer.writerows(all_rfc_data)

print(f"All data saved to '{output_file}'.")
print("Processing complete.")