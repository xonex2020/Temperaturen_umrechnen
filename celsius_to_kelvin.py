
def celsius_to_kelvin(c,krest=273.15):
    K = 0
    C = c
    if K == 0:
        print("Tempreture in Celsius: ", C)
        K = C + krest
        print("Tempreture in Kelvin: ", K)
    else:
        return K


userInput = 0
while True:
    try:
        userInput = float(input("Gib die Temperatur in Grad Celsius ein: "))
    except ValueError:
        print("wrong input only numbers!")
        continue

    else:
        celsius_to_kelvin(userInput)
        break