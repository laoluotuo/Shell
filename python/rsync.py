#!/usr/bin/env python
#wraps up sync to synchronize two directories

from subprocess import call
import sys

source = "/tmp/sync_dir_A"
target = "/tmp/sync_dir_B"
rsync  = "rsync"
arguments = "-a"
cmd = "%s %s %s %s" % (rsync,arguments,source,target)

def sync():

    ret = call(cmd,shell=True)
    if ret !=0:
        print "rsync failed"
        sys.exit(1)
sync()
