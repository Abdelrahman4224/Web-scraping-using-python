#istall pandas , requests , bountiful soup ,html5lib
!mamba install pandas==1.3.3 -y
!mamba install requests==2.26.0 -y
!mamba install bs4==4.10.0 -y
!mamba install html5lib==1.1 -y

#import modules
from bs4 import BeautifulSoup
import html5lib
import requests
import pandas as pd





url = "https://web.archive.org/web/20200318083015/https://en.wikipedia.org/wiki/List_of_largest_banks"   #define url 
html_data = requests.get(url).text           															 #get the html text from url using requests

soup = BeautifulSoup(html_data, "html5lib")   															 #parse the html using bountiful soup and creat a soup object

data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])   									 # creat an empty data frame with columns name and market cap


table = soup.find_all("table", {"class" : "wikitable sortable mw-collapsible"})              # using find all to get all the tables in the webpage and store them in a list also using class parameter to filter the tables

# Get all rows from the table
for row in table[2].find_all('tr'):  # in html table row represented by tag <tr> , i use table[2] to choose the table from the list and avoid looping through all tables
    # Get all columns in each row.
    cols = row.find_all('td')  
    if len(cols) >= 3:  # Ensure there are at least 3 columns (Rank, Bank Name, and Total Assets) the columns of the table
        rank = cols[0].get_text(strip=True)  # Get the text content of the 1st column (Rank) 
        bank_name = cols[1].get_text(strip=True)  # Get the text content of the 2nd column (Bank Name)
        assets = cols[2].get_text(strip=True)  # Get the text content of the 3rd column (Total Assets)
        data = data.append({"Name": bank_name, "Market Cap (US$ Billion)": assets}, ignore_index=True)   # store everthing in the panda dataframe
		
		
		
data.head(5)   #print first five rows for testing
data.to_json("bank_market_cap.json")  #store the data as json format in a file
