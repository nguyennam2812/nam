# If ... Else: Nếu.. khác
# Câu lệnh If
Bằng: a == b
Không bằng: a != b
Nhỏ hơn: a < b
Nhỏ hơn hoặc bằng: a <= b
Lớn hơn: a > b
Lớn hơn hoặc bằng: a >= b

VD:
a = 33
b = 200
if b > a:
  print("b is greater than a") # b is greater than a

# Câu lệnh If không thụt lề (sẽ gây ra lỗi):
a = 33
b = 200
if b > a:
print("b is greater than a") 

>>> File "demo_if_error.py", line 4
    print("b is greater than a")
        ^
IndentationError: expected an indented block

# elif nếu các điều kiện trước đó không đúng, hãy thử điều kiện này".
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal") # >> a and b are equal

# else sẽ thay thế cho các  điều kiện trc đó nếu ko đúng
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b") # a is greater than b

# if
if a > b: print("a is greater than b")  

>> "a is greater than b"

# if.. else : nếu.. ko
a = 2
b = 330
print("A") if a > b else print("B")  # B

VD:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B") # = 

# and : và
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True") # Both conditions are True

# or
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True") # At least one of the conditions is True
 
# not
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b") # a is NOT greater than b

# if lồng nhau
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.") 
# Above ten,
# and also above 20!

#if câu lệnh không được để trống, nhưng nếu vì lý do nào đó bạn có một ifcâu lệnh không có nội dung, hãy nhập vào passcâu lệnh để tránh bị lỗi.
a = 33
b = 200
if b > a:
  pass

# Vòng lặp While (đã học)
# Vòng lặp for (đã học )

## Functions (hàm pyhton)
# tạo hàm bằng def
def my_function():
  print("Hello from a function")
my_function() # Hello from a function

# Arguments: hàm nghịch
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

>> " Emil Refsnes
Tobias Refsnes
Linus Refsnes "

# Slg đối số (slg đối số phải bằng vs hàm)
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes") # Emil Refsnes

Vd:
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil") 

>> "Traceback (most recent call last):
  File "demo_function_args_error.py", line 4, in <module>
    my_function("Emil")
TypeError: my_function() missing 1 required positional argument: 'lname'"

# Nếu số lượng đối số không xác định, hãy thêm a *trước tên tham số:
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus") # The youngest child is Linus

# Đối số từ khóa (cú pháp key = value )
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") # The youngest child is Linus

# Nếu bạn không biết có bao nhiêu đối số từ khóa sẽ được truyền vào hàm của mình, hãy thêm hai dấu hoa thị: **trước tên tham số trong định nghĩa hàm.
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes") # His last name is Refsnes

# Giá trị tham số mặc định
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
>> I am from Sweden
I am from India
I am from Norway
I am from Brazil

# Truyền một danh sách như một đối số
Bạn có thể gửi bất kỳ kiểu dữ liệu đối số nào vào một hàm (chuỗi, số, danh sách, từ điển, v.v.) và nó sẽ được coi là cùng một kiểu dữ liệu bên trong hàm.
Ví dụ nếu bạn gửi một List làm đối số, nó vẫn sẽ là một List khi đến hàm:
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

>> apple
banana
cherry

# return
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

>> 15
25
45

# function  không đc để trống  hãy dùng pass tránh lỗi
def myfunction():
  pass
# Đổi số chỉ vị trí 
Để chỉ rõ rằng một hàm chỉ có thể có các đối số theo vị trí, hãy thêm vào , / sau các đối số:\
def my_function(x, /):
  print(x)
my_function(3) # 3

# Nếu không có, , /bạn thực sự được phép sử dụng đối số từ khóa ngay cả khi hàm mong đợi đối số theo vị trí:
def my_function(x):
  print(x)
my_function(x = 3) #3

#Nhưng khi thêm, , /bạn sẽ gặp lỗi nếu bạn cố gửi đối số từ khóa:
Ví dụ
def my_function(x, /):
  print(x
my_function(x = 3)

>> Traceback (most recent call last):
  File "./prog.py", line 4, in <module>
TypeError: my_function() got some positional-only arguments passed as keyword arguments: 'x'

# Đối số chỉ từ khóa
Để chỉ rõ rằng một hàm chỉ có thể có các đối số từ khóa, hãy thêm *, trước các đối số:
Ví dụ
def my_function(*, x):
  print(x)
my_function(x = 3) # 3

# Kết hợp Chỉ vị trí và Chỉ từ khóa
Bất kỳ đối số nào trước chỉ / ,mang tính vị trí và bất kỳ đối số nào sau chỉ *, mang tính từ khóa.
Ví dụ
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)
my_function(5, 6, c = 7, d = 8) # 26

