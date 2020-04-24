import requests
from bs4 import BeautifulSoup
import re

base_url = "https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html"

r = requests.get(base_url)
soup = BeautifulSoup(r.text,features="html.parser")
print ((soup))
for story_heading in soup.find_all(class_="subheadline"): 
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())