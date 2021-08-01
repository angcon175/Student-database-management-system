'''a = input("Hey,Whats your name?")
print(f'Hello {a}')'''

'''a = input("Hey,Whats your name?")
print('Hello ' + a )'''

'''def add(first,sec):
    return first+sec

de = int(input ('Enter first Number'))
du = int (input ('Enter Second Number'))
sum = (add(de,du))

print(f'{sum}')'''

'''doc_list = ['Angcon','Joyeta','Rina','Tapas']
l2 = list()
doc_list.append('Anjan')
doc_list.remove('Anjan')
print(doc_list)'''

'''
A = int(input("Whats your mark?"))
def show_grade(grade):
    print(f'You got {grade}')
if A>=80:
    show_grade('A+')
elif A<80 and A>=70:
    show_grade('A')
'''
'''
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
A = int(input("Put your number : "))
print(is_even(A))
'''

'''list = [Kukur, Goru, Sagol, Bolod, Pada]
list1 = [2, 9, 19, 4, 27]
tot = sum(list)
print(tot)'''

'''import math
def is_prime(num):
    if int(math.sqrt(num)) % 2 == 0:
        print('This is not a Prime.')
    else:
        print('This is a Prime number')

A = int(input("Enter your number: "))
is_prime(A)'''

'''class animal():
    def __init__(self,name):
        self.Name = name

def getattr(self):
    return self.Nam

'''

'''for x in range(2,11):
    print(1/x)'''


def getMissingNo(A):
    n = len(A)
    total = (n + 1) * (n + 2) / 2
    sum_of_A = sum(A)
    return total - sum_of_A


# Driver program to test the above function
A = [1, 2, 3, 5, 6]
miss = getMissingNo(A)
print(miss)







