# đệ quy
Trong ví dụ này, tri_recursion() là một hàm mà chúng ta đã định nghĩa để gọi chính nó ("recurse"). Chúng ta sử dụng biến k làm dữ liệu, biến này giảm ( -1 ) mỗi lần chúng ta đệ quy. Đệ quy kết thúc khi điều kiện không lớn hơn 0 (tức là khi nó bằng 0).
Đối với một nhà phát triển mới, có thể mất một thời gian để tìm hiểu chính xác cách thức hoạt động này, cách tốt nhất để tìm hiểu là thử nghiệm và sửa đổi nó.

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results")
tri_recursion(6)

>> Recursion Example Results
1 
3 
6
10
15
21 

# Lambda​ (lambda arguments : expression )
Thêm 10 vào đối số avà trả về kết quả:
x = lambda a : a + 10
print(x(5)) # 15

Tóm tắt đối số a, b, và cvà trả về kết quả:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2)) # 13

# lambda được thể hiện rõ hơn khi bạn sử dụng chúng như một hàm ẩn danh bên trong một hàm khác.
Sử dụng định nghĩa hàm đó để tạo một hàm luôn nhân đôi, hoặc 3 số bạn gửi vào:
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11)) # 22

# sử dụng cùng một định nghĩa hàm để tạo cả hai hàm trong cùng một chương trình:
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11)) # 22
print(mytripler(11)) # 33

## Arrays (mảng)
cars = ["Ford", "Volvo", "BMW"] # ['Ford', 'Volvo', 'BMW']
# ruy cập các phần tử của một mảng
x = cars[0] # Ford
# Lặp lại các phần tử mảng for in
for x in cars:
  print(x)  
>> 

Ford
Volvo
BMW

# Thêm phần tử mảng  append()
cars.append("Honda") # ['Ford', 'Volvo', 'BMW', 'Honda']
# Xóa các phần tử mảng popm ()
cars.pop(1)  # ['Ford', 'BMW']
# remove()
cars.remove("Volvo")

# Phương pháp mảng
append() Thêm một phần tử vào cuối danh sách
clear() Xóa tất cả các phần tử khỏi danh sách
copy() Trả về một bản sao của danh sách
count() Trả về số lượng phần tử có giá trị được chỉ định
extend() Thêm các phần tử của danh sách (hoặc bất kỳ phần tử lặp nào) vào cuối danh sách hiện tại
index() Trả về chỉ mục của phần tử đầu tiên có giá trị được chỉ định
insert() Thêm một phần tử ở vị trí được chỉ định
pop() Xóa phần tử ở vị trí được chỉ định
remove() Xóa mục đầu tiên có giá trị được chỉ định
reverse() Đảo ngược thứ tự của danh sách
sort() Sắp xếp danh sách

## Classes and Objects
# TẠO 1 CLASS
class MyClass:
  x = 5 # <class '__main__.MyClass'>

# Tạo đối tượng
class MyClass:
  x = 5
p1 = MyClass()
print(p1.x) # 5

# Tạo một lớp có tên là Person, sử dụng hàm __init__() để gán giá trị cho tên và tuổi:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age) 
# John
# 36

# đối tượng KHÔNG có hàm __str__():
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36) 
print(p1) # <__main__.Person object at 0x15039e602100>

# Biểu diễn chuỗi của một đối tượng VỚI hàm __str__():
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"
p1 = Person("John", 36)
print(p1)

# Phương pháp đối tượng
Chèn một hàm in ra lời chào và thực thi nó trên đối tượng p1:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc() # Hello my name is John

# Tham số tự
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age
  def myfunc(abc):
    print("Hello my name is " + abc.name)
p1 = Person("John", 36)
p1.myfunc() # Hello my name is John

# Sửa đổi Thuộc tính Đối tượng
p1.age = 40 # 40
# Xóa Thuộc tính Đối tượng
del p1.age 
>> Traceback (most recent call last):
  File "demo_class7.py", line 13, in <module>
    print(p1.age)
AttributeError: 'Person' object has no attribute 'age'

# Xóa Đối Tượng
Traceback (most recent call last):
  File "demo_class8.py", line 13, in <module>
    print(p1)
NameError: 'p1' is not defined

