'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given

scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains n. The second line contains an array A[] of n integers each separated by a space.

Constraints

2 <= n <= 10
-100 <= A[i] <= 100

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5

Sample Output 0

5

Explanation 0

Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum is 5. Hence, we print as the runner-up score. 

'''

# SOLUTION:

# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     print(sorted(list(set(arr)))[-2])



'''

Given the names and grades for each student in a class of N students, store them in 
a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example
    records = [["chi", 20.0], ["beta", 50.0], ["alpha"], 50.0]
    The ordered list of scores is [20.0, 50.0], so the second lowest score is 50.0. There are two students with that score: ["beta", "alpha"]. 

Ordered alphabetically, the names are printed as:
    alpha
    beta

Input Format

The first line contains an integer, N, the number of students.
The 2N subsequent lines describe each student over 2 lines.
    - The first line contains a student's name.
    - The second line contains their grade.

Constraints
    2 <= N <= 5
    There will always be one or more students having the second lowest grade.

Output Format

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, 
order their names alphabetically and print each one on a new line.

Sample Input 0

    5
    Harry
    37.21
    Berry
    37.21
    Tina
    37.2
    Akriti
    41
    Harsh
    39

Sample Output 0

    Berry
    Harry

Explanation 0

There are

students in this class whose names and grades are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, 
so we order their names alphabetically and print each name on a new line.

'''




#SOLUTION
# 1st way

# if __name__ == '__main__':
#     score_list = []
#     grade = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
        
#         score_list.append([name, score])
#         grade.append(score)
    
#     grade = sorted(set(grade))    
#     sc = grade[1]
#     names = []
#     for value in score_list:
#         if sc == value[1]:
#             names.append(value[0])
#     names.sort()
    
#     for name in names:
#         print(name)

# 2nd way

# N = int(input())
# students = []
# for i in range(2*N):
#     students.append(input().split())
# grades = {}
# for j in range(0, len(students), 2):
#     grades[students[j][0]] = float(students[j + 1][0])
# result = []
# num_to_match = sorted(set(grades.values()))[1]
# for pupil in grades.keys():
#     if grades[pupil] == num_to_match:
#         result.append(pupil)
# for k in sorted(result):
#     print(k)


'''
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal.


Example:
    marks key: value pairs are
    'alpha': [20,30,40]
    'beta': [30,50,70]
    query_name = 'beta'

The query_name is 'beta'. beta's average score is (20+50+70)/3 = 50.

Input Format:
    The first line contains the integer n, the number of students' records. The next n lines contain the names and marks
    obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.



Constraints:
    0<=n<=10
    0<=marks[i]<=100
    length of marks array=3


Output Format:
    Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
'''


