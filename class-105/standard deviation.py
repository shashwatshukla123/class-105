import math
import csv
with open ('C:/class-python/class-py/class-105/data.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]
def mean(data):
    n=len(data)
    total=0
    for x in data:
        total+=int(x)

    mean=total/n
    return mean 

# squring and getting the value
squared_list=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    squared_list.append(a)

# getting the sum of square list
sum=0
for i in squared_list:
    sum=sum+i 

print(len(data))

# dividing the sum of square list by total value (N)
result=sum/(len(data))

# getting the SD by taking the squre root of  result
std_deviation=math.sqrt(result)
print("standard deviation is: ",std_deviation)