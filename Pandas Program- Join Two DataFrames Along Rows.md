# 🧪 Pandas Program: Join Two DataFrames Along Rows

## 🎯 AIM

To write a Python program using Pandas to **join two DataFrames along rows** (row-wise concatenation) and assign all data to a new DataFrame.

---

## 🧠 ALGORITHM

1. **Import Libraries**: Import the `pandas` library.
2. **Create First DataFrame**: Use a dictionary to create `student_data1`.
3. **Create Second DataFrame**: Use another dictionary to create `student_data2`.
4. **Concatenate DataFrames**: Use `pd.concat()` with `axis=0` to concatenate both DataFrames row-wise.
5. **Display Result**: Print the new combined DataFrame.

---

## 💻 Program

```
import pandas as pd

student_data1 = {'ID': [1, 2, 3],
                 'Name': ['Arun', 'Beena', 'Charles'],
                 'Score': [85, 90, 78]}

student_data2 = {'ID': [4, 5, 6],
                 'Name': ['David', 'Ella', 'Frank'],
                 'Score': [88, 92, 80]}

df1 = pd.DataFrame(student_data1)
df2 = pd.DataFrame(student_data2)

combined_df = pd.concat([df1, df2], axis=0)

print("Joined DataFrame (Row-wise):")
print(combined_df)

```
## Output

![alt text](<Screenshot 2025-10-22 175146.png>)


## Result
Both DataFrames were successfully joined along the rows using Pandas’ concat() method.