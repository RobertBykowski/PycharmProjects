import random
tab = []
tab_prefix = {
    "500" : "Orange",
    "508" : "T-mobile",
    "506" : "Virgin Mobile",
    "509" : "Orange_2",
}
for i in range(6): # ilość cyfr
    num2 = random.randrange(0,10) #wybiera z liczb do 0-10
    tab.append(num2)
    listToStr = "".join(map(str, tab))
for key in tab_prefix:
    print(f"{key}-{listToStr[:3]}-{listToStr[3:6]}-{listToStr[6:9]} telefon w sieci {tab_prefix[key]}")






