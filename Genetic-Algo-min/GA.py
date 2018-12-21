import random

chrmsm=[
        [1,1,0,1,0,1],
        [0,1,0,1,0,0],
        [1,0,1,0,1,0],
        [0,1,1,0,0,1],
        [0,0,0,1,0,1],
       ]

fsum=[]
nrmls=[]

k=0
for i in chrmsm:
    s=0
    for j in i:
        s=s+j
        k=k+j
    fsum.append(s)
print(fsum)  
for i in fsum:
     l=i/k
     nrmls.append(l)
        
     m=0
cmls=[]     
for i in nrmls:
    m=i+m
    cmls.append(m)
   
s1=random.uniform(0,1)
s2=random.uniform(0,1) 
print(s1,s2)
p1=0
print(cmls)
print("Selected Chromosome")
for i in cmls:
    if(s1<i):
     break 
    else:
        p1=p1+1
print(p1)

 
p2=0
for i in cmls:
    if(s2<i):
        break
    else:
         p2=p2+1
print(p2)

print(chrmsm[p1])
print(chrmsm[p2]) 

q=int(random.uniform(1,5))


for i in range(q-1,6):
    y=chrmsm[p1][i]
    z=chrmsm[p2][i]
    chrmsm[p1][i]=z
    chrmsm[p2][i]=y
print("Crossover")

print(chrmsm[p1])
print(chrmsm[p2])
    
s1=int(random.uniform(1,6))
s2=int(random.uniform(1,6))


if chrmsm[p1][s1]==0:
    chrmsm[p1][s1]=1
else:
    chrmsm[p1][s1]=0


if chrmsm[p2][s2]==0:
    chrmsm[p2][s2]=1
else:
    chrmsm[p2][s2]=0   
print("mutated")

    
print(chrmsm[p1])
print(chrmsm[p2])   
