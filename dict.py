'''student={
    "name":"Prerita",
    "age":18,
    "grade":"A"}
print(student)
a=student.get("name")
print(a)
name=student["name"]
age=student["age"]
print(name,age)
#phone=student["phoneno"]
#print(phone)
student["name"]="prerna"
print(student)

for key,value in student.items():
    print(f"{key}:{value}")
for key in student.keys():
    print(f"{key}")
for value in student.values():
    print(f"{value}")

squares={num:num**2 for num in range(1,6)}
print(squares)
phone=student.get("phone")
print(phone)

del student["age"]
print(student)

w=student.get("name")
print(w)

dict={0:10,1:20}
dict[2]=30
print(dict)

dict2={3:40,4:50}
dict3={5:60,6:70}
dict.update(dict2)
dict.update(dict3)
print(dict)'''

'''d={"x":10,"y":20,"z":30}
for key,value in d.items():
    print(f"{key}:{value}")

multi={num:num*num for num in range(1,6)}
print(multi)

square={num:num**2 for num in range(1,16)}
print(square)

myd={"data1":100,"data2":-54,"data3":247}
value=myd.values()
totalvalue=sum(value)
print(totalvalue)

color_dict={"red":"#ff0000","green":"#008000","black":"#00000","white":"fffff"}
keys_c=list(color_dict.keys())
keys_c.sort()
sorted_dict={i:color_dict[i] for i in keys_c}
print(sorted_dict)

dic={1:10,2:20,3:30,4:40,5:50,6:60}
a=dic.get(1)
if  a ==None:
    print("no")
else:
    print("yess")'''

class A:  
     def __init__(self):  
         self.A=1  
         self.B=2  
obj=A()  
print(obj.__dict__)

dic={1:10,2:20,3:30,4:40,5:50,6:60}
maxi=max(dic.keys())
maxiv=max(dic.values())
print("maximum key:",maxi," and maximum value:",maxiv)
mini=min(dic.keys())
miniv=min(dic.values())
print("minimum key:",mini," and minimum value:",miniv)
