hours = input("total hours worked: ")
rate = input("pay rate: ")


try:
    hr = float(hours)
    rt = float(rate)
    if hours <= str(40):
        pay = hr * rt
        print(pay)
    elif hours >= str(40):
        base_pay = float(40 * rt)
        overtime = int(hr - 40)
        overtime_rate = int(rt * 1.5)
        overtime_pay = int(base_pay + (overtime * overtime_rate))
        print(overtime_pay)
except:
    print("enter a numerical value")
input()