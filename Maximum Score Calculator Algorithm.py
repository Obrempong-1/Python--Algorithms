student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max_score = student_scores[0]

for n in range(0, len(student_scores)):
    if student_scores[n] > max_score:
        max_score = student_scores[n]

print(f"The highest score in the class is: {max_score} ")


'''This program finds the highest score among the students.

1. It takes a list of student scores as input separated by spaces.
2. The input is split into individual values which are strings and then converted to integers.
3. It sets the first score as the initial max_score.
4. It loops through the list and compares each score with the current max_score:
- If a score is larger, max_score is updated.
5. After checking all scores, the program prints the highest score.

Algorithm Type: Linear (O(n))
    - Time Complexity: O(n) because the list is looped through once.
    - Space Complexity: O(n) because the list of scores is stored in memory. '''
