#def say_hi(name):  #функция
  #  print(f"Hello {name}")

#say_hi("bobb")
#say_hi("vova")

#def force_num(num,force):
#    print(num**force)

#force_num(7,3)
#возведение в степень

#def multiplication(num1,num2):
 #   print(num1*num2)

#multiplication(8,6)
#умножение

#def amount(num1,num2):
#    print(num1 + num2)

#amount(5, 62378)
#сумма

#def difference(num1,num2):
#    print(num1-num2)

#difference(15,64)
#разность

def division(num1,num2):
    try:
        print(num1//num2)
    except ZeroDivisionError:
        print(" Go to doctor")

division(20,0)