# classđịnh nghĩa không được để trống, nhưng nếu vì lý do nào đó bạn có một classđịnh nghĩa không có nội dung, hãy thêm vào passcâu lệnh để tránh bị lỗi.
class Person:
  pass

# Python Inheritance ( lớp )
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
#Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()

# Create a Parent Class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
#Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname() # John Doe

# Create a Child Class
x = Student("Mike", "Olsen")
x.printname()  # Mike Olsen

# Thêm hàm __init__() 
Muốn thêm __init__()hàm vào lớp con (thay vì passtừ khóa).
Thêm hàm __init__()vào Studentlớp:
Lưu ý: Hàm này __init__()được gọi tự động mỗi khi lớp được sử dụng để tạo một đối tượng mới.
Lưu ý:__init__() Hàm con sẽ ghi đè lên tính kế thừa của hàm cha __init__().
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname) # Mike Olsen

# Trình lặp Python  __iter__() và __next__().
# Iterator so với Iterable
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
>> apple
banana
cherry

# Chuỗi cũng là đối tượng có thể lặp lại, chứa một chuỗi ký tự:
mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

>> 
b
a
n
a
n
a

# Lặp qua một Iterator
for
Lặp lại các giá trị của một tuple:
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
  print(x)

>> 
apple
banana
cherry

# Lặp lại các ký tự của một chuỗi:
mystr = "banana"
for x in mystr:
  print(x)

> 
b
a
n
a
n
a

# Tạo một Iterator
Để tạo một đối tượng/lớp như một trình lặp, bạn phải triển khai các phương thức __iter__()và __next__()đối tượng 
Lớp/Đối tượng Python , tất cả các lớp đều có một hàm gọi là __init__(), cho phép bạn khởi tạo một số thứ khi đối tượng được tạo.
__iter__()hoạt động tương tự, bạn có thể thực hiện các thao tác (khởi tạo, v.v.), nhưng phải luôn trả về chính đối tượng lặp.
__next__()cũng cho phép bạn thực hiện các phép toán và phải trả về mục tiếp theo trong chuỗi.

# Tạo một trình lặp trả về các số, bắt đầu từ 1 và mỗi chuỗi sẽ tăng thêm một (trả về 1,2,3,4,5, v.v.):
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    x = self.a
    self.a += 1
    return x
myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

> 
1
2
3
4
5

# Dừng lặp
Để ngăn chặn việc lặp lại diễn ra mãi mãi, chúng ta có thể sử dụng câu StopIterationlệnh.
Trong __next__()phương pháp này, chúng ta có thể thêm điều kiện kết thúc để đưa ra lỗi nếu quá trình lặp được thực hiện một số lần nhất định:
 Dừng lại sau 20 lần lặp lại:
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
  print(x)

>> 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20

# Python Polymorphism (Đa hình Python)
# Đếm  số kí tự
x = "Hello World!"
print(len(x)) # 12

# Đối với tuple, len()trả về số lượng phần tử trong tuple:
mytuple = ("apple", "banana", "cherry")
print(len(mytuple))  #3

# Đối với dict , len()trả về số cặp khóa/giá trị trong từ điển:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
} 
print(len(thisdict)) #3

# Đa hình lớp
Đa hình thường được sử dụng trong các phương thức Class, trong đó chúng ta có thể có nhiều lớp có cùng tên phương thức.
Ví dụ, giả sử chúng ta có ba lớp: Car, Boat, và Plane, và tất cả chúng đều có một phương thức gọi là move():
Ví dụ
Các lớp khác nhau có cùng phương pháp:
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Drive!")
class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Sail!")
class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Fly!")
car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class
for x in (car1, boat1, plane1):
  x.move()

>>
Drive!
Sail!
Fly!

# Đa hình lớp kế thừa
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

>>
Ford
Mustang
Move!
Ibiza
Touring 20
Sail!
Boeing
747
Fly!
Trong ví dụ trên, bạn có thể thấy Carlớp này trống, nhưng nó kế thừa brand, model, và move()từ Vehicle.
Các lớp Boatvà Planecũng kế thừa brand, model, và move()từ Vehicle, nhưng cả hai đều ghi đè phương move()thức.
Nhờ tính đa hình, chúng ta có thể thực thi cùng một phương thức cho tất cả các lớp.

# Phạm vi Python
def myfunc():
  x = 300
  print(x)
myfunc() # 300

# Biến cục bộ có thể được truy cập từ một hàm bên trong hàm đó:
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()
myfunc() # 300

