tbl_name = {"kanika": 7, "parul": 3, "anmol": 9}

print(sorted(tbl_name.items(), key=lambda x: x[1], reverse=True))

# importing pandas
import pandas as pd


# read text file into pandas DataFrame
# df = pd.read_csv("C:/Users/QL725WY/OneDrive - EY/Desktop/practice/delimeter.txt")


# print(df)


def remove_delimiters(delimiters, s):
    new_s = s
    count = 0
    lst = {}
    for i in delimiters:  # replace each delimiter in turn with a space
        with open(s, 'r') as file:
            data = file.read()
            if i in data:
                counter = lst.get(i)
                if counter is None:
                    lst[i] = 1
                else:
                    lst[i] = lst[i] + 1
                data1 = data.replace(i, ' \n')
        print(lst)
    return ' '.join(data1.split())


# print(remove_delimiters("@ # * : $", "C:/Users/QL725WY/OneDrive - EY/Desktop/practice/delimeter.txt"))

s = 'kanika sodhi'


def camelcase(s):
    res = ""
    res = res + s[:1].upper() + s[1:len(s)]
    return s


print(camelcase("kanika sodhi"))


def camelCase(st):
    output = ''.join(x for x in st.title() if x.isalnum())
    return output[0].lower() + output[1:]


print(camelCase("kanika sodhi"))


def to_camel_case(text):
    s = text.replace("-", " ").replace("_", " ")
    s = s.split()
    if len(text) == 0:
        return text
    return s[0] + ''.join(i.capitalize() for i in s[1:])


print(to_camel_case("kanika sodhi"))


def sum2no(num, tgt):
    n1 = 0
    n2 = len(num) - 1
    res = []
    result = 0
    while n1 < n2:
        result = num[n1] + num[n2]
        if tgt == result:
            return res.append([n1, n2])
        elif tgt > result:
            num[n2] -= 1
        elif tgt < result:
            num[n1] += 1
    return list((-1, -1))


print(sum2no([1, 4, 5, 8, 0, 8], 9))

# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("C:/Users/QL725WY/OneDrive - EY/Desktop/practice/emp.csv")
print(data)
# converting and overwriting values in column
data["name"] = data["name"].str.upper().str.title()

# display
print(data)
