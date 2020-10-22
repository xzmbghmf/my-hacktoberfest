print("Which Yumenosaki Ebnsemble Stars! unit will you work for?")
print()
print("Welcome to Yumenosaki Academy! The units are currently looking for producers, and based on your choices, you will be allocated to one of the idol groups in Yumenosaki academy.")
print("Please respond with a number 1 - 5, where 1 is strongly disagree and 5 is strongly agree.")
print()

trickstar1 = input("I like idols who have genuine character onstage.")

fine1 = input("I like idols who are elegant and polite onstage.")

undead1 = input("I like idols groups whose members each have an individual style.")

kngihts1 = input("I like chivalrous idols who engage in much fanservice.")

ryuseitai1 = input("I like quirky idols with a variety of personalities.")

rabits1 = input("I like idols who are bright and cheerful.")

twink1 = input("I like idols who are a bit mischievous and are bright and flashy.")

akatsuki1 = input("I like idols who are able to maintain an air of gravity in public.")

trickstar2 = input("I prefer idols who are comfortable when interacting with their audience.")

fine2 = input("I like idols who are polished and have a strong presence in the idol industry.")

undead2 = input("I like idols who are highly flexible when doing idol work.")

knights2 = input("I like idols who usually participate in media that uses their appearance.")

ryuseitai2 = input("I like idol groups who are like a squad of heroes.")

rabits2 = input("I like idols who have fresh approaches when taking on work.")

twink2 = input("I like idols who are able to play by ear.")

akatsuki2 = input("I like idols who do more traditional, cultural work.")


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
