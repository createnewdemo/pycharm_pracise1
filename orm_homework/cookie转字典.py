#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 11:11
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : cookie转字典.py
data = 'shshshfpa=c571820e-9c16-b0b6-1b57-c56f75a0933d-1539094005; shshshfpb=1d66d9125a15b4e5da107c3f92e62b707463e76af503f062d5bbcb5f7c; 3AB9D23F7A4B3C9B=2WZYTPYH7AOAQ2QOYFXSDSQ3ZNIGCNMLI2NTVRCRHPA3LDVYODD4XGYIBA6UQ3YIKDJLVUU5MWPCQPJENEJKKTBWJE; unpl=V2_ZzNtbUVSQBMgCUdQLBFaA2JWRQoRVkRCJQ1GXX0aWwxkBEBaclRCFnQUR1FnGV0UZAMZWEBcRhxFCEdkeB5fA2AFEFlBZxBFLV0CFi9JH1c%2bbRdZQVZLFX0MQ1B7KWwGZzMSXHJXQBdzAE5Seh5sNWAzIm1HVUsUcjhHZHopHlE7BRNUQVNAWHULRFJzEVoEYDMTbUE%3d; CCC_SE=ADC_91emn6gwBKOUbjOIieScwP4zX2hRGIQz0n%2fxmp2PTtY%2fUJvNJNXeoTB3%2fbSlZ5J6XK3yHutzB8Oc13%2fqDEW2Am5ccYCKXMhWS8BV49GGg%2fCg9KWUXIb77dy5XyQicE9p1sCtKFnIK9uEEYhgdZy%2fuxwi5OQid5cFfOhnxvZ045o5ND807O4Qf4zjBKcaNGktocV4mkK8cK3GS1VdZSTiaU55oEFGgSuDT1pi78HjwFj2NqahNvmIlHprJugQB%2bqk%2bGptLIqxkxMaWLLZ5KEUD6BkUp1ocIKOAW4kz53ZIzw6NUIQn2M53qpbN1MUIV4DzcYSdFLFaUAyzyr44sCJT7m0xLrJtbaWThWJfxFSdeWSm4j%2ff1x3bMJjjDmnJpeDhBcFrydxyJaminuJjRVKQWVCy%2bR%2fim82xdDCE1zbCl%2bPTJlMRBPoNAStFkzXq24%2bAccXyyKUTAgOkZQFB%2bvK0Buhrs7El5wUY1taX1pBEvE%3d; __jda=122270672.123799706.1586526227.1586526227.1586526229.1; __jdc=122270672; __jdu=123799706; areaId=2; ipLoc-djd=2-2824-0-0; wxa_level=1; retina=0; webp=1; __jdv=122270672%7Cbaidu-search%7Ct_262767352_baidusearch%7Ccpc%7C45209195451_0_6427d005f9774dffb06fa418726826c6%7C1586526235460; mba_muid=123799706; autoOpenApp_downCloseDate_auto=1586526236210_21600000; visitkey=23187129858291741; TrackerID=folVLiW1Zz2nZzOia_3VsIhBKYnRuBY3X2RKQi5K8sMxoev7KTKU7gBNzdh8JR2UaPTkJbVusLuHWLgRz5tc5xYBcsrUciIImCUcyJV1D4i5Hmx9vlZ-ZecuycdZ8GF6; pt_key=AAJekHgpADCU3O_N7WTToKQbn9cd12QPzoL39Vbc1XmNeQwC-fRueAmGn0HoEajtg5YkXbsaxZI; pt_pin=%E4%B8%8B%E4%B8%AA%E8%B7%AF%E5%8F%A3%E4%B8%8B; pt_token=n7lifizw; pwdt_id=%E4%B8%8B%E4%B8%AA%E8%B7%AF%E5%8F%A3%E4%B8%8B; PPRD_P=UUID.123799706; sc_width=1536; shshshfp=ddce03db1ee7ce1ea383210c8f2bd08e; cid=3; wq_area=2_2824_0%7C2; __wga=1586526746521.1586526250170.1586526250170.1586526250170.6.1; shshshsID=3672ca37317f54274e1deb7b3e008277_7_1586526746904; wqmnx1=MDEyNjM3MGgvLm9lb250Mzg0bChzLjYpVzUoIGVoMDdhMzVZZi00WUQjKEg%3D; __jdb=122270672.15.123799706|1.1586526229; mba_sid=1586526235462241148049356798.14'
cookie = {}
for line in data.split('&'):
    key, value = line.split('=', 1)
    cookie[key] = value
print(cookie)

