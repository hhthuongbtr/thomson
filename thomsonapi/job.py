import time
import json
from xml.dom import minidom
from .thomson import Thomson
from .workflow import Workflow
from .utils import DateTime as ThomsonTime

class Job:
    def __init__(self, host, user, passwd):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.ts = Thomson(host, user, passwd)
        from xmlReq_JobReq import HEADERS
        self.headers = HEADERS

    def parse_dom_object(self, dom_object, workflow_list_json):
        str_tmp = str(dom_object.attributes.items())
        State = dom_object.attributes['State'].value if "'State'" in str_tmp else ''
        Status = dom_object.attributes['Status'].value if "'Status'" in str_tmp else ''
        JId = dom_object.attributes['JId'].value if "'JId'" in str_tmp else ''
        Prog = dom_object.attributes['Prog'].value if "'Prog'" in str_tmp else ''
        StartDate =  dom_object.attributes['StartDate'].value \
        if "'StartDate'" in str_tmp else ''
        Ver = dom_object.attributes['Ver'].value if "'Ver'" in str_tmp else ''
        EndDate = dom_object.attributes['EndDate'].value if "'EndDate'" in str_tmp else ''
        jobname, workflowIdRef = JobDetail(self.host, self.user, self.passwd, str(JId)).get_job_name() if JId else ''
        '''Get workflow name'''
        workflow_name = ''
        workflow_list_json = json.loads(workflow_list_json)
        for workflow in workflow_list_json:
            if workflow['wid'] == workflowIdRef:
                workflow_name = workflow['name']
                break
        return State,Status,JId,Prog,StartDate,EndDate,Ver,jobname,workflowIdRef,workflow_name

    def parse_xml(self, xml):
        xmldoc = minidom.parseString(xml)
        itemlist = xmldoc.getElementsByTagName('jGetList:JItem')
        args=[]
        workflow_list_json = Workflow(self.host, self.user, self.passwd).get_workflow()
        for s in itemlist:
            State,Status,JId,Prog,StartDate,EndDate,Ver,jobname,workflowIdRef,workflow_name = self.parse_dom_object(s, workflow_list_json)
            args.append({'jname'    : jobname,
                        'wid'       : workflowIdRef,
                        'wname'     : workflow_name,
                        'state'     : State,
                        'status'    : Status,
                        'jid'       : int(JId),
                        # 'prog'      : int(Prog),
                        'startdate' : StartDate \
                        if StartDate else None,
                        # 'ver'       : int(Ver),
                        'enddate'   : EndDate \
                        if EndDate else None
                })
        return json.dumps(args)

    # return json theo name id job
    def parse_xml_name(self, xml):
        xmldoc = minidom.parseString(xml)
        itemlist = xmldoc.getElementsByTagName('jGetList:JItem')
        args=[]
        workflow_list_json = Workflow(self.host, self.user, self.passwd).get_workflow()
        for s in itemlist:
            State,Status,JId,Prog,StartDate,EndDate,Ver,jobname,workflowIdRef,workflow_name = self.parse_dom_object(s, workflow_list_json)
            args.append({'jname'    : jobname,
                        'jid'       : int(JId),
                })
        return json.dumps(args)

    def count_object(self, xml):
        xmldoc = minidom.parseString(xml)
        itemlist = xmldoc.getElementsByTagName('jGetList:JItem')
        return len(itemlist)


    def get_job_xml(self):
        from xmlReq_JobReq import BODY
        body = BODY
        response_xml = self.ts.get_response(self.headers, body)
        return response_xml

    def get_jobid_list(self):
        response_xml = self.get_job_xml()
        xmldoc = minidom.parseString(response_xml)
        itemlist = xmldoc.getElementsByTagName('jGetList:JItem')
        args=[]
        for s in itemlist:
            str_tmp = str(s.attributes.items())
            JId = s.attributes['JId'].value if "'JId'" in str_tmp else ''
            args.append(int(JId))
        return args

    def get_job(self):
        response_xml = self.get_job_xml()
        return self.parse_xml(response_xml)

    def get_job_name(self): # get name id job
        response_xml = self.get_job_xml()
        return self.parse_xml_name(response_xml)

    def count_job(self):
        response_xml = self.get_job_xml()
        return self.count_object(response_xml)

    def get_Waiting_xml(self):
        from xmlReq_JobReq import WAITTING
        body = WAITTING
        response_xml = self.ts.get_response(self.headers, body)
        return response_xml

    def get_Waiting(self):
        response_xml = self.get_Waiting_xml()
        return self.parse_xml(response_xml)

    def count_Waiting(self):
        response_xml = self.get_Waiting_xml()
        return self.count_object(response_xml)

    def get_Running_xml(self):
        from xmlReq_JobReq import RUNNING
        body = RUNNING
        response_xml = self.ts.get_response(self.headers, body)
        return response_xml

    def get_Running(self):
        xml = self.get_Running_xml()
        return self.parse_xml(xml)

    def count_Running(self):
        response_xml = self.get_Running_xml()
        return self.count_object(response_xml)

    def get_Paused_xml(self):
        from xmlReq_JobReq import PAUSED
        body = PAUSED
        response_xml = self.ts.get_response(self.headers, body)
        return response_xml

    def get_Paused(self):
        response_xml = self.get_Paused_xml()
        return self.parse_xml(response_xml)

    def count_Paused(self):
        response_xml = self.get_Paused_xml()
        return self.count_object(response_xml)

    def get_Completed_xml(self):
        from xmlReq_JobReq import COMPLETED
        body = COMPLETED
        response_xml = self.ts.get_response(self.headers, body)
        return response_xml

    def get_Completed(self):
        response_xml = self.get_Completed_xml()
        return self.parse_xml(response_xml)

    def count_Completed(self):
        response_xml = self.get_Completed_xml()
        return self.count_object(response_xml)

    def get_Aborted_xml(self):
        from xmlReq_JobReq import ABORTED
        body = ABORTED
        response_xml = self.ts.get_response(self.headers, body)
        return response_xml

    def get_Aborted(self):
        response_xml = self.get_Aborted_xml()
        return self.parse_xml(response_xml)

    def count_Aborted(self):
        response_xml = self.get_Aborted_xml()
        return self.count_object(response_xml)

    def get_job_detail_by_job_id(self, arr_job_id):
        job_xml = self.get_job_xml()
        xmldoc = minidom.parseString(job_xml)
        itemlist = xmldoc.getElementsByTagName('jGetList:JItem')
        args=[]
        workflow_list_json = Workflow(self.host, self.user, self.passwd).get_workflow()
        for job in itemlist:
            str_tmp = str(job.attributes.items())
            JId = job.attributes['JId'].value if "'JId'" in str_tmp else '-1'
            if int(JId) in arr_job_id:
                State,Status,JId,Prog,StartDate,EndDate,Ver,jobname,workflowIdRef,workflow_name = self.parse_dom_object(job, workflow_list_json)
                args.append({'jname'    : jobname,
                            'wid'       : workflowIdRef,
                            'wname'     : workflow_name,
                            'state'     : State,
                            'status'    : Status,
                            'jid'       : JId,
                            'prog'      : Prog,
                            'startdate' : ThomsonTime().conver_UTC_2_unix_timestamp(StartDate) \
                            if StartDate else None,
                            'ver'       : Ver,
                            'enddate'   : ThomsonTime().conver_UTC_2_unix_timestamp(EndDate) \
                            if EndDate else None
                    })
        return args

    def get_job_status(self):
        agrs = []
        agrs.append({
            'total'     :self.count_job(),
            'running'   :self.count_Running(),
            'completed' :self.count_Completed(),
            'waiting'   :self.count_Waiting(),
            'paused'    :self.count_Paused(),
            'aborted'   :self.count_Aborted()
            })
        return json.dumps(agrs)

