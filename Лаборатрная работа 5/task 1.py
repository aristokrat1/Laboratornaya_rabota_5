from pprint import pprint
numbers = [n for n in range(0,16)]
bin = [bin(number) for number in numbers]
hex = [hex(number) for number in numbers]
oct = [oct(number) for number in numbers]
dictionaries = [dict(zip(["bin","dec","hex","oct"],[bin[number],number,hex[number],oct[number]])) for number in numbers]
pprint(dictionaries)
# TODO решить с помощью list comprehension и распечатать его
