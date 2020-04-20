#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 14:22
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : wyyyy.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/19 22:29
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : searchByname.py

"""
bilibili
变量 ：{"s":"达瓦达瓦","limit":"8","csrf_token":""}
常量：010001
常量 ：00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7
常量 ：0CoJUm6Qyw8W8jud

bilibili
{"logs":"[{\"action\":\"searchkeywordclient\",\"json\":{\"type\":\"song\",\"keyword\":\"回个电话\",\"offset\":0}}]","csrf_token":""}
010001
00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7
0CoJUm6Qyw8W8jud

bilibili
{"logs":"[{\"action\":\"searchkeywordclient\",\"json\":{\"type\":\"song\",\"keyword\":\"大王\",\"offset\":0}}]","csrf_token":""}
====010001
====00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7
====0CoJUm6Qyw8W8jud
"""

"""
function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }


    defg 是传递的参数
    function d(d, e, f, g) {
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }


"""
import requests
import os
import time
import json
import base64
import requests
import codecs
from Crypto.Cipher import AES


def createSecretKey(size):
    return (''.join(map(lambda xx: (hex(ord(xx))[2:]), str(os.urandom(size)))))[0:16]


# 进行aes加密
def aesEncrypt(text, secKey):
    pad = 16 - len(text) % 16
    if isinstance(text, bytes):
        text = text.decode('utf-8')
    text = text + str(pad * chr(pad))
    encryptor = AES.new(str.encode(secKey), AES.MODE_CBC, b'0102030405060708')
    # print(text,len(text),type(text))
    ciphertext = encryptor.encrypt(str.encode(text))
    ciphertext = base64.b64encode(ciphertext)
    return ciphertext


# 进行rsa加密
def rsaEncrypt(text, pubKey, modulus):
    text = text[::-1]
    rs = int(codecs.encode(text.encode('utf-8'), 'hex_codec'), 16) ** int(pubKey, 16) % int(modulus, 16)
    return format(rs, 'x').zfill(256)


# 将明文text进行两次aes加密获得密文encText，因为secKey是在客户端上生成的，所以还需要对其进行RSA加密再传给服务端
def encrypted_request(text):
    modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    nonce = '0CoJUm6Qyw8W8jud'
    pubKey = '010001'
    text = json.dumps(text)
    secKey = createSecretKey(16)
    encText = aesEncrypt(aesEncrypt(text, nonce), secKey)
    encSecKey = rsaEncrypt(secKey, pubKey, modulus)
    data = {
        'params': encText,
        'encSecKey': encSecKey
    }
    return data


# 偏移量
def get_offset():
    name = '一天'
    text = {
        "hlpretag": "<span class='s-fc7'>",
        "hlposttag": "</span>",
        "s": name,
        "type": "1",
        "offset": "0",
        "total": "true",
        "limit": "30",
        "csrf_token": ""
    }
    return text


def get_json_data(url):
    text = get_offset()
    data = encrypted_request(text)
    json_text = get_req(url, data)
    # print(json_text)
    return json_text


def get_req(url, data):
    headers = {
        'pragma': 'no-cache',
        'cookie': '_ntes_nnid=c557afbc4dc9feb576252f2e1b0d697f,1573198801321; _ntes_nuid=c557afbc4dc9feb576252f2e1b0d697f; WM_TID=eE51s0AHVzxFEEFRFFN5qWCTvyWI5Bes; ntes_kaola_ad=1; UM_distinctid=1716c7f5d63333-095e2e6ab9c647-3a614f0b-1fa400-1716c7f5d646d8; vinfo_n_f_l_n3=19eb076404e7073a.1.1.1586663216354.1586663908865.1586684911851; WM_NI=4IA7NVdgVPI1ij%2FG5o%2B706xUSUhHZuVoR1eEhuU9c9WAYtpy04yJi22cQQTTZmWkOFd2AQ3gUW2pn7wdyPinyHkP6nJBnHl6UYi1PO5syW%2BAY%2B5chNM8asmYdKY9EYZhU3o%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee9bdb7398aca7b0ee43b0968eb6c15b829a9ebbb54bb48686dae75f90e88e90c12af0fea7c3b92af8978fd8cd5ea8b99ab1cc3babb6e1a8b865e9e900d7fb5f918ba8a9d97f96b19ed2e84facab9bdae233959f9795f373f4ecb7abec3af2bd9fb2d7609ab3998cce4ea8ee8fb2b26d9789fe91ed3db5bcb7b1ec66bb98a5b1b5668a9ea2a9ef3e9787a7d2d345f7adb7b8aa4b9bf5fb84eb468fe8af94f053a89597dac8539ab89bd4ee37e2a3; _iuqxldmzr_=32; JSESSIONID-WYYY=3oHPmKEt4cFEgav31KMR6SE%2BHcEfjFSdYkcWw%2FihAHXqgiplAhhhHo1ycd5uB7m9DauR%5CJctdTpmfcEGqo6V4f56hVqjk%5C6BS3115HMJD%2FuRFsdP7srfH18V4eJUNP9xZ7Zat%2BNs%2BhjRfPsM1hqg7i%2BZ32D07EvOe5j1%2F6ia0btdPae%5C%3A1587326422038',
        'origin': 'https://music.163.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'authority': 'music.163.com',
        'referer': 'https://music.163.com/search/',
    }

    response = requests.post(url, headers=headers,
                             data=data)

    # print(response.content)
    return response.text


def parese_songs_json(json_text):
    result = json.loads(json_text)
    songs = result['result']['songs']
    songs_dict = {}
    for item in songs:
        song_name = item['name']
        song_id = item['id']
        author_name = item['ar'][0]['name']
        author_id = item['ar'][0]['id']
        album_id = item['al']['id']
        album_name = item['al']['name']
        songs_dict = {
            'name': song_name,
            'id': song_id
        }
        print("歌曲名称:" + song_name + "======" +
              "歌曲id:" + str(song_id) + "====" +
              "作者:" + author_name + "======" +
              "作者id:" + str(author_id) + "======" +
              "专辑:" + album_name + "======" +
              "专辑id:" + str(album_id))
    print(songs_dict)


from urllib.request import urlretrieve


def download(url, id):
    try:
        text = {
            "ids": "[{}]".format(id),
            "br": 128000,
            "csrf_token": ""
        }
        data = encrypted_request(text)
        json_text = get_req(url, data)
        result = json.loads(json_text)
        dow_url = result['data'][0]['url']
        print(dow_url)
        res = requests.get(dow_url).content
        with open("{}.m4a".format(id), "ab") as f:
            f.write(res)
    except Exception as e:
        print("付费歌曲请充钱", e)


def search(url, name):
    text = {
        "hlpretag": "<span class='s-fc7'>",
        "hlposttag": "</span>",
        "s": name,
        "type": "1",
        "offset": "0",
        "total": "true",
        "limit": "30",
        "csrf_token": ""
    }
    data = encrypted_request(text)
    json_text = get_req(url, data)
    parese_songs_json(json_text)


if __name__ == '__main__':
    songs_url = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token='
    download_url = 'https://music.163.com/weapi/song/enhance/player/url?csrf_token='
    name = input("请输入歌曲名称:")
    search(songs_url, name)
    id = input("请在上方选个id输入下载:")
    download(download_url, id)

"""

bilibili{"hlpretag":"<span class=\"s-fc7\">","hlposttag":"</span>","s":"德默西亚","type":"1","offset":"0","total":"true","limit":"30","csrf_token":""}====010001====00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7====0CoJUm6Qyw8W8jud

"""