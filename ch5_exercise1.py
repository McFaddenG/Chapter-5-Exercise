total = 0
count = 0
average = 0

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = float(num)
    except ValueError:
        print("Invalid input")
        continue
        
    count = count + 1  
    total = total + num
    total = int(total)
    average = float(total / count)
    
print(total,count,average)