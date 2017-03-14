import os,sys
import datetime, time
import math
class Person(object):
    def __init__(self,name,age=0):
        self.name = name
        self.age = age

    def __del__(self):
        pass

    def println(self):
        print "NAME:%s, AGE:%02d" % (self.name,self.age)

class Teacher(Person):
    def println(self):
        print "Teacher's NAME:%s, AGE:%02d" % (self.name,self.age)

class Student(Person):
    def __init__(self,name,dep,age):
        super(Student,self).__init__(name,age=age)
        #super(Person,self).__init__(name,age=age)
        self.dep=dep

    def println(self):
        print  "NAME:%s, AGE:%02d, dep:%s"  % (self.name,self.age,self.dep)
#main
if __name__ =="__main__":
    p1 = Person("song")
    p2 = Person("song",18)
    t1 = Teacher("songxf",48)
    s1=Student("cd","gis",19)
    s1.println()
    p1.println()
    p2.println()
    t1.println()