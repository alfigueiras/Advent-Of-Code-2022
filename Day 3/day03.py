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