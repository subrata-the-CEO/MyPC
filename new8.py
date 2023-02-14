#Tax Prediction
CTC = int(input("Please Enter Your Annual CTC - "))
if CTC >= 500000:
    print("Employee Is Taxable")
else:
    print ("Employee Is Not Taxable")
if 500000<CTC<=750000:
    print (f"Amount of Tax = {CTC*0.10}")
if 750000<CTC<=1000000:
        print (f"Amount of Tax = {CTC*0.15}")
if 1000000<CTC<=1250000:
    print (f"Amount of Tax = {CTC*0.20}")
if 1250000<CTC<=1500000:
    print (f"Amount of Tax = {CTC*0.25}")
if CTC>1500000:
    print (f"Amount of Tax = {CTC*0.30}")
