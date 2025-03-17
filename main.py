# #strings in python
# my_string:str='Hello world'
# print(my_string)         #singlequote
# my_string:str="Hello world"   #double quote
# print(my_string) 
# my_string:str='''Hello      
# world'''    #triple quote
# print(my_string) 
# my_string: str = r'Hello\t,\n Worl\\d!'
# print(my_string)   #raw string

# #unicode character
# print(r"\u0041 = ", "\u0041")
# print(r"\u0042 = ", "\u0042")
# print(r"\u0043 = ", "\u0043")


# #upper &lower case
# name:str="Shazia Nasir"
# print(name.upper())
# print(name.lower())

# # split
# print(name.split())
# print(name.split("z"))

# join
# #%operator
# name:str="Shazia"
# first_letter:str=name[0]
# age:int=48
# weight:float=58.2
# my_data='''My name is %s, first letter of my name is \'%c\', I am %d years old and my weight id %f Kg.''' % (name,
#  first_letter, age, weight)
# print(my_data)

#fstring
# name:str="Shazia"
# age:int=48
# print(f"My name is{name}and my age is{age}")

# type casting
#1.implicit casting
num_int: int = 10
num_float = num_int + 5.5  # int + float = float. skipped type hint to see what data type is assigned at runtime
print(num_float, type(num_float))

num_str = "100"
num_int = 5

print(int(num_str) + num_int)

#explicit casting
num_float: float = 9.8
num_int = int(num_float) # skipped type hint to see what data type is assigned at runtime
print(num_int, type(num_int))
