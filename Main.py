myString = "Different Hello"
print(myString[::-1]) #odwrócenie napisu

name = "Sam"
last_letters = name[1:]
print('P' + last_letters)
x = "Hello World"
x = x.upper()
print(x)
x = x.split()
print(x)
print('Hello {}'.format('Kuba'))
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

# zaokraglanie liczb {value:width.precision f}

result = 100/777
print("The result was {r:1.3f}".format(r = result))
my_list = ['one','two','three']
my_list.append('four')
print(my_list)

#dictionaries

prices_lookup = {'apple': 3,'oranges': 5.5, 'milk': 1.99, 'list': [0,1,2,'c']}
print(prices_lookup['apple'])
print(prices_lookup['list'])
print(prices_lookup['list'][3].upper())
prices_lookup['int'] = 3
print(prices_lookup)

#importowanie i otwieranie plikow

with open('mytxtFile') as myFile:
    content = myFile.read()
print(content)

with open('mytxtFile',mode='a') as f:
    f.write('\nSecond Line')
with open('mytxtFile', mode='r') as f:
    print(f.read())
with open('file', mode='w') as d:
    d.write("To jest nowy Dokument")
with open('file', mode='r') as d:
    print(d.read())





