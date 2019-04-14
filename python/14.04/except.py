x = int(input("First value "))
y = int(input("Second value "))

try:
    result = x / y
except ZeroDivisionError:
    print("Dzielenie przez zero")
else:
    print(result)