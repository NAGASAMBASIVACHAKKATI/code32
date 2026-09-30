import time
#print(dir(time))
print(time.asctime())
print(time.time())
def trffsing1():
    print("red colour-stop!")
    time.sleep(10)
    print("yellow colour light-ready")

    time.sleep(5)
    print("Green colour light-go")
trffsing1()
