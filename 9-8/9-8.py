# RegEx (Biểu thức chính quy Python)
RegEx hay Biểu thức chính quy là một chuỗi ký tự tạo thành một mẫu tìm kiếm.
RegEx có thể được sử dụng để kiểm tra xem một chuỗi có chứa mẫu tìm kiếm đã chỉ định hay không.
# Mô-đun RegEx
import re
Vd:
import re
#Check if the string starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")

>> YES! We have a match!

# Hàm RegEx
findall Trả về danh sách chứa tất cả các kết quả khớp
search Trả về đối tượng Match nếu có kết quả khớp ở bất kỳ đâu trong chuỗi
split Trả về danh sách trong đó chuỗi đã được chia tách tại mỗi kết quả khớp
sub Thay thế một hoặc nhiều kết quả khớp bằng một chuỗi

# Siêu ký tự
- Một tập hợp các ký tự viết chữ thường "[a-m]" 
import re
txt = "The rain in Spain"
#Find all lower case characters alphabetically between "a" and "m":
x = re.findall("[a-m]", txt)
print(x)
>> ['h', 'e', 'a', 'i', 'i', 'a', 'i']

- Báo hiệu một chuỗi ký tự đặc biệt ( là số)(cũng có thể được sử dụng để thoát khỏi các ký tự đặc biệt) "\d"
import re
txt = "That will be 59 dollars"
#Find all digit characters:
x = re.findall("\d", txt)
print(x)
>> ['5', '9']

- Bất kỳ ký tự nào (trừ ký tự xuống dòng) "he..o"
import re
txt = "hello planet"
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
x = re.findall("he..o", txt)
print(x)
>> ['hello'] # #Tìm kiếm một chuỗi bắt đầu bằng "he", theo sau là hai ký tự (bất kỳ) và một chữ "o":

- Bắt đầu bằng "^hello"
import re
txt = "hello planet"
#Check if the string starts with 'hello':
x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")
>> Yes, the string starts with 'hello' # ktra xem  chuỗi bắt đầu bằng 'hello'

- Kết thúc bằng "planet$"
import re
txt = "hello planet"
#Check if the string ends with 'planet':
x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match") # Yes, the string ends with 'planet' # ktra xem chuỗi bắt bằng planet hay ko

- Không có hoặc nhiều lần xuất hiện "he.*o"
import re
txt = "hello planet"
x = re.findall("he.*o", txt) # ['hello'] # Tìm kiếm một chuỗi bắt đầu bằng "he", theo sau là 0 hoặc nhiều ký tự (bất kỳ) và một chữ "o":
print(x)

- Một hoặc nhiều lần xuất hiện "he.+o"
import re
txt = "hello planet"
x = re.findall("he.+o", txt)
print(x)  # ['hello'] # #Tìm kiếm một chuỗi bắt đầu bằng "he", theo sau là 1 hoặc nhiều ký tự (bất kỳ) và một chữ "o":

- Không hoặc một lần xuất hiện "he.?o"
import re
txt = "hello planet"
x = re.findall("he.?o", txt)
print(x) # [] # #Tìm kiếm một chuỗi bắt đầu bằng "he", theo sau là 0 hoặc 1 (bất kỳ) ký tự và "o":
# Lần này chúng ta không tìm được kết quả nào trùng khớp, vì không có số không, không phải một, mà là hai ký tự giữa "he" và "o".

- Chính xác số lần xuất hiện đã chỉ định "he.{2}o"
# import re

txt = "hello planet"
#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":
x = re.findall("he.?o", txt)
print(x)
#This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"

- Hoặc "falls|stays"
import re
txt = "hello planet"
#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
x = re.findall("he.{2}o", txt)
print(x) # ['hello']

- Chụp và nhóm

# Chuỗi đặc biệt
\A Trả về kết quả khớp nếu các ký tự được chỉ định ở đầu chuỗi "\AThe"
\b Trả về kết quả khớp khi các ký tự được chỉ định ở đầu hoặc cuối một từ
(ký tự "r" ở đầu đảm bảo rằng chuỗi được coi là "chuỗi thô") r"\bain"

r"ain\b"

\B Trả về kết quả khớp khi các ký tự được chỉ định có mặt, nhưng KHÔNG ở đầu (hoặc cuối) của một từ
(ký tự "r" ở đầu đảm bảo rằng chuỗi được coi là "chuỗi thô") r"\Bain"

