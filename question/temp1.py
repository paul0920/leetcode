import collections

A = [1,0,1,0,1]
S = 2

c = collections.Counter({0: 1})
psum = res = 0
for i in A:
    psum += i
    print A
    print psum
    print c
    res += c[psum - S]
    c[psum] += 1
    print ""
print res