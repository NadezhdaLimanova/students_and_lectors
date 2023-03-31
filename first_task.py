class Student:
    students_list = []

    def __init__(self, name, surname, gender):
        Student.students_list.append(self)
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lector, course, grade): # метод для подсчета оценки для лектора за лекцию
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _avg_grades(self): # внутренняя функция для подсчета средней оценки за все домашние задания
        total = 0
        counter = 0
        for i in self.grades.values():
            for y in i:
                total += y
                counter += 1
        res = round(total / counter, 1)
        return res

    def __lt__(self, other): # метод для сравнения студентов по средней оценке
        if not isinstance(other, Student):
            print('Такого студента нет')
        return self._avg_grades() < other._avg_grades()

    def __str__(self): # метод для выведения информации о классе
        a = ', '.join(self.courses_in_progress)
        b = ', '.join(self.finished_courses)
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._avg_grades()}'
        result += f'\nКурсы в процессе изучения: {a}\nЗавершенные курсы: {b}'
        return result

class Mentor:
    def __init__(self, name, surname ):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    lectors_list = [] # список для всех экземпляров класса
    def __init__(self, name, surname):
        Lecturer.lectors_list.append(self)
        super().__init__(name, surname)
        self.grades = {}

    def _avg_grades(self): # внутренняя функция для подсчета средней оценки за все лекции
        total = 0
        counter = 0
        for i in self.grades.values():
            for y in i:
                total += y
                counter += 1
        res = round(total / counter, 1)
        return res

    def __lt__(self, other): # метод для сравнения лекторов по средней оценке
        if not isinstance(other, Lecturer):
            print('Такого лектора нет')
        return self._avg_grades() < other._avg_grades()

    def __str__(self): # метод для выведения информации о классе
         res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._avg_grades()}'
         return res

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade): # метод для подсчета оценки для студента за дз
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
         res = f'Имя: {self.name}\nФамилия: {self.surname}'
         return res

def avg_rate_course(list, course):  # функция для подсчета средней оценки за домашние задания или за лекции
    total = 0
    counter = 0
    for i in list:
        for y, j in i.grades.items():
            for a in j:
                if y == course:
                    counter += 1
                    total += a
    return total / counter


best_student = Student('Good', 'Boy', 'your_gender') # студент №1
best_student.finished_courses += ['Ведение в программирование']
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']

worst_student = Student('Bad', 'Boy', 'your_gender') # студент №2
worst_student.finished_courses += ['Ведение в программирование']
worst_student.courses_in_progress += ['Python']
worst_student.courses_in_progress += ['Git']

first_lector = Lecturer('First', 'Lector') # лектор №1
first_lector.courses_attached += ['Python']
first_lector.courses_attached += ['Git']

second_lector = Lecturer('Second', 'Lector') # лектор №2
second_lector.courses_attached += ['Python']
second_lector.courses_attached += ['Git']

good_reviewer = Reviewer('Some', 'Buddy') # ревьювер №1
good_reviewer.courses_attached += ['Python']
good_reviewer.courses_attached += ['Git']

bad_reviewer = Reviewer('Another', 'Buddy') # ревьювер №2
bad_reviewer.courses_attached += ['Python']
bad_reviewer.courses_attached += ['Git']

good_reviewer.rate_hw(best_student, 'Python', 10) # подсчет оценок студента №1
good_reviewer.rate_hw(best_student, 'Python', 10)
good_reviewer.rate_hw(best_student, 'Python', 10)
bad_reviewer.rate_hw(best_student, 'Python', 8)
bad_reviewer.rate_hw(best_student, 'Python', 8)
bad_reviewer.rate_hw(best_student, 'Git', 3)

good_reviewer.rate_hw(worst_student, 'Python', 5) # подсчет оценок студента №2
good_reviewer.rate_hw(worst_student, 'Python', 5)
good_reviewer.rate_hw(worst_student, 'Git', 8)
bad_reviewer.rate_hw(worst_student, 'Python', 8)
bad_reviewer.rate_hw(worst_student, 'Python', 8)
bad_reviewer.rate_hw(worst_student, 'Python', 8)

best_student.rate_hw(first_lector, 'Python', 10) # подсчет оценок лектора №1
best_student.rate_hw(first_lector, 'Python', 10)
worst_student.rate_hw(first_lector, 'Python', 9)
worst_student.rate_hw(first_lector, 'Git', 10)

worst_student.rate_hw(second_lector, 'Python', 8) # подсчет оценок лектора №2
best_student.rate_hw(second_lector, 'Python', 8)
best_student.rate_hw(second_lector, 'Python', 9)
best_student.rate_hw(second_lector, 'Git', 7)

print(best_student)
print(best_student.grades, end='\n\n')

print(worst_student)
print(worst_student.grades, end='\n\n')

print(first_lector)
print(first_lector.grades, end ='\n\n')

print(second_lector)
print(second_lector.grades, end='\n\n')

print(good_reviewer, end='\n\n')
print(bad_reviewer, end='\n\n')

print(first_lector.__lt__(second_lector))
print(worst_student.__lt__(best_student))

print(avg_rate_course(Student.students_list, 'Python'))
print(avg_rate_course(Lecturer.lectors_list, 'Python'))



