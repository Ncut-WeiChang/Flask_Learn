import json
import os

students_dict = {}

def get_student_info(student_id : str):
    """
    用迴圈讀取每筆學生資料，並用判斷式比對特定鍵值(即student_id)

    之資料，找到要異動查找資料的學號就將該次迴圈讀到的所有學生資料透過

    json.dumps()轉成字串，若找不到就主動丟出錯誤狀況。
    """
    for row in students_dict:
        if row['student_id'] == student_id:
            return json.dumps(row, ensure_ascii=False, indent=3)
        else:
            raise ValueError("=>發生錯誤: 學號 "+student_id+" 找不到.")

def add_course(student_id : str, course_name : str, course_score : float):
    """
    用迴圈讀取每筆學生資料，首先判斷course_name和course_score是否為空，

    若是則主動丟出錯誤狀況，若不是則繼續用判斷式比對特定鍵值(即student_id)

    之資料，找到要異動的學號就將course_name和course_score的資料轉為字典型態

    ，新增至該次迴圈讀到的學生資料中，找不到學號也主動丟出錯誤狀況
    """
    if not course_name or not course_score:
        raise ValueError("=>其它例外: 課程名稱或分數不可空白.")
    for row in students_dict:
        if row['student_id'] == student_id:
            row['courses'].append({"name": course_name,"score": course_score})
            return "=>課程已成功新增。"
        else:
            raise ValueError("=>發生錯誤: 學號 "+student_id+" 找不到.")

def calculate_average_score(student_data : str):
    """
    用迴圈讀取每筆學生資料，並用判斷式比對特定鍵值(即student_id)

    之資料，找到要讀取的學號，就用len()函式取得該學生的課程筆數，

    並用迴圈加總所有課程的成績，用此計算學生平均成績，若找不到學號也主動丟出錯誤狀況
    """
    for row in students_dict:
        if row['student_id'] == student_data:
                score_sum = 0.0
                score_len = len(row['courses'])
                for item in row['courses']:
                    score_sum += item['score']
                return "=>各科平均分數: " + str(score_sum/score_len)
        else:
            raise ValueError("=>發生錯誤: 學號 "+student_data+" 找不到.")

if os.path.isfile('students.json'):
    with open('students.json', 'r', encoding='UTF-8') as f:
        students_dict = json.load(f)

    while True:
        print("***************選單***************")
        print("1. 查詢指定學號成績")
        print("2. 新增指定學號的課程名稱與分數")
        print("3. 顯示指定學號的各科平均分數")
        print("4. 離開")
        print("**********************************")

        option = input("請選擇操作項目：")

        if option == '1':
            try:
                sid = input("請輸入學號:")
                result = get_student_info(str(sid))
                print('=>學生資料:'+result)
            except Exception as e:
                print(e)
            continue
        elif option == '2':
            try:
                sid = input("請輸入學號:")
                cname = input("請輸入要新增課程的名稱:")
                cscore = input("請輸入要新增課程的分數:")
                result = add_course(str(sid), str(cname), float(cscore))
                print(result)
            except Exception as e:
                print(e)
            continue
        elif option == '3':
            try:
                sid = input("請輸入學號:")
                result = calculate_average_score(str(sid))
                print(result)
            except Exception as e:
                print(e)
            continue
        elif option == '4':
            # 結束程式並將學生資料字典(students_dict)寫入 students.json
            with open('students.json', 'w', encoding="utf-8") as f:
                json.dump(students_dict, f, ensure_ascii=False, indent=4)
            print('=>程式結束。')
            break
        else:
            input("=>請輸入有效的選項。")
else:
    print('students.json 檔案不存在')
