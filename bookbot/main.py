from stats import count_words, sort_report
import sys

def get_book_text(file_path):
  with open(file_path) as f:
    return f.read()

def check_args():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
  check_args()

  book_text = get_book_text(sys.argv[1])
  word_count = count_words(book_text)
  print(f"Found {word_count} total words")
  print("---")
  result = sort_report(book_text)
  
  for item in result:
    if not item["char"].isalpha():
      continue
    
    print(f"{item["char"]}: {item["num"]}")


if __name__ == "__main__":
  main()
