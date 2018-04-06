from linepy import *
import timeit
from time import strftime
import time

client = LINE()
client.log("AuthToken:" + str(client.authToken))

oepoll = OEPoll(client)

MySelf = client.getProfile()
JoinedGroups = client.getGroupIdsJoined()
print("My MID:" + MySelf.mid)
