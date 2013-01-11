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
        self.id = ''
        self.record = record
        self.ttl = ttl
        self.rtype = rtype
        self.ip = ip
        
    def Update(self, api, zone_id, version_id):
        print('Updating record ' + self.record + '. Type: ' + self.rtype + '. IP: ' + self.ip + '...')
        zoneRecordReturn = gandirpclib.domain.zone_record_update(api, zone_id, version_id, opts={'id': self.id}, 
                                              params={'name': self.record, 'type': self.rtype, 'value' : self.ip, 'ttl' : self.ttl})
        print (zoneRecordReturn)            
        