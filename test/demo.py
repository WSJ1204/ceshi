import requests

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = "https://125.208.12.72:10089/ccfsp/Sv/Interface/Introduce/interface_introduce.asp"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"
}

res = requests.get(url, headers=headers, verify=False)

print(res.status_code)