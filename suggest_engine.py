# 引用生成詞
from thanks_word import generate_words as callAPIThxword

# 引用產品服務A
from connect2postgres import get_tag_from_productid as callAPITags
# 引用產品服務B
from E import get_product_info as callAPIProductInfo


# 假設變數區 ==================
state_list = ['wait_user', 'ask_interest', 'first_question', 'question_loop_False', 'question_loop_True', 'end_conversation']


# 各場景實作細節=========================================
def state6to1(json_object):
    print('::推薦系統訊息:: in sugg.... state6to1 - start')
    # 更新現在狀態 到1
    json_object['json']['cur_state'] = 'basic_info'
    print('::推薦系統訊息:: in sugg.... state6to1 - finish')
    return json_object['json']

def state6to1_1(json_object):
    print('::推薦系統訊息:: in sugg.... state6to1 - start')
    # 更新現在狀態
    json_object['json']['cur_state'] = 'basic_info_1'
    print('::推薦系統訊息:: in sugg.... state6to1 - finish')
    return json_object['json']

def state1_1to1_2(json_object):
    print('::推薦系統訊息:: in sugg.... state1_1to1_2 - start')
    # 讀取、更新收禮者姓名
    user_input = json_object['outside']['msg']
    json_object['json']['subject'] = user_input

    # 更新現在狀態
    json_object['json']['cur_state'] = 'basic_info_2'
    print('::推薦系統訊息:: in sugg.... state1_1to1_2 - finish')
    return json_object['json']

def state1_2to1_3(json_object):
    print('::推薦系統訊息:: in sugg.... state1_2to1_3 - start')
    # 讀取、更新收禮者性別
    gender = json_object['outside']['msg']
    json_object['json']['gender'] = gender

    # 更新現在狀態
    json_object['json']['cur_state'] = 'basic_info_3'
    print('::推薦系統訊息:: in sugg.... state1_2to1_3 - finish')
    return json_object['json']

def state1_3to1_4(json_object):
    print('::推薦系統訊息:: in sugg.... state1_3to1_4 - start')
    # 讀取、更新收禮者年齡
    age = json_object['outside']['msg']
    json_object['json']['age'] = int(age)

    # 更新現在狀態
    json_object['json']['cur_state'] = 'basic_info_4'
    print('::推薦系統訊息:: in sugg.... state1_3to1_4 - finish')
    return json_object['json']


def state1_4to1_5(json_object):
    print('::推薦系統訊息:: in sugg.... state1_4to1_5 - start')
    # 讀取、更新收禮者關係
    relationship = json_object['outside']['msg']
    json_object['json']['relationship'] = relationship

    # 更新現在狀態
    json_object['json']['cur_state'] = 'basic_info_5'
    print('::推薦系統訊息:: in sugg.... state1_4to1_5 - finish')
    return json_object['json']


def state1_5to2_1(json_object):
    print('::推薦系統訊息:: in sugg.... state1_5to2_1 - start')
    # 讀取、更新購買禮物預算
    budget = json_object['outside']['msg']
    json_object['json']['budget'] = [0, int(budget)]

    # 更新現在狀態
    json_object['json']['cur_state'] = '9question'
    print('::推薦系統訊息:: in sugg.... state1_5to2_1 - finish')
    return json_object['json']


def state2_1to2_2(json_object):
    print('::推薦系統訊息:: in sugg.... state2_1to2_2 - start')

    try:
        # 讀取、更新選擇的9question
        json_object['json']['9question'] = json_object['outside']['msg'].split('_')[1]

    except Exception as e:
        print(e)
        return json_object['json']

    # 更新現在狀態
    json_object['json']['cur_state'] = '6question'
    print('::推薦系統訊息:: in sugg.... state2_1to2_2 - finish')
    return json_object['json']


def state2_2to2_3(json_object):
    print('::推薦系統訊息:: in sugg.... state2_2to2_3 - start')

    try:
        # 讀取、更新選擇的9question
        json_object['json']['6question'] = json_object['outside']['msg'].split('_')[1]

    except Exception as e:
        print(e)
        return json_object['json']

    # 更新現在狀態
    json_object['json']['cur_state'] = 'open_question'
    print('::推薦系統訊息:: in sugg.... state2_2to2_3 - finish')
    return json_object['json']


