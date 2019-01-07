#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string
import hashlib
import itertools
import re

ss =  string.letters + string.digits

class md5_crack():
    def __init__(self, prefix):
        self.prefix = prefix

    def dict_pd_yield(self, strings, length):
        for x in itertools.product(strings, repeat=length):
            yield ''.join(x)

    def run(self):
        t = False
        h = hashlib.new('md5')
        for i in xrange(4, 100, 1):
            for s in self.dict_pd_yield(ss, i):
                # h.update(s.encode('utf-8'))
                h.update(s)
                res = h.hexdigest()
                print(s)
                if res[:len(self.prefix)] == self.prefix:
                    print s, ":", res
                    # print "done"
                    t = True
                    break
            if t:
                break 


