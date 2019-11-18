#Noah Wehner
#integration project
name = input("whats your name?")
age = input("whats your age?")
print("welcome", name,"You are", age, "years old")
#greeting code
print("welcome to a simple integration project but answer this simple question ")
answer = input("what is 2 + 2 = ")
#simple calculations
if ( answer == "4"):
    print("correct!")
else:
    print("That's the wrong numberrrrr")
#standard conditional structure
mystr = "123"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
mytuple = ("3", "2", "1")

for x in mytuple:
  print(x)
#iterative structures
def my_function(fun):
  print( " It's cold " + fun)

my_function("Outside")
my_function("Inside")
my_function("Everywhere")
#function

def my_function(colors):
  for x in colors:
    print(x)

colors = ["blue", "Old Gold", "White"]

my_function(colors)
#passing parameters
