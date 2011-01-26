# -*- coding: utf-8 -*-
####################################################
# Sample script that shows how to save result data #
####################################################
from datetime import datetime
import urllib, urllib2

# You need to enter the real URL and have the server running
CODESPEED_URL = 'http://localhost:8000/'

temp = datetime.today()

data = {
    'commitid': '1',
    'project': 'snoopy',
    'executable': 'phonebook_search',
    'benchmark': 'float',
    'environment': "snoopy",
    'result_value': 4000,
    'result_date': datetime.today(), # Optional
    'std_dev': 1.11111, # Optional. Default is blank
    'max': 4001.6, # Optional. Default is blank
    'min': 3995.1, # Optional. Default is blank
}

def add(data):
    params = urllib.urlencode(data)
    response = "None"
    print "Executable %s, revision %s, benchmark %s" % (data['executable'], data['commitid'], data['benchmark'])
    f = urllib2.urlopen(CODESPEED_URL + 'result/add/', params)
    response = f.read()
    f.close()
    print "Server (%s) response: %s\n" % (CODESPEED_URL, response)

if __name__ == "__main__":
    add(data)
