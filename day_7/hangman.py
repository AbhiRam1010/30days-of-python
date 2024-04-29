import random
word_list= ["arrogant","german","skywyas","maxico"]
choise = random.choice(word_list)
lenth=len(choise)
draw = []
# for n in range (lenth):
for letter in choise:
   draw += "_"
print(draw)
end_of_game= False

while not end_of_game:
    guess = input("guess a letter:  ").lower()
    for position in range(lenth):
        letter = choise[position]
        # print(f'current position: {position}\n current letter: {letter}\n guessed letter: {guess}')
        if letter == guess:
            draw[position]=letter
    print(draw)
if "_" not in draw:
    end_of_game= True
    print("you won")