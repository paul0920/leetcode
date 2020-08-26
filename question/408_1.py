# This code handles lots of edge cases manually,
# not a good strategy by converting abbr into
# alphabets and numbers into a list


# word = "internationalization"
# abbr = "i12iz4n"

# word = "apple"
# abbr = "a2e"

word = "a"
abbr = "2"

word = "hi"
abbr = "h2"

word = "hi"
abbr = "2i"

word = "word"
abbr = "w0ord"

# word = "abbreviation"
# abbr = "a10n"

n = 0
arr = []

for i in range(len(abbr)):

    if not abbr[i].isdigit():
        if i == 0:
            arr.append(abbr[i])

        else:
            if n != 0:
                arr.append(str(n))
                n = 0

            # Process the case with "0" between alphabets
            elif abbr[i - 1] == '0':
                print False
                exit()

            arr.append(abbr[i])

    else:

        if i == 0:
            n = int(abbr[i])
            if len(abbr) == 1:
                arr.append(str(n))
                n = 0

        else:
            if abbr[i - 1].isdigit():

                # Process the case with "01"
                if abbr[i - 1] == '0':
                    print False
                    exit()

                n = n * 10 + int(abbr[i])

            else:
                n = int(abbr[i])

if n != 0:
    arr.append(str(n))

print arr

if len(arr) > len(word):
    print False
    exit()

# Process the case such as
# word = "a"
# abbr = "2"
if len(word) == 1:
    if word[0] != abbr[0] and arr[0] != "1":
        print False
        exit()

j, k = 0, 0

while j < len(word) and k < len(arr):

    if not arr[k].isdigit():

        if arr[k] != word[j]:
            print False
            exit()

    else:
        j += int(arr[k]) - 1

    k += 1
    j += 1

print j == len(word) and k == len(arr)
