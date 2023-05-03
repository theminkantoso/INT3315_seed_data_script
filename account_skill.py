import random
# INSERT INTO `proteam`.`skill_account` (`account_id`, `skill_id`) VALUES ('1', '1');

def yes_or_no(p: float) -> bool:
    return True if random.random() < p else False
f = open("account3.txt", "a", encoding="utf-8")


for x in range(10, 10000): #1638
    for i in range(1, 23):
        temp = random.choice([8, 13, 50])
        xac_suat = 1/float(temp)
        if yes_or_no(xac_suat):
            f.write("INSERT INTO `proteam`.`skill_account` (`account_id`, `skill_id`) VALUES ")
            f.write("('" + str(x) + "','" + str(i) + "');" + "\n")

f.close()


