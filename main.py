num = input('Enter a number (decimal only): ')
num1 = num.replace(".", "")

# type your code here
if "." in num == False or num1.isdigit() == False or num.count(".") > 1:
 num = "error "
 dp = "error"
 print("Please follow the instruction given and redo the test.")
else:
 num.find(".")
 dp = len(num[num.find(".")+1:])
 

# do not change any code beyond this point
print('The number', num, 'has', dp, 'decimal places.')
