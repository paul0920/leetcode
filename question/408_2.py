# word = "internationalization"
# abbr = "i12iz4n"
#
# word = "apple"
# abbr = "a2e"
#
# word = "a"
# abbr = "2"
#
word = "hi"
abbr = "h2"
#
# word = "hi"
# abbr = "2i"
#
# word = "word"
# abbr = "w0ord"
#
# word = "abbreviation"
# abbr = "a10n"
#
# word = "internationalization"
# abbr = "i5a11o1"

i = 0
n = "0"

print len(word)
print ""

for c in abbr:

    if c.isdigit():

        # Handle the case such as "w0ord"
        if c == n:
            print False
            exit()

        else:
            n += c

    else:

        n = int(n)

        print "i:", i, "n:", n

        i += n

        print "i:", i, "n:", n

        # Remember to have "=" since i can be out of index
        if i >= len(word) or word[i] != c:
            print False
            exit()

        i += 1
        n = "0"

        print ""

# Remember to have "int(n)" since the last element of
# abbr can be a number
print i + int(n) == len(word)
