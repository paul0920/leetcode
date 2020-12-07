# The finally keyword is used in try...except blocks.
# It defines a block of code to run when the try...except...else block is final.
#
# The finally block will be executed no matter if the try block raises an error or not.
#
# This can be useful to close objects and clean up resources.


num = None
# num = 1

try:
    num *= 2
except:
    print "WRONG"
else:
    print "OK"
finally:
    print "The try...except block is finished, num: ", num

# num2 = None
#
# print num2 * 2
