## Python Tuples (Bộ Python)
#  tuple là một tập hợp được sắp xếp và không thể thay đổi .
# Tuple cho phép các giá trị trùng lặp:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple) #('apple', 'banana', 'cherry', 'apple', 'cherry')
# Độ dài của Tuple len()
thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) # 3

# Tạo Tuple Với Một Mục
thêm dấu phẩy sau phần tử đó, nếu không Python sẽ không nhận dạng được đó là một tuple.
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# <class 'tuple'>
 #<class 'str'>
# tuple có thể thuộc bất kỳ kiểu dữ liệu nào:

# kiểu() <class'tuple'>
 
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])  # banana

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) # lấy 2 đến 4

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4]) # lấy 0 đến 3

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:]) # lấy từ 2 đến cuối

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1]) # lấy từ -4 đến -2

#Kiểm tra xem mục có tồn tại không băngt in
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple") #Yes, 'apple' is in the fruits tuple

# Thay đổi giá trị Tuple
Chuyển đổi tuple thành danh sách để có thể thay đổi nó:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x) # thay vị trí số 1 bằng kiwi rồi in ra

# Thêm các mục
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y) # thêm cam vào danh sách

#  Thêm tuple vào tuple nhớ hêm dấu phẩy sau tupple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple) # thêm cam vào ds

#  xóa Tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y) # xóa táo khói ds và in ra

# Unpack Tuples (gải nén)
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red) 
# apple
# banana
# cherry

#  Sử dụng Asterisk*
Nếu số biến ít hơn số giá trị, bạn có thể thêm an *vào tên biến và các giá trị sẽ được gán cho biến dưới dạng danh sách:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red) 
#fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *red) = fruits
# print(green)
# print(yellow)
# print(red)

# Nếu dấu hoa thị được thêm vào tên biến khác ngoài tên biến trước đó, Python sẽ gán giá trị cho biến cho đến khi số giá trị còn lại bằng với số biến còn lại.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
# apple
['mango', 'papaya', 'pineapple']
cherry #

# - Vòng lặp Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# Lặp qua các số chỉ mục range()và len()
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# Sử dụng vòng lặp While sd len()
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
# Vòng lặp while
i = 1
while i < 6:
  print(i)
  i += 1 # in ra từ 1 đến 5

# break ( dừng )
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 # in ra từ 1 đến 3

# continue (tiếp tục)
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i) # 1 2 4 5 6 

#else dùngf khi điều kiện ko còn đúng nữa
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6") 

#Nối các Tuple
# dùng toán tử  +
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# Nhân
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
#count() Trả về số lần giá trị được chỉ định xuất hiện trong một tuple
#index() Tìm kiếm tuple cho một giá trị được chỉ định và trả về vị trí nơi tìm thấy giá trị đó


## Python Sets ( bộ)
# Các mục trong bộ không thể thay đổi, nhưng bạn có thể xóa mục và thêm mục mới.
thisset = {"apple", "banana", "cherry"}
print(thisset)
# Một tuple là một tập hợp được sắp xếp và không thể thay đổi .
# Không có thứ tự
# Không thể thay đổi
Sau khi tạo một bộ, bạn không thể thay đổi các mục trong bộ đó nhưng có thể xóa các mục và thêm các mục mới.
# Không được phép trùng lặp
# True và  số  cho là trùng lặp
# các mục khác tương tuư như tuple

# Truy cập mục
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

# kiểm tra true false có trong ko
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset) #true

thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset) #false

# thêm add() 
thisset.add("orange")
# Thêm Bộ update()
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# xóa set
thisset.remove("banana")
#Loại bỏ "chuối" bằng cách sử dụng discard() phương pháp: discard()
thisset.discard("banana")
# xóa ngẫu nhiên : pop()
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
# làm rồng tập hợp: clear()
thisset.clear()
# xóa hết TOÀN BỘ TẬP HỢP : del
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

# Nối các tập hợp: union() hoặc | 
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) 
print(set3) #{1, 'b', 'c', 2, 3, 'a'}

#Nối nhiều tập hợp bằng union() hoăc |
myset = set1.union(set2, set3, set4)

# Cập nhật update()
set1.update(set2)
# set1.update(set2)

# Tìm ra phaanf tử có tong cả 2: set1.update(set2)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3) # appple

# nối băng & chỉ cho nối cùng loại tập hợp vs nhau ko nối vs các loai khác nhau
set3 = set1 & set2
print(set3)

#intersection_update()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1) # apple

# tìm điểm khác difference() hoặc dùng toán tử -
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3) # {'banana', 'cherry'}

#difference_update() XÓA BÓ KO CÓ TRONG CẢ 2
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1) # {'banana', 'cherry'}

