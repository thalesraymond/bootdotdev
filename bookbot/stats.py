def count_words(text):
  words = text.split()
  return len(words)

def count_symbols(text):
  result = {}
  for char in text:
    unique_char = char.lower()
    if unique_char in result:
      result[unique_char] += 1
    else:
      result[unique_char] = 1

  return result

def sort_report(text):
  dict_result = count_symbols(text)
  result_list = []
  for key, value in dict_result.items():
    item = {}
    item["char"] = key
    item["num"] = value
    result_list.append(item)
  result_list.sort(key=get_sorting_num, reverse=True)
  return result_list

def get_sorting_num(item):
  return item["num"]