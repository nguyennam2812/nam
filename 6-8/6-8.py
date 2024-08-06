# Giá trị Boolean
True hoặc False
print(10 > 9) # True
print(10 == 9) # False
print(10 < 9) # False

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")  #b is not greater than a
# Bất kỳ chuỗi nào cũng được True, ngoại trừ chuỗi rỗng.
# Vd chuỗi False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# một lớp có __len__hàm trả về 0hoặc False:
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))

#hàm True
def myFunction() :
  return True
print(myFunction())

#In ra "YES!" nếu hàm trả về True, nếu không thì in ra "NO!":
def myFunction() :
  return True=
if myFunction():
  print("YES!")
else:
  print("NO!")

# isinstance()
x = 200
print(isinstance(x, int))

# Toán tử Python
# Toán tử số học Python
+ cộng
- trừ
* nhân
/ chia
% Toán tử chia lấy phần dư 
** Toán tử mũ
// chia lấy phần nguyên

#Toán tử gán Python
x = 5 # x=5
x +=3 # x=x+3 hiển thị 8
x -=3 # x=x-3 
x *=3 # x=x*3
x /=3 # x=X/3
...

#toán tử so sánh
== bằng
!= ko bằng
< ; >; <=; >=

#Toán tử logic Python
and và
or hoặc
not không

# toán tử nhận dạng
is là 
is not : ko là

# Toán tử thành viên Python
 in # x in y ( x cód trong y)
not in 

# Toán tử Bitwise của Python
# Các toán tử bitwise được sử dụng để so sánh các số (nhị phân):
& and : Đặt mỗi bit thành 1 nếu cả hai bit đều là 1
OR (|): Đặt mỗi bit thành 1 nếu một trong hai bit là 1
XOR (^):Đặt mỗi bit thành 1 nếu chỉ có một trong hai bit là 1
NOT (~): Đảo ngược tất cả các bit
<< (dịch trái) :Dịch chuyển sang trái bằng cách đẩy số không vào từ bên phải và để các bit ngoài cùng bên trái rơi ra
>> (dichj phải): Dịch chuyển sang phải bằng cách đẩy các bản sao của bit ngoài cùng bên trái vào từ bên trái và để các bit ngoài cùng bên phải rơi ra

#Ưu tiên điều hành]
Trong ngoặc trc, nhân chia trc cộng trừ, trái qua phải, phép bitwise trc cọng trừ

# Danh sách python
thislist = ["apple", "banana", "cherry"]
print(thislist) #['apple', 'banana', 'cherry']
# mục đầu tiên có thứ tự từ 0, 1, 2, ...
# có thể thêm, xóa, trùng nhau

#Độ dài danh sách
# len()
thislist = ["apple", "banana", "cherry"]
print(len(thislist)) # 3
# Các mục danh sách có thể thuộc bất kỳ kiểu dữ liệu nào:
# Một danh sách có thể chứa các kiểu dữ liệu khác nhau:
# Danh sách được định nghĩa là các đối tượng có kiểu dữ liệu là 'list':
# Hàm tạo list()
# Bộ sưu tập Python (Mảng)
Có bốn kiểu dữ liệu tập hợp trong ngôn ngữ lập trình Python:

List là một tập hợp được "sắp xếp" và có thể "thay đổi". Cho phép các thành viên "trùng" lặp.
Tuple là một tập hợp được "sắp xếp" và "không thể thay đổi". Cho phép các thành viên "trùng lặp".
Set là một tập hợp "không được sắp xếp, không thể thay đổi" và "không được lập chỉ mục." "Không có thành viên trùng lặp".
Dictionary là một bộ sưu tập được "sắp xếp" và "có thể thay đổi". "Không có thành viên trùng lặp."

#Truy cập các mục danh sách
#Truy cập mục
thislist = ["apple", "banana", "cherry"]
print(thislist[1]) # banana

#Chỉ số tiêu cực 
#1đề cập đến mục cuối cùng, -2đề cập đến mục thứ hai từ cuối, v.v.
thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) #chery

#Phạm vi chỉ số
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #cherry", "orange", "kiwi 
# lấy từ 2 đến 5 lấy cả 2 và 5

# lấy từ đầu đến 4 không lấy 4
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) #['apple', 'banana', 'cherry', 'orange']

# lấy từ 2 đến cuối lấy cả 2
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) #['cherry', 'orange', 'kiwi', 'melon', 'mango']

# lấy từ -4 đến -1 lấy -4 ko lấy -1
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) #['orange', 'kiwi', 'melon']