# Global Scope
Biến được tạo bên ngoài hàm là biến toàn cục và có thể được bất kỳ ai sử dụng:
x = 300
def myfunc():
  print(x)
myfunc()
print(x)

>> 
300
300

# Đặt tên biến
Hàm này sẽ in ra giá trị cục bộ xvà sau đó mã sẽ in ra giá trị toàn cục x:
x = 300
def myfunc():
  x = 200
  print(x)
myfunc()
print(x)

# Nếu bạn sử dụng globaltừ khóa, biến sẽ thuộc về phạm vi toàn cục:
def myfunc():
  global x
  x = 300
myfunc()
print(x) # 300

# Để thay đổi giá trị của biến toàn cục bên trong một hàm, hãy tham chiếu đến biến đó bằng cách sử dụng globaltừ khóa:
x = 300
def myfunc():
  global x
  x = 200
myfunc()
print(x) # 200

# Nếu bạn sử dụng nonlocaltừ khóa, biến sẽ thuộc về hàm bên ngoài:
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x
print(myfunc1()) # 200

## Các mô-đun
# Tạo một mô-đun
Lưu mã này vào một tệp có tên mymodule.py
def greeting(name):
  print("Hello, " + name)

# Sử dụng một mô-đun
import mymodule
mymodule.greeting("Jonathan") # Hello, Jonathan

# Biến trong Module
Lưu mã này vào tập tinmymodule.py
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

VD:
import mymodule
a = mymodule.person1["age"]
print(a) # 36

# Tạo bí danh cho mymodulecalled mx:
import mymodule as mx
a = mx.person1["age"]
print(a)N # 36

# TÍCH HỢP MÔ ĐUN
Nhập và sử dụng platformmô-đun:
import platform
x = platform.system()
print(x) # Windows

# Liệt kê tất cả các tên đã xác định thuộc về mô-đun nền tảng:
import platform
x = dir(platform)
print(x) 
>> ['DEV_NULL', '_UNIXCONFDIR', 'WIN32_CLIENT_RELEASES', 'WIN32_SERVER_RELEASES', '__builtins__', '__cached__', '__copyright__', '__doc__', '__file__', '__loader__', '__name__', '__package __', '__spec__', '__version__', '_default_architecture', '_dist_try_harder', '_follow_symlinks', '_ironpython26_sys_version_parser', '_ironpython_sys_version_parser', '_java_getprop', '_libc_search', '_linux_distribution', '_lsb_release_version', '_mac_ver_xml', '_node', '_norm_version', '_perse_release_file', '_platform', '_platform_cache', '_pypy_sys_version_parser', '_release_filename', '_release_version', '_supported_dists', '_sys_version', '_sys_version_cache', '_sys_version_parser', '_syscmd_file', '_syscmd_uname', '_syscmd_ver', '_uname_cache', '_ver_output', 'architecture', 'collections', 'dist', 'java_ver', 'libc_ver', 'linux_distribution', 'mac_ver', 'machine', 'node', 'os', 'platform', 'popen', 'processor', 'python_branch', 'python_build', 'python_compiler', 'python_implementation', 'python_revision', 'python_version', 'python_version_tuple', 're', 'release', 'subprocess', 'sys', 'system', 'system_aliases', 'uname', 'uname_result', 'version', 'warnings', 'win32_ver']

# Nhập từ mô-đun from
from mymodule import person1
print (person1["age"]) #36

## Ngày giờ
# Ngày tháng datetime
import datetime
x = datetime.datetime.now()
print(x) # 2024-08-08 21:50:51.390192

# Trả về năm và tên ngày trong tuần:
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

>> 2024
Thursday

# Tạo Đối tượng Ngày
Tạo một đối tượng ngày:
import datetime
x = datetime.datetime(2020, 5, 17)
print(x) # 2020-05-17 00:00:00

# Phương pháp strftime()
Phương pháp này được gọi là strftime(), và lấy một tham số, format, để chỉ định định dạng của chuỗi trả về:
import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B")) # June

