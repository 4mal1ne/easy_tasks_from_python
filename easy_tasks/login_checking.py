user_login = input('Enter your login: ')

if user_login and len(user_login) <= 15:
    user_password = input('Enter your password: ')
    if user_password and len(user_password) <= 20:
        print(f'Welcome, {user_login}!!!')
    elif len(user_password) > 20:
        print('The password is too long, please try again')
    else:
        print("Don't try to hack me, man!")
elif len(user_login) > 15:
    print('The login is too long, please try again')
else:
    print('Your login is incorrect')
