file=open("AdventOfCode/Day 3/data03.txt", "r")

data=[]
for string in file:
    r_string=string.replace("\n","")
    s1,s2=r_string[:len(r_string)//2], r_string[len(r_string)//2:]
    
    data.append([s1,s2])

#PART 1
def common_element_priority(pair):
    found=False
    i=0
    while i<len(pair[0]) and not found:
        j=0
        letter="a"
        while j<len(pair[1]):
            if pair[0][i]==pair[1][j]:
                found=True
                letter=pair[0][i]          
            j+=1
        i+=1     
    if letter.isupper():
        priority=ord(letter)-38
    else:
        priority=ord(letter)-96
    return priority

priorites_sum=0
for pair in data:
    priorites_sum+=common_element_priority(pair)
print(priorites_sum)

#PART 2

    