## %a Ngày trong tuần, phiên bản rút gọn Thứ tư
%A Ngày trong tuần, phiên bản đầy đủ Thứ tư
%w Ngày trong tuần dưới dạng số 0-6, 0 là Chủ Nhật 3
%d Ngày trong tháng 01-31 31
%b Tên tháng, phiên bản rút gọn Tháng 12
%B Tên tháng, phiên bản đầy đủ Tháng 12
%m Tháng dưới dạng số 01-12 12
%y Năm, phiên bản rút gọn, không có thế kỷ 18
%Y Năm, phiên bản đầy đủ 2018
%H Giờ 00-23 17
%I Giờ 00-12 05
%p Sáng/Chiều Chiều
%M Phút 00-59 41
%S Giây 00-59 08
%f Micro giây 000000-999999 548513
%z Độ lệch UTC +0100
%Z Múi giờ CST
%j Số ngày trong năm 001-366 365
%U Số tuần trong năm, Chủ Nhật là ngày đầu tiên của tuần, 00-53 52
%W Số tuần trong năm, Thứ Hai là ngày đầu tiên của tuần, 00-53 52
%c Phiên bản địa phương của ngày và giờ Thứ Hai, 31 tháng 12 năm 2018 lúc 17:41:00
%C Thế kỷ 20
%x Phiên bản địa phương của ngày 31/12/18
%X Phiên bản địa phương của giờ 17:41:00
%% A % ký tự %
%G Năm ISO 8601 2018
%u Ngày trong tuần theo ISO 8601 (1-7) 1
%V Số tuần theo ISO 8601 (01-53) 01

## toán
Các hàm min()và max()có thể được sử dụng để tìm giá trị thấp nhất hoặc cao nhất trong một đối tượng lặp lại:
Ví dụNhận máy chủ Python của riêng bạn
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x) # 5
print(y) #25

# Hàm abs()trả về giá trị tuyệt đối (dương) của số đã chỉ định:
Ví dụ
x = abs(-7.25)
print(x) # 7.25

# Hàm trả về giá trị của x lũy thừa của y (x y ).pow(x, y)

Ví dụ
Trả về giá trị của 4 mũ 3 (tương tự như 4 * 4 * 4):
x = pow(4, 3)
print(x) # 64

# Mô-đun Toán học
Ví dụ, phương pháp này math.sqrt()trả về căn bậc hai của một số:
Ví dụ
import math
x = math.sqrt(64) # căn bậc 2
print(x) # 8

# Phương pháp này math.ceil()làm tròn một số lên đến số nguyên gần nhất và math.floor() làm tròn một số xuống đến số nguyên gần nhất rồi trả về kết quả:
Ví dụ
import math
x = math.ceil(1.4)
y = math.floor(1.4)
print(x) # returns 2
print(y) # returns 1

# Hằng math.pisố trả về giá trị PI (3.14...):
Ví dụ
import math
x = math.pi
print(x) # 3.141592653589793

# Phương pháp toán học
Mô tả phương thức
math.acos() Trả về arc cosin của một số
math.acosh() Trả về arc cosin hyperbolic nghịch đảo của một số
math.asin() Trả về arc sin của một số
math.asinh() Trả về arc sin hyperbolic nghịch đảo của một số
math.atan() Trả về arc tan của một số theo radian
math.atan2() Trả về arc tan của y/x theo radian
math.atanh() Trả về arc tan hyperbolic nghịch đảo của một số
math.ceil() Làm tròn một số lên đến số nguyên gần nhất
math.comb() Trả về số cách chọn k mục từ n mục mà không lặp lại và không sắp xếp theo thứ tự
math.copysign() Trả về một số float bao gồm giá trị của tham số đầu tiên và dấu của tham số thứ hai
math.cos() Trả về cosin của một số
math.cosh() Trả về cosin hyperbolic của một số
math.degrees() Chuyển đổi một góc từ radian sang độ
math.dist() Trả về khoảng cách Euclidean giữa hai điểm (p và q), trong đó p và q là tọa độ của điểm đó
math.erf() Trả về hàm lỗi của một số
math.erfc() Trả về hàm lỗi bù của một số
math.exp() Trả về E mũ x
math.expm1() Trả về Ex - 1
math.fabs() Trả về giá trị tuyệt đối của một số
math.factorial() Trả về giai thừa của một số
math.floor() Làm tròn một số xuống số nguyên gần nhất
math.fmod() Trả về phần dư của x/y
math.frexp() Trả về mantissa và mũ của một số đã chỉ định
math.fsum() Trả về tổng của tất cả các mục trong bất kỳ phần tử lặp nào (bộ, mảng, danh sách, v.v.)
math.gamma() Trả về hàm gamma tại x
math.gcd() Trả về ước chung lớn nhất của hai số nguyên
math.hypot() Trả về chuẩn Euclidean
math.isclose() Kiểm tra xem hai giá trị có gần nhau hay không
math.isfinite() Kiểm tra xem một số có hữu hạn hay không
math.isinf() Kiểm tra xem một số có vô hạn hay không
math.isnan() Kiểm tra xem một giá trị có phải là NaN (không phải là số) hay không
math.isqrt() Làm tròn một số căn bậc hai xuống số nguyên gần nhất
math.ldexp() Trả về nghịch đảo của math.frexp() là x * (2**i) của các số x và i đã cho
math.lgamma() Trả về giá trị log gamma của x
math.log() Trả về logarit tự nhiên của một số hoặc logarit của số theo cơ số
math.log10() Trả về logarit cơ số 10 của x
math.log1p() Trả về logarit tự nhiên của 1+x
math.log2() Trả về cơ số 2 logarit của x
math.perm() Trả về số cách chọn k phần tử từ n phần tử theo thứ tự và không lặp lại
math.pow() Trả về giá trị của x theo lũy thừa của y
math.prod() Trả về tích của tất cả các phần tử trong một phần tử có thể lặp lại
math.radians() Chuyển đổi giá trị độ thành radian
math.remainder() Trả về giá trị gần nhất có thể khiến tử số chia hết hoàn toàn cho mẫu số
math.sin() Trả về sin của một số
math.sinh() Trả về sin hyperbolic của một số
math.sqrt() Trả về căn bậc hai của một số
math.tan() Trả về tan của một số
math.tanh() Trả về tan hyperbolic của một số
math.trunc() Trả về phần nguyên bị cắt bớt của một số

