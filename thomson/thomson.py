import json
from xml.dom import minidom
import requests# $ pip install requests
from requests.auth import HTTPDigestAuth
from .utils import DateTime as ThonsonTime

class Thomson:
    def __init__(self, host, user, passwd):
        self.user = user
        self.passwd = passwd
        self.host = host
        self.url = 'http://%s/services/Maltese'%(self.host)

    def get_response(self, headers, body):
        response = requests.post(self.url, data=body, headers=headers, \
            auth=HTTPDigestAuth(self.user, self.passwd), timeout=5)
        response_xml = response.content[response.content.find('<soapenv:Envelope') :\
         response.content.find('</soapenv:Envelope>') + len('</soapenv:Envelope>')]
        return response_xml

    def get_datetime(self):
        from . import xmlReq_DateAndTimeReq as DateAndTimeReq
        headers = DateAndTimeReq.HEADERS
        body = DateAndTimeReq.BODY
        response_xml = self.get_response(headers, body)
        xmldoc = minidom.parseString(response_xml)
        itemlist = xmldoc.getElementsByTagName('GetDateAndTime:RspOkGetDate')
        DateAndTime = itemlist[0].attributes['DateAndTime'].value if \
        "'DateAndTime'" in str(itemlist[0].attributes.items()) else ""
        OlsonTZ = itemlist[0].attributes['OlsonTZ'].value if \
        "'OlsonTZ'" in str(itemlist[0].attributes.items()) else ""
        #Convert response data to Json
        args = []
        args.append({'dateAndTime'  : ThonsonTime().conver_UTC_2_unix_timestamp(DateAndTime) \
            if DateAndTime else 1,
                    'timeZone'      : OlsonTZ if OlsonTZ else "Asia/Ho_Chi_Minh"
            })
        return json.dumps(args)

    def get_mountpoint(self):
        from . import xmlReq_MountPointReq as MountPointReq
        headers = MountPointReq.HEADERS
        body = MountPointReq.BODY
        response_xml = self.get_response(headers, body)
        xmldoc = minidom.parseString(response_xml)
        itemlist = xmldoc.getElementsByTagName('GetMountPoints:MountPoint')
        args = []
        for s in itemlist:
            Name = s.attributes['Name'].value if "'Name'" in \
            str(s.attributes.items()) else ""
            args.append({'name'             : Name if Name else ""
                })
        return json.dumps(args)

    def get_system_status(self):
        from . import xmlReq_SystemReq as SystemReq
        headers = SystemReq.HEADERS
        body = SystemReq.BODY
        response_xml = self.get_response(headers, body)
        xmldoc = minidom.parseString(response_xml)
        itemlist = xmldoc.getElementsByTagName('sGetStatus:RspOkSGS')
        Status = itemlist[0].attributes['Status'].value if 'Status' in\
         str(itemlist[0].attributes.items()) else ""
        CPU = itemlist[0].attributes['CPU'].value if "'CPU'" in\
         str(itemlist[0].attributes.items()) else '-1'
        AllocCpu = itemlist[0].attributes['AllocCpu'].value if "'AllocCpu'" in\
         str(itemlist[0].attributes.items()) else '-1'
        Mem = itemlist[0].attributes['Mem'].value if "'Mem'" in\
         str(itemlist[0].attributes.items()) else '-1'
        AllocMem = itemlist[0].attributes['AllocMem'].value if "'AllocMem'" in\
         str(itemlist[0].attributes.items()) else '-1'
        agrs = []
        agrs.append({'status'   : Status,
                     'cpu'      : int(CPU),
                     'alloccpu' : int(AllocCpu),
                     'mem'      : int(Mem),
                     'allocmem' : int(AllocMem)
                    })
        return json.dumps(agrs)

    def get_license_xml(self):
        from .xmlReq_SystemReq import LICENSE_HEADERS, LICENSE_BODY
        headers = LICENSE_HEADERS
        body = LICENSE_BODY
        response_xml = self.get_response(headers, body)
        return response_xml

    def parse_license_xml_object(self, license_obj):
        str_license_obj = str(license_obj.attributes.items())
        Nb = license_obj.attributes['Nb'].value if "'Nb'" in str_license_obj else ''
        Name = license_obj.attributes['Name'].value if "'Name'" in str_license_obj else ''
        NbOfUsedLicenceDec = license_obj.attributes['NbOfUsedLicenceDec'].value if "'NbOfUsedLicenceDec'" in str_license_obj else ''
        NbOfUsedLicence = license_obj.attributes['NbOfUsedLicence'].value if "'NbOfUsedLicence'" in str_license_obj else ''
        Desc = license_obj.attributes['Desc'].value if "'Desc'" in str_license_obj else ''
        return Nb,Name,NbOfUsedLicenceDec,NbOfUsedLicence,Desc

    def parse_license(self, license_xml):
        xmldoc = minidom.parseString(license_xml)
        args=[]
        version_item = xmldoc.getElementsByTagName('sGetVersions:SRItem')
        str_version_obj = str(version_item[0].attributes.items())
        version = version_item[0].attributes['Ver'].value if "'Ver'" in str_version_obj else ''
        args_license=[]
        itemlist = xmldoc.getElementsByTagName('sGetVersions:LicItem')
        for license_obj in itemlist:
            Nb,Name,NbOfUsedLicenceDec,NbOfUsedLicence,Desc = self.parse_license_xml_object(license_obj)
            args_license.append({'license' : Desc,
                        'partnumber'       : Name,
                        'used'             : NbOfUsedLicenceDec,
                        'max'              : int(Nb)
                })
        args.append({
            'version'       : version,
            'license_list'  : args_license
            })
        return args

    def get_license(self):
        license_xml = self.get_license_xml()
        arr_license = self.parse_license(license_xml)
        return json.dumps(arr_license)
