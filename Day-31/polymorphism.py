#polymorphism
#________________method overriding

class hotstar:
    def __init__(self,name):
        print(f"welcome to hotstar,{name}")
    def login(self):
        print("you can login to hotstar")
    def dashboard(self):
        print("you can see thr dashboard")
    def search(self):
        print("you can see the search")
    def play_controllers(self):
        print("pause,resume,play")
    def history(self):
        print("you can see recernt videos")
    def ads(self):
        print("you can see ads")
    def  quality(self):
        print("you can see low clarity")
    def access(self):
        print("you have limited access")
    def downloads(self):
        print("you can't download")

class premiumhotstar(hotstar):
    def  __init__(self,name):
        print(f"welcome to hotstar{name}.we blessed to have u")
    def ads(self):
        print("you don't have ads")
    def  quality(self):
        print("you can see high clarity")
    def access(self):
        print("you have unlimited access")
    def downloads(self):
        print("you can download")





sajid=hotstar("sajid")
sajid.login()
sajid.dashboard()
sajid.search()
sajid.play_controllers()
sajid.history()
sajid.ads()
sajid.quality()
sajid.access()
sajid.downloads()

zaib=premiumhotstar("zaib")
zaib.login()
zaib.dashboard()
zaib.search()
zaib.play_controllers()
zaib.history()
zaib.ads()
zaib.quality()
zaib.access()
zaib.downloads()