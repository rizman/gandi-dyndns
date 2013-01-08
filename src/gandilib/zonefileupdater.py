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
        for record in self.records:
            record.Update()
        