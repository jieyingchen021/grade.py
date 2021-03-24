temperature1=float(input("Please enter the temperature of Marketing\n"))
temperature2=float(input("Please enter the temperature of HR\n"))
temperature3=float(input("Please enter the temperature of Business\n"))
temperature4=float(input("Please enter the temperature of Executive\n"))
marketing= temperature1 
hr = temperature2 
business = temperature3 
exeuctive = temperature4
avg_temp = float(marketing+hr+business+exeuctive//4) 
if avg_temp > 65:
  print("AC should be on")
elif avg_temp < 65:
  print("AC should be off")
elif avg_temp == 65:
  print("AC should be off")
else:
  print("Wrong input")
