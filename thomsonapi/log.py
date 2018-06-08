import json
from xml.dom import minidom
from .thomson import Thomson


class Log:
    def __init__(self, host, user, passwd):
        self.ts = Thomson(host, user, passwd)
        from xmlReq_LogReq import HEADERS
        self.headers = HEADERS

    def parse_xml(self, xml):
        args = []
        xmldoc = minidom.parseString(xml)
        itemlist = xmldoc.getElementsByTagName('lGet:RspOkLog')
        for log in itemlist.item(0).childNodes:
            text = str(log.attributes.items())
            JId = log.attributes['JId'].value if "'JId'" in text else '-1'
            Cat = log.attributes['Cat'].value if "'Cat'" in text else ''
            LId = log.attributes['LId'].value if "'LId'" in text else ''
            try:
                Res = log.attributes['Res'].value if "'Res'" in text else ''
            except Exception as e:
                Res = ''
                #print text
            #Res = log.attributes['Res'].value if 'Res' in text else ''
            JName = log.attributes['JName'].value if "'JName'" in text else ''
            NId =  log.attributes['NId'].value if "'NId'" in text else ''
            Sev = log.attributes['Sev'].value if "'Sev'" in text else ''
            Desc = log.attributes['Desc'].value if "'Desc'" in text else ''
            OpDate = log.attributes['OpDate'].value if "'OpDate'" in text else None
            ClDate = log.attributes['ClDate'].value if "'ClDate'" in text else None
            text = ''
            #Convert response data to Json
            args.append({'jid'             : int(JId),
                        'cat'              : Cat,
                        'lid'              : int(LId),
                        'res'              : Res,
                        'jname'            : JName,
                        'nid'              : int(NId),
                        'sev'              : Sev,
                        'desc'             : Desc,
                        'opdate'           : int(OpDate[:10]) if OpDate else None,
                        'cldate'           : int(ClDate[:10]) if ClDate else None
                })
        return json.dumps(args)

    #Getting All Logs
    def get_log(self):
        from xmlReq_LogReq import BODY
        body = BODY
        response_xml = self.ts.get_response(self.headers, body)
        return self.parse_xml(response_xml)

    #Getting Open Logs of All Severities
    def get_open(self):
        from xmlReq_LogReq import OPEN
        body = OPEN
        response_xml = self.ts.get_response(self.headers, body)
        return self.parse_xml(response_xml)

    #Getting All open log of Specific Jobs
    def get_by_jobID(self, jobID):
        from xmlReq_LogReq import ID
        body = ID
        body = body.replace('JobID', str(jobID))
        response_xml = self.ts.get_response(self.headers, body)
        return self.parse_xml(response_xml)

    def get_sys_log(self):
        from xmlReq_LogReq import SYSTEM
        body = SYSTEM
        response_xml = self.ts.get_response(self.headers, body)
        return self.parse_xml(response_xml)


