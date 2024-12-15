#-Дано по условиям
grades=[[5,3,3,5,4,],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students={'Johnny','Bilbo','Steve','Khendrik','Aaron'}
#-упорядочим имена по алфавиту
students_list=sorted(students)
print(students_list)
average_grades=dict() #- пустой словарь
for students,grades_list in zip(students_list,grades):
    average_grades[students]=sum(grades_list)/len(grades_list)#-расчитываем ср. балл
print(average_grades)