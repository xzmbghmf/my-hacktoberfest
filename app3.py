print("Which Yumenosaki Ebnsemble Stars! unit will you work for?")
print()
print("Welcome to Yumenosaki Academy! The units are currently looking for producers, and based on your choices, you will be allocated to one of the idol groups in Yumenosaki academy.")
print("Please respond with a number 1 - 5, where 1 is strongly disagree and 5 is strongly agree.")
print()

knb1 = input("I like to play sports.")

sa1 = input("I prefer cartoons to movies with human actors.")

tg1 = input("I am not afraid of gore and monsters.")

knb2 = input("I prefer working in teams to working alone.")

sa2 = input("I like happy endings where no one dies :D")

tg2 = input("I prefer stories with deep meanings and angsty endings to stories with happy fairytale endings.")


knb_final = int(knb1) + int(knb2)
sa_final = int(sa1) + int(sa2)
tg_final = int(tg1)+ int(tg2)

print()

if knb_final > sa_final and knb_final > tg_final:
  print("You should watch Kuroke No Basuke! It's a really nice basketball anime :)")
elif sa_final > tg_final:
  print("You should watch Spirited Away! It's a touching movie that never fails to make me cry no matter how many times I watch it T_T")
else:
  print("You should watch Tokyo Ghoul! The anime is less gory and violent compared to the manga, and it really says a lot about society.")
  print("I hope you liked your anime recommendation!You can make a pull request if you want more animes :D")
