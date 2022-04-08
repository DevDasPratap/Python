# oldNum=input('Age')
# newNum=int(oldNum) +5
# print(newNum)


# oldStr=input('String')
# newStr=str(oldStr)
# print(newStr)
name='Pratap Das'
# print(name.lower())
# print(name.upper())
# print(name.find('a'))
# print(name.find('D'))
# print(name.find('das'))
# print(name.find('Das'))
# print(name.replace('Pratap Das', 'Hi Dev Das'))
# print('a' in name) //True/false
# print(5+2)
# print(5//2)
# print(5**2)
# i=5
# i=i+2
# print(i)
# result=2+3*5
# print(result)
# print(3<2)
# print(3>2)
# print(3==2)
# print(3!=3)
# print(3>2 or 2<3)
# print(5>2 and 2<5)


# age=10
# if age >= 18:
#   print('You r adult')
#   print('You can vote')
# elif age < 18 and age >3:
#   print('You r in school')
# else:
#   print('You are a child')
# print('Thank you')


# first=input('Enter first number: ')
# operator=input('Enter operator: +, -, /, % : ')
# second=input('Enter second number: ')
# first=int(first)
# second=int(second)
# if operator=='+':
#   print(first + second)
# elif operator=='-':
#   print(first - second)
# elif operator=='/':
#   print(first / second)
# elif operator=='%':
#   print(first % second)
# else:
#   print('Envlid enter')


# number=range(5)
# print(number)


# i=1
# while i <= 16:
#   print(i, end=' ') #print in vertically
#   #print(i)
#   i = i+1


#partten
# i=1
# while i<= 5:
#   print(i * ' *')
#   i=i+1

# i=10
# while i >= 0:
#   print(i * ' *')
#   i=i-1


# for i in range(10):
#   print(i, end=' ')


#list[], tupple(), set{}
##list
# marks=[80, 70, 91, 50, 79]
# print(marks)
# print(marks[0])
# print(marks[-4]) #reverse
# print(marks[1:4])
# marks.append(96)
# print(marks)
# marks.insert(0, 88)
# print(marks)
# for score in marks:
#   print(score, end=' ')
# print(end='\n')
# print(99 in marks)
# print(91 in marks)
# print(len(marks))
# i=0
# while i < len(marks):
#   print(marks[i], end=' ')
#   i=i+1
# print(end='\n')
# marks.clear()
# print(marks)


# students=['Pratap', 'dev', 'Devdas', 'Dipankar', 'sarkar', 'Talii']
# for student in students:
#   # if student == 'sarkar':
#   #   break
#   if student == 'Dipankar':
#     continue
#   print(student)


# #tupple
# marks=(91, 96, 88, 81, 88, 70, 81)
# print(marks.count(88))
# print(marks.index(81))


#set(duplicate remove)
# marks={91, 96, 88, 81, 88, 70, 81}
# print(marks)
# for score in marks:
#   print(score, end=' ')


##Dictionary
# marks={'cpp': 91, 'Html': 90, 'css': 88, 'JavaScript':96}
# print(marks['cpp'])
# marks['NodeJs']= 91
# print(marks)
# marks['JavaScript']=99
# print(marks)


##function
#inbuld function: int(), str(), bool()
#Module function: ex=> import math

# import math
# print(dir(math))

# from math import sqrt
# print(sqrt(16))

#User define function
def sum(first, second):
  print(first + second)
sum(5, 2)
