import sys

# sys.argv is a variable that is a list of all the things you've typed, separated by spaces, in the command line after 'python'
# In the following case, if you type in 'python 5_command_line_arguments.py Ollie', the list returned will be: ["5_command_line_arguments.py", "Ollie"]
# If you don't add something after the file name, you'll get an IndexError
# sys.exit exits out of the program and prints out what's in the parentheses if it's a string (it's got other possible actions depending on the parameter)

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print(f"Hello, my name is {arg}")