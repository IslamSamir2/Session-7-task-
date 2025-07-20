import pandas as pd
students_data = [['Alice' , 20 , 'A' , 85],
['Bob' , 22 , 'B' , 78],
['Charlie' , 19 , 'A' , 92],
['David' , 21 , 'C' , 65],
['Eva' , 20 , 'B' , 74]]
Sd = pd.DataFrame(students_data, columns=['Name', 'Age', 'Grade', 'Marks'])
print(Sd.head(3))
print(Sd[['Name','Marks']])
print(Sd.loc[Sd['Grade'] == 'A'])