#Kiểm tra xem mục có tồn tại không
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") #Yes, 'apple' is in the fruits list

#Thay đổi mục danh sách
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) #['apple', 'blackcurrant', 'cherry']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) #thay banana và cheery bằng blackcurrant", "watermelon ( thay 1 và 2)

#Thay đổi giá trị thứ hai bằng cách thay thế nó bằng hai giá trị mới
# Nếu bạn chèn nhiều mục hơn số mục thay thế, các mục mới sẽ được chèn vào vị trí bạn chỉ định và các mục còn lại sẽ di chuyển tương ứng:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) #['apple', 'blackcurrant', 'watermelon', 'cherry']

# Nếu bạn chèn ít mục hơn số mục thay thế, các mục mới sẽ được chèn vào nơi bạn chỉ định và các mục còn lại sẽ di chuyển tương ứng:
#Thay đổi giá trị thứ hai và thứ ba bằng cách thay thế nó bằng một giá trị:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) #['apple', 'watermelon']

# Chèn mục insert()
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) #['apple', 'banana', 'watermelon', 'cherry']

#Thêm mục danh sách append()
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) #['apple', 'banana', 'cherry', 'orange']

#Mở rộng danh sách extend()
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) #['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

#Thêm bất kỳ Iterable nào extend()
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) #['apple', 'banana', 'cherry', 'kiwi', 'orange']

#Xóa các mục danh sách remove()
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) #['apple', 'cherry']

# Xóa chỉ mục đã chỉ địnH pop()
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) # ['apple', 'cherry']
# NẾU pop() sẽ xóa mục cuối cùng

# del khóa cũng xóa chỉ mục đã chỉ định, hoặc tất cả
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) 


# clear() xóa tất
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Danh sách vòng lặp for
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
# apple
# banana
# cherry

#Lặp qua các số chỉ mục range()và len()
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i]) 
# apple
 banana
 cherry

#white
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#Một vòng lặp ngắn forsẽ in ra tất cả các mục trong danh sách:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#Dựa trên danh sách các loại trái cây, bạn muốn có một danh sách mới, chỉ chứa những loại trái cây có chữ cái "a" trong tên.
fruits =['apple', "chery", "kiwi","màngo"]
newlist =[]
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist) #['apple', 'banana', 'mango']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) #tương tự vd trên

#Giá trị trả về là một danh sách mới, giữ nguyên danh sách cũ.
newlist = [expression for item in iterable if condition == True]

#Chỉ chấp nhận các mặt hàng không phải là "apple":
newlist = [x for x in fruits if x != "apple"]

#range()hàm này để tạo một đối tượng lặp lại:
newlist = [x for x in range(10)] #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
newlist = [x for x in range(10) if x < 5] #Chỉ chấp nhận các số nhỏ hơn 5:

#viết hoa tất
newlist = [x.upper() for x in fruits]
#Đặt tất cả giá trị trong danh sách mới thành 'hello':
newlist = ['hello' for x in fruits]

#thay cam bằng chuổi
newlist = [x if x != "banana" else "orange" for x in fruits]

#Sắp xếp danh sách sort()
Sắp xếp danh sách theo thứ tự bảng chữ cái, và số
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) # ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

#Sắp xếp giảm dần, hoặc ngược bangr chữ reverse = True
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#Tùy chỉnh chức năng sắp xếp key = function
Sắp xếp danh sách dựa trên mức độ gần với 50:
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist) #[50, 65, 23, 82, 100]

#sắp xếp phân biệt chữ hoa thường
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Đảo ngược danh sách reverse()
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) #['cherry', 'Kiwi', 'Orange', 'banana']

#Sao chép danh sách list(), copy()
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#Sử dụng toán tử slice : ( để sao chép)
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#Tham gia hai danh sách'
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

#cách2
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

#c3
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

# append() thêm
# clear() xóa
# copy() sao chép
# count() Trả về số lượng phần tử có giá trị được chỉ định
# extend() Thêm các phần tử của một danh sách (hoặc bất kỳ phần tử lặp nào) vào cuối danh sách hiện tại
# index() Trả về chỉ số của phần tử đầu tiên có giá trị được chỉ định
# insert() thêm chỉ định
# pop() Xóa phần tử ở vị trí đã chỉ định
# remove() Xóa mục có giá trị được chỉ định
# reverse() Đảo ngược thứ tự của danh sách
# sort() Sắp xếp danh sách