def state2_3to3(json_object):
    print('::推薦系統訊息:: in sugg.... state2_3to3 - start')

    try:
        # 讀取、更新選擇的9question
        category = json_object['outside']['msg']
        json_object['json']['open_question'] = category
    except Exception as e:
        print(e)
        return json_object['json']

    # 呼叫產品服務A
    response = callAPITags(json_object['json']['conds'])
    # 更新下一個TAG
    json_object['json']['next_tag'] = response['next_tag']
    # 更新產品數量
    json_object['json']['product_cnt'] = response['product_cnt']
    # 更新現在狀態
    json_object['json']['cur_state'] = 'first_question'

    print('::推薦系統訊息:: in sugg.... state2_3to3 - finish')
    return json_object['json']


def state1to2(json_object):
    print('::推薦系統訊息:: in sugg.... state1to2 - start')
    # 讀取、更新收禮者姓名
    name = json_object['outside']['msg']['name']
    json_object['json']['subject'] = name

    # 讀取、更新收禮者性別
    gender = json_object['outside']['msg']['gender']
    json_object['json']['gender'] = gender

    # 讀取、更新收禮者年齡
    age = json_object['outside']['msg']['age']
    json_object['json']['age'] = int(age)

    # 讀取、更新收禮者關係
    relationship = json_object['outside']['msg']['relationship']
    json_object['json']['relationship'] = relationship

    # 讀取、更新購買禮物預算
    budget = json_object['outside']['msg']['budget']
    json_object['json']['budget'] = budget

    # 更新現在狀態
    # json_object['json']['cur_state'] = 'ask_interest'
    # 之後開放
    json_object['json']['cur_state'] = 'question_all'
    print('::推薦系統訊息:: in sugg.... state1to2 - finish')
    return json_object['json']


def state2to3(json_object):
    print('::推薦系統訊息:: in sugg.... state2to3 - start')
    # 讀取需要的input: 使用者輸入了開放式問題的答案
    user_input = json_object['outside']['msg']
    json_object['json']['open_question'] = user_input
    #    tags = {'conds': json_object['json']['conds']}
    # 呼叫產品服務A
    response = callAPITags(json_object['json']['conds'])
    # 更新下一個TAG
    json_object['json']['next_tag'] = response['next_tag']
    # 更新產品數量
    json_object['json']['product_cnt'] = response['product_cnt']
    # 更新現在狀態
    json_object['json']['cur_state'] = 'first_question'
    print('::推薦系統訊息:: in sugg.... state2to3 - finish')
    return json_object['json']


def state3(json_object):
    '''
    回報送禮對象、候選禮物數。轉場進入詢問loop，詢問對Ntag是否有興趣
    :param json_object:
    :return:
    '''
    print('::推薦系統訊息:: in sugg.... state3 - start')
    # 讀取需要的input: 使用者感興趣的tags
    #tags = {'conds': json_object['json']['conds']}
    response = callAPITags(json_object['json']['conds'])
    print("收到產品服務A回傳值:",str(response))
    json_object['json']['next_tag'] = response['next_tag']
    json_object['json']['product_cnt'] = response['product_cnt']
    json_object['json']['cur_state'] = 'first_question'
    print('::推薦系統訊息:: in sugg.... state3 - finish')
    return json_object['json']


def state3to4(json_object):
    print('::推薦系統訊息:: in sugg.... state3to4 - start')
    # 重新拿一個Ntag
    # tags = json_object['json']['conds']
    # tags = {'conds': tags}
    response = callAPITags(json_object['json']['conds'])
    json_object['json']['next_tag'] = response['next_tag']
    json_object['json']['cur_state'] = 'question_loop_False'
    print(f"load result:\n\t tags: {json_object['json']['conds']}\n\t Ntag = {json_object['json']['next_tag']}")
    print('::推薦系統訊息:: in sugg.... state3to4 - finish')
    return json_object['json']


def state3to5(json_object):
    '''
    已確認使用者對Ntag有興趣，把Ntag收進conds，檢查後選禮物數量確定下一步去哪
    :param json_object:
    :return:
    '''
    threshold = 10
    print('::推薦系統訊息:: in sugg.... state3to5 - start')
    # 讀取需要參數: tags,Ntag
    tags = json_object['json']['conds']
    Ntag = json_object['json']['next_tag']
    tags.append(Ntag)
    #tags = {'conds': tags}
    print(f'load result:\n\t tags: {tags}\n\t Ntag = {Ntag}')
    # 透過API要資料，並更新對應值
    response = callAPITags(tags)
    json_object['json']['next_tag'], json_object['json']['product_cnt'] = response['next_tag'], response['product_cnt']
    # 依據候選禮物數判斷下一步
    if response['product_cnt'] <= threshold:
        # 進入場景6
        new_json_object = state3to6(json_object)
        #json_object['json']['cur_state'] = 'end_conversation'
        return new_json_object
    else:
        # 轉換到場景5
        json_object['json']['cur_state'] = 'question_loop_True'
        print('::推薦系統訊息:: in sugg.... state3to5 - finish')
        return json_object['json']


