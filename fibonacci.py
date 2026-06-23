def fibonacci(num):
    if num == 0 or num==1:
        return num
    else :
        return fibonacci(num-1)+fibonacci(num-2)
numero = int(input("da el numero: "))
print("fibonacci de",numero,"es =",fibonacci(numero))