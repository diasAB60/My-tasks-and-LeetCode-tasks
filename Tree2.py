print("     Small Currency Converter\n")

print("     Your currency:")

print("1-KZT" \
" 2-RUB" \
" 3-USD" \
" 4-EUR")

summ = 0
result = 0

print("")

n = int(input("Choose the currency number: "))

if (n == 1):
    print("Excellent, you choosed KZT. Please write KZT summ: ")
    summ = int(input("..."))
    print("")
    print("Please select the currency you want to convert to: ")
    print("")
    print("1-RUB  2-USD  3-EUR")
    k = int(input())
    if (k == 1):
        result = summ / 6.75
        print("KZT in RUB:", round(result, 2))
    elif (k == 2): 
        result = summ / 538.46
        print("KZT in USD:", round(result, 2))
    elif (k == 3):
        result = summ / 629.52
        print("KZT in EUR:", round(result, 2))
    else:
        print("You choosed a wrong number. Please try again")
elif (n == 2):
    print("Excellent, you choosed RUB. Please write RUB summ: ")
    summ = int(input("..."))
    print("")
    print("Please select the currency you want to convert to: ")
    print("")
    print("1-KZT  2-USD  3-EUR")
    k = int(input())
    if (k == 1):
        result = summ / 0.15
        print("RUB in KZT:", round(result, 2))
    elif (k == 2): 
        result = summ / 79.80
        print("RUB in USD:", round(result, 2))
    elif (k == 3):
        result = summ / 93.22
        print("RUB in EUR:", round(result, 2))
    else:
        print("You choosed a wrong number. Please try again")
elif (n == 3):
    print("Excellent, you choosed USD. Please write USD summ: ")
    summ = int(input("..."))
    print("")
    print("Please select the currency you want to convert to: ")
    print("")
    print("1-KZT  2-RUB  3-EUR")
    k = int(input())
    if (k == 1):
        result = summ / 0.0019
        print("USD in KZT:", round(result, 2))
    elif (k == 2): 
        result = summ / 0.013
        print("USD in RUB:", round(result, 2))
    elif (k == 3):
        result = summ / 0.86
        print("USD in EUR:", round(result, 2))
    else:
        print("You choosed a wrong number. Please try again")
elif (n == 4):
    print("Excellent, you choosed EUR. Please write EUR summ: ")
    summ = int(input("..."))
    print("")
    print("Please select the currency you want to convert to: ")
    print("")
    print("1-KZT  2-RUB  3-USD")
    k = int(input())
    if (k == 1):
        result = summ / 0.0016
        print("EUR in KZT:", round(result, 2))
    elif (k == 2): 
        result = summ / 0.011
        print("EUR in RUB:", round(result, 2))
    elif (k == 3):
        result = summ / 0.86
        print("EUR in USD:", round(result, 2))
    else:
        print("You choosed a wrong number. Please try again")
else:
    print("You choosed a wrong number. Please try again")

print("")
print("Thank you for using our Small Currency Converter! Bye!")