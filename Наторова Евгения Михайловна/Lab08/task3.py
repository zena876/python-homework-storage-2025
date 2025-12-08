import re

def splt_words():
    text = input("Введите строку для разбития на слова в формат: ")
    result = re.split(r'[.,!?-]', text)
    print("Список слов без пустых элементов:", result)

if __name__== "__main__":
    splt_words()
    
