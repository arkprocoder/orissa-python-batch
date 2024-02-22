# multi level inheritance...

class Grandfather:

    def grands(self):
        print("grand father")

class Father(Grandfather):

    def father(self):
        print("father")

class Son(Father):
    def son(self):
        print("son")


s1=Son()
s1.son()
s1.father()
s1.grands()


f1=Father()
f1.father()
f1.grands()