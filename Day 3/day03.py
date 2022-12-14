file=open("AdventOfCode/Day 3/data03.txt", "r")

data=[]
for string in file:
    r_string=string.replace("\n","")
    s1,s2=r_string[:len(r_string)//2], r_string[len(r_string)//2:]
    data.append([s1,s2])

file.close()

#PART 1
def common_elements(pair):
    i=0
    common=[]
    while i<len(pair[0]):
        j=0
        while j<len(pair[1]):
            if pair[0][i]==pair[1][j]:
                if pair[0][i] not in common:
                    common.append(pair[0][i])          
            j+=1
        i+=1     
    return common

priorities_sum=0
for pair in data:
    for l in common_elements(pair):
        if str(l).isupper():
            priorities_sum+=ord(l)-38
        else:
            priorities_sum+=ord(l)-96
print(priorities_sum)

#PART 2
file=open("AdventOfCode/Day 3/data03.txt", "r")
data2=[]

for string in file:
    r_string=string.replace("\n","")
    data2.append(r_string)

i=0
order_sum=0
while i<len(data2)//3:
    common1_2=common_elements([data2[3*i], data2[3*i+1]])
    letter=str(common_elements([common1_2, data2[3*i+2]])[0])
    if letter.isupper():
        order_sum+=ord(letter)-38
    else:
        order_sum+=ord(letter)-96
    i+=1

print(order_sum)
    