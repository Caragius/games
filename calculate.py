def calculator():
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    operation = str(input("Введите операцию: "))
    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
    elif operation == "*":
        print(num1 * num2)
    elif operation == "/":
        if num2 == 0:
            print("деление на ноль")
        elif num2 != 0:
            print(num1 / num2)
    elif operation == "//":
        if num2 == 0:
            print("деление на ноль")
        elif num2 != 0:
            print(num1 // num2)
    elif operation == "%":
        if num2 == 0:
            print("деление на ноль")
        elif num2 != 0:
            print(num1 % num2)
    elif operation == "**":
        print(num1 ** num2)
    # calculator()

    pov = str(input("Вы хотите еще раз воспользоваться калькулятром? (да/нет): "))
    if pov == "да":
        calculator()
    elif pov == "нет":
        print("")


calculator()
