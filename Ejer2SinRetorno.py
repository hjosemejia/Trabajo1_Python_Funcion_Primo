def funcion_primo(num):
    resp = 0
    if num == 2:
        print(f"EL NUMERO {num} ES PRIMO ")
    else:
        for i in range(2, num):
            if num % i == 0:
                resp = resp + 1
    if resp == 0:
        print(f"EL NUMERO {num} ES PRIMO ")
    else:
        print(f"EL NUMERO {num} NO ES PRIMO ")          

def main():
    num = int(input("DIGITE UN NUMERO: "))
    funcion_primo(num)

if __name__ == "__main__":
    main()
