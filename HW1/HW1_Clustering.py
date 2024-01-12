import math

def distance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

def minDisToCen(data,centroids):
    x,y=data[0],data[1]
    result=0
    dis=distance(x,y,centroids[0][0],centroids[0][1])
    for i in range(1,len(centroids)):
        tmp=distance(x,y,centroids[i][0],centroids[i][1])
        if(tmp<dis):
            dis=tmp
            result=i
    return result
        

def assign(datas,centroids):
    newgroups=dict()
    for i in range(len(centroids)):
        newgroups[i]=[]
    for point in datas:
        idx=minDisToCen(point,centroids)
        newgroups[idx].append(point)
    return newgroups        
            
def update(groups,centroids):
    newcen=[]   
    for i in range(len(centroids)):
        avx,avy=0,0
        for j in range(len(groups[i])):
            avx+=groups[i][j][0]
            avy+=groups[i][j][1]
        avx/=len(groups[i])
        avy/=len(groups[i])
        newcen.append([avx,avy])
        
    return newcen,newcen==centroids


def printBetweenProcess(groups):
    print("--------------------------------")
    for idx in range(len(groups)):
        print(str(idx) + " : "+str(groups[idx]))
    print("centroids : "+str(centroids))    
    print("--------------------------------")
    
    
isEnd=False
Datas=[[1,2],[3,3],[2,2],[8,8],[6,6],[7,7],[-3,-3],[-2,-4],[-7,-7]]
centroids=[]
for i in range(int(input())):
    centroids.append([int(x) for x in input().split()])
groups=dict()

for idx,point in enumerate(centroids):
    groups[idx]=[point]
    
printBetweenProcess(groups)
while (not isEnd):
    groups=assign(Datas,centroids)
    centroids,isEnd=update(groups,centroids)
    printBetweenProcess(groups)