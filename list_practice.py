scores = [85, 90, 78, 92, 88]

print(scores[0])

scores.append(95)

for score in scores:
    print (score)

print (len(scores))

total = sum (scores)
average = total / len(scores)
highest = max(scores)
lowest = min(scores)

print (f"Total score:{total}")
print (f"Average score:{average}")
print (f"Highest score:{highest}")
print (f"Lowest score:{lowest}")
# print (f"Average :{total/len(scores)} ")
# print (f"Highest score:{max(scores)}")
# print (f"Lowest score:{min(scores)}")

print(scores[1:4])
print(scores[:3])
print(scores[-2:])
print(scores[::2])
print(scores[::-1])

# new_scores = sorted(scores, reverse=True)
# print (scores)
# print (new_scores)

if 92 in scores:
    print (f"92 is at index {scores.index(92)}")
    print (f"92 appears {scores.count(92)} times")

new_scores = []
count = int (input("How many scores?"))
while count <=0:
    print ("Your count must be greater than 0.")
    count = int (input("How many scores?"))
for i in range(count):  # Assuming we want to enter 5 scores
    # for _ in range (count):  # Using underscore as a throwaway variable
    #new_score = int(input("Enter a score:"))
    new_score = int (input(f"Enter score {i+1}: "))
    while new_score < 0 or new_score>100:
        print ("Score must be between 0 and 100.")
        new_score = int (input(f"Enter score {i+1}: "))
    new_scores.append(new_score)
print(new_scores)

Total = sum(new_scores)
Average = Total / len(new_scores)
Highest = max(new_scores)
Lowest = min(new_scores)

print (f"Total new_score:{Total}")
print (f"Average new_score:{Average}")
print (f"Highest new_score:{Highest}")
print (f"Lowest new_score:{Lowest}")