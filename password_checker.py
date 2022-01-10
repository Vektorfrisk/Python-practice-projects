def is_password_valid(password):
    num_count=0
    for i in password:
        if type(i)== int:
            num_count+=1
    if num_count>=3:
        if len(password)>=8:
            upper=0
            lower=0
            for a in password:
                if a.isupper():
                    upper+=1
                if a.islower():
                    lower+=1
            if upper>=1 and lower>=1:
                print("The password is valid")
    else:
        print("Invalid Password")


password1 = input(str("Enter a valid password: "))
is_password_valid(password1)

        
