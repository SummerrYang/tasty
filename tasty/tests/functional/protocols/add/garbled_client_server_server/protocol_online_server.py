from tasty.types import conversions
from tasty.types import *
from tasty.types.driver import TestDriver
__params__ = {'la': 32, 'lb': 32}
driver = TestDriver()

def protocol(client, server, params):
    server.b = Unsigned(bitlen=67, empty=True, signed=False, dim=[1]).input(src=driver, desc='b')
    client.ga = Garbled(val=Unsigned(bitlen=215, dim=[1], signed=False, passive=True, empty=True), passive=True, signed=False, bitlen=215, dim=[1])
    server.gb = Garbled(val=server.b, signed=False, bitlen=67, dim=[1])
    conversions.Garbled_Garbled_send(server.gb, client.gb, 67, [1], False)
    conversions.Garbled_Garbled_receive(client.gc, server.gc, 216, [1], False)
    server.c = Unsigned(val=server.gc, signed=False, bitlen=216, dim=[1])
    server.c.output(dest=driver, desc='c')
