import re
import requests
import requests.exceptions
import json
from urllib.parse import urlsplit
from collections import deque
from bs4 import BeautifulSoup

starting_url = input("Введіть веб-сторінку для пошуку ")
unprocessed_urls = deque([starting_url])
processed_urls = set()
emails = set()
while len(unprocessed_urls):
    url = unprocessed_urls.popleft()
    processed_urls.add(url)
    parts = urlsplit(url)
    base_url = "{0.scheme}://{0.netloc}".format(parts)
    path = url[:url.rfind('/')+1] if '/' in parts.path else url
    print("Crawling URL %s" % url)
    try:
        response = requests.get(url)
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
        continue
    new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
    emails.update(new_emails)
    soup = BeautifulSoup(response.text, 'html.parser')
emails_list = list(emails)
emails_dict = {}
for i in range(len(emails_list)):
        emails_dict[i]=emails_list
json_emails = json.dumps(emails_dict, indent=2)
with open("D:\\git\\VKN\\emails.json", "w") as f:
    f.write(json_emails)