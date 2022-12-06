# - wygeneruj listę 10 losowych liczb z przedziału 1-100
# - sprawdź największą i najmniejszą
import random
def main(n):
    list = []
    for _ in range(n):
        list.append(random.randint(1,n))
    n = 10
    list_in_row = [list[k:k + n] for k in range(0, len(list), n)]
    print(list_in_row, "", end="\n")
    print()
    print("min=>",min(list),"max=>",max(list))
    print(f"Sum all = {sum(list)}")

main(int(input("Let me know number 1-100: ")))

