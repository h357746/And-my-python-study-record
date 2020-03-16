import requests
import json

headers = {
    'Referer': 'https://jiekou.ouliweb.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}

def get_question():
    # 获取要查询的题目
    print("请输入要查询的题目：")
    question = input()
    return question

def cx_question(question):
    # 使用接口查询题目并获取返回的答案
    #接口一 cx_interface = 'https://jiekou.ouliweb.cn/jiekou.php?key=7327bS1uu9U3w931pU&info=&info='
    cx_interface ='http://149.129.113.103/wkapi.php?tm='
    cx_url = cx_interface+question
    #接口返回数据示例： {"code": 1, "msg": "查询成功", "problem": "吴江霖先生认为,心理学有两大分支,即生理心理学和社会心理学。()", "answer": "正确","ps": "需要接口请联系QQ：987178465"}
    resp = requests.get(cx_url, headers=headers)
    dict_answ = json.loads(resp.text)
    return dict_answ

def return_answ(answ):
    # 输出题目和答案
    tm = answ["tm"]
    answer = answ["answer"]
    if answ["tm"] == "暂无答案" :
        print('没有查到题目，请重试！')
    else:
        print("题目："+tm)
        print("正确答案："+answer)

def main():
    while True:
        ques = get_question()
        answ = cx_question(ques)
        return_answ(answ)
        print("是否继续查题？y/n")
        contin = input()
        if contin == "n" :
            break
            print("结束查询！")


if __name__ == '__main__':
    main()