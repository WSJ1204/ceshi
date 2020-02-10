import tornado.ioloop
import tornado.web
import asyncio
import requests
import json

# 屏蔽ssl认证告警
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#  python3.8 asyncio 在 windows 上默认使用 ProactorEventLoop
import platform
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

    async def post(self):
        url = 'https://125.208.12.72:10089/ccfsp/Sv/Interface/Introduce/interface_introduce.asp'

        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"
        }

        json_str = {
            "ESBREQ": {
                "DATA": {
                    "Supervisor": "%E7%8E%8B%E6%99%93%E9%BE%99",
                    "FilterStatus": "1",
                    "Abstract": "+%E5%A7%94%E6%89%98%E6%9C%AA%E5%BE%85%E6%8A%A5%E7%8A%B6%E6%80%81++%5B%E4%B8%A5%E9%87%8D%5D%E5%90%88%E5%90%8C%E7%BC%96%E5%8F%B7%E4%B8%BA%3AG300002797%2C%E8%B5%84%E9%87%91%E8%B4%A6%E5%8F%B7%E4%B8%BA%3A34431789%E7%9A%84%E5%A7%94%E6%89%98%E6%9C%AA%E6%8A%A5%0D%0A%E5%90%88%E5%90%8C%E7%BC%96%E5%8F%B7%E4%B8%BA%3AGC00011348%2C%E8%B5%84%E9%87%91%E8%B4%A6%E5%8F%B7%E4%B8%BA%3A33654016%E7%9A%84%E5%A7%94%E6%89%98%E6%9C%AA%E6%8A%A5%0D%0A+",
                    "warntime": "2019-12-25+13%3A07%3A23",
                    "DeviceIP": "10.17.22.22",
                    "DeviceUsage": "%E6%8E%A5%E5%8F%A3%E5%BA%93%E5%A4%87%E6%9C%BA",
                    "SSMSystem": "%E8%BF%90%E7%BB%B4%E7%AE%A1%E7%90%86%E5%B9%B3%E5%8F%B0(%E6%AD%A3%E5%BC%8F)",
                    "AppName": "%E6%95%B0%E6%8D%AE%E5%BA%93%E6%9F%A5%E8%AF%A2",
                    "KCMMSystem": "%E8%8A%82%E7%82%B9%E4%BA%8C",
                    "PolicyDescription": "%E4%B8%80%E8%88%AC%E4%B8%BA%E6%95%B0%E6%8D%AE%E5%A4%8D%E5%88%B6%E5%BB%B6%E8%BF%9F%EF%BC%8C%E7%99%BB%E8%AE%B0%E4%BA%8B%E4%BB%B6%E5%8D%B3%E5%8F%AF%EF%BC%8C%E4%B8%80%E8%88%AC%E5%BD%93%E6%97%B6%E6%A3%80%E6%9F%A5%E5%A7%94%E6%89%98%E5%B7%B2%E6%8A%A5%E3%80%82%E5%AE%9E%E9%99%85%E4%B8%8D%E5%BD%B1%E5%93%8D%E4%B8%9A%E5%8A%A1%E3%80%82",
                    "IndexNmae": "%E5%80%BC",
                    "Level": "%E4%B8%A5%E9%87%8D",
                    "Room": "%E4%B8%9C%E5%9D%9D%E6%9C%BA%E6%88%BF",
                    "DeviceName": "DBJF-JD2-OIWBK",
                    "IndexExample": "%E5%A7%94%E6%89%98%E6%9C%AA%E5%BE%85%E6%8A%A5%E7%8A%B6%E6%80%81"
                },
                "HEADER": {
                    "MESSAGE_ID": "MonitorEvent"
                }
            }
        }

        # payload = parse.unquote(json.dumps(json_str)) # unquote解码
        # print(payload)

        response = requests.post(url, headers=headers, json=json_str, verify=False)  # verify=False解除ssl认证
        if response.content:
            data = response.json()
        self.write(data)
        print(response.status_code)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
