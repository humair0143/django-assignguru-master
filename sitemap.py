import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import random

df = pd.read_excel(r'C:\Users\hn_01\OneDrive\Desktop\assignguru\django-assignguru-master\set.xlsx')
arr1 = []
arr2 = []

for index, row in df.iterrows():
    arr1.append(row['setid'])
    arr2.append(row['sid'])

urls = []

urls.append('<?xml version="1.0" encoding="UTF-8"?>')
urls.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
urls.append('<url>')
count = 0


while count < len(arr1)-1:
    count += 1
    print(count)
    urls.append('<url>')
    urls.append('<loc>https://www.assignguru.com/mcqs/'+str(arr2[count])+'/'+str(arr1[count])+'</loc>')
    urls.append('<lastmod>2021-05-13T20:50:15+01:00</lastmod>')
    urls.append('<priority>0.8</priority>')
    urls.append('</url>')

urls.append('</urlset>')



df_sitemap = pd.DataFrame({
    'urls': urls,
    })

df_sitemap.to_excel(excel_writer=r"C:\Users\hn_01\OneDrive\Desktop\assignguru\django-assignguru-master\sitemap1.xlsx")