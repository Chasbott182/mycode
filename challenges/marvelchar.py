#!/usr/bin/env python3
import argparse
marvelchars = {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"She-Hulk":
  {"real name": "jennifer walters",
  "powers": "super strength & intelligence",
  "archenemy": "Titania"}
}

value = "Stat does not exist."

#while value == "Stat does not exist.":

user = argparse.ArgumentParser(description="Which character")

acc_adj=["Starlord", "Mystique", "She-Hulk"]

user.add_argument("adj", choices=acc_adj, help="Which character")
# add an optional argument
user.add_argument("-a", metavar="ADVERB", default="so", help="What statistic")

# char_name = input(" Which character do you want to know about? (Starlord, Mystique, She-Hulk):")
#
# char_stat = input("  What statistic do you want to know about? (real name, powers, archenemy):")

name = marvelchars.get(user,"Name does not exist.")
value = name.get(user,"Stat does not exist.")

print( f"{name}'s {user} is: {value}")
