while True:
    user_input = input("Quanti anni hai? ")
    if not user_input.isdigit():
        print("Ciao!")
        break
    age = int(user_input)
    if age >= 18:
        print("Maggiorenne")
    else:
        print("Non maggiorenne")