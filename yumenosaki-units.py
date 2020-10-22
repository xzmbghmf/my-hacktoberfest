print("Which Yumenosaki Ensemble Stars! unit will you work for?")
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

valkyrie1 = input("I like idols who are artistic and who like capitalizing their artistic attributes.")

switch1 = input("I like idols who strive to be unique.")

mam1 = input("I like idols who like flashy performances.")

trickstar2 = input("I prefer idols who are comfortable when interacting with their audience.")

fine2 = input("I like idols who are polished and have a strong presence in the idol industry.")

undead2 = input("I like idols who are highly flexible when doing idol work.")

knights2 = input("I like idols who usually participate in media that uses their appearance.")

ryuseitai2 = input("I like idol groups who are like a squad of heroes.")

rabits2 = input("I like idols who have fresh approaches when taking on work.")

twink2 = input("I like idols who are able to play by ear.")

akatsuki2 = input("I like idols who do more traditional, cultural work.")

valkyrie2 = input("I like idols who have a distinct perspective of the world around them.")

switch2 = input("I like idols who like to showcase the unifying power of their worldview.")

mam2 = input("I prefer to work with an idol that works solo.")


trickstar_final = int(trickstar1) + int(trickstar2)
fine_final = int(fine1) + int(fine2)
undead_final = int(undead1) + int(undead2)
knights_final = int(knights1) + int(knights2)
ryuseitai_final = int(ryuseitai1) + int(ryuseitai2)
rabits_final = int(rabits1) + int(rabits2)
twink_final = int(twink1) + int(twink2)
akatsuki_final = int(akatsuki1) + int(akatsuki2)
valkyrie_final = int(valkyrie1) + int(valkyrie2)
switch_final = int(switch1) + int(switch2)
mam_final = int(mam1) + int(mam2)

print()

if trickstar_final > fine_final and trickstar_final > undead_final and trickstar_final > knights_final and trickstar_final > ryuseitai_final and trickstar_final > rabits_final and trickstar_final > twink_final and trickstar_final > akatsuki final and trickstar_final > valkyrie_final and trickstar_final > switch_final and trickstar_final > mam_final:
  print("You should work for Trickstar! This idol group consists of 4 members: Hidaka Hokuto who is the leader, Isara Mao, Akehoshi Subaru and Yuuki Makoto! Their theme colour is orange and their fanservice is both dazzling and comfortably personal with their audience.")
elif fine_final > undead_final and fine_final > knights_final and fine_final > ryuseitai_final and fine_final > rabits_final and fine_final > twink_final and fine_final > akatsuki_final and fine_final > valkyrie_final and fine_final > switch_final and fine_final > mam_final:
  print("You should work for fine (pronounced fee-nay)! This idol group consists of 4 members: Tenshouin Eichi who is the leader, Hibiki Wataru, Fushimi Yuzuru and Himemiya Tori. Thier theme colour is ivory and their polished and polite fanservice allows them to take command of their audience.")
elif undead_final > knights_final and undead_final > ryuseitai_final and undead_final > rabits_final and undead_final > twink_final and undead_final > akatsuki_final and undead_final > valkyrie_final and undead_final > switch_final and undead_final > mam_final:
  print("You should work for Undead! This idol group consists of 4 members: Sakuma Rei who is the leader, Hakaze Kaoru, Otogari Adonis and Oogami Koga. Thier theme colour is purple and during fan-service, each member delights with their individual style.")
elif knights_final > ryuseitai_final and knights_final > rabits_final and knights_final > twink_final and knights_final > akatsuki_final and knights_final > valkyrie_final and knights_final > switch_final and knights_final > mam_final:
  print("You should work for Knights! This idol group consists of 5 members: Suou Tsukasa who is the leader in the Ensemble Stars!! era and as of now, Tsukinaga Leo who was the leader during the Ensemble Stars! era, Sena Izumi (my best boi uwu), Sakuma Ritsu and Narukami Arashi. Their theme colour is navy and they make full use of their knightly personae and engage in plenty of fanservice.")
elif ryuseitai_final > rabits_final and ryuseitai_final > twink_final and ryuseitai_final > akatsuki_final and ryuseitai_final > valkyrie_final and ryuseitai_final > switch_final and ryuseitai_final > mam_final:
  print("You should work for Ryuseitai! This idol group consists of 5 members: Morisawa Chiaki who is the leader, Shinkai Kanata, Nagumo Tetora, Takamine Midori and Sengoku Shinobu. Their theme colours are the five colors of each member's role, which are based off of super sentai roles. Chiaki represents the colour red, Kanata blue, Tetora black, Midori green and Shinobu yellow. Their fanservice is laden with the quirkiness of their varied personalities.")
elif rabits_final > twink_final and rabits_final > akatsuki_final and rabits_final > valkyrie_final and rabits_final > switch_final and rabits_final > mam_final:
  print("You should work for Ra*Bits! This idol group has 4 members: Mashiro Tomoya who is the leader, Nito Nazuna, Shino Hajime and Tenma Mitsuru. Their theme colour is light blue and their fanservice is bright and cheerful.")
elif twink_final > akatsuki_final and twink_final > valkyrie_final and twink_final > switch_final and twink_final > mam_final:
  print("You should work for 2wink! This idol group consists of 2 members: Aoi Hinata who is the leader and Aoi Yuta. Their theme colour is neon and they're a mischievous unit known for their bright and flashy fanservice.")
elif akatsuki_final > valkyrie_final and akatsuki_final > switch_final and akatsuki_final > mam_final:
  print("You should work for Akatsuki! This idol group consists of 3 members: Hasumi Keito who is the leader, Kiryu Kuro and Kanzaki Souma. Their theme colour is red and they are reserved in their fanservice in an effort to maintain an air of gravity.")
elif valkyrie_final > switch_final and valkyrie_final > mam_final:
  print("You should work doe Valkyrie! This idol groups consists of 2 members: Itsuki Shu who is the leader and Kagehira Mika. Their theme colour is wine red and they're a group with their own, distinct perspective on the world and retain a highly individual, inflexible distance when interacting with their fans.")
elif: switch_final > mam_final:
  print("You should work for Switch! This idol group consists of 3 members: Sakasaki Natsume who is the leader, Aoba Tsumugi and Harukawa Sora. Their theme colour is yellow-green and they are an entertaining group that showcases the unifying power of their worldview through on-stage banter towards their fans.")
else:
  print("You should work for MaM! It is the only unit which has 1 member: Mikejima Madara. His theme colour is grey and he specialises in flashy performances.")
