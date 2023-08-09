import requests
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup
def mod_res(r):
  url = "https://jade-secretive-plastic.glitch.me/"
  l = []
  
  soup = BeautifulSoup(r,"html.parser")
  for link in soup.findAll("a"):
    l.append(link.get("href"))
  for i in l:
    r = r.replace(i,f"{url}/search?query={i}")  
  return r
def change_res(r, abs_url):
  
    absolutize = lambda m: ' src="' + urljoin(abs_url, m.group(1)) + '"'
    htm = re.sub(r' src="([^"]+)"', absolutize, r)
    absolutize2 = lambda m: ' href="' + urljoin(abs_url, m.group(1)) + '"'
    html = re.sub(r' href="([^"]+)"', absolutize2, htm)
    return html
  



def get_res(q):
    
    r = (requests.get(q).text)
    

    r2 = r.replace('\n', '').replace('\r', '').replace('\t','')
    

    x = change_res(r2,q)
  

    y = mod_res(x)

    t = re.sub("\\'", "'", y)
    
    return t
