# strings
course = 'Python Programming'
print(len(course))
print(course[0])
print(course[-1]) # end of the string
print(course[0:3])
print(course[0:])
print(course[:3])
print(course[:])

course = 'Python \"Programming' # escape character
course = 'Python \nProgramming' # new line
print(course)

first = 'Mohammed'
last = 'Mubarak'
full = first + ' ' + last
print(full)
full = f"{first} {last}"
print(full)

course = 'Python Programming'
print(course.upper()) # with '.' after a function we can find available methods
print(course) # the original not effected
print(course.lower())
print(course.title())
print(course.strip()) # trim the space end and starting
print(course.find('pro'))
print(course.replace('P', 'j'))
print('Pro' in course) # True
print('Pro' not in course) # False

