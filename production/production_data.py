import requests

url = "https://ohiodnr.gov/static/documents/oil-gas/production/20210309_2020_1%20-%204.xls"
response = requests.get(url)
with open("production_data.xls", "wb") as file:
    file.write(response.content)
