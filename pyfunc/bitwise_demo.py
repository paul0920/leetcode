
a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
c = 0

c = a & b         # 12 = 0000 1100
print "Line 1(AND) - Value of c is ", c

c = a | b         # 61 = 0011 1101
print "Line 2(OR)  - Value of c is ", c

c = a ^ b         # 49 = 0011 0001
print "Line 3(XOR) - Value of c is ", c

# The bitwise inversion of a is defined as -(a + 1)
# It only applies to integral numbers.
c = ~a            # -61 = 1100 0011
print "Line 4(complement) - Value of c is ", c

c = a << 2        # 240 = 1111 0000
print "Line 5(left shift) - Value of c is ", c

c = a >> 2        # 15 = 0000 1111
print "Line 6(right shift) - Value of c is ", c
