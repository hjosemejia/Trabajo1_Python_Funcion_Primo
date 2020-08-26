def funcion_primo(num):
    if num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True        

def main():
    num = int(input("DIGITE UN NUMERO: "))
    resul = funcion_primo(num)
    if  resul == True:
        print(f"EL NUMERO {num} ES PRIMO ")
    else:
        print(f"EL NUMERO {num} NO ES PRIMO ")
if __name__ == "__main__":
    main()