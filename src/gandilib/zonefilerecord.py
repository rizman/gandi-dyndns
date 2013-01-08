'''
Created on 4 janv. 2013

@author: Radrizzi
'''

class ZoneFileRecord:
    '''
    This class represents a single record inside a DNS zonefile
    '''

    def __init__(self, record, rtype, ip, ttl=10800):
        self.record = record
        self.ttl = ttl
        self.rtype = rtype
        self.ip = ip
        
    def Update(self):
        print('Updating record ' + self.record + '. Type: ' + self.rtype + '. IP: ' + self.ip)        
        