# import os

# def makeCommits (days : int):
#     if days < 1:
#         # push
#         os.system('git push')
#     else:
#         dates = f"{days} days ago"
#         with open('data.txt', 'a') as file:
#             file.write(f"{dates} <- this was the commit for the day \n")

#         # staging
#         os.system('git add data.txt')

#         #  commit
#         os.system('git commit --date="' + dates +'" -m"First commit for the day"')

#         return days * makeCommits(days - 1)

# makeCommits(50)

import os
from random import randint

for i in range(1, 50):

    for j in range(0, randint(0, 5)):
        d = str(i) + 'days ago'
        with open('data.txt', 'a') as file:
            file.write(d)
        
        os.system('git add .')
        os.system('git commit --date="' + d + '" -m "commit"')

os.system('git push -u origin main')