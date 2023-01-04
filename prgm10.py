
import matplotlib.pyplot as plt
data = {'Walking': 29, 'Cycling': 15, 'Car': 35, 'Bus': 18, 'Train':3}
courses = list(data.keys())
values = list(data.values())
fig = plt.figure(figsize=(10, 5))
plt.bar(courses, values, color='green',width=0.1)
plt.xlabel("Mode of Transportation")
plt.ylabel("Frequency")
plt.title("Mode of transportation of students")
plt.show()