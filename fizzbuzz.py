# anoop abraham, 2018-02-17
# fizzbuzz:https://en.wikipedia.org/wiki/Fizz_buzz

i = 1

while i <= 10:
    if i % 3 == 0:
        print("Fizz")
    if i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i = i + 1
