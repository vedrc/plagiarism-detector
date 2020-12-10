from googleapiclient.discovery import build
import json
import requests

API_KEY = "AIzaSyBTxtSKhYVox2d-GdjAURjXTFoxG0K3ue0" #The API_KEY you acquired
SEARCH_ENGINE_ID = "1305a039473f46481" #The search-engine-ID you created
query = []
lineQuery = "placeholder"
query = input("Plagirism Query: ")
"""
while lineQuery != "":
    lineQuery = input("Plagirism Query: ")
    query.append(lineQuery)
"""
query = str(query)
exclude = input("URL to exclude? ")
query = ('"' +query+'"')
page = 1
start = (page - 1) * 10 + 1
url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"
data = requests.get(url).json()
# get the result items
search_items = data.get("items")
# iterate over 10 results found
if search_items == None:
    print("No plagiarism detected.")
else:
    print("Looks like we found some plagiarism! Here are the top 10 sources we found. \n")

    for i, search_item in enumerate(search_items, start=1):
        # extract the page url
        link = search_item.get("link")
        if link == exclude:
            continue
        print(link, "\n")

