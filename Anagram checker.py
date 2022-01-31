

N = int(input("Enter number of inputs: "))
lst = []
for i in range(0, N):
    lst.append(input("Enter word: "))
lst_letters = []
for words in lst:
    for letter in words:
        if letter not in lst_letters:
            lst_letters.append(letter)
count = 0        
for let in lst_letters:
    num = 0
    for x in lst:
        num+=x.count(let)
    if num%N == 0:
        count += 1
    else:
        break
    #print(let)
    #print(num)

if count == len(lst_letters):
    #print(count)
    #print(len(lst_letters))
    print("Possible")
else:
    print('Not Possible')


        

