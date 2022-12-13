import math
file=open("AdventOfCode/Day 12/data12.txt", "r")

data=[]

for row in file:
    replaced_row=row.replace("\n", "")
    data.append(list(replaced_row))

#PART 1
start=[0,0]
end=[0,0]
foundStart=False
foundEnd=False
i=0
j=0

def neighbours(pos1, pos2):
    neighbors=[]
    if pos1<len(data)-1:
        if ord(data[pos1+1][pos2])-ord(data[pos1][pos2])<2:
            neighbors.append([pos1+1, pos2])
    if pos1>0:
        if ord(data[pos1-1][pos2])-ord(data[pos1][pos2])<2:
            neighbors.append([pos1-1, pos2])
    if pos2<len(data[pos1])-1:
        if ord(data[pos1][pos2+1])-ord(data[pos1][pos2])<2:
            neighbors.append([pos1, pos2+1])
    if pos2>0:
        if ord(data[pos1][pos2-1])-ord(data[pos1][pos2])<2:
            neighbors.append([pos1, pos2-1])
    return neighbors

while i<len(data) and not (foundStart and foundEnd):
    while j<len(data[i]):
        if data[i][j]=="S":
            start=[i,j]
            data[i][j]="a"
            foundStart=True
        elif data[i][j]=="E":
            end=[i,j]
            data[i][j]="z"
            foundEnd=True
        j+=1
    j=0
    i+=1

#BF Search

def bfsearch(startPosition, endPosition):
    visited=[startPosition]
    distances=[[math.inf for k2 in k1] for k1 in data]
    distances[startPosition[0]][startPosition[1]]=0
    queue=[startPosition]
    foundFinal=False

    while len(queue)>0 and not foundFinal:
        u=queue.pop(0)
        for neighbour in neighbours(u[0], u[1]):
            if neighbour not in visited:
                alt=distances[u[0]][u[1]]+1
                if alt<distances[neighbour[0]][neighbour[1]]:
                    distances[neighbour[0]][neighbour[1]]=alt
                visited.append(neighbour)
                queue.append(neighbour)
            if neighbour==endPosition:
                foundFinal=True
    print(distances[endPosition[0]][endPosition[1]])
    return distances[endPosition[0]][endPosition[1]]

print(bfsearch(start, end))

#PART 2
stepsFromAToEnd=[]
i=0
while i<len(data):
    while j<len(data[i]):
        if data[i][j]=="a":
            stepsFromAToEnd.append(bfsearch([i,j],end))
        j+=1
    j=0
    i+=1
print(min(stepsFromAToEnd))