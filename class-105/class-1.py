import math
import csv
with open ('C:/class-python/class-py/class-105/class1.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

# to remove header from csv
file_data.pop(0)

total_marks=0
total_entires=len(file_data)

for marks in file_data:
    total_marks+=float(marks[1])
    
# print(total_marks)

mean=total_marks/total_entires
print("mean is: "+str(mean))

import pandas as pd
import plotly.express as px

df=pd.read_csv('C:/class-python/class-py/class-105/class1.csv')
fig=px.scatter(df,x='Student Number',y='Marks')
fig.update_layout(shapes=[
    dict(
        type="line",
        y0=mean,
        y1=mean,
        x0=0,
        x1=total_entires
    )
])

fig.update_yaxes(rangemode="tozero")
fig.show()