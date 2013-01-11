'''
Created on 4 janv. 2013

@author: Radrizzi
'''
import gandirpclib.domain

class ZoneFileRecord:
    '''
    This class represents a single record inside a DNS zonefile
    '''

    def __init__(self, record, rtype, ip, ttl=10800):
        self.record_id = ''
        self.record = record
        self.ttl = ttl
        self.rtype = rtype
        self.ip = ip
        
    def Update(self, api, zone_id, version_id):
        print('Updating record ' + self.record + '. Type: ' + self.rtype + '. IP: ' + self.ip + '...')
        
        #Can't get update to work :-(
        #zoneRecordReturn = gandirpclib.domain.zone_record_update(api, zone_id, version_id, opts={'id': self.record_id}, 
        #                                      params={'name': self.record, 'type': self.rtype, 'value' : self.ip, 'ttl' : self.ttl})
        
        gandirpclib.domain.zone_record_delete(api, zone_id, version_id, opts={'name' : self.record, 'type' : self.rtype})
        
        newRecordParams = {'name' : self.record, 'type' : self.rtype, 'ttl' : self.ttl, 'value' : self.ip}
        zoneRecordReturn = gandirpclib.domain.zone_record_add(api, zone_id, version_id, newRecordParams)            
        