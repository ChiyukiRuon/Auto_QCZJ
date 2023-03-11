import os
import json
import yaml
import time
import requests


# 获取AccessToken
def getAccessToken(session, openid):
    time_stamp = str(int(time.time()))  # 获取时间戳
    url = "https://qczj.h5yunban.com/qczj-youth-learning/cgi-bin/login/we-chat/callback?callback=https%3A%2F%2Fqczj.h5yunban.com%2Fqczj-youth-learning%2Findex.php&scope=snsapi_userinfo&appid=wx56b888a1409a2920&openid=" + openid + "&nickname=ZhangSan&headimg=&time=" + time_stamp + "&source=common&sign=&t=" + time_stamp
    res = session.get(url)
    access_token = res.text[45:81]  # 比较懒，直接截取字符串了
    print("获取到AccessToken:", access_token)
    return access_token


# 获取当前最新的课程代号
def getCurrentCourse(session, access_token):
    url = "https://qczj.h5yunban.com/qczj-youth-learning/cgi-bin/common-api/course/current?accessToken=" + access_token
    res = session.get(url)
    res_json = json.loads(res.text)
    if res_json["status"] == 200:  # 验证正常
        print("获取到最新课程代号:", res_json["result"]["id"])
        return res_json["result"]["id"]
    else:
        print("获取最新课程失败！")
        print(res.text)
        exit(0)


# 签到 成功返回True，失败返回False
def getJoin(session, access_token, current_course, nid, cardNo):
    data = {
        "course": current_course,  # 大学习期次的代码，如C0046，本脚本已经帮你获取啦
        "subOrg": None,
        "nid": nid,  # 团组织编号，形如N003************
        "cardNo": cardNo  # 打卡昵称
    }
    url = "https://qczj.h5yunban.com/qczj-youth-learning/cgi-bin/user-api/course/join?accessToken=" + access_token
    res = session.post(url, json=data)  # 特别注意，此处应选择json格式发送data数据
    print("签到结果:", res.text)
    res_json = json.loads(res.text)
    if res_json["status"] == 200:  # 验证正常
        print("’{}‘似乎签到成功了".format(cardNo))
        return True
    else:
        print("’{}‘签到失败！".format(cardNo))
        exit(0)


# 查找config下的配置文件
def find_config():
    file_name = []
    for file in os.listdir('./config'):
        if os.path.splitext(file)[1] == '.yaml':
            file_name.append(file)

    return file_name


def main():
    yaml_file = find_config()
    print("共获取到{}个配置文件：{}".format(len(yaml_file), yaml_file))
    for i in range(len(yaml_file)):
        with open('./config/{}'.format(yaml_file[i]), 'r', encoding='utf-8') as f:
            file = f.read()
            yaml_data = yaml.safe_load(file)
            print(yaml_data)
            if yaml_data['enable']:
                openid = yaml_data['openid']
                cardNo = yaml_data['cardNo']
                nid = yaml_data['nid']
                print("正在为用户:’{}‘签到".format(cardNo))

                session = requests.session()
                session.headers = {
                    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4'
                }

                # 获取token
                time.sleep(2)
                access_token = getAccessToken(session, openid)

                # 获取最新的章节
                time.sleep(2)
                current_course = getCurrentCourse(session, access_token)

                # 签到
                time.sleep(2)
                getJoin(session, access_token, current_course, nid, cardNo)

                time.sleep(2)
            else:
                print("配置文件:’{}‘未启用!".format(yaml_file[i]))
                pass

        f.close()


def main_handler(event, context):
    main()

    return 0


if __name__ == '__main__':
    main()
