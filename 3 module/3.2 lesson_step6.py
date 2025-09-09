from selenium import webdriver

assert abs(-42) == 42, "Should be absolute value of a number"

#Форматирование строк с помощью str.format

print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))

#Форматирование строк с помощью f-strings
str1 = "one"
str2 = "two"
str3 = "three"
print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")

s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')
