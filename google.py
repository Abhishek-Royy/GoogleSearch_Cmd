
from googlesearch import search

# Input from the user
query = input("Enter the query: ")

for url in search(query, num=15, stop=10, pause=2):
    print(url)
