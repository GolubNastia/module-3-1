calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    a = len(string), string.upper(), string.lower()
    return a


print(string_info('Capybara'))
print(string_info('Armageddon'))

def is_contains(string , list_to_search):
    count_calls()
    a = string.lower()
    b = [i.lower() for i in list_to_search]
    if a in b:
        return (True)
    else:
        return (False)


print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)




