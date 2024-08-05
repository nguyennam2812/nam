#Python Strings ( chuỗi python)
#Strings(dây)
print("hello")
Prin('hello') # hai hàm này hiển thị giống nhau

#Trích dẫn bên trong 
print("It's is alright") # It's is alright
print('He is call"Joh"') # He is call "Joh"
print("he is 'John'")   #  He is 'Joh' 

# gán chuối cho biến 
a="Hello"
print(a)

#Chuỗi đa dòng
a = """Lorem ipsum dolor sit amet,      
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
# Hiển thị 
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua. 

# Chuổi là mảng
#Lấy ký tự ở vị trí 1 (hãy nhớ rằng ký tự đầu tiên có vị trí 0):
a = "Hello, World!"
print(a[1]) # Hiển thị chữ "e" trong cụm từ "Hello"

#vòng lặp chuỗi
for x in "banana":
    print(x)
#Hiển thị
b
a
n
a
n
a

#Chiều dài chuỗi dùng len()
a ="Hello, World"
print(len(a)) #hiển thị 13

#Kiểm tra chuỗi
txt ="The best things in life are free"
pritn("free" in txt) # nếu có Hiển thị "TRue" ko có "False"

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
# hiển thi(Yes, 'free' is present.)

# kiểm tra cụm từ nào đó có không trong đoạn văn not in
txt = "The best things in life are free!"
print("expensive" not in txt)
# Hiển thị true

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
# Hiển thị No, 'expensive' is NOT present.

#Python - Slicing Strings
#Slicing 
b ="Hello, World"
print(b[2:5]) #Lấy các ký tự từ vị trí khoảng (2:5)
# hiển thị( llo ) 

b ="Hello, World!"
print(b[:5])  #Lấy các ký tự từ khoảng (0:5)
# hiển thi( Hello )

b ="Hello, World!"
print(b[2:]) #Lấy các ký tự từ vị trí thứ [2 cho đến hết:

#chỉ số tiêu cực
b = "Hello, World!"
print(b[-5:-2]) # orl
#Nhận các ký tự:
#Từ: "o" trong "World!" (vị trí -5)
#Đến, nhưng không bao gồm: "d" trong "World!" (vị trí -2):

# Sửa đỗi chuỗi
# Chữ in hoa "upper()"
a = "Hello, World!"
print(a.upper())