# Hằng số toán học
Mô tả hằng số
math.e Trả về số Euler (2.7182...)
math.inf Trả về số thực dấu phẩy động vô cực dương
math.nan Trả về giá trị thực dấu phẩy động NaN (Không phải số)
math.pi Trả về PI (3.1415...)
math.tau Trả về tau (6.2831...)

## PythonJSON
JSON là cú pháp để lưu trữ và trao đổi dữ liệu.
JSON là văn bản, được viết bằng ký hiệu đối tượng JavaScript.

import json

#Chuyển đổi từ JSON sang Python:
import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"]) # 30

# Chuyển đổi từ Python sang JSON (json.dumps())
Chuyển đổi từ Python sang JSON:
import json
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)

>> {"name": "John", "age": 30, "city": "New York"}

# Chuyển đổi các đối tượng Python thành chuỗi JSON và in các giá trị:
import json
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

>> 
{"name": "John", "age": 30}
["apple", "bananas"]
["apple", "bananas"]
"hello"
42
31.76
true
false
null

#Khi bạn chuyển đổi từ Python sang JSON, các đối tượng Python sẽ được chuyển đổi thành JSON (JavaScript) tương đương:
Python	JSON
dict	Object
list	Array
tuple	Array
str	String
int	Number
float	Number
True	true
False	false
None	null

# Chuyển đổi một đối tượng Python chứa tất cả các kiểu dữ liệu hợp lệ:

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

>>
{"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann","Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}

# Định dạng kết quả
Sử dụng tham indentsố để xác định số lượng thụt lề:
json.dumps(x, indent=4)

>> 
{
    "name": "John",
    "age": 30,
    "married": true,
    "divorced": false,
    "children": [
        "Ann",
        "Billy"
    ],
    "pets": null,
    "cars": [
        {
            "model": "BMW 230",
            "mpg": 27.5
        },
        {
            "model": "Ford Edge",
            "mpg": 24.1
        }
    ]
}

# Sử dụng tham separatorssố để thay đổi dấu phân cách mặc định:
json.dumps(x, indent=4, separators=(". ", " = "))

>> 
{
    "name" = "John".
    "age" = 30.
    "married" = true.
    "divorced" = false.
    "children" = [
        "Ann".
        "Billy"
    ].
    "pets" = null.
    "cars" = [
        {
            "model" = "BMW 230".
            "mpg" = 27.5
        }.
        {
            "model" = "Ford Edge".
            "mpg" = 24.1
        }
    ]
}

#Phương pháp này json.dumps()có các tham số để sắp xếp các khóa trong kết quả:
Ví dụ
Sử dụng tham sort_keyssố để chỉ định kết quả có được sắp xếp hay không:
json.dumps(x, indent=4, sort_keys=True)

>> 
{
    "age": 30,
    "cars": [
        {
            "model": "BMW 230",
            "mpg": 27.5
        },
        {
            "model": "Ford Edge",
            "mpg": 24.1
        }
    ],
    "children": [
        "Ann",
        "Billy"
    ],
    "divorced": false,
    "married": true,
    "name": "John",
    "pets": null
}









