import random

times = int(input("how many times:"))
lst = []
def roll():
    dice = random.randint(1,6)
    if dice % 2 == 0 or dice % 2 == 1:
        lst.append(dice)
    else:
        # dice = random.randint(1, 7)
        if dice %2 == 0 or dice == 1:
            lst.append(dice)
        else:
            print("not enough dice")

for i in range (times):
    roll()
# for i in range(1,7):
#     print("the number",i,"occured",lst.count(i),"times")
print(lst)

