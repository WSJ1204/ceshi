from urllib.request import Request, urlopen
import ssl

request = Request('https://125.208.12.72:10089/ccfsp/Sv/Interface/Introduce/interface_introduce.asp')

request.add_header(
    'User-agent',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3554.0 Safari/537.36'
)

context = ssl._create_unverified_context()

res = urlopen(request, context=context)
print()
