def restart(health):
  reset = input('Would you like to try again (yes/no)? ')
  if reset == 'yes':
    health = 10
    game(health)
  else:
    print('Goodbye quitter!')

def healt_check(health):
  if health <= 0:
    print('You lose!')
    restart(health)
  else:
    print('Still alive, but watch yourself before you reck yourself')

def game(health):
  left_or_right = input('First choice... Left or Right (left/right)?').lower()
  if left_or_right == 'left':
    lev_1 = input('Good job, you follow the path and reach a lake... Do you swim across or go around (across/around)?').lower()
    if lev_1 == 'around':
      print('You went around and reached the other side of the lake.')
    elif lev_1 == 'across':
      print('You swam across the lake and made it to the other side but were bit by a fish and lost 5 health')
      health -= 5
      healt_check(health)
    else:
      print('You lose...')
      restart(health)
    lev_2 = input('You notice a house and a river. Which do you go to (house/river)?').lower()
    if lev_2 == 'house':
      print('You reach the house and are greeted by the owner... He thinks you are rude and smacks you in the face, -5 health')
      health -= 5
      healt_check(health)
    elif lev_2 == 'river':
      print('Congrats you find a boat and calmly sail to teh finish line!')
  else:
    print("You ran into flesh eating bee's and died...")
    restart(health)

print('Welcome to my first game')

name  = input('What is your name? ')
age = int(input('What is your age? '))
health = 10

print("Hello", name, 'you are', age, 'years old.')

if age <= 18:
  print('You must be 18 o older to play')
else:
  wants_to_play = input('Do you want to play? ').lower()
  if wants_to_play == 'yes':
    print('Lets play!')
    print('You are starting with', health, 'health! ')
    game(health)
  else:
    print('Goodbye')

