Another_Estimate = "y"

while Another_Estimate.lower() == "y":
    people = float(input("How many people attending: "))

# math formulas
    quotient = round(people//10)
    remainder = round(people % 10)

    print(quotient, "vans will be filled completely.", remainder, "people need to arrange separate transport.")
    Another_Estimate = input("Do you need another estimate? (Y or N): ")
    if Another_Estimate == "n":
        print('Thank You, Have a Great Day!')
        break
