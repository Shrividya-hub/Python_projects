#sorting hat

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print('=================SORTING HAT=================')
 
#question 01

print('Q1) Do you like Dawn or Dusk?')

print('  1) Dawn')
print('  2) Dusk')

answer = int(input('enter your answer (1-2):'))

if answer == 1:
  gryffindor += 1
  ravenclaw += 1
elif answer == 2:
  hufflepuff += 1
  slytherin +=1
else:
  print('wrong input')

#question 2

print("\nQ2) When I'm dead, I want people to remember me as:")

print('  1) The Good')
print('  2) The Great')
print('  3) The Wise')
print('  4) The Bold')

answer = int(input('enter your answer (1-4):'))

if answer == 1:
  hufflepuff += 1
elif answer == 2:
  slytherin += 1
elif answer == 3:
  ravenclaw += 1
elif answer == 4:
  gryffindor += 1
else:
  print('wrong input')

#question 3

print('\nQ3) Which kind of instrument most pleases your ear?')

print('  1) The violin')
print('  2) The trumpet')
print('  3) The piano')
print('  4) The drum')

answer = int(input('enter your answer (1-4):'))

if answer == 1:
  slytherin += 1
elif answer == 2:
  hufflepuff += 1
elif answer == 3:
  ravenclaw += 1
elif answer == 4:
  gryffindor += 1
else:
  print("wrong input")

#question 4

print('\nQ4) Which of the following would you most hate people to call you?')

print('  1) Ordinary')
print('  2) Ignorant')
print('  3) Selfish')
print('  4) Cowardly')

answer = int(input('enter your answer (1-4):'))

if answer == 1:
  ravenclaw += 1
elif answer == 2:
  slytherin += 1
elif answer == 3:
  gryffindor += 1
elif answer == 4:
  hufflepuff += 1
else:
  print('wrong input')

#question 5

print('\nQ5) Which of these qualities do you value most?')

print('  1) Determination')
print('  2) Ambition')
print('  3) Kindness')
print('  4) Intelligence')

answer = int(input('enter your answer (1-4):'))

if answer == 1:
  gryffindor += 1
elif answer == 2:
  slytherin += 1
elif answer == 3:
  hufflepuff += 1
elif answer == 4:
  ravenclaw += 1
else:
  print ('wrong input')

#score of each house

print('\n🦁 Gryffindor:',gryffindor)
print('🦅 Ravenclaw:',ravenclaw)
print('🦡 Hufflepuff',hufflepuff)
print('🐍 Slytherin',slytherin)

#house with most point!

if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
  print('\nCongrats! You have been sorted into🦁 Gryffindor')
elif ravenclaw >= hufflepuff and ravenclaw >= slytherin:
  print('\nCongrats! You have been sorted into🦅 Ravenclaw')
elif hufflepuff >= slytherin:
  print('\nCongrats! You have been sorted into🦡 Hufflepuff')
else:
  print('\nCongrats! You have been sorted into🐍 Slytherin')
