#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os, sys, argparse, random

def main(args):
    absroot = os.path.abspath(args.dir)
    files = os.listdir(absroot)
    count = 0
    if args.random and args.num > 0:
        files = random.sample(files, args.num)

    for f in files:
        if args.full:
            print os.path.join(absroot, f)
        else:
            print f
        count = count + 1
        if args.num > 0 and count >= args.num:
            break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extended ls command for programmer')
    parser.add_argument('-n', '--num', required=False, type=int, help='Number of files to show')
    parser.add_argument('-f', '--full', action='store_true', help='Show full path')
    parser.add_argument('-r', '--random', action='store_true', help='Use random sampling')
    parser.add_argument('dir', help='Working directory')
    args = parser.parse_args()
    main(args)
