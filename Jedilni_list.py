# -*- coding: utf-8 -*-
print "PROGRAM ZA VNAŠANJE MENU-ja"

menu = {}

while True:
    jed = raw_input("Prosim vnesi ime jedi: ")
    jed_cena = raw_input("Porsim vnesi ceno za '%s': " % jed)
    menu[jed] = jed_cena

    nov = raw_input("Boš dodal novo jed? (da/ne) ")

    if nov.lower() == "ne":
        break

print "Jedilni list"
i = 1
for key, value in menu.iteritems():
    print(str(i) + ". " + key + " " + value + " " + "EUR")
    i += 1

with open("menu.txt", "w+") as menu_file:
    for jed in menu:
        menu_file.write("%s, %s EUR\n" % (jed, menu[jed]))
