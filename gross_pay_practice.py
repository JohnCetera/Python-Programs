def computepay(hours: object, rate: object):


    if hours <= int(40):
        pay = float(hours * rate)
        print("$" + str(pay))
    elif hours >= int(40):
        base_pay = float(40 * rate)
        overtime = int(hours - 40)
        overtime_rate = int(rate*1.5)
        overtime_pay = int(base_pay + (overtime * overtime_rate))
        print("$" + str(overtime_pay))


computepay(int(input("Enter hours worked: ")), int(input("Enter pay rate: ")))