r"ain\B"

\d Trả về kết quả khớp khi chuỗi chứa các chữ số (các số từ 0-9) "\d"
\D Trả về kết quả khớp khi chuỗi KHÔNG chứa các chữ số "\D"
\s Trả về kết quả khớp khi chuỗi chứa ký tự khoảng trắng "\s"
\S Trả về kết quả khớp khi chuỗi KHÔNG chứa ký tự khoảng trắng "\S"
\w Trả về kết quả khớp trong đó chuỗi chứa bất kỳ ký tự từ nào (ký tự từ a đến Z, chữ số từ 0-9 và ký tự gạch dưới _) "\w"
\W Trả về kết quả khớp trong đó chuỗi KHÔNG chứa bất kỳ ký tự từ nào "\W"
\Z Trả về kết quả khớp nếu các ký tự được chỉ định nằm ở cuối chuỗi "Spain\Z"

# Bộ
[arn] Trả về kết quả khớp khi có một trong các ký tự được chỉ định (a, r hoặc n)
[a-n] Trả về kết quả khớp cho bất kỳ ký tự thường nào, theo thứ tự bảng chữ cái giữa a và n
[^arn] Trả về kết quả khớp cho bất kỳ ký tự nào TRỪ a, r và n
[0123] Trả về kết quả khớp khi có bất kỳ chữ số nào được chỉ định (0, 1, 2 hoặc 3)
[0-9] Trả về kết quả khớp cho bất kỳ chữ số nào giữa 0 và 9
[0-5][0-9] Trả về kết quả khớp cho bất kỳ số có hai chữ số nào từ 00 đến 59
[a-zA-Z] Trả về kết quả khớp cho bất kỳ ký tự nào theo thứ tự bảng chữ cái giữa a và z, chữ thường HOẶC chữ hoa
[+] Trong các tập hợp, +, *, ., |, (), $,{} không có ý nghĩa đặc biệt, do đó [+] có nghĩa là: trả về kết quả khớp cho bất kỳ ký tự + nào trong chuỗi

# Hàm findall()
In danh sách tất cả các kết quả khớp:
import re
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x) # ['ai', 'ai']

Trả về danh sách trống nếu không tìm thấy kết quả khớp:
import re
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)  
>> 
[]
No match

# Hàm search()
import re
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

# Thực hiện tìm kiếm nhưng không có kết quả nào khớp:

# Nếu không tìm thấy kết quả khớp, giá trị Nonesẽ được trả về:
import re
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x) # None

# Hàm này split()trả về một danh sách trong đó chuỗi đã bị chia tách tại mỗi lần khớp:
Ví dụ
Tách tại mỗi ký tự khoảng trắng:
import re
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x) # ['The', 'rain', 'in', 'Spain']

# Bạn có thể kiểm soát số lần xuất hiện bằng cách chỉ định tham maxsplit số:
Ví dụ
Chỉ tách chuỗi ở lần xuất hiện đầu tiên:
import re
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
>>
['The', 'rain in Spain']

# Hàm sub()
Chức năng này sub()thay thế các kết quả khớp với văn bản bạn chọn:
Ví dụ
Thay thế mọi ký tự khoảng trắng bằng số 9:
import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x) # The9rain9in9Spain

Bạn có thể kiểm soát số lần thay thế bằng cách chỉ định tham count số:
Ví dụ
Thay thế 2 lần xuất hiện đầu tiên:
import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x) # The9rain9in Spain


# Đối tượng phù hợp
Thực hiện tìm kiếm sẽ trả về Đối tượng phù hợp:
import re
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object
>> <_sre.SRE_Match object; span=(5, 7), match='ai'>

# .span()trả về một bộ chứa vị trí bắt đầu và kết thúc của sự khớp.
# .stringtrả về chuỗi được truyền vào hàm
# .group()trả về phần của chuỗi có sự khớp
Ví dụ
In ra vị trí (vị trí bắt đầu và kết thúc) của lần khớp đầu tiên.
Biểu thức chính quy tìm kiếm bất kỳ từ nào bắt đầu bằng chữ "S" viết hoa:
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span()) # (12, 17)

 VD: In chuỗi được truyền vào hàm:
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string) # The rain in Spain

