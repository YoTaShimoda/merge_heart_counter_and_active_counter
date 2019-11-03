import read_data
import written_file
import return_file_path
import csv

numfour_heart_count_file = return_file_path.numfour_return_heart_file_path()
numfour_active_count_file = return_file_path.numfour_return_active_file_path()
numfive_heart_count_file = return_file_path.numfive_return_heart_file_path()
numfive_active_count_file = return_file_path.numfive_return_active_file_path()

for numfour in range(len(return_file_path.numfour_return_heart_file_path())):
  file_path = '/Users/yota/merge_heart_counter_and_active_counter/result/result4/' + return_file_path.numfour_write_csv_file_path(numfour_heart_count_file[numfour])
  with open(file_path, 'w') as f:
    writer = csv.writer(f)
    writer.writerows(written_file.written_file(numfour_active_count_file[numfour], read_data.read_data(numfour_heart_count_file[numfour])))

for numfive in range(len(return_file_path.numfive_return_heart_file_path())):
  file_path = '/Users/yota/merge_heart_counter_and_active_counter/result/result5/' + return_file_path.numfive_write_csv_file_path(numfive_heart_count_file[numfive])
  with open(file_path, 'w') as f:
    writer = csv.writer(f)
    writer.writerows(written_file.written_file(numfive_active_count_file[numfive], read_data.read_data(numfive_heart_count_file[numfive])))
