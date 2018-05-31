# encoding: utf-8

import sys
import datetime

if len(sys.argv) > 1 and len(sys.argv[1].strip()):
	text = sys.argv[1]
else:
	text = sys.stdin.read()

def ts2datetime(text):
    query = int(text)
    readable_time = datetime.datetime.fromtimestamp(query).strftime('%Y-%m-%d %H:%M:%S.%f')
    return str(readable_time)

result = ts2datetime(text)

print """<?xml version="1.0"?>
<items>
  <item>
    <title>%s</title>
  </item>
""" % result
