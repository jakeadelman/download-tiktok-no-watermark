from tls_client import Session, response
from colorama import Fore, init
from bs4 import BeautifulSoup
from random import randint
# import subprocess
import requests
import os
import re
import js2py 

init(autoreset=True)



class SnapTikReversed:


    def __init__(self, userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'):
        self.userAgent = userAgent
        self.client = Session(client_identifier='chrome_109')
        self.token = self.get_token()
        self.base = []
        self.url = ""
        self.code = """// I just wanted to say, Snaptik.app, if you see this, please enhance your security measures. It was surprisingly easy to reverse engineer the rather ineffective "protection" you're currently employing.
                        // Author: cxstles on github
                        // Date: Sep 29th, 2023.

                        function start(val1,val2,val3,val4,val5,val6){                     
                        // Initialize variables
                         let h, u, n, t, e, r;

                        // Get values from command line arguments
                        h = val1;
                        u = parseInt(val2);
                        n = val3;
                        t = parseInt(val4);
                        e = parseInt(val5);
                        r = parseInt(val6);

                        // Decode function
                        function decodeString(d, e, f) {
                        const baseChars =
                            "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/";
                        const charArray = baseChars.split("").slice(0, e);
                        const outputChars = baseChars.split("").slice(0, f);

                        let j = d
                            .split("")
                            .reverse()
                            .reduce(function (a, b, c) {
                            if (charArray.indexOf(b) !== -1) {
                                return a + charArray.indexOf(b) * Math.pow(e, c);
                            }
                            return a;
                            }, 0);

                        let k = "";
                        while (j > 0) {
                            k = outputChars[j % f] + k;
                            j = Math.floor(j / f);
                        }

                        return k || "0";
                        }

                        function evalFunction(h, u, n, t, e, r) {
                        r = "";

                        for (let i = 0, len = h.length; i < len; i++) {
                            let s = "";
                            while (h[i] !== n[e]) {
                            s += h[i];
                            i++;
                            }
                            for (let j = 0; j < n.length; j++) {
                            s = s.replace(new RegExp(n[j], "g"), j);
                            }
                            r += String.fromCharCode(parseInt(decodeString(s, e, 10)) - t);
                        }
                        return decodeURIComponent(escape(r));
                        }
                        return evalFunction(h,u,n,t,e,r)

                        console.log(evalFunction(h, u, n, t, e, r));
                        }
                        """

    def get_token(self) -> response:
        try:
            response = self.client.get("https://snaptik.app")
            soup = BeautifulSoup(response.text, "lxml")
            for _input in soup.find_all("input"):
                if _input.get("name") == "token":
                    self.token = _input.get("value")
            return self.token
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None

    def send_request(self, video: str) -> response:
        try:
            headers = {
                'authority': 'snaptik.app',
                'accept': '*/*',
                'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
                'dnt': '1',
                'origin': 'https://snaptik.app',
                'referer': 'https://snaptik.app/',
                'sec-ch-ua': '"Opera";v="99", "Chromium";v="113", "Not-A.Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin'
            }
            response = self.client.get('https://snaptik.app/abc2.php', headers=headers, params={
                'url': video,
                'token': self.token
            })
            _var = re.findall(r'\(\".*?,.*?,.*?,.*?,.*?.*?\)', response.text)
            self.base = []
            for e in (_var[0].split(",")):
                self.base.append(str(e).replace("(", "").replace(")", "").replace('"', ""))
            return self.base
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None

    def decode(self, variable: list):
        try:
            process1 = js2py.eval_js(self.code)
            output = process1(str(variable[0]), str(variable[1]), str(variable[2]), str(variable[3]), str(variable[4]), str(variable[5]))
            return output
        except Exception as e:
            print(f"Decode error: {e}")
            return None

    def get_video(self, video: str, _path: str=None) -> response:
        try:
            _page = self.send_request(video)
            _page = self.decode(_page)
            soup = BeautifulSoup(_page, "lxml")
        
            for a in soup.find_all("a"):
                url = a.get("href")
                url = str(url).replace('\\', "").replace('"', "")

                if "snaptik" in url:
                    self.url = url
        
            response = requests.get(self.url)
            id = f"{randint(1000000, 9999999)}.mp4"

            if _path:
                file_path = os.path.join(_path, id)
            else:
                file_path = id

            with open(file_path, "wb") as file:
                file.write(response.content)

            return f">> [{Fore.GREEN}{video}{Fore.RESET}] success | {file_path}"
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None


def download(video_url, output_name, output_dir):
    sn = SnapTikReversed()
    token = sn.get_token()
    my_vid = sn.send_request(video=video_url)
    my_vid1= sn.decode(variable=my_vid)
    print(my_vid1)
    sp = BeautifulSoup(my_vid1)

    d = 0
    for a in sp.find_all('a', href=True):
        if d==0:
            link = a['href']
            link = link.replace('\\"',"")
            name = output_dir + output_name + '.mp4'
            with open(name, 'wb') as out_file:
                content = requests.get(link, stream=True).content
                out_file.write(content)
        d=d+1
    return(True)

