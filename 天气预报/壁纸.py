# -*- coding: gbk -*-
import requests
from tqdm import tqdm


def bz(self):
    url = 'http://api.63code.com/bing/api.php'
    r = requests.get(url)
    with open('bz.jpg', 'wb') as f:
        f.write(r.content)
