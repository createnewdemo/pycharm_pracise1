#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 15:17
# @Author  : lihanhan
# @Email   : demo1li@163.com
# @File    : demo.py
import requests
def person_info():
    headers = {
        'origin': 'https://www.icourse163.org',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'EDUWEBDEVICE=7003e9ff58564b13aa0f823850d04dba; WM_TID=lobU3%2FJ8TCdEAFAFRBNtroQQhwux78un; MOOC_PRIVACY_INFO_APPROVED=true; bpmns=1; hasVolume=true; videoResolutionType=3; __utma=63145271.1831901193.1580133908.1580133908.1580133908.1; __utmz=63145271.1580133908.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); videoVolume=1; videoRate=1.5; __yadk_uid=uovzBQ9QBmpc4h0kkrYouBPqZhg9yqVw; NTES_YD_PASSPORT=QfN1guuQpoD5JUHCY.J21l_18maOpdX7Yxi.oJtSUJlUa7s5atXR4ytYJ2cFnl_8pQFpGN21xtgeXM8oyo1.51C4I_7daCgorpNP22Mnf5uuo0WqMIrxix1sDpleiUgebelyixXJYTFTXoGjAS_h4bye1E7FpGTQzYZ5geWtAefsiXpoE9lE8fcgst1euemTYpJjbZ0BDz6Dky2qzkDsBFkZh; P_INFO=18737695639|1587026453|1|imooc|00&99|null&null&null#hen&411300#10#0|&0||18737695639; hb_MA-A976-948FFA05E931_source=www.baidu.com; NTESSTUDYSI=4abc4a78462544f6b996bd491ac85689; STUDY_INFO="yd.067986b2b7c44ffab@163.com|8|1435459112|1587107774663"; STUDY_SESS="815q28PDysQoj0YitJRbgh8FHIWS+7HoQGVUdJEIBsm3RvEmpUMnDTGz3HMvUVdRSOoupefl5ZCmWMkCOcQZK/4teePm2R//KBBW/HhB9TdBUEeGAXu9KhOl9ibQwtLxV/IhPyQ4R0jYPYPt9xfEcGxzOXKYvl+3LeQ6pne7l6sLhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="hCZGa0CfQfKmP5yl4TZYbF5tx5PMiBxSH861CcgrQrKnyHg80qne6cEzCBXHGtcCT7kuonB+aMzcvpYiRy8I+oi0mnO9oZIOWuqeaYdKbEk8Tsb1Uc40IkqG0ntTFyaNgKiae0tB0yQp/bpR+UdWsAd2j3NEnrCZTVGHWEIG+yffEj60NTBGxpenf6BP+Ec6pQnJcst2EKcC3m3HiPEO9qAdGXTIOuJYpC4f1eM3Ty7ZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1435459112#|#1587026500288; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1587026272,1587026402,1587026812,1587107777; WM_NI=PqXtuZ3zJeF3aGQ5mevXflSGcxmsSpG2FdyUhC1%2BILXJAhUOQWpqXTuckeQgvXEYIUdVRd96DTf9UT9sFFybpUuu2hSqCUDMvwqQ1BlCvBgw%2FnPlm060oYIqGtm0gv8fNGc%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee96eb5eed95a5d8c85cb7968bb6d55b879e9e85ae5ab48fc0d0ae67a9bea7d9bc2af0fea7c3b92a94af9895f852f1a68686c539a3999fd6f06fb688aa8dd24da1a8a394d27c85ee8a85fc5fac9dffcccc489c968f89d8459389c092db60b7bda586d46db6888bbacc5fa88a9e85bc3e888caadad860fbad8aa7fc6ab48bbb96b16491af8db6c747b6a9bfb2b44ab09dbaa3e67dedb2a08df03cf6f0a1bacc7b85aca3d1e67efcba82a8e237e2a3; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1587108112',
        'edu-script-token': '4abc4a78462544f6b996bd491ac85689',
        'pragma': 'no-cache',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'authority': 'www.icourse163.org',
        'referer': 'https://www.icourse163.org/home.htm?userId=1144669226',
    }

    params = (
        ('csrfKey', '4abc4a78462544f6b996bd491ac85689'),
    )

    data = {
      'memberId': '1144669226'
    }

    response = requests.post('https://www.icourse163.org/web/j/memberBean.getMocMemberPersonalDtoById.rpc', headers=headers, params=params, data=data)


    print(response.text)

