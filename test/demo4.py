import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
URL = "https://125.208.12.72:10089/ccfsp/Sv/Interface/Introduce/interface_introduce.asp"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36"}


s = requests.Session()
s.headers.update(headers)
r = s.get(URL)
soup = BeautifulSoup(r.content)

r = s.post(URL,verify=False)
print(r.url)