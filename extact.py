import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Find all div elements that contain the investor data
rows = soup.find_all('div', id=lambda x: x and x.startswith('search-results-data-table-row-'))

# Prepare CSV file
with open('investors_list.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Write header
    csvwriter.writerow(['Limited Partners', 'Description'])

    # Process each row
    for row in rows:
        cells = row.find_all('div', class_='cell-editable__content')
        if len(cells) >= 2:  # Ensure we have at least 2 cells
            limited_partners = cells[0].get_text(strip=True)
            description = cells[1].get_text(strip=True)

            csvwriter.writerow([limited_partners, description])

print("Data has been extracted and saved to 'investors_list.csv'")