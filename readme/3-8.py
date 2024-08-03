#cú pháp bắt đầu
print ("Hello, World")

# phiên bản python 
import sys
print(sys.version)

#cú pháp python
#1 thụt lề python
if 5>2: 
    print("five is greater than two") #Python sử dụng thụt lề để chỉ một khối mã.

if 5 > 2:
 print("Five is greater than two!") 
        print("Five is greater than two!") #sử dụng cùng số lượng khoảng trắng trong cùng một khối mã, nếu không Python sẽ báo lỗi:

#3 bình luận ghi chú mã 
print("hello, World") #GHi chú 

"""
This is a comment
written in
more than just one line
"""
#Biến python 
x = 5
y ="Hello, World"

x = 5
y ="John"
print(x)
print(y)

x = 4
x ="sally"
print(x) #Biến không cần phải được khai báo với bất kỳ kiểu dữ liệu cụ thể nào và thậm chí có thể thay đổi kiểu dữ liệu sau khi đã được thiết lập.

#kiểu dữ liệu cho biến
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = "John"
# is the same as # Hai trường hợp này giống nhau
x = 'John'

a=4   # hiển thị  4
A="Sally" # hiển thị Sally

#các biến hợp lệ
#Tên biến phải bắt đầu bằng một chữ cái hoặc ký tự gạch dưới
"""Tên biến không thể bắt đầu bằng số
Tên biến chỉ có thể chứa các ký tự chữ và số và dấu gạch dưới (Az, 0-9 và _)
Tên biến phân biệt chữ hoa chữ thường (age, Age và AGE là ba biến khác nhau)
Tên biến không thể là bất kỳ từ khóa Python nào """
myvar = "John" 
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Nhiều giá trị cho biến
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Một Giá Trị Cho Nhiều Biến
X = Y = z = "hi"
print(x)
print(y)
print(z)

#giải nén các biến 
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

##Biến đầu ra
x ="một"
print(x)

x ="một"
y ="hai"
z ="ba"
print(x, y, z)