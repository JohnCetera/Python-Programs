# US to Canadian Dollar - 1:1.34646
# US to Euro - 1:0.89629
# US to Indian Rupee - 1:69.6050
# US to Japaneses Yen - 1:109.93
# US to Mexican Peso - 1:19.0332
# US to South African rand - 1:14.4422
# US to British pound - 1:0.79051


def currency_conversion():
    # get dollars to convert
    us_dollars = float(input("Enter amount of US dollars to convert: "))
    # conversion maths with 3 decimal places
    cad = "{:,.3f}".format(us_dollars * 1.34646)
    eur = "{:,.3f}".format(us_dollars * 0.89629)
    inr = "{:,.3f}".format(us_dollars * 69.6050)
    jpy = "{:,.3f}".format(us_dollars * 109.93)
    mxn = "{:,.3f}".format(us_dollars * 19.0332)
    zar = "{:,.3f}".format(us_dollars * 14.4422)
    gbp = "{:,.3f}".format(us_dollars * 0.79051)
    # gather all the conversions
    conversions = ["Canadian dollar: $" + str(cad), "Euro: $" + str(eur), "Indian rupee: $" + str(inr),
                   "Japanese yen: $" + str(jpy), "Mexican peso: $" + str(mxn), "South African rand: $" + str(zar),
                   "British pound: $" + str(gbp)]
    # print the conversion list on separate lines
    print(*conversions, sep="\n")
    # pause and wait for key press to exit
    input("Press any key to exit.")


currency_conversion()
