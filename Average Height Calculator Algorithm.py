student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
total_height = 0
number_of_students = 0

for height in student_heights:
    total_height += height  # which is total height 0 plus each height in the list
    number_of_students += 1
average_height = total_height / number_of_students
print(f"The average height of the students is {round(average_height)}m")




''' This program calculates the average height of students.
 1. It takes a list of student heights as input separated by spaces.
 2. The input is split into individual values which are strings and converted to integers.
 3. It then loops through the list to find:
      - The total sum of all heights.
      - The number of students in the list.
 4. It divides the total height by the number of students to get the average height.
 5. Finally, it rounds the average to the nearest whole number and prints it.

Algorithm Type: Linear (O(n))
    - Time Complexity: O(n) this is  because it loops through the list twice.
    - Space Complexity: O(n) this is due to storing the list of heights in memory.'''

