row1=['*','*','*']
row2=['*','*','*']
row3=['*','*','*']
map=[row1,row2,row3]
position = input("Where do you to put treasure? ")
horizental =int(position[0])
vertical= int(position[1])
selected_row=map[vertical-1]
selected_row[horizental-1]="X"
print(f"{row1}\n{row2}\n{row3}")


# map[vertical-1][horizental-1]='*'

