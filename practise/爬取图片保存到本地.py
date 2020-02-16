import requests
import os

url = "https://img14.360buyimg.com/n1/jfs/t1/104141/4/10178/389067/5e16debbE771ac5c2/e3830ea05bccd9b9.jpg"
root = "F://pics//"
path = root + url.split('/')[-1]
'''r = requests.get(url)
r.encoding = r.apparent_encoding
print(r.status_code)'''
try:
    if not os.path.exists(root):  # 判断是否存在根目录
        os.mkdir(root)
    if not os.path.exists(path):  # 判断是否存在图片文件
        r = requests.get(url)
        r.encoding = r.apparent_encoding
        print(r.status_code)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已经存在")
except:
    print("爬取失败")
