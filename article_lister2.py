#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 17:20:06 2017

@author: brownloaner
"""

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


def get_articles(search_term):
    headers = {
            # Request headers
            'Ocp-Apim-Subscription-Key': 'cae5f7f041164177a83a0ac5318e6424',
            }
    
    query_term = search_term + " after 2000"
    params = urllib.urlencode({
            # Request parameters
        'query': query_term,
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
        'count': '5',
        'offset': '0',
        'orderby': 'CC:desc',
        'attributes': 'Ti,CC,AA.AuN,Y,J.Jn,E',
    })
    
    try:
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("GET", "/academic/v1.0/evaluate?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        #print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    
    ####################################
    data_json = json.loads(data)
    #print(json.loads(data_json["entities"][0]["E"]))
    ob = [{'title': data_json["entities"][x]["Ti"],
            'author': data_json["entities"][x]["AA"],
            #'journal': data_json["entities"][x]["J"][0]["Jn"],
            'journal': json.loads(data_json["entities"][x]["E"])["VFN"],
            'year': data_json["entities"][x]["Y"],
            'link': json.loads(data_json["entities"][x]["E"])["S"][0]["U"],
            'citations': data_json["entities"][x]["CC"],
            'description': json.loads(data_json["entities"][x]["E"]).get("D")} for x in range(0,5)]
            

    print(ob)
    
    return ob
"""data_json = json.loads(data)
description = json.loads(data_json["entities"][0]["E"])["D"]
link = json.loads(data_json["entities"][0]["E"])["S"][0]["U"]
title = data_json["entities"][0]["Ti"]
author = data_json["entities"][0]["AuN"]
citation_number = data_json["entities"][0]["CC"]
year = data_json["entities"][0]["Y"]
journal = data_json["entities"][0]["J.Jn"]"""

if __name__ == '__main__':
    get_articles('hippocampus')
