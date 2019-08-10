# examples/tutorial/hello_world2.py
from charm4py import charm, Chare, Group, Future

class Hello(Chare):

    def SayHi(self, future):
        print("Hello World from element", self.thisIndex)
        self.reduce(future)

def main(args):
    # create Group of Hello objects (one object exists and runs on each core)
    hellos = Group(Hello)
    # call method 'SayHi' of all group members, wait for method to be invoked on all
    f = Future()
    hellos.SayHi(f)
    f.get()
    exit()

charm.start(main)
