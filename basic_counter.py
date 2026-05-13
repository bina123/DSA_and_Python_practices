from collections import Counter

fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

fruits_count = Counter(fruits)

print(fruits_count['apple'])
print(fruits_count['orange'])

print(fruits_count.most_common(3))