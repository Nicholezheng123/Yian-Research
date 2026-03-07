import subprocess

# Define the RFC range
start_rfc = 8001
end_rfc = 9671

# Base URL for RFC documents
base_url = "https://www.rfc-editor.org/rfc/rfc{}.html"

# Loop through each RFC number and download the corresponding HTML file
for rfc_num in range(start_rfc, end_rfc + 1):
    url = base_url.format(rfc_num)
    output_file = f"rfc{rfc_num}.html" 
    
    try:
        subprocess.run(["curl", "-o", output_file, url], check=True)
        print(f"Downloaded: {output_file}")
    except subprocess.CalledProcessError:
        print(f"Failed to download: {url}")
