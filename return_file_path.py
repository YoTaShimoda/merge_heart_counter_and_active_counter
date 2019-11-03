import glob

def numfour_return_heart_file_path():
  numfour = sorted(glob.glob('/Users/yota/merge_heart_counter_and_active_counter/heart_rate/heart_no4/*'))
  return numfour

def numfive_return_heart_file_path():
  numfive = sorted(glob.glob('/Users/yota/merge_heart_counter_and_active_counter/heart_rate/heart_no5/*'))
  return numfive

def numfour_return_active_file_path():
 numfour = sorted(glob.glob('/Users/yota/merge_heart_counter_and_active_counter/time_plus_csv_data/plus_file4/*'))
 return numfour

def numfive_return_active_file_path():
 numfive = sorted(glob.glob('/Users/yota/merge_heart_counter_and_active_counter/time_plus_csv_data/plus_file5/*'))
 return numfive

def numfour_write_csv_file_path(file_name):
  file_path = file_name.replace('/Users/yota/merge_heart_counter_and_active_counter/heart_rate/heart_no4/', '')
  return file_path

def numfive_write_csv_file_path(file_name):
  file_path = file_name.replace('/Users/yota/merge_heart_counter_and_active_counter/heart_rate/heart_no5/', '')
  return file_path