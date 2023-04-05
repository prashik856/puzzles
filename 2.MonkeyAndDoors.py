n = 100
result = 0
for i in range(1, 100+1):
    count = 0
    #print("Number: " + str(i))
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    #print("Count: " +str(count))
    if count % 2 == 1:
        # odd
        result += 1
print("Result: " + str(result))