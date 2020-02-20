def raises():

    # get current salary
    salary = input("Enter your current pay rate: ")
    # try to convert input to float
    try:

        # convert input to float
        pay = float(salary)

        # calculate next 3 years worth of pay increases, round 2 decimal places
        a = pay*0.05
        b = a+a*0.05
        c = b+b*0.05

        # format pay increase with comma and 2 decimal places
        pay_increase_1 = "{:,.2f}".format(a)
        pay_increase_2 = "{:,.2f}".format(b)
        pay_increase_3 = "{:,.2f}".format(c)

        # calculate next 3 years salary based on pay increases
        d = pay*1.05
        e = pay+a+b
        f = e+c

        # format salary with comma and 2 decimal places
        pay_rate_1 = "{:,.2f}".format(d)
        pay_rate_2 = "{:,.2f}".format(e)
        pay_rate_3 = "{:,.2f}".format(f)

        # print the results
        print("\n" "Pay increase next year: $" + str(pay_increase_1), "\n" "Your pay will be: $" + str(pay_rate_1), "\n" 
            "\n" "Pay increase in two years: $" + str(pay_increase_2), "\n" "Your pay will be: $" + str(pay_rate_2), "\n"
            "\n" "Pay increase in three years: $" + str(pay_increase_3), "\n" "Your pay will be: $" + str(pay_rate_3))

        # pause program until key is pressed
        input("Press enter to quit.")

        # catch non-numbers being entered
    except:
        print("Please enter numbers only!")

        # restart program
        raises()

# call the program


raises()
