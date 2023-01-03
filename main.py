import requests, random

my_deck = []
opponents_deck = []

def pokemon(name):
  pokemon_ID = random.randint(1,151)
  url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_ID)
  response = requests.get(url)
  pokemon = response.json()

  return {'name':pokemon['name'],'id':pokemon['id'],'weight':pokemon['weight'],'height':pokemon['height']}
pokemon('name')

def play():
  counter = 5

  while counter !=0:
    my_pokemon = pokemon('name')
    #I added my first random pokemon to my empty deck
    my_deck.append(my_pokemon['name'])
    print('your Pokemon is {}'.format(my_pokemon['name']))
    try:
       pokemon_choice = input('Which stas would you like to use? (id, height, weight)').lower()
    # I stored the answer from the input pokemon_choice into a variable my_choice
       my_choice = my_pokemon[pokemon_choice]
       opponent_pokemon = pokemon('name')
    #I added my opponents first random opponent_pokemon to opponent's empty deck
       opponents_deck.append(opponent_pokemon['name'])
  
       print('Your opponent has chosen {}'.format(opponent_pokemon['name']))
       opponents_choice = opponent_pokemon[pokemon_choice]
    
      

       if my_choice > opponents_choice:
      # As I won, I added the oponets pokemon to my_deck and removed the same one from the opponents_deck.
          my_deck.append(opponent_pokemon['name'])
          opponents_deck.pop()
          print('now you have:' , my_deck)
          counter -=1
       elif my_choice < opponents_choice:
      #As I lost, I added my_pokemon to the opponents_deck and removed the same one from my_deck.
          opponents_deck.append(my_pokemon['name'])
          my_deck.pop()
          print('Now your opponents has:' , opponents_deck)
          counter -=1
    
       if counter == 0:
        if len(my_deck) > len(opponents_deck):
          print('Congratulations you have won the match')
        elif len(my_deck < opponents_deck):
          print('Sorry you have lost the match')
        else:
          print("It's a draw!")

        exit_game = input('would you like to continure playing? (y/n').lower()
        if exit_game == 'y':
          counter = 5
        else:
          print('Thank ypu for playing')
    except:
      print('spelling error, try again')
play()