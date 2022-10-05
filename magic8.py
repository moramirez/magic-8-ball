import random

name = 'ez'
#print(name)

question = 'will mo be a successful programmer?'
#print(question)

answer = ''

random_number =  random.randint(1, 9)
#print(random_number)

if random_number == 1:
  answer = 'Yes - definitely.'

elif random_number == 2: 
  answer = 'It is decidely so.'

elif random_number == 3:
  answer = "Without a doubt."

elif random_number == 4: 
  answer = 'Reply hazy, try again.'

elif random_number == 5:
  answer = 'Ask again later.'

elif random_number == 6:
  answer = 'DUH!!!'

elif random_number == 7:
  answer = 'My sources say obvi.'

elif random_number == 8:
  answer = 'Outlook looking REALLY good.'

elif random_number == 9:
  answer = 'Very much so.'

else:
   answer = "Error"


print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + answer)
















