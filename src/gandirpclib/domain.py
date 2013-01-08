'''
Created on 4 janv. 2013

@author: Radrizzi
'''
import xmlrpclib

api = xmlrpclib.ServerProxy('https://rpc.gandi.net/xmlrpc/')

def get_api_version(apikey):
    return api.version.info(apikey)

'''
Check if the given domain exists
'''
def exists(apikey, domain):
    try:
        api.domain.info(apikey, domain)
        return True
    except xmlrpclib.Fault as err:
        print err
        return False

'''
Get the zone_id of the given domain
'''    
def get_zone_id(apikey, domain):
    return api.domain.info(apikey, domain)['zone_id']
        
