another_estimate = "y"

# Federal withholding = 20%
# fica = 8%
# State income tax = 2%
while another_estimate.lower() =="y":
    hours = input("Total Hours Worked: ")
    rate = input("Pay Rate: ")
    try:
        hr = float(hours)
        rt = float(rate)
        if hr <= 40:
            gross_pay = hr * rt
            fwt = gross_pay * float(20 / 100)
            fica = gross_pay * float(8 / 100)
            state_income_tax = gross_pay * float(2 / 100)
            net_income = gross_pay - fwt - fica - state_income_tax
            print("Gross Pay: ", "$", "{: .2f}".format(gross_pay,))
            print("Federal Withholding Tax: ", "$", "{: .2f}".format(fwt))
            print("FICA: ", "$", "{: .2f}".format(fica))
            print("State Income Tax: ", "$", "{: .2f}".format(state_income_tax))
            print("Net Pay: ", "$", "{: .2f}".format(net_income))

        else:
            hr > 40
            print("Cannot work more than 40 hours.")
        another_estimate = input("Do you need another estimate? (y/n): ")
    except:
        print("You did not enter numerical values.")

        if another_estimate == "n":
            break






