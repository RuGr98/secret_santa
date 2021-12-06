import random
import numpy as np

name=input("Give me your name(ola peza,agglika): ")
fr_list=['nikos','andreas','pantelis','nasos','xristos','panos']

for i in range(len(fr_list)):
    if name == fr_list[i-1]:
        fr_list.remove(fr_list[i-1])
match=random.choice(fr_list)
fr_list.remove(match)
print("You'll be a secret santa to "+match+' !!')
