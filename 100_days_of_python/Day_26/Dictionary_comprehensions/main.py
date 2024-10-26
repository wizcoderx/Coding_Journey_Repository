import random
names = ['Alex','Angela','Anamay']

results = {students:random.randint(1,100) for students in names}
print(results)

passed_students = {

    students:score for (students, score) in results.items() if score >=60

}

print(passed_students)