class JobDetail:
    def __init__(self, host, user, passwd, jid):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.ts = Thomson(host, user, passwd)
        self.jid = jid
        from xmlReq_JobDetailReq import HEADERS, BODY
        self.headers = HEADERS
        self.body = BODY.replace('JobID', str(self.jid))

    def parse_xml(self, xml):
        xmldoc = minidom.parseString(xml)
        joblist = xmldoc.getElementsByTagName('wd:Job')
        job = joblist[0]
        jobname = job.attributes['name'].value if "'name'" in \
        str(job.attributes.items()) else ''
        workflowIdRef = job.attributes['workflowIdRef'].value if \
        "'workflowIdRef'" in str(job.attributes.items()) else ''
        args_param = []
        paramlist = xmldoc.getElementsByTagName('wd:ParamDesc')
        for param in paramlist:
            name = param.attributes['name'].value if "'name'" in \
            str(param.attributes.items()) else ''
            value = param.attributes['value'].value if "'value'" in \
            str(param.attributes.items()) else ''
            args_param.append({'name'              : name,
                               'value'             : value
                        })
        args = []
        args.append({'jobname'                      : jobname,
                     'workflowIdRef'                : workflowIdRef,
                     'params'                       : args_param
                     })
        return json.dumps(args)

    def get_param_xml(self):
        response_xml = self.ts.get_response(self.headers, self.body)
        return response_xml

    def get_param(self):
        response_xml = self.get_param_xml()
        return self.parse_xml(response_xml)


    def get_job_name(self):
        response_xml = self.get_param_xml()
        xmldoc = minidom.parseString(response_xml)
        joblist = xmldoc.getElementsByTagName('wd:Job')
        job = joblist[0]
        jobname = job.attributes['name'].value if "'name'" in \
        str(job.attributes.items()) else ''
        workflowIdRef = job.attributes['workflowIdRef'].value if \
        "'workflowIdRef'" in str(job.attributes.items()) else ''
        return jobname, workflowIdRef
        
    def parse_status(self, xml):
        result = 'NotOK'
        try:
            xmldoc = minidom.parseString(xml)
            if xmldoc.getElementsByTagName('mg:RspNotOK'):
                message = xmldoc.getElementsByTagName('mg:RspNotOK')
                result = message[0].attributes['Desc'].value \
                 if "'Desc'" in str(message[0].attributes.items()) else result
            elif xmldoc.getElementsByTagName('mg:RspDone'):
                result = 'OK'
        except Exception as e:
            print e
            result = 'Unknow'
        return result

    def start(self):
        from xmlReq_JobDetailReq import START_HEADERS, START_BODY
        headers = START_HEADERS
        body = START_BODY
        body = body.replace('JobID', str(self.jid))
        response_xml = self.ts.get_response(headers, body)
        time.sleep(1)
        status = self.parse_status(response_xml)
        return status

    def restart(self):
        try:
            if self.abort() == 'OK':
                return self.start()
            else :
                message = 'can not stop job'
                return message
        except Exception as identifier:
            return identifier

    def abort(self):
        from xmlReq_JobDetailReq import ABORT_HEADERS, ABORT_BODY
        headers = ABORT_HEADERS
        body = ABORT_BODY
        body = body.replace('JobID', str(self.jid))
        response_xml = self.ts.get_response(headers, body)
        return self.parse_status(response_xml)

    def delete(self):
        from xmlReq_JobDetailReq import DELETE_HEADERS, DELETE_BODY
        headers = DELETE_HEADERS
        body = DELETE_BODY
        body = body.replace('JobID', str(self.jid))
        response_xml = self.ts.get_response(headers, body)
        return self.parse_status(response_xml)

    def get_info(self):
        jid = int(self.jid)
        args={}
        State = None
        Status = None
        JId = None
        Prog = None
        StartDate = None
        Ver = None
        EndDate = None
        jobname = None
        workflowIdRef = None

        job = Job(self.host, self.user, self.passwd)
        #print job.__class__.__dict__
        job_xml = job.get_job_xml()
        xmldoc = minidom.parseString(job_xml)
        itemlist = xmldoc.getElementsByTagName('jGetList:JItem')
        for job in itemlist:
            str_tmp = str(job.attributes.items())
            JId = job.attributes['JId'].value if "'JId'" in str_tmp else '-1'
            if int(JId) == jid:
                str_tmp = str(job.attributes.items())
                State = job.attributes['State'].value if "'State'" in str_tmp else ''
                Status = job.attributes['Status'].value if "'Status'" in str_tmp else ''
                JId = job.attributes['JId'].value if "'JId'" in str_tmp else ''
                #Prog = job.attributes['Prog'].value if "'Prog'" in str_tmp else ''
                StartDate =  job.attributes['StartDate'].value \
                if "'StartDate'" in str_tmp else ''
                #Ver = job.attributes['Ver'].value if "'Ver'" in str_tmp else ''
                EndDate = job.attributes['EndDate'].value if "'EndDate'" in str_tmp else ''
                jobname, workflowIdRef = self.get_job_name() if JId else ''
                break
        args = {'jname'     : jobname,
                'wid'       : workflowIdRef,
                'wname'     : workflowIdRef[workflowIdRef.find("_")+1:] if workflowIdRef else "",
                'state'     : State,
                'status'    : Status,
                'jid'       : int(JId),
                'startdate' : ThomsonTime().conver_UTC_2_unix_timestamp(StartDate) if StartDate else None,
                'enddate'   : ThomsonTime().conver_UTC_2_unix_timestamp(EndDate) if EndDate else None
                }
        return json.dumps(args)

    def add_job_param_to_body(self, body):
        job_info = self.get_info()
        if not job_info:
            return None
        job_info = json.loads(job_info)
        body = body.replace("[jid]", str(job_info['jid']))
        body = body.replace("[wid]", job_info['wid'])
        body = body.replace("[job_name]", job_info['jname'])
        return body

    def set_backup(self, value):
        is_backup = value
        from xmlReq_JobModifyReq import MODIFY_HEADERS, ACTIVE_BACKUP_BODY
        headers = MODIFY_HEADERS
        body = ACTIVE_BACKUP_BODY
        body = self.add_job_param_to_body(body)
        if not body:
            return 1
        body = body.replace("[is_backup]", is_backup)
        print body
        response_xml = self.ts.get_response(headers, body)
        return self.parse_status(response_xml)

    def set_main_ip_address(self, value):
        ip_address = value
        from xmlReq_JobModifyReq import MODIFY_HEADERS, MAIN_IP_ADDRESS_BODY
        headers = MODIFY_HEADERS
        body = MAIN_IP_ADDRESS_BODY
        body = self.add_job_param_to_body(body)
        if not body:
            return 1
        body = body.replace("[ip_address]", ip_address)
        response_xml = self.ts.get_response(headers, body)
        return self.parse_status(response_xml)

    def set_main_udp_port(self, value):
        udp_port = value
        from xmlReq_JobModifyReq import MODIFY_HEADERS, MAIN_UDP_PORT_BODY
        headers = MODIFY_HEADERS
        body = MAIN_UDP_PORT_BODY
        body = self.add_job_param_to_body(body)
        if not body:
            return 1
        body = body.replace("[udp_port]", udp_port)
        response_xml = self.ts.get_response(headers, body)
        return self.parse_status(response_xml)


    def set_backup_ip_address(self, value):
        ip_address = value
        from xmlReq_JobModifyReq import MODIFY_HEADERS, BACKUP_IP_ADDRESS_BODY
        headers = MODIFY_HEADERS
        body = BACKUP_IP_ADDRESS_BODY
        body = self.add_job_param_to_body(body)
        if not body:
            return 1
        body = body.replace("[ip_address]", ip_address)
        response_xml = self.ts.get_response(headers, body)
        return self.parse_status(response_xml)

    def set_backup_udp_port(self, value):
        udp_port = value
        from xmlReq_JobModifyReq import MODIFY_HEADERS, BACKUP_UDP_PORT_BODY
        headers = MODIFY_HEADERS
        body = BACKUP_UDP_PORT_BODY
        body = self.add_job_param_to_body(body)
        if not body:
            return 1
        body = body.replace("[udp_port]", udp_port)
        response_xml = self.ts.get_response(headers, body)
        return self.parse_status(response_xml)


