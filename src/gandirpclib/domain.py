'''
Created on 4 janv. 2013

@author: Radrizzi
'''
import xmlrpclib

api = xmlrpclib.ServerProxy('https://rpc.gandi.net/xmlrpc/')

def api_version_info(apikey):
    return api.version.info(apikey)

def zone_version_list(apikey, zone_id):
    return api.domain.zone.version.list(apikey, zone_id)

def zone_version_new(apikey, zone_id):
    return api.domain.zone.version.new(apikey, zone_id)

def zone_record_list(apikey, zone_id, version_id=0, opts={}):
    return api.domain.zone.record.list(apikey, zone_id, version_id, opts)

def zone_version_set(apikey, zone_id, version_id):
    return api.domain.zone.version.set(apikey, zone_id, version_id)

def zone_record_update(apikey, zone_id, version_id, opts={}, params={}):
    return api.domain.zone.record.update(apikey, zone_id, version_id, opts, params)
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
        
