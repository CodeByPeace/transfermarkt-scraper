import requests
from bs4 import BeautifulSoup
import pandas as pd
session = requests.Session()

session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
data = []
for page in range(1, 21):
    url = f'https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop?page={page}'
    response = session.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'items'})
    
    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        if len(cols) > 8:
            player_name = cols[3].text.strip()
            market_value = cols[8].text.strip()
            data.append({'Player': player_name, 'Market Value': market_value})
df = pd.DataFrame(data)
print(df)
df.to_csv('transfermarkt_players.csv', index=False)