# read csv file
import pandas as pd

customers = pd.read_csv("customers_list_light.csv")
print(customers)

# import html page to scrape data
from bs4 import BeautifulSoup as bs

with open("companies.html", "r", encoding="utf-8") as f:
    soup = bs(f.read(), "html.parser")

companies_html_elements = soup.body.ul.find_all("li")
companies = []
for company in companies_html_elements:
    companies.append(company.span.text)

print(companies[:10])  # print first 10 companies

#Enrich dataset
customers["Valid"] = False
for index, company in customers.iterrows():
    if company["name"] in companies:
         print(f"Company {company['name']} found")
         customers.at[index, "Valid"] = True
    else:
         print(f"Company {company['name']} not found")
         customers.at[index, "Valid"] = False

print(customers)

#Save to disk 
customers.to_csv("results.csv", index=False)