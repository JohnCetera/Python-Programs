stop = "n"
while stop.lower() == "n":
    degrees = input("Original temperature? F or C: ")
    temperature = float(input("Enter the temperature(number only): "))

    if degrees == "f" or degrees == "F":
        print(temperature, "F = ", round((temperature - 32) / 1.8, 1), "C")

    elif degrees == "c" or degrees == "C":
        print(temperature, "C = ", round(temperature * 1.8 + 32, 1), "F")
    stop = input("Exit? y or n: ")
    if stop == "y":
        break
