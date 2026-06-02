import random as rd
import string as st

user = int(input("Enter a Length :"))
password = ""

character = st.digits + st.ascii_letters + st.punctuation
for i in range(user):
    password += rd.choice(character)

    
print('password :',password)

