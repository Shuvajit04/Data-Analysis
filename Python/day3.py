import pandas as pd

df = pd.read_csv("Book1.csv")

print(df.head())
print(df.info())
print(df.describe())

print("Missing values per column:\n", df.isnull().sum())
##visualization
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Book1.csv")

df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")
df = df.dropna(subset=["City", "Salary"])

avg_salary = df.groupby("City")["Salary"].mean()

colors = plt.cm.tab10.colors

plt.figure(figsize=(8, 5))
avg_salary.plot(kind='bar', color=colors[:len(avg_salary)])
plt.title("Average Salary by City")
plt.xlabel("City")
plt.ylabel("Average Salary")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
df["Salary"].plot(kind='hist', bins=5, edgecolor='black')
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 7))
avg_salary.plot(
    kind='pie',
    autopct='%1.1f%%',
    startangle=90,
    colors=colors[:len(avg_salary)]
)
plt.ylabel("")
plt.title("Salary Share by City")
plt.tight_layout()
plt.show()
##pie
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Book1.csv")

df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")
df = df.dropna(subset=["City", "Salary"])

city_salary = df.groupby("City")["Salary"].mean()

colors = plt.cm.tab10.colors

plt.figure(figsize=(7, 7))
plt.pie(
    city_salary,
    labels=city_salary.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors[:len(city_salary)]
)
plt.title("Average Salary Distribution by City")
plt.axis('equal')
plt.show()