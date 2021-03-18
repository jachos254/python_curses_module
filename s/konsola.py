# margin = 5
# width = 5
# for x in range(margin, 60 - margin, width):
#     for y in range(margin, 10, width):
#         food = (x, y)
#         print(food)

# alien_row1 = []
# alien_row2 = []
# alien_row3 = []
# alien_row4 = []
# alien_row5 = []
alien_row = []

for y in range(1,31,3):
    for x in range(1, 81, 9):
            alien_row.append((y, x))

print(alien_row[1])