def course_info():
    import requests

    headers = {
        'origin': 'https://www.icourse163.org',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'EDUWEBDEVICE=7003e9ff58564b13aa0f823850d04dba; WM_TID=lobU3%2FJ8TCdEAFAFRBNtroQQhwux78un; MOOC_PRIVACY_INFO_APPROVED=true; bpmns=1; hasVolume=true; videoResolutionType=3; __utma=63145271.1831901193.1580133908.1580133908.1580133908.1; __utmz=63145271.1580133908.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); videoVolume=1; videoRate=1.5; __yadk_uid=uovzBQ9QBmpc4h0kkrYouBPqZhg9yqVw; NTES_YD_PASSPORT=QfN1guuQpoD5JUHCY.J21l_18maOpdX7Yxi.oJtSUJlUa7s5atXR4ytYJ2cFnl_8pQFpGN21xtgeXM8oyo1.51C4I_7daCgorpNP22Mnf5uuo0WqMIrxix1sDpleiUgebelyixXJYTFTXoGjAS_h4bye1E7FpGTQzYZ5geWtAefsiXpoE9lE8fcgst1euemTYpJjbZ0BDz6Dky2qzkDsBFkZh; P_INFO=18737695639|1587026453|1|imooc|00&99|null&null&null#hen&411300#10#0|&0||18737695639; hb_MA-A976-948FFA05E931_source=www.baidu.com; NTESSTUDYSI=4abc4a78462544f6b996bd491ac85689; STUDY_INFO="yd.067986b2b7c44ffab@163.com|8|1435459112|1587107774663"; STUDY_SESS="815q28PDysQoj0YitJRbgh8FHIWS+7HoQGVUdJEIBsm3RvEmpUMnDTGz3HMvUVdRSOoupefl5ZCmWMkCOcQZK/4teePm2R//KBBW/HhB9TdBUEeGAXu9KhOl9ibQwtLxV/IhPyQ4R0jYPYPt9xfEcGxzOXKYvl+3LeQ6pne7l6sLhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="hCZGa0CfQfKmP5yl4TZYbF5tx5PMiBxSH861CcgrQrKnyHg80qne6cEzCBXHGtcCT7kuonB+aMzcvpYiRy8I+oi0mnO9oZIOWuqeaYdKbEk8Tsb1Uc40IkqG0ntTFyaNgKiae0tB0yQp/bpR+UdWsAd2j3NEnrCZTVGHWEIG+yffEj60NTBGxpenf6BP+Ec6pQnJcst2EKcC3m3HiPEO9qAdGXTIOuJYpC4f1eM3Ty7ZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1435459112#|#1587026500288; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1587026272,1587026402,1587026812,1587107777; WM_NI=PqXtuZ3zJeF3aGQ5mevXflSGcxmsSpG2FdyUhC1%2BILXJAhUOQWpqXTuckeQgvXEYIUdVRd96DTf9UT9sFFybpUuu2hSqCUDMvwqQ1BlCvBgw%2FnPlm060oYIqGtm0gv8fNGc%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee96eb5eed95a5d8c85cb7968bb6d55b879e9e85ae5ab48fc0d0ae67a9bea7d9bc2af0fea7c3b92a94af9895f852f1a68686c539a3999fd6f06fb688aa8dd24da1a8a394d27c85ee8a85fc5fac9dffcccc489c968f89d8459389c092db60b7bda586d46db6888bbacc5fa88a9e85bc3e888caadad860fbad8aa7fc6ab48bbb96b16491af8db6c747b6a9bfb2b44ab09dbaa3e67dedb2a08df03cf6f0a1bacc7b85aca3d1e67efcba82a8e237e2a3; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1587108112',
        'edu-script-token': '4abc4a78462544f6b996bd491ac85689',
        'pragma': 'no-cache',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'authority': 'www.icourse163.org',
        'referer': 'https://www.icourse163.org/home.htm?userId=1144669226',
    }

    params = (
        ('csrfKey', '4abc4a78462544f6b996bd491ac85689'),
    )

    data = {
        'uid': '1144669226',
        'pageIndex': '1',
        'pageSize': '32'
    }

    response = requests.post(
        'https://www.icourse163.org/web/j/learnerCourseRpcBean.getOtherLearnedCoursePagination.rpc', headers=headers,
        params=params, data=data)
    print(response.text)

if __name__ == '__main__':
    course_info()