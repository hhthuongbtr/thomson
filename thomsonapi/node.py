import json
from xml.dom import minidom
from .thomson import Thomson
from .job import Job

class Node:
    def __init__(self, host, user, passwd):
        self.user = user
        self.passwd = passwd
        self.host = host
        self.ts = Thomson(host, user, passwd)
        from . import xmlReq_NodeReq as NodeReq
        self.headers =NodeReq.HEADERS
        self.body = NodeReq.BODY

    def get_nodes_xml(self):
        response_xml = self.ts.get_response(self.headers, self.body)
        return response_xml

    def parse_dom_object(self, dom_object):
        text = str(dom_object.attributes.items())
        NStatus = dom_object.attributes['NStatus'].value if "'NStatus'" in text else ''
        Cpu = dom_object.attributes['Cpu'].value if "'Cpu'" in text else '-1'
        AllocCpu = dom_object.attributes['AllocCpu'].value if "'AllocCpu'" in text else '-1'
        Unreachable = dom_object.attributes['Unreachable'].value if "'Unreachable'" in text else ''
        NId = dom_object.attributes['NId'].value if "'NId'" in text else '-1'
        NState = dom_object.attributes['NState'].value if "'NState'" in text else ''
        Mem =  dom_object.attributes['Mem'].value if "'Mem'" in text else '-1'
        AllocMem = dom_object.attributes['AllocMem'].value if "'AllocMem'" in text else '-1'
        return NStatus,Cpu,AllocCpu,Unreachable,NId,NState,Mem,AllocMem

    def parse_xml_none_error(self, xml):
        args = []
        xmldoc = minidom.parseString(xml)
        itemlist = xmldoc.getElementsByTagName('sGetNodesStats:RspSGNSOk')
        for node in itemlist.item(0).childNodes:
            NStatus,Cpu,AllocCpu,Unreachable,NId,NState,Mem,AllocMem = self.parse_dom_object(node)
            args.append({'status'             : NStatus,
                        'cpu'                 : int(Cpu),
                        'alloccpu'            : int(AllocCpu),
                        'uncreahable'         : Unreachable,
                        'nid'                 : int(NId),
                        'state'               : NState,
                        'mem'                 : int(Mem),
                        'allocmem'            : int(AllocMem)
                })
        return json.dumps(args)

    def get_nodes(self):
        """
        get node without jcounter, jerror
        """
        xml = self.get_nodes_xml()
        return self.parse_xml_none_error(xml)

    def parse_xml(self, xml):
        args = []
        xmldoc = minidom.parseString(xml)
        itemlist = xmldoc.getElementsByTagName('sGetNodesStats:RspSGNSOk')
        for node in itemlist.item(0).childNodes:
            NStatus,Cpu,AllocCpu,Unreachable,NId,NState,Mem,AllocMem = self.parse_dom_object(node)
            JError, JCounter = NodeDetail(self.host, self.user, self.passwd, NId).count_job_error()
            args.append({'status'             : NStatus,
                        'cpu'                 : int(Cpu),
                        'alloccpu'            : int(AllocCpu),
                        'uncreahable'         : Unreachable,
                        'nid'                 : int(NId),
                        'state'               : NState,
                        'mem'                 : int(Mem),
                        'allocmem'            : int(AllocMem),
                        'jerror'              : JError,
                        'jcounter'            : JCounter
                })
        return json.dumps(args)

    def get_info(self):
        xml = self.get_nodes_xml()
        return self.parse_xml(xml)

class NodeDetail:
    def __init__(self, host, user, passwd, node_id):
        self.user = user
        self.passwd = passwd
        self.host = host
        self.node = Node(host, user, passwd)
        self.nid = int(node_id)

    def get_dom_node(self):
        dom_node = None
        nodes_xml = self.node.get_nodes_xml()
        xmldoc = minidom.parseString(nodes_xml)
        itemlist = xmldoc.getElementsByTagName('sGetNodesStats:RspSGNSOk')
        for node in itemlist.item(0).childNodes:
            text = str(node.attributes.items())
            NId = node.attributes['NId'].value if "'NId'" in text else -1
            if int(NId) == self.nid:
                dom_node = node
        return dom_node

    def get_array_job_id(self):
        array_jid = []
        dom_node = self.get_dom_node()
        for node_status_detail in dom_node.childNodes:
            text = str(node_status_detail.attributes.items())
            jid = node_status_detail.attributes['JId'].value if "'JId'" in text else ''
            if jid:
                array_jid.append(int(jid))
        return array_jid

    def get_list_job(self):
        args = []
        array_jid = self.get_array_job_id()
        dom_node = self.get_dom_node()
        NStatus,Cpu,AllocCpu,Unreachable,NId,NState,Mem,AllocMem = self.node.parse_dom_object(dom_node)
        JError, JCounter = self.count_job_error()
        job_list = Job(self.host, self.user, self.passwd).get_job_detail_by_job_id(array_jid)
        args.append({'status'             : NStatus,
                    'cpu'                 : int(Cpu),
                    'alloccpu'            : int(AllocCpu),
                    'uncreahable'         : Unreachable,
                    'nid'                 : int(NId),
                    'state'               : NState,
                    'mem'                 : int(Mem),
                    'allocmem'            : int(AllocMem),
                    'jerror'              : JError,
                    'jcounter'            : JCounter,
                    'job_list'            : job_list
            })
        return json.dumps(args)

    def count_job_error(self):
        array_jid = self.get_array_job_id()
        job_list = Job(self.host, self.user, self.passwd).get_job_detail_by_job_id(array_jid)
        error=0
        for job in job_list:
            if job['status'] != 'Ok':
                error += 1
        return error, len(array_jid)
