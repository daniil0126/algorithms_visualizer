n = int(input())
mas = list(map(int,input().split()))
count = 0;
for run in range(n-1):
    for i in range(n-1-run):
        if mas[i]>mas[i+1]:
          count+=1
          mas[i],mas[i+1]=mas[i+1],mas[i];  
print(mas)
    