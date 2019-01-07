#!/usr/bin/env python
# coding=utf-8
# author=Sn00ker

import click 
import os
import subprocess

from lib.md5_decrypt import md5_decrypt
from core.md5_crack import md5_crack
from core.ssh_crack import bruteForcer

@click.group()
@click.pass_context
def option_init(ctx):
    pass 

@option_init.command("dirsearch", help="run dirsearch")
@click.pass_context
@click.option("-u", "--url", default = "", type=str, help="target url: https://www.baidu.com")
@click.option("-l", "--log", default = "snooker.log", type=str, help="target log in data/dirsearch/xxx.log input xxx.log")

def dirsearch(ctx, url, log):
    
    cmd = "python3 thirdparty/dirsearch/dirsearch.py -u " + url + " -e * " + "--simple-report data/dirsearch/" + log 
    os.system(cmd)


@option_init.command("md5_d", help="run md5 decrypt")
@click.pass_context
@click.option("-v", "--value", default = "", type=str, help="target input: 05c444a4a24821f9b90dc12e21e487ac")
def md5_dec(ctx, value):
    cmd = "https://md5.pinasthika.com/api/decrypt?value={}".format(value)
    
    md5_d = md5_decrypt(cmd)
    md5_d.run()
    # os.system(cmd)

@option_init.command("md5_crack", help="run md5 crack")
@click.pass_context
@click.option("-p", "--prefix", default = "", type=str, help="target input: abcde")
def md5_c(ctx, prefix):
    cmd = prefix
    m= md5_crack(cmd)
    m.run()
    # os.system(cmd)

@option_init.command("ssh_crack", help="run ssh crack")
@click.pass_context
@click.option("-uf", "--userfile", default="data/userfile.txt", type=str, help="target user file")
@click.option("-pf", "--passfile", default="data/passfile.txt", type=str, help="target password file")
@click.option("-t", "--target", default="", type=str, help="target addr")
def ssh_c(ctx, userfile, passfile, target):
    cmd = bruteForcer(userfile, passfile, target)
    cmd.run()















def main():
    print("[*] main start")
    option_init(obj={})

if __name__ == "__main__":
    main()
