import requests
from bs4 import BeautifulSoup
import pandas as pd


url = ''
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all <tr> tags on the page
trs = soup.find_all('tr')

# Create a list to store the scraped data
data = []

# Loop over each <tr> tag and extract the contents of its <td> tags
for tr in trs:
    tds = tr.find_all('td')
    data.append([tds[0].text.strip(), tds[1].text.strip()])

# Create a Pandas DataFrame from the scraped data
df = pd.DataFrame(data, columns=['Column 1', 'Column 2'])

# Export the DataFrame to an Excel file
df.to_excel('output.xlsx', index=False)
