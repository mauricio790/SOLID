from Student import Student
from Primaria import Primaria
from Secundaria import Secundaria

class App():
    def __init__(self):
        pass

    def graduateStudent(self):
        student = Student()

        primaria = Primaria()
        student.graduate(primaria)

        secundaria = Secundaria()
        student.graduate(secundaria)

app = App()
app.graduateStudent()