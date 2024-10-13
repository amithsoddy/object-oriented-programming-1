class student:
    grade=9
    name="amith"
    def intro(self):
        print("hello i am a student")
    def details(self):
        print(self.grade,self.name)
ob=student()
ob.intro()
ob.details()
