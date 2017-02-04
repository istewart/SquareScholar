#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 15:36:10 2017

@author: brownloaner
"""

########### Python 2.7 #############
import httplib, urllib, base64
import json
import pprint

pp = pprint.PrettyPrinter(indent=4)

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'cae5f7f041164177a83a0ac5318e6424',
}

params = urllib.urlencode({
    # Request parameters
    'query': 'hippocampus after 2000',
    'complete': '0',
    'count': '1',
    'offset': '0',
    'timeout': '2000',
    'model': 'latest',
})

try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("GET", "/academic/v1.0/interpret?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    #print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
q = json.loads(data)

interpreted = q['interpretations'][0]['rules'][0]['output']['value']


########### Python 2.7 #############

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'cae5f7f041164177a83a0ac5318e6424',
}

params = urllib.urlencode({
    # Request parameters
    'expr': interpreted,
    'model': 'latest',
    'attributes': 'Y,F.FN',
    'count': '17',
    'offset': '0',
})

try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("GET", "/academic/v1.0/calchistogram?%s" % params, "{body}", headers)
    response = conn.getresponse()
    hist_data = response.read()
    print(hist_data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################

hist_json = json.loads(hist_data)
hist_json["histograms"]

