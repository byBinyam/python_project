print("Welcome to Payroll Report")
user = input("Enter Employee Name or '0' to Quit: ")
end = 0

while user != end:
    Hours = float(input("Please Enter Hours worked: "))
    Rate = float(input("Please Enter Rate of Pay: $"))

    if Hours <= 40:
        GrossPay = round(Rate * Hours, 2)
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
        if GrossPay > 0:
            State_tax = GrossPay * 0.02
        elif GrossPay > 3000:
            State_tax = ((GrossPay - 3000) * 0.03) + 60
        elif GrossPay > 5000:
            State_tax = ((GrossPay - 5000) * 0.05) + 120
        elif GrossPay > 17000:
            State_tax = ((GrossPay - 17000) * 0.0575) + 720
        Fica_tax = GrossPay * 7.65 / 100
        Estimated_tax = Fica_tax + Federal_tax + State_tax
        Net_pay = GrossPay - Estimated_tax

        print("Employee Name: ", user)
        print("Gross Pay: $", GrossPay)
        print("Your Fed Tax is: $", Federal_tax)
        print("Your State Tax is: $", State_tax)
        print("Your Fica Tax is: $", Fica_tax)
        print("Your net pay is: $", Net_pay)
    else:
        RegularPay = Rate * 40
        OverTime = Hours - 40
        OverTimeRate = Rate * 1.5
        OverTimePay = round(OverTimeRate * OverTime, 2)
        GrossPay = round(RegularPay + OverTimePay, 2)

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
        if GrossPay > 0:
            State_tax = GrossPay * 0.02
        elif GrossPay > 3000:
            State_tax = ((GrossPay - 3000) * 0.03) + 60
        elif GrossPay > 5000:
            State_tax = ((GrossPay - 5000) * 0.05) + 120
        elif GrossPay > 17000:
            State_tax = ((GrossPay - 17000) * 0.0575) + 720
        Fica_tax = GrossPay * 7.65 / 100
        Estimated_tax = Fica_tax + Federal_tax + State_tax
        Net_pay = GrossPay - Estimated_tax

        print("Employee Name: ", user)
        print("Gross Pay: $", GrossPay)
        print("(Overtime pay: $", OverTimePay, ")")
        print("Your Fed Tax is: $", Federal_tax)
        print("Your State Tax is: $", State_tax)
        print("Your Fica Tax is: $", Fica_tax)
        print("Your net pay is: $", Net_pay)
    user = input("Enter Next Employee or type '0' to Exit: ")
else:
    print("Exiting program....")
