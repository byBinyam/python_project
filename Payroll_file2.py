import datetime
print(datetime.datetime.now())
print("Welcome to Payroll Report.\n")

while True:
    def main():
        Hours, Rate = dataentry()
        GrossPay = calculate_pay(Hours, Rate)
        Federal_tax = Fed_tax(GrossPay)
        State_tax = St_tax(GrossPay)
        Fica_tax = GrossPay * 7.65 / 100
        Estimated_tax = Fica_tax + Federal_tax + State_tax
        Net_pay = GrossPay - Estimated_tax
        display_pay(Hours, GrossPay, State_tax, Federal_tax, Fica_tax, Net_pay)

    def dataentry():
        Employee = input("Please enter your name: ")
        print(f"Welcome {Employee}.\n")
        while True:
            try:
                Hours = float(input("How many hours did you work this week? : "))
                break
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")

        Rate = float(input("What is your hourly wage? : $"))
        return Hours, Rate


    def calculate_pay(Hours, Rate):
        if Hours <= 40:
            GrossPay = round(Rate * Hours, 2)
        else:
            RegularPay = Rate * 40
            OverTime = Hours - 40
            OverTimeRate = Rate * 1.5
            OverTimePay = round(OverTimeRate * OverTime, 2)
            GrossPay = round(RegularPay + OverTimePay, 2)
        return GrossPay


    def Fed_tax(GrossPay):
        if GrossPay > 0:
            Federal_tax = GrossPay * 0.1
        elif GrossPay > 14200:
            Federal_tax = ((GrossPay - 14200) * 0.12) + 1420
        elif GrossPay > 54200:
            Federal_tax = ((GrossPay - 54200) * 0.22) + 6220
        elif GrossPay > 86350:
            Federal_tax = ((GrossPay - 86350) * 0.24) + 13293
        elif GrossPay > 164900:
            Federal_tax = ((GrossPay - 164900) * 0.32) + 32145
        elif GrossPay > 209400:
            Federal_tax = ((GrossPay - 209400) * 0.35) + 46385
        elif GrossPay > 523600:
            Federal_tax = ((GrossPay - 523600) * 0.37) + 156355
        return Federal_tax


    def St_tax(GrossPay):
        if GrossPay > 0:
            State_tax = GrossPay * 0.02
        elif GrossPay > 3000:
            State_tax = ((GrossPay - 3000) * 0.03) + 60
        elif GrossPay > 5000:
            State_tax = ((GrossPay - 5000) * 0.05) + 120
        elif GrossPay > 17000:
            State_tax = ((GrossPay - 17000) * 0.0575) + 720
        return State_tax


    def display_pay(Hours, GrossPay, State_tax, Federal_tax, Fica_tax, Net_pay):

        print(f"You worked {Hours} hours during this pay period\n")
        print(f"Your gross pay is: ${format(GrossPay, '.2f')}\n")
        print(f"Your Fed Tax is: ${format(Federal_tax, '.2f')}\n")
        print(f"Your State Tax is: ${format(State_tax,'.2f')}\n")
        print(f"Your Fica Tax is: ${format(Fica_tax, '.2f')}\n")
        print(f"Your net pay is: ${format(Net_pay, '.2f')}\n")
    main()

    color = input("Please type Yay to Continue or type Nay to quit:")
    if color.lower() == 'nay':
        break

#else:
    #print("Exiting program....")