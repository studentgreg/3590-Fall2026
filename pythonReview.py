message = "Welcome to Internship Ready"
print(message)
print(type(message))
print(type(3),type(3.14),type(True),type(False))
print("greg","reis",sep="-")
print("greg","reis",sep="")
print(type(3==6/2))
print("You say 'goodbye'")
print('And I say "hello"')
first_name = "Greg"
last_name = "Reis"
print(first_name,last_name)
print(first_name + " " + last_name)
print("FIU" " is " "61 years old")
print(True + True)

a = 3
b = 10
print(a+b) # addition
print(b-a) # subtraction
print(a*b) # multiplication
print(b/a) # division
print(b//a) # floor division
print(a**b) # exponentiation ^
print(-10//3)
print(b%a) # modulo - remainder of the division of 10 by 3
print(-10%3) # -10/3 = -3.33 => -4 * 3 = -12, then
# -10 - (-12) = 2
print(2 ^ 10) # 0010 XOR 1010 = 1000

x= 3
print(1 < x < 10)

professors = ["whittaker","xian","kianoosh","mustafa","sergio","patricia"]
print(professors[0]) # first element
print(professors[-1]) # last element
print(professors[1:3]) # from index 1 to index 2
print(professors[3:]) # from index 3 to end
print(professors[:5]) # from beginning to index 4
print(professors)
print(professors[:])
print(professors[::-1])

professors.append("debra")
print(professors)
professors.extend(["rita","todd"])
print(professors)
professors.insert(2,"greg") # insert allows you to include the index
print(professors)
professors[3] = "nestor"
print(professors)
professors.remove("mustafa")
print(professors)
prof=professors.pop(1)
print(prof,professors)
professors.append("patricia")
print(professors)
print(professors.count("patricia"))
professors.reverse()
print(professors)
professors.sort(reverse=True)
print(professors)

faculty = professors.copy()

print(professors)
print(faculty)
faculty.append("greg")
print(professors)

print("nestor" in professors)

p = [1,2,3]
q = [1,2,3]
print(p is q)
print(p == q)

m = 5
n = 5
print(m is n)
print(m == n)

t = 50000
r = 50000
print(t is r)
print(t == r)

# any number until 256 will be cached and considered the same
# any number above 256 will be considered different

for i in professors:
    if len(i) > 4:
        print(i.upper())
    else:
        print(i.lower())

# Dictionaries, Pandas Dataframes, Streamlit - Tuesday - Sep 8th 2026
# go.fiu.edu/ttafall2026

temperature = [89.2, 92.3, 90.7]
date = ["09/02/2025", "09/03/2025", "09/04/2025"]
odo = [6.14, 6.7, 7.8]

water_data = {
    "temperature" : [89.2, 92.3, 90.7],
    "date" : ["09/02/2025", "09/03/2025", "09/04/2025"],
    "odo" : [6.14, 6.7, 7.8]
}

print(water_data)
print(water_data["temperature"][0])
print(water_data.keys())

import pandas as pd

df = pd.DataFrame(water_data)
print(df)