#PUNEET GOYAL
# 1. DONE THAT.
print('Question 1. ','DONE',sep='\n')
# 2.
print("Question 2.")

print(5**9)
print(3//2)
print(7//3)
print(7/3)
print(6==6)

a = 20
a += 30
a %= 3;
print(a)
print(True*False)
print(True&False)
print(True and False)
print(((6>3) and (7<4) or (18==3)) and (9>3))
print(True is False)
print('False' in 'False')Tec
print(((True == False) or (False > True)) and (False <= True))


#3.
print('Question 3.')
s1 = "Nice to have it"
s2 = "here"
print(s1+' '+s2)

#4.
print('Question 4.')
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2][0])

#5.
print('Question 5.')
s1 = "Nice to have it"
s2 = "here"
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
a.insert(0,s1)
a.append(s2)
print(a)


#6.
print('Question 6. ')
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))

#7.
print('Question 7. ')
import string
s = input("Enter a string: ")
alp = set(string.ascii_lowercase)
if((set(s) - alp) == True):
    print("Anagram",end="\n\n")
else:
    print("Not Anagram",end="\n\n")

#8.
print('Question 8. ')
print(eval("{0}+{0}{0}+{0}{0}{0}".format(int(input("Enter a number: ")))))


#9.
print('Question 9. ')
s = input("Enter a sequence of words: ")
print(','.join(sorted(s.split(','))))


#10.
print('Question 10. ')
d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'],'Marks': [57,87,67,79]}
print(d['Student'][d['Marks'].index(max(d['Marks']))])
