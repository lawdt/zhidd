#! /usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import sys
import subprocess
import re
import json

def get_sensors(ilo_ip,ilo_user,ilo_password):
    command = 'ipmitool -H %s -U %s -P %s -I lanplus sdr type 0x0d' % (ilo_ip, ilo_user, ilo_password)
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return out

# парсим аргументы.
parser = argparse.ArgumentParser(description='sample app for ipmi HP disks discovery')
parser.add_argument('ilo_ip', help='ILO_IP')
parser.add_argument('ilo_user', help='ILO_USER')
parser.add_argument('ilo_password', help='ILO_PASSWORD')
if len(sys.argv) < 3:
    parser.print_usage()
    sys.exit(1)
namespace = parser.parse_args()
#print (namespace)

sensors = get_sensors(namespace.ilo_ip,namespace.ilo_user,namespace.ilo_password)
disks = []
for line in sensors.splitlines():
    #print(line)
    if re.findall(r'.*Drive Present',line):
        name, address, status, position, present = line.split(' | ')
        disks.append([name, address, status, position, present])
#print(disks[0][0])
data = {}
for i in disks:
    key = "{#DISKNAME}"
    data.setdefault("data", []).append({key: str(i[0]).rstrip()})
json_data = json.dumps(data)
print(json_data)