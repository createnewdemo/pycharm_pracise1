# coding: utf-8
import requests
from urllib import request

'''
/**
 * 敬告使用者
 *
 * 联众识图网站SDK页面提供的接口、实例文件均为第三方开发，非联众识图开发，因技术原因，联众识图平台未进行代码审查，亦不能确定代码的功能作用，请接入的开发者审查代码后调用。如实例中包含恶意代码或针对某网站、软件的攻击行为，请联系联众识图平台删除链接。
 *
 * 联众识别平台仅为残障人士以及有需要的个人和企业提供图像识别和图像识别分类服务，联众平台仅仅被动接受开发者传入的图像返回图像中的文字或结果信息，不参与破解，不为恶意软件提供帮助，不针对任何网站或个人。
 * 请勿利用联众识别做违反国家法律法规的行为，否则强制停止使用，不予退费，联众将依法向有关部门递交您的个人资料！
 * 违法软件是指的是包括但不限于以下用途的软件：
 * 1、破解、入侵系统，或正常登录但超越授权范围获取信息。
 * 2、赌博
 * 3、薅羊毛
 * 4、批量登录、批量注册、批量支付
 * 5、游戏外挂、游戏辅助
 * 6、超越访问频率限制
 * 7、批量盗取公民个人信息，获取手机号、身份证等隐私信息
 *
 */
'''


def main(api_username, api_password, file_name, api_post_url, yzm_min, yzm_max, yzm_type, tools_token):
    '''
            main() 参数介绍
            api_username    （API账号）             --必须提供
            api_password    （API账号密码）         --必须提供
            file_name       （需要识别的图片路径）   --必须提供
            api_post_url    （API接口地址）         --必须提供
            yzm_min         （识别结果最小长度值）        --可空提供
            yzm_max         （识别结果最大长度值）        --可空提供
            yzm_type        （识别类型）          --可空提供
            tools_token     （V1软件Token）     --可空提供
    '''
    # api_username =
    # api_password =
    # file_name = 'c:/temp/lianzhong_vcode.png'
    # api_post_url = "http://v1-http-api.jsdama.com/api.php?mod=php&act=upload"
    # yzm_min = '1'
    # yzm_max = '8'
    # yzm_type = '1303'
    # tools_token = api_username

    # proxies = {'http': 'http://127.0.0.1:8888'}
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
        # 'Content-Type': 'multipart/form-data; boundary=---------------------------227973204131376',
        'Connection': 'keep-alive',
        'Host': 'v1-http-api.jsdama.com',
        'Upgrade-Insecure-Requests': '1'
    }

    files = {
        'upload': (file_name, open(file_name, 'rb'), 'image/png')
    }

    data = {
        'user_name': api_username,
        'user_pw': api_password,
        'yzm_minlen': yzm_min,
        'yzm_maxlen': yzm_max,
        'yzmtype_mark': yzm_type,
        'zztool_token': tools_token
    }
    s = requests.session()
    # r = s.post(api_post_url, headers=headers, data=data, files=files, verify=False, proxies=proxies)
    r = s.post(api_post_url, headers=headers, data=data, files=files, verify=False)
    print(r.text)


def download_vcode():
    try:
        # request.urlretrieve(url,'captcha.png')
        # image = Image.open('captcha.png')
        url = 'http://www.yundama.com/index/captcha?r=0.340528384743771'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'}
        s = requests.session()
        resp = s.get(url, headers=headers, verify=False)
        file_name = 'c:/temp/test.png'
        with open(file_name, 'wb') as f:
            f.write(resp.content)
    except Exception as e:
        print(e)


def get_image():
    url = 'http://www.yundama.com/index/captcha?r=0.340528384743771'
    request.urlretrieve(url, 'captcha.png')
    with open('captcha.png', 'rb') as fp:
        image = fp.read()
        return image


if __name__ == '__main__':
    get_image()
    download_vcode()
    main('anyi123',
         'lianzhong123?',
         'captcha.png',
         "http://v1-http-api.jsdama.com/api.php?mod=php&act=upload",
         '1',
         '8',
         '1001',
         '')

    '''
		main() 参数介绍
		api_username    （API账号）             --必须提供
		api_password    （API账号密码）         --必须提供
		file_name       （需要识别的图片路径）   --必须提供
		api_post_url    （API接口地址）         --必须提供
		yzm_min         （识别结果最小长度值）        --可空提供
		yzm_max         （识别结果最大长度值）        --可空提供
		yzm_type        （识别类型）          --可空提供
		tools_token     （V1软件Token）     --可空提供


    '''
