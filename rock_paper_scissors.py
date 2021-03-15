import random as r
def play():
  i = input('Choose r for rock, p for paper or s for scissors:')
  rps = r.randint(0, 2)
  comp = ''
  #checks random numbers
  if rps == 0:
    comp = 'rock'
  elif rps == 1:
    comp = 'paper'
  elif rps == 2:
    comp = 'scissors'
  else:
    rps = 'ERROR'
  #sets ans to the winner
  ans = ''
  if comp == i:
      ans = 'tie'
  elif comp == 'rock' and i == 'p':
      ans = 'The computer chose rock and you chose paper, you have won!!!'
  elif comp == 'rock' and i == 's':
      ans = 'The computer chose rock and you chose scissors, you have lost :('
  elif comp == 'paper' and i == 's':
      ans = 'The computer chose paper and you chose scissors, you have won!!!'
  elif comp == 'paper' and i == 'r':
      ans = 'The computer chose paper and you chose rock, you have lost :(' 
  elif comp == 'scissors' and i == 'r':
      ans = 'The computer chose scissors and you chose rock, you have won!!!'
  elif comp == 'scissors' and i == 'p':
      ans = 'The computer chose scissors and you chose paper, you have lost :('
  else:
      ans = 'It is a tie'
  return ans

print(play())
