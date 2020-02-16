import os

os.chdir("C:/python")
libs = {"numpy", "matplotlib", "pillow", "sklearn", "requests", \
        "jieba", "beautifulsoup4", "wheel", "networkx", "sympy", \
        "pyinstaller", "django", "flask", "werobot", "pyqt5", \
        "pandas", "pyopengl", "pypdf2", "docopt", "pygame", "selenium"}
try:
    for lib in libs:
        os.system("pip install " + lib + "-i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com")
    print("Successful")
except:
    print("Failed Somehow")
