import csv
import math
import helper
import shutil

def read_and_write_file(hfile, mfile):
        with open(hfile,encoding='utf-8') as f:
            reader = csv.reader(f)
            list = [row for row in reader]  # リスト型に変換している
            start_time = list[1][3]
            start_time_second = start_time[-2:]
            start_time_minute = start_time[3:5]
            start_time_hour = start_time[:2]
            if int(start_time_second) == 0:
                load_start_second = 0
            else:
                load_start_second = 60-int(start_time_second)
            read_data = {}
            for i in range(3,150):              #開始位置決定用   要確認
                time_value = list[i][1]
                time_value_second = int(time_value[-2:])
                if load_start_second == time_value_second :
                    if list[i][2] == None or list[i][2] == '':                              # 後でNoneなのかゼロなのか聞く
                        load_start_index_value = i+60
                    else:
                        load_start_index_value = i
                    break

            load_start_index_value = int(load_start_index_value)
            count = 0                # 実行回数決定用
            for row in list:
                count += 1
            count = count-3-load_start_index_value
            count = math.floor(count / 60)

            value_sum = 0
            null_count = 0
            for i in range(0,count):
                for a in range(0,60):
                    value = list[load_start_index_value][2]
                    try:
                        value_sum += int(value)
                    except:
                        null_count+=1

                    load_start_index_value += 1
                average = round((value_sum/60),1)
                time = list[load_start_index_value][1]

                try:
                    hour = time[:2]
                    hour = int(hour)+int(start_time_hour)
                except:
                    hour = time[:1]
                    hour = int(hour)+int(start_time_hour)

                if len(time) <= 7:
                    minute = time[2:4]
                else:
                    minute = time[3:5]

                minute = int(minute)+int(start_time_minute)

                if minute > 59:       # 時間計算
                    minute = minute - 60
                    hour = int(hour) + 1
                if hour < 10:
                    hour = '0' + str(hour)
                else:
                    str(hour)

                if minute < 10:      #分が一桁だと、マッチしないので、05分という形に変換する。
                    minute = '0'+ str(minute)
                else:
                    minute = str(minute)

                read_data_index = helper.create_write_data(hour,minute)           # read_data(辞書型)に追加するフォーマットに変換
                if null_count>0:
                    read_data[read_data_index] = None

                else:
                    read_data[read_data_index] = average

                null_count = 0
                value_sum = 0
        print(len(read_data))
        file_name = mfile
        with open(file_name,encoding='utf-8') as f:
            reader = csv.reader(f)
            list= [row for row in reader]
            leng = len(list)
            read_leng = len(read_data)
            for i in range(5,leng):   #総当たりでしかできていないので要改良
                if list[i][0] in read_data:
                    list[i].append(read_data[list[i][0]])

        write_file_name = file_name.replace('.csv','_marge_result.csv')
        with open(write_file_name,'a',encoding='utf-8') as f:
            writer = csv.writer(f)

            writer.writerows(list)
            shutil.move(write_file_name,'/Users/yota/merge_heart_counter_and_active_counter/result4')
