# __author__ = 'Cai'

end=1000

sum = 0
for i in range(1,end):
    if i % 3 == 0 or i % 5 ==0 :
        sum += i
        print i
print sum