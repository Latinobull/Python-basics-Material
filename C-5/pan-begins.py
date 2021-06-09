# DATA SCIENCE WITH PANDAS
"""
iPython better for data structures

pandas.DataFrame with List and Dictionaries
"""
import pandas

df1 = pandas.DataFrame(
    [[2, 4, 6], [10, 20, 30], [60, 100, 200]], columns=["Age", "Price", "Value"]
)
print(df1)

# df2 = pandas.DataFrame([{"Name": "Charlie", "Last": "Puente"}, {"Name": "Esiena"}])
# print(df2)
pandas.set_option("display.max_rows", None)
df3 = pandas.read_csv("employees.csv")
df3 = df3.where(df3["Salary"] == 78133.48)
df3 = df3.dropna()
print(df3)
