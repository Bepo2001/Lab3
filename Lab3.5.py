x=int(input("Enter a number of repetitions"))
def announce(f):
       def wrapper():
              for i in range(x):
                     f()

       return wrapper
@announce
def hello():
       print ('Hello')
hello()