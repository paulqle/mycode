#!/usr/bin/env python3

message = 'Here is your grade: '

# wrap connection in a float() to accept decimals as numbers
score = int(input("What is your score?"))

# if input value was higher or equal to 25
if score >= 90:
    message = message + 'Grade is A - you rock!'
elif score >= 80:
    message = message + 'Grade is B - nice job'
elif score >= 70:
    message = message + 'Grade is C - need to study more'
elif score >= 60:
    message = message + 'Grade is D - did you study?'
elif score <= 59:
    message = message + 'Grade is F - oh boy'

else:
    message = message + 'did not enter a score'
print(message)
