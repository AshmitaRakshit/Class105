import csv
with open('./class2.csv', newline='') as f:
    reader = csv.reader(f)
    #csv.reader method,reads and returns the current row and then moves to the next
    file_data = list(reader)
    #list(reader) adds the data to the list

file_data.pop(0)
#to remove the title from the data
#----------------------------------
#print(file_data)
# sorting data  to get the height of people.
#new_data=[]
#for i in range(len(file_data)):
	#n_num = file_data[i][1]
	#new_data.append(float(n_num))
#Then create a empty list named new_data .
#Then use a for loop on file_data to get the elements inside the nested lists
#and append them to the new_data list.

# #getting the mean
#n = len(new_data)
#total =0
#for x in new_data:
    #total += x

#mean = total / n

#print("Mean / Average is: " + str(mean))
#-----------------------------------------
total_marks=0
total_entries=len(file_data)

for marks in file_data:
    total_marks+=float(marks[1])

mean=total_marks/total_entries
print("Mean / Average is: " + str(mean))

import pandas as pd
import plotly_express as px
df=pd.read_csv("class2.csv")
fig=px.scatter(df,x="Student Number", y="Marks")
fig.update_layout(shapes=[
dict(
    type="line",
    y0=mean,y1=mean,x0=0,x1=total_entries
)
])
#fig.update_yaxis(rangemode="tozero")
fig.show()
