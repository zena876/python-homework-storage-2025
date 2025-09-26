if __name__ == '__main__':
    number = []
    while len(number) < 10:
        temp = input("введите число: ")
        try:
            temp_int = int(temp)
            number.append(int(temp))
        except ValueError:
            print("ошика")
    print(f"максимальное - max(i for i in number)")
    print(f"минимальное - min(i for i in number)")
    print(f"сумма - sum(i for i in number)")
