import random
boys = ["ali", "reza", "yasin", "benyamin", "mehrdad", "sajjad", "aidin", "shahin"]
girls = ["sara", "zari", "neda", "homa", "eli", "goli", "mary", "mina"]
marriage = []
boy_marrid = []
girl_marrid = []
for name in boys:
    flag = False
    while flag == False:
        boy = boys[random.randint(0,7)]
        girl = girls[random.randint(0,7)]
        if boy not in boy_marrid:
            if girl not in girl_marrid:
                tuple = (boy, girl)
                boy_marrid.append(boy)
                girl_marrid.append(girl)
                flag =True
    marriage.append(tuple)
print(marriage)