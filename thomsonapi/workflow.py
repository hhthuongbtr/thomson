import json
from xml.dom import minidom
from .thomson import Thomson


class Workflow:
    def __init__(self, host, user, passwd):
        self.ts = Thomson(host, user, passwd)
        from xmlReq_WorkflowReq import HEADERS
        self.headers = HEADERS

    def parse_xml(self, xml):
        xmldoc = minidom.parseString(xml)
        itemlist = xmldoc.getElementsByTagName('wGetList:WItem')
        args=[]
        for s in itemlist:
            str_tmp = str(s.attributes.items())
            Name = s.attributes['Name'].value if "'Name'" in str_tmp else ''
            WId = s.attributes['WId'].value if "'WId'" in str_tmp else ''
            PubVer = s.attributes['PubVer'].value if "'PubVer'" in str_tmp else ''
            PriVer = s.attributes['PriVer'].value if "'PriVer'" in str_tmp else ''
            #Convert response data to Json
            args.append({'name'             : Name,
                        'wid'               : WId,
                        'pubver'            : int(PubVer),
                        'priver'            : int(PriVer)
                })
        return json.dumps(args)   

    def get_workflow(self):
        from xmlReq_WorkflowReq import BODY
        body = BODY
        response_xml = self.ts.get_response(self.headers, body)
        return self.parse_xml(response_xml)

class WorkflowDetail:
    def __init__(self, host, user, passwd, wfid):
        self.ts = Thomson(host, user, passwd)
        from xmlReq_WorkflowDetailReq import HEADERS, BODY
        self.headers = HEADERS
        self.body = BODY
        self.body = self.body.replace('WorkflowID', wfid)
        self.wfid = wfid

    def parse_xml(self, xml):
        xmldoc = minidom.parseString(xml)
        wflist = xmldoc.getElementsByTagName('wd:Workflow')
        wf = wflist[0]
        wfname = wf.attributes['name'].value if "'name'" in \
        str(wf.attributes.items()) else ''
        wfid = wf.attributes['id'].value if "'id'" in \
        str(wf.attributes.items()) else ''
        wfpriority = wf.attributes['priority'].value if "'priority'" in \
        str(wf.attributes.items()) else ''
        wfcategory = wf.attributes['category'].value if "'category'" in \
        str(wf.attributes.items()) else ''
        wfcolor = wf.attributes['color'].value if "'color'" in \
        str(wf.attributes.items()) else ''
        args_param = []
        paramlist = xmldoc.getElementsByTagName('wd:Param')
        for param in paramlist:
            name = param.attributes['name'].value if "'name'" in \
            str(param.attributes.items()) else ''
            value = param.attributes['value'].value if "'value'" in \
            str(param.attributes.items()) else ''
            args_param.append({'name'              : name,
                               'value'             : value
                        })
        args = []
        args.append({'id'                      : wfid,
                     'name'                    : wfname,
                     'priority'                : wfpriority,
                     'category'                : wfcategory,
                     'color'                   : wfcolor,
                     'params'                  : args_param
                     })
        return json.dumps(args)

    def get_param(self):
        response_xml = self.ts.get_response(self.headers, self.body)
        return self.parse_xml(response_xml)
