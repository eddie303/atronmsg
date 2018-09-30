#!/usr/bin/env python3

from urllib.parse import quote
import pycurl
import argparse

parser=argparse.ArgumentParser(description="Short message display for Voyetra/Turtle Beach Audiotron.")
parser.add_argument('--ip', help="Audiotron IP address or hostname (default: 192.168.1.12)", default="192.168.1.12")
parser.add_argument('--user', help="Username for Audiotron web interface (default: admin)", default="admin")
parser.add_argument('--password', help="Password for Audiotron web interface (default: admin)", default="admin")
parser.add_argument('--line1', help="Message on line 1", default="")
parser.add_argument('--line2', help="Message on line 2", default="")
parser.add_argument('--timeout', help="Message timeout (in seconds, default: 30)", default=30)

args = parser.parse_args()

if(args.line1):
    aurl = "http://"+quote(str(args.user))+":"+quote(str(args.password))+"@"+quote(str(args.ip))+"/apimsg.asp?line1="+quote(str(args.line1))+"&line2="+quote(str(args.line2))+"&timeout="+quote(str(args.timeout))

    c=pycurl.Curl()
    c.setopt(c.URL, aurl)
    c.perform()
    c.close()
    # print(aurl)
else:
    parser.print_help()
