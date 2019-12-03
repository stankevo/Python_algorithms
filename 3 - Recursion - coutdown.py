def countdown(x):
    if x == 0:
        print('Done!')
        return
    else:
        print(x, '...')
        countdown(x-1)

# check how the call stack is unwounded
def countdown2(x):
    if x == 0:
        print('Done!')
        return
    else:
        print(x, '...')
        countdown2(x-1)
        print('foo') # the return statement well return us to this place


countdown(5)
print('\ncheck how the call stack is unwounded')
countdown2(5)