#!/usr/bin/env python

import subprocess
import sys


def callCommand(command):
    if type(command) is str:
        command = command.split()
    try :
       return (True, subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0])
    except subprocess.CalledProcessError:
        print "Suprocess error on command '", command
        return (False, None)
    

def parseCommit(commitId):
    success, out = callCommand("git log -n 1 --format=%B " + commitId)
    if not success:
        print "Error when showing commit ", commitId
        return
    
    print out

    return


def runningInsideGitRepo():
    command      = 'git status'
    success, out = callCommand(command)
    if success:
        if 'fatal: Not a git repository' in out:
            return False
        else:
            return True
    else:
        print "Failure to query for git repo"
        return False

def usage():
    print "----------------------------------------------------------------"
    print "Incorrect call. This script requires a git repo and a commit id"
    print __file__, " <commit id>"
    print "\n"

if __name__ == "__main__":
    if len(sys.argv) != 2 or not runningInsideGitRepo():
        usage()
    else :
        parseCommit(sys.argv[1])
