class school():
    def __init__(self, nameS ,major , clases ,students):
        self.name = nameS
        self.Major= major
        self.clase = clases # number of classes in school
        self.student = students  # number of student in school


school1 = school("adnan bin majid","mr.ahmed ali",600,6400)
print(f"the name of the school is {school1.name} and it's Major is {school1.Major}")    