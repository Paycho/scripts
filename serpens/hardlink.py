#!/usr/bin/python

import os
import shutil
import sys
import syslog

args = sys.argv

torrentid = args[1]
torrentname = args[2]
torrentrootpath = args[3]

logfile = open("/home/paycho/hardlink.log", "w+")
logfile.write("\n#####\n\tAttempting to hardlink files, args:\n\t ".join(args))

# These file types will not be linked
excluded_extensions = ['.png', '.nfo', '.jpg', '.txt']

# These prefixed will be removed from the link, the link will still be made though!
unwanted_prefixes = ['aaf-']

# These dirs are skipped
unwanted_dirs = ['Sample', 'sample', 'SAMPLE']

destination = '/home/paycho/sync/complete'

if torrentrootpath[-1:] == "/":
    torrentrootpath = torrentrootpath[0:-1]

torrentpath = os.path.join(torrentrootpath, torrentname)

def remove_prefix(name):
    for prefix in unwanted_prefixes:
        if name.startswith(prefix):
            return name.replace(prefix, '', 1)
    return name

def process_dir(dirname):
    for root, dirs, files in os.walk(dirname):
        for unwanted in unwanted_dirs:
            if unwanted in dirs:
                dirs.remove(unwanted)

        for name in files:
            ext = os.path.splitext(name)[1]
            if ext not in excluded_extensions:
                source = os.path.join(root, name)
                suffix = os.path.relpath(root, torrentrootpath)
                destinationdir = destination + '/' + suffix
                if not os.path.exists(destinationdir):
                    os.makedirs(destinationdir)
                os.link(source, os.path.join(destinationdir, name))
try:
    # If the torrent contains a dir, process it
    if os.path.isdir(torrentpath):
        process_dir(torrentpath)
    else:
        # Torrent is a single file, no processing needed.
        # Note that if the torrent contains a single file, it is assumed it is not one of the
        # excluded file types as defined in excluded_extensions.
        torrentname = remove_prefix(torrentname)
        destinationpath = os.path.join(destination, torrentname)
        os.link(torrentpath, destinationpath)
except:
    logfile.write("Error: ", sys.exc_info()[0])
    shutil.copyfile("/home/paycho/hardlink.log", "/home/paycho/hardlinkerror.log")
finally:
    logfile.close()
