def run(runfile):
    with open(runfile, "r") as rnf:  # to run the file
        exec(rnf.read())

print('What month were you born? (1-12)')
month = {'1': 'January', '2': 'February',
             '3': 'March', '4': 'April',
             '5': 'May', '6': 'June', '7': 'July',
             '8': 'August', '9': 'September',
             '10': 'October', '11': 'November',
             '12': 'December'}
month = (month.get(input()))


print('What day?')
day = (int(input('>')))

print('What year?')
year = (int(input('>')))
myAge = int(2017 - year)
print(f'So you were born {month}, {day}, {year}?')

newage = (myAge + 1)

while True:
    answer = input('Is this correct? (y/n):')
    if answer in ('y', 'n'):
        break
    print('Try again.')
    continue
if answer == 'y':
        print('You are', myAge)

if (myAge >= 1) and (myAge <= 200):
    print('\nYou will be', newage, 'on this day in one human year.')
if (myAge > 17) and (myAge <= 60):
    print('You are an adult!')
elif (myAge >= 60) and (myAge <= 200):
    print('You are old!')
elif (myAge <= 17) and (myAge >= 13):
    print('You are a teenager.')
elif (myAge >= 4) and (myAge < 13):
    print('You are a child..')
elif (myAge >= 2) and (myAge < 4):
    print('You are a toddler.')
if (myAge <= 1) and (myAge > 0):
    print('You are a baby!!')
if (myAge < 0) and (myAge > 200):
    print('How can', myAge, 'be your age?')

if answer == 'n':
    run('birth.py')

