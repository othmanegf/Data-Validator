from Cu import check_word, check_digit, remove_space, phone_number, email

# Test the check_word function to see if the word 'saad' is present in the given text
checkword = check_word('othmane', 'I am othmane .')
print(checkword)

# Test the check_digit function to check if the string contains at least one digit
checkdigtal = check_digit('my number is 45-9557')
print(checkdigtal)

# Test the remove_space function to replace spaces with hyphens in the given string
removespace = remove_space('Hi there I am othmane')
print(removespace)

# Test the phone_number function to validate the phone number format
phonenumber = phone_number('06-866-518-54')
print(phonenumber)

# Test the email function to validate the email address format
emailcheck = email('othmane@email.com')
print(emailcheck)