year = input('please enter the year of your birth: ')
# make sure the input is a string, and within the last 120 years
while year.isnumeric() == False or int(year) <= 1900:
    print('please enter a valid year')
    year = input('please enter the year of your birth: ')

print('Great. You are in year ' + str(2022-int(year)))