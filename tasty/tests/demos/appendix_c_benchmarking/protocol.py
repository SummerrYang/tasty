# -*- coding: utf-8 -*-
from tasty import state
from tasty import utils

from tasty.types import *


class BenchmarkingDriver(Driver):
    """ basic benchmarking driver """
    def next_data_in(self):
        """ yield bitlength for each protocol run: 5, 10, ..., 80"""
        for bitlen in xrange(5, 81, 5):
            self.params = {"l" : bitlen}
            self.client_inputs = {"x": utils.rand.randint(0, 2**bitlen - 1)}
            self.server_inputs = {"y": utils.rand.randint(0, 2**bitlen - 1)}
            yield

__params__ = {"l" : 32}

def protocol(client, server, params):
    """ TASTYL program to multiply two unsigned values held by C and S using HE """
    LENGTH = params["l"] # use parameter yielded by next_params
    client.x = Unsigned(bitlen=LENGTH).input(src=driver, desc="x")
    server.y = Unsigned(bitlen=LENGTH).input(src=driver, desc="y")

    client.hx = Homomorphic(val=client.x)

    server.hx <<= client.hx

    server.hr = server.hx * server.y

    client.hr <<= server.hr
    client.r = Unsigned(val=client.hr)
    client.r.output(dest=driver, desc="r")
