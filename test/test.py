import subprocess

def check_load_balancing():
    whoami1 = subprocess.check_output(["curl","-s","-H","Host:whoami.docker.localhost","http://127.0.0.1"]).split(' ')[1]
    whoami2 = subprocess.check_output(["curl","-s","-H","Host:whoami.docker.localhost","http://127.0.0.1"]).split(' ')[1]

    if whoami1 != whoami2:
        print "success!"
        return 1
    else:
        print "fail"
        return 0

check_load_balancing()
