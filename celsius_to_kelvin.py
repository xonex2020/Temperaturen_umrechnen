
def celsius_to_kelvin(c,krest=273.15):
    K = 0
    C = c
    if K == 0:
        print("Tempreture in Celsius: ", C)
        K = C + krest
        print("Tempreture in Kelvin: ", K)
    else:
        return K


celsius_to_kelvin(0)
