def is_password_valid(password):
    num_count=0
    upper=0
    lower=0
    for i in password:
        if i.isdigit():
            num_count += 1
        if i.isupper():
            upper+=1
        if i.islower():
            lower+=1
      if num_count >= 3:
         if len(password)>= 8:
            if upper>=1 and lower>=1:
               return(print("Password is valid"))
                
    else:
        return(print("Invalid Password"))


password1 = input(str("Enter a valid password: "))
is_password_valid(password1)

        
