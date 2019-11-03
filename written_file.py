import csv
import read_data

def written_file(file_name, data_dict):
  with open(file_name,encoding='utf-8') as f:
    reader = csv.reader(f)
    active_file_data_list= [row for row in reader]
    read_data_keys_list = list(data_dict.keys())
    read_data_list = list(data_dict.values())
    break_count = False
    for row in range(5, len(active_file_data_list)):
      for time in range(len(read_data_keys_list)):
        if active_file_data_list[row][0] == read_data_keys_list[time]:
          read_data_row = time
          active_data_write_start_row = row
          break_count = True
          break
                  
        if break_count == True:
          break
        else:
          continue
    
    for row in range(read_data_row, len(read_data_list)):
      try:
        active_file_data_list[active_data_write_start_row].append(read_data_list[row])
      except:
        print(file_name)
        continue
      active_data_write_start_row += 1

  return active_file_data_list