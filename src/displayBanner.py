import time
def displayBanner():
    banner = open('./banner/banner.txt', 'r')
    print(banner.read())
    time.sleep(2)

def choice():
    while True:
        choice = int(input(">"))
        if choice == 0:
            break
        elif choice == 1:
            exit()
        else:
            print("Retry")