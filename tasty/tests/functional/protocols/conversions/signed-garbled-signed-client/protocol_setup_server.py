from tasty.types import conversions
from tasty.types import *
from tasty.types.driver import TestDriver
__params__ = {'la': 33, 'lb': 33, 'dima': 10, 'dimb': 10}
driver = TestDriver()

def protocol(client, server, params):
    client.ga = Garbled(val=Signed(bitlen=32, dim=[1], signed=True, passive=True, empty=True), passive=True, signed=True, bitlen=32, dim=[1])
    client.cc = Signed(val=client.ga, passive=True, signed=True, bitlen=32, dim=[1])
    conversions.Signed_Garbled_send(server.b, client.gb, 32, [1], True)
    client.sc = Signed(val=client.gb, passive=True, signed=True, bitlen=32, dim=[1])
    conversions.Garbled_Garbled_receive(client.ga, server.ga, 32, [1], True)
    server.gb = Garbled(val=Signed(bitlen=32, dim=[1], signed=True, passive=True, empty=True), signed=True, bitlen=32, dim=[1])