#symmetric_difference() GIỮ LẠI NHỮNG THỨ KO CÓ TRONG CẢ 2 hoặc dùng ^
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3) # {'google', 'banana', 'microsoft', 'cherry'}

# symmetric_difference_update() giữ lại thành phần  ko có trong cả 2
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)

#add() Thêm một phần tử vào tập hợp
clear() Xóa tất cả các phần tử khỏi tập hợp
copy() Trả về một bản sao của tập hợp
difference() - Trả về một tập hợp chứa sự khác biệt giữa hai hoặc nhiều tập hợp
difference_update() -= Xóa các mục trong tập hợp này cũng được bao gồm trong một tập hợp khác được chỉ định
discard() Xóa mục được chỉ định
intersection() & Trả về một tập hợp, tức là giao của hai tập hợp khác
intersection_update() &= Xóa các mục trong tập hợp này không có trong các tập hợp khác được chỉ định
isdisjoint() Trả về liệu hai tập hợp có giao nhau hay không
issubset() <= Trả về liệu một tập hợp khác có chứa tập hợp này hay không
< Trả về liệu tất cả các mục trong tập hợp này có có trong các tập hợp khác được chỉ định hay không
issuperset() >= Trả về liệu tập hợp này có chứa một tập hợp khác hay không
> Trả về liệu tất cả các mục trong các tập hợp khác được chỉ định có có trong tập hợp này hay không
pop() Xóa một phần tử khỏi tập hợp
remove() Xóa phần tử được chỉ định phần tử
symmetric_difference() ^ Trả về một tập hợp với các hiệu đối xứng của hai tập hợp
symmetric_difference_update() ^= Chèn các hiệu đối xứng từ tập hợp này và một tập hợp khác
union() | Trả về một tập hợp chứa hợp của các tập hợp
update() |= Cập nhật tập hợp với hợp của tập hợp này và các tập hợp khác

#Python Dictionaries (từ điển)
# Truy cập mục
Lấy giá trị của khóa "model":

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"] # Mustang

 Cách khác; get()
Lấy giá trị của khóa "model":
x = thisdict.get("model")

# Tìm các từ khoá trong từ điển key()
x = thisdict.keys() #dict_keys(['brand', 'model', 'year'])

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change
#dict_keys(['brand', 'model', 'year'])
#dict_keys(['brand', 'model', 'year', 'color'])

# Nhận giá trị values()
x = thisdict.values()

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

# items() trả về dạng xem tương ứng
x = thisdict.items() # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

# kiểm tra xem có khóa trong từ điển ko
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# thay đổi  các mục
## đổi giá trị
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

# update() thay đổi mục
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

# thêm các mục
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# hoặc update()sẽ cập nhật từ điển với các mục từ một đối số nhất định. Nếu mục không tồn tại, mục sẽ được thêm vào.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"}) 

# Xóa các mục trong từ điển
# pop()
thisdict.pop("model")
# popitem() xóa ngẫu nhiên một mục
thisdict.popitem()
# del xóa theo khóa hoăc xóa tất
del thisdict["model"]
del thisdict
# clear() làmd rỗng
thisdict.clear() # {}

# lặp for
for x in thisdict:
  print(x)
# in tất giá trị trong  từ điển ra
for x in thisdict:
  print(thisdict[x])
# Ford
# Mustang
# 1964

# trả vè giấ trị values() của keya() hoăc items()
for x in thisdict.keys():
  print(x)

# Sao chép từ điển
# copy()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
# dict()
mydict = dict(thisdict)
print(mydict)

# Từ điển lồng nhau
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# Tạo ba từ điển, sau đó tạo một từ điển chứa ba từ điển kia:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# truy cập vào từ điển
print(myfamily["child2"]["name"]) # Tobias

# Lặp qua các từ điển lồng nhau
# Lặp qua các từ điển lồng nhau
Lặp qua các khóa và giá trị của tất cả các từ điển lồng nhau:
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

#  tóm tăts phương pháp
clear() Xóa tất cả các phần tử khỏi từ điển
copy() Trả về một bản sao của từ điển
fromkeys() Trả về một từ điển có các khóa và giá trị được chỉ định
get() Trả về giá trị của khóa được chỉ định
items() Trả về một danh sách chứa một bộ cho mỗi cặp giá trị khóa
keys() Trả về một danh sách chứa các khóa của từ điển
pop() Xóa phần tử có khóa được chỉ định
popitem() Xóa cặp khóa-giá trị được chèn cuối cùng
setdefault() Trả về giá trị của khóa được chỉ định. Nếu khóa không tồn tại: chèn khóa, với giá trị được chỉ định
update() Cập nhật từ điển với các cặp khóa-giá trị được chỉ định
values() Trả về danh sách tất cả các giá trị trong từ điển


