from typing import Union;
from types import FunctionType;

def TypeValidator(*AcceptedTypes: str):
   """
   Enter the accepted "types" of arguments your target function accepts. E.G.: 'str' (string), 'bool' (boolean), 'int' (integer).
   
   You can store the TypeValidator inside a variable like this:
   variableName = TypeValidator('str', 'float', 'int') and your type validator will see if the arguments inside your TargetFunction (below) match these types. This may be important if, say, your TargetFunction is a function that adds numbers. You don't want the user to enter 'False' (bool) as an argument.
   """
   acceptedTypesList = []
   for i in AcceptedTypes:
      acceptedTypesList = [*acceptedTypesList, f"<class '{i}'>"];
   
   def FunctionWrapper(TargetFunction: FunctionType, *arguments):
      """
      What you are seeing as you hover over this is the FUNCTION WRAPPER, which accepts two parameters:
      (1) The TargetFunction, written as DECLARATION (do NOT call the TargetFunction inside the ( ). THAT IS BAD... in this case).
      (2) The arguments you would normally put inside your target function when you call them. NOTE: Normally, when you call a function that takes in parameters, you put the arguments inside that function, like: myGreeting("Jamie").

      HOWEVER...

      Because you are using the TypeValidator, that argument (in this case, "Jamie") actually goes inside the SECOND PARAMETER of whatever your 'function wrapper' returns:
      def myGreeting(name): 
         #Your code logic goes here.

      MyFunctionWrapper = TypeValidator('str') #IF myGreeting accepts more than one TYPE of argument, you can put it in the TypeValidator and separate them by ",".\n
      MyGreetingWithValidator = MyFunctionWrapper(myGreeting, 'Jamie') #Note that 'Jamie' does NOT go inside myGreeting. It goes inside as the SECOND PARAMETER of MyFunctionWrapper so the TypeValidator can check to see if 'Jamie' is a 'str' (see MyFunctionWrapper).
      """
      if len(arguments) == 1:
         return TargetFunction(arguments[0]) if str(type(arguments[0])) in acceptedTypesList else f"Sorry... <class'{arguments[0]}'> is NOT in within the accepted types of {acceptedTypesList}"
      else:
         for arg in arguments:
            if str(type(arg)) not in acceptedTypesList:
               return f"Sorry... <class '{arg}'> not in {acceptedTypesList}";

         return TargetFunction(*arguments)
   return FunctionWrapper

addNumbersWithValidator = TypeValidator('int', 'float')
groceryListWithValidator = TypeValidator('list');

def addThreeNumbers(a: Union[int, float], b: Union[int, float], c: Union[int, float]):
   return a + b + c;

def greeting(name: str):
   return f"Hello, {name}. How are you?";

def groceryList(list: list):
   return list;

print(addNumbersWithValidator)
print(TypeValidator('str')(greeting, 'Jamie'))
print(addNumbersWithValidator(addThreeNumbers, 5,7, "nine"));
print(addNumbersWithValidator(addThreeNumbers, 5,7,15))
print(groceryListWithValidator(groceryList, ['apples', 'iced tea', 'roast beef', 'turkey', 'lettuce', 'iced water', 'iced coffee']));


