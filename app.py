#!/usr/bin/env python3

import re
import os
from subprocess import Popen, PIPE
import signal

__author__ = 'Valkeru'

template = '#Zoom +\n' \
           '"Microsoft Natural® Ergonomic Keyboard 4000" "{DEV}" none key/418 "XKey/XF86Bluetooth"\n' \
           '#Zoom -\n' \
           '"Microsoft Natural® Ergonomic Keyboard 4000" "{DEV}" none key/419 "XKey/XF86WLAN"\n'

input_devices = Popen("/usr/bin/evrouter -D /dev/input/event*", shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
devices = []

for line in input_devices.stdout:
    line = line.decode('utf-8').strip()
    if re.match('(.)+Ergonomic Keyboard 4000', line):
        devices.append(re.search('/dev/input/event\d', line)[0])

necessary_dev = devices[1]

template = re.sub('{DEV}', necessary_dev, template)

file = os.environ['HOME'] + '/.evrouterrc'

fd = open(file, 'w')
fd.write(template)
fd.close()

pidfile = '/tmp/.evrouter:0'

if os.path.isfile(pidfile):
    pid_fd = open(pidfile, 'r')
    evrouter_pid = pid_fd.read().strip()
    pid_fd.close()
    os.remove(pidfile)

    os.kill(int(evrouter_pid), signal.SIGKILL)

os.system("evrouter {}".format(necessary_dev))