def state3to6(json_object):
    '''
    透過API拿商品資訊(品名、連結)& 感謝詞
    :param json_object:
    :return:
    '''
    print('::推薦系統訊息:: in sugg.... state3to6 - start')

    # 透過API拿產品資訊，並更新對應值
    #   讀取需要參數: tags, subject
    tags = {'conds': json_object['json']['conds']}
    print(f'load result:\n\t tags: {tags}')
    #   解析回傳json並更新對應值
    response = callAPIProductInfo(json_object['json']['conds'])
    json_object['json']['products'] = response
    print(f'測試行1: {json_object}')

    # -----------------------------
    # 透過API拿感謝詞，並更新對應值
    #   讀取需要參數:  subject, tags
    response = callAPIThxword(json_object['json']['subject'], json_object['json']['conds'])
    json_object['json']['thx words'] = response['thx words']

    # -----------------------------
    # 狀態轉換
    json_object['json']['cur_state'] = 'end_conversation'
    print(f"check result:\n\t product: {json_object['json']['products']}\n\t thx word: {json_object['json']['thx words']}")
    print('::推薦系統訊息:: in sugg.... state3to6 - finish')
    return json_object['json']


# 兩個路線分配器 =================================
def decisionmix(json_object):
    print('decisionmix')
    # 讀取需要的input: 使用者表示了有興趣或沒興趣
    user_input = json_object['outside']['msg']
    if user_input == '有':
        # 進入場景5
        #json_object['json']['cur_state'] = 'question_loop_True'
        new_json_object = state3to5(json_object)
        return new_json_object
    elif user_input == '無':
        # 進入場景4
        new_json_object = state3to4(json_object)
        #json_object['json']['cur_state'] = 'question_loop_False'
        return new_json_object
    else:
        print('error input in decisionMIX')


# 主程式，系統會先跑這支函式 ========================
def main(source, json_object):
    # 先整理對話引擎傳來的 使用者資料&前端訊息

    # 使用者資料
    # try:
    #     user_msg  = userdata["json"]
    #     print(" 讀取JSON")
    # except Exception as e:
    #     print(f'::SYS錯誤訊息:: 沒有得到使用者訊息\n{e}\n== 對話系統傳來資料不符 ================================')
    #     return '\n\n', e
    #
    #     # 前端訊息
    # try:
    #     front_input  = userdata["outside"]['msg']
    #     print(" 讀取OUTSIDE")
    #     # 裝後面要用的參數
    #     json_object = {"json":user_msg, "outside":front_input}
    # except Exception as e:
    #     print(f'::SYS錯誤訊息::\n{e}\n== 對話系統傳來資料不符 ================================')
    #     return '\n\n', e
    # print(f"::SYS訊息:: 輸入參數 {json_object}")

    # 根據現在的狀態(cur_state)進入function
    cur_state = json_object['json']['cur_state']

    # Web 專屬流程
    if cur_state == 'end_conversation' and source == 'web':
        json_return = state6to1(json_object)
    elif cur_state == 'basic_info':
        json_return = state1to2(json_object)
    elif cur_state == 'question_all':
        json_return = state2to3(json_object)

    # LineBot 專屬流程
    elif cur_state == 'end_conversation' and source == 'linebot':
        json_return = state6to1_1(json_object)
    elif cur_state == 'basic_info_1':
        json_return = state1_1to1_2(json_object)
    elif cur_state == 'basic_info_2':
        json_return = state1_2to1_3(json_object)
    elif cur_state == 'basic_info_3':
        json_return = state1_3to1_4(json_object)
    elif cur_state == 'basic_info_4':
        json_return = state1_4to1_5(json_object)
    elif cur_state == 'basic_info_5':
        json_return = state1_5to2_1(json_object)
    elif cur_state == '9question':
        json_return = state2_1to2_2(json_object)
    elif cur_state == '6question':
        json_return = state2_2to2_3(json_object)
    elif cur_state == 'open_question' and source == 'linebot':
        json_return = state2_3to3(json_object)

    elif cur_state == 'ask_interest':
        json_return = state2to3(json_object)

    # 通用流程
    elif cur_state == 'first_question':
        json_return = decisionmix(json_object)
    #elif cur_state == 'question_loop_False':
    #    json_return = state5(json_object)
    #elif cur_state == 'question_loop_True':
    #    json_return = state6(json_object)
    else:
        json_return = 'ERROR! in 推薦系統SUGG'
    print(json_return)
    return json_return


#if __name__ == "__main__":
#    main(test_json)

# 測試區域結束 ====================================
