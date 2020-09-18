food = {'pizza': 324, 'sandwich': 78, 'hot dog': 90}
div =[]

count= 3 
food_list=list(food.values())
food_name=list(food.keys())



# for values in food_list:
#     div.append (values/ (count))



winner = max(food_list)
index = food_list.index(winner)
winning_candidate = food_name[index]


print(winning_candidate)


#print (f' Food: {food_name[0]} Price: {food_list[0]}')




