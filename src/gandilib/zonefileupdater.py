'''
Created on 4 janv. 2013

@author: Radrizzi
'''
import gandirpclib.domain
from gandilib import zonefilerecord

class ZoneFileUpdater:
    def __init__(self, api, domain, records, rtypes, ipv4, ipv6):
        self.records = []
        self.api = api
        self.domain = domain
        self.zone_id = gandirpclib.domain.get_zone_id(api, domain)
        self.rtypes = rtypes
        self.ipv4 = ipv4
        self.ipv6 = ipv6
        
        
        for rtype in self.rtypes:
            for record in records:
                if rtype == 'A':
                    if ipv4 != '':
                        self.records.append(zonefilerecord.ZoneFileRecord(record, rtype, ipv4))
                    else:
                        print ('Missing IPv4 for record ' + record + '. Will not be processed')
                if rtype == "AAAA":
                    if ipv6 != '':
                        self.records.append(zonefilerecord.ZoneFileRecord(record, rtype, ipv6))
                    else:
                        print ('Missing IPv6 for record ' + record + '. Will not be processed')
                
            
        
    def Update(self):
        #Check whether the IP of a record changed. If not, remove from list
        changed_records = []
        for record in self.records:
            zoneRecordReturn = gandirpclib.domain.zone_record_list(self.api, self.zone_id, opts={'name': record.record, 'type': record.rtype})
            if zoneRecordReturn != []:
                if zoneRecordReturn[0]['value'] != record.ip:
                    record.record_id = zoneRecordReturn[0]['id']
                    changed_records.append(record)
                else:
                    print('Record: ' + record.record + ', Type: ' + record.rtype + ' unchanged. Nothing to be done.')
            else:
                print('Record: ' + record.record + ', Type: ' + record.rtype + ' does not exist. Create first through Gandi.Net Web UI')
        
        self.records = changed_records
        
        #create a new version of the zone file only if records are to be updated
        if len(self.records) > 0:
            self.version_id = gandirpclib.domain.zone_version_new(self.api, self.zone_id)
            print('New zone file version id is: ' + str(self.version_id))
            for record in self.records:
                record.Update(self.api, self.zone_id, self.version_id)
                
            if gandirpclib.domain.zone_version_set(self.api, self.zone_id, self.version_id) == True:
                print('Zone updated.')
        else:
            print ('No change detected. Nothing will be updated')
        