# In ra phần chuỗi có sự trùng khớp.
Biểu thức chính quy tìm kiếm bất kỳ từ nào bắt đầu bằng chữ "S" viết hoa:
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group()) # Spain

## PIP
Điều hướng dòng lệnh đến vị trí thư mục tập lệnh của Python và nhập lệnh sau:
Ví dụ
Kiểm tra phiên bản PIP:
C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip --version

# Nhập gói "camelcase" vào dự án của bạn.
Viết hoa chữ cái đầu tiên
import camelcase
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt)) # Lorem Ipsum Dolor Sit Amet

# Gỡ cài đặt gói có tên "camelcase":
C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip uninstall camelcase
Trình quản lý gói PIP sẽ yêu cầu bạn xác nhận rằng bạn muốn xóa gói camelcase:
Uninstalling camelcase-02.1:
  Would remove:
    c:\users\Your Name\appdata\local\programs\python\python36-32\lib\site-packages\camelcase-0.2-py3.6.egg-info
    c:\users\Your Name\appdata\local\programs\python\python36-32\lib\site-packages\camelcase\*
Proceed (y/n)?

#Sử dụng listlệnh để liệt kê tất cả các gói được cài đặt trên hệ thống của bạn:
C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip list
Kết quả:
Package         Version
-----------------------
camelcase       0.2
mysql-connector 2.1.6
pip             18.1
pymongo         3.6.1
setuptools      39.0.1

# Thử ngoại trừ
try cho phép bạn kiểm tra lỗi của một khối mã.
except cho phép bạn xử lý lỗi.
else cho phép bạn thực thi mã khi không có lỗi.
finally cho phép bạn thực thi mã, bất kể kết quả của khối try và except.

# Xử lý ngoại lệ
Khối này try sẽ tạo ra một ngoại lệ vì xkhông được xác định:
try:
  print(x)
except:
  print("An exception occurred")
>> An exception occurred
Vì khối try gây ra lỗi nên khối except sẽ được thực thi.
Nếu không có khối try, chương trình sẽ bị sập và đưa ra lỗi:
Ví dụ
Câu lệnh này sẽ gây ra lỗi vì xkhông được định nghĩa:
print(x) 
>>
Traceback (most recent call last):
  File "demo_try_except_error.py", line 3, in <module>
    print(x)
NameError: name 'x' is not defined

# Nhiều ngoại lệ
In một thông báo nếu khối thử đưa ra lỗi a NameErrorvà một thông báo khác cho các lỗi khác:
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
>> Variable x is not defined

#Khác
Bạn có thể sử dụng elsetừ khóa để xác định khối mã sẽ được thực thi nếu không có lỗi nào được phát hiện:
Ví dụ
Trong ví dụ này, trykhối không tạo ra bất kỳ lỗi nào:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
>> 
Hello
Nothing went wrong

# Cuối cùng
Khối này finally, nếu được chỉ định, sẽ được thực thi bất kể khối thử có phát sinh lỗi hay không.
Ví dụ
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
>>
Something went wrong
The 'try except' is finished

# Hãy thử mở và ghi vào một tệp không thể ghi:
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
>> Something went wrong when writing to the file

# Đưa ra một ngoại lệ
Đưa ra lỗi và dừng chương trình nếu x nhỏ hơn 0
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")
>>
Traceback (most recent call last):
  File "demo_ref_keyword_raise.py", line 4, in <module>
    raise Exception("Sorry, no numbers below zero")
Exception: Sorry, no numbers below zero

# Đưa ra lỗi TypeError nếu x không phải là số nguyên:
x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")
>> Traceback (most recent call last):
  File "demo_ref_keyword_raise2.py", line 4, in <module>
    raise TypeError("Only integers are allowed")
TypeError: Only integers are allowed

# Input
username = input("Enter username:")
print("Username is: " + username)
>> Enter username:

# String Formatting Định dạng chuỗi Python
# Dây F
txt = f"The price is 49 dollars"
print(txt) # The price is 49 dollars

# Trình giữ chỗ và Trình sửa đổi
Thêm chỗ giữ chỗ cho pricebiến:
price = 59
txt = f"The price is {price} dollars"
print(txt) # The price is 59 dollars

# Hiển thị giá trị 95có 2 chữ số thập phân:
txt = f"The price is {95:.2f} dollars"
print(txt) # The price is 95.00 dollars







