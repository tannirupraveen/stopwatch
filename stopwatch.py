import time

def stopwatch():

print("Simple Stopwatch") print("Press 'Enter' to start/stop the stopwatch and 'r' to reset.") print("Press 'q' to quit.\n")

running False

start time=0

elapsed time=0

while True:

user input input("Command: ").lower()

if user input = '': if not running:

#Start the stopwatch running True start time time.time() elapsed_time print("Stopwatch started.")

else:

#Stop the stopwatch

running False elapsed time time.time() start time

print(f Stopwatch stopped. Elapsed time: (elapsed_time:.2f}

seconds.")

elif user_input = 'r':

#Reset the stopwatch

running False

start time=0

elapsed time = 0 print("Stopwatch reset.")

elif user input = 'q": #Quit the stopwatch

print("Exiting stopwatch. Goodbye!")

break

else:

print("Invalid command. Use 'Enter' to start/stop, 'r' to reset, 'q' to

quit.")

if_name_main__":

stopwatch()