# Define your functions
def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  drink_type = get_drink_type()
  cup_type = plastic_or_paper_cup()
  print('Alright, that\'s a {} {} in a {}!'.format(size, drink_type, cup_type))
  name = input('can I get your name please? \n>')
  print('Thanks, {}! Your drink will be ready shortly.'.format(name))
  return coffee_bot

def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res =='a':
    return 'Small'
  elif res == 'b':
    return 'Medium'
  elif res == 'c':
    return 'Large'
  else:
    print_message()
    return get_size()

  return res

def print_message():
  print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.')

def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n>')
  if res =='a':
    return 'Brewed Coffee'
  elif res == 'b':
    return 'Mocha'
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()
  return res

def order_latte():
  res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n>')
  if res == 'a':
    return '2% milk'
  elif res == 'b':
    return 'Non-fat milk'
  elif res == 'c':
    return 'Soy milk'
  else: 
    print_message()
    return order_latte()
  return res

def plastic_or_paper_cup():
  res = input('What kind of cup would you like?\n[a] Plastic \n[b]Paper \n>')
  if res == 'a':
    return 'Plastic cup'
  elif res == 'b':
    return 'Paper cup'
  else: 
    print_message()
    return plastic_or_paper_cup()
  return res

# Call coffee_bot()!
coffee_bot()
