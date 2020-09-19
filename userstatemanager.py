import json
import os


# version 2.0
# developer 674
# perpose as backen of app.py, support app.py to maintain its userstate record whitch is stored as json format in .json

'''
[JSON結構] 以dictionary作為包裝

userid  使用者ID:要用來追蹤使用者用，一個使用者只能有一個
cur_state   使用者互動狀態:用來控制前端表現

subject 收禮對象
gender  收禮對象性別
age     收禮者年齡
relationship    與收禮者關係
budget  購買禮物的預算

9question   九大問題的答案
6question   六大問題的答案
open_question   開放式問題的答案

conds   收禮對象有興趣的標籤
next_tag    詢問使用者的下一個標籤
product_cnt 候選禮物數量
'''

def SetInitialValue(userId):
    '''
    回傳使用者資料的初始值
    :input userId: str-使用者id
    :return: dict-使用者資料初始值
    '''
    return_obj = {}
    return_obj['userId']    = userId  # 使用者id，比對用
    return_obj['cur_state'] = 'end_conversation'  # 現在狀態
    return_obj['subject']   = "None"  # 送禮對象
    return_obj['gender']    = 'None'
    return_obj['age']       = '99'
    return_obj['relationship'] = '仇人'
    return_obj['budget']    = 500
    return_obj['9question'] = 'None'
    return_obj['6question'] = 'None'
    return_obj['open_question'] = 'None'
    return_obj['interested_things'] = ''
    return_obj['conds']     = []  # 感興趣的標籤
    return_obj['next_tag']  = "None"  # 待詢問標籤
    return_obj['product_cnt']       = -1  # 待選禮物數，設定-1為初始值
    return return_obj


def GetUserState(request_source, userid):
    '''
    讀取使用者資料JSON檔，並回傳
    :input request_source: str 訊息來源LineBot或者Web
    :input userid: str 使用者ID
    :return: 使用者狀態(json)
    '''
    # 兩種檔案名稱，以使用者來源區分
    #       * lineuserstate_<由line傳來的userid>.json
    #       * webuserstate_<由web傳來的userid>.json
    # 收到request，請求回傳使用者資料
    # 產生檔案路徑
    if request_source == 'linebot':
        file_name = 'LINEuserstate_' + userid + '.json'
    elif request_source == 'web':
        file_name = 'WEBuserstate_' + userid + '.json'
    else:
        print(f'wrong source: {request_source}')
    print('filename:',file_name)
    file_path = os.path.join(os.getcwd(), 'userstate', file_name)
    print('filepath:',file_path)

    # 搜尋檔案 →找到，讀取
    if os.path.exists(file_path) == True:
        with open(file_path, 'r', encoding='utf8') as json_file:
            content = json.load(json_file)
        print(f'==================\n{content}\n=====================')
        print(f'user[{userid}] personal data loads SUCCESS')
    # 搜尋檔案 →找不到，新建，給初始值
    else:
        print('the file is not exist, so I create a new one ')
        with open(file_path, 'w', encoding='utf8') as json_file:
            content = SetInitialValue(userid)
            json.dump(content, json_file, indent=4, ensure_ascii=False)
        print(f'write in content :\n{content}\n')
        print(f'new user [{userid}] personal data creates SUCCESS')

    # 回傳response
    print('\n::return_content:',content)
    print('::return_datatype:', type(content))
    return content


def UpdateUserState(request_source, userid, cur_state, subject, gender, age, relationship, budget, question9, question6, question_open, conds, next_tag, product_cnt):
    '''
    更新使用者狀態
    :param request_source: 必須輸入
    :param userid: 必須輸入
    :param cur_state: 必須輸入
    :param subject: 可省略輸入
    :param question9: 可省略輸入
    :param question6: 可省略輸入
    :param question_open: 可省略輸入
    :param conds: 可省略輸入
    :param next_tag: 可省略輸入
    :param product_cnt: 可省略輸入
    :return: BOOL, 寫入結果
             False, 'Invalid Format in cur_state'
             True,  'saves SUCCESS'
    '''

    # 收到request，請求回傳更新使用者資料
    # 解析request傳來的json內容[暫時沒有]

    # 檢查cur_state格式
    state_list = ['wait_user', 'basic_info', 'basic_info_1', 'basic_info_2', 'basic_info_3', 'basic_info_4', 'basic_info_5',
                  'question_all', '9question', '6question', 'open_question', 'ask_interest',
                  'first_question', 'question_loop_False', 'question_loop_True', 'end_conversation']

    # 如果傳來的cur_state為非法字元
    if (cur_state in state_list) == False:
        print('Invalid Value in cur_state: check your format and send request again')
        return False, 'Invalid Format in cur_state'

    # 產生檔案路徑
    if request_source == 'linebot':
        file_name = 'LINEuserstate_' + userid + '.json'
    elif request_source == 'web':
        file_name = 'WEBuserstate_' + userid + '.json'
    else:
        print(f'wrong source: {request_source}')
    print('filename:', file_name)
    file_path = os.path.join(os.getcwd(), 'userstate',file_name)
    print('filepath:', file_path)

    #  所有已知訊息整理成json格式
    save_obj = {}
    save_obj['userId'] = userid  # 使用者id，比對用

    # 處理傳4存3、傳5存3
    if cur_state == "question_loop_False" or cur_state == "question_loop_True":
        cur_state = "first_question"
    elif cur_state == "end_conversation":
        with open(file_path, 'w', encoding='utf8') as json_file:
            content = SetInitialValue(userid)
            json.dump(content, json_file, indent=4, ensure_ascii=False)
        return True, 'saves SUCCESS'

    save_obj['cur_state'] = cur_state  # 現在狀態
    save_obj['subject']   = subject  # 送禮對象
    save_obj['gender']    = gender
    save_obj['age']       = age
    save_obj['relationship'] = relationship
    save_obj['budget']    = budget
    save_obj['9question'] = question9
    save_obj['6question'] = question6
    save_obj['open_question'] = question_open
    save_obj['conds']         = conds  # 感興趣的標籤
    save_obj['next_tag']      = next_tag  # 待詢問標籤
    save_obj['product_cnt']   = product_cnt  # 待選禮物數，設定-1為初始值

    # 存入JSON檔中
    with open(file_path, 'w', encoding='utf8') as json_file:
        json.dump(save_obj, json_file, indent=4, ensure_ascii=False)
    print(f'write in content :\n{save_obj}\n')
    print(f'user [{userid}] personal data saves SUCCESS')
    return True, 'saves SUCCESS'

# 定期清理webuser的json
# 待開發