HEADERS = {
    'content-type': 'text/xml; charset=utf-8',
    'SOAPAction': 'JobGetList'
}

BODY = """<soapenv:Envelope
    xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:job="JobGetList" xmlns:job1="JobGlobal">
        <soapenv:Header/>
        <soapenv:Body>
            <job:JobGetListReq Cmd="Start" OpV="01.00.00" >
                <job1:JState>Waiting</job1:JState>
                <job1:JState>Running</job1:JState>
                <job1:JState>Paused</job1:JState>
                <job1:JState>Completed</job1:JState>
                <job1:JState>Aborted</job1:JState>
            </job:JobGetListReq>
        </soapenv:Body>
    </soapenv:Envelope>"""

WAITTING = """<soapenv:Envelope
    xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:job="JobGetList" xmlns:job1="JobGlobal">
        <soapenv:Header/>
        <soapenv:Body>
            <job:JobGetListReq Cmd="Start" OpV="01.00.00" >
                <job1:JState>Waiting</job1:JState>
            </job:JobGetListReq>
        </soapenv:Body>
    </soapenv:Envelope>"""

RUNNING = """<soapenv:Envelope
    xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:job="JobGetList" xmlns:job1="JobGlobal">
        <soapenv:Header/>
        <soapenv:Body>
            <job:JobGetListReq Cmd="Start" OpV="01.00.00" >
                <job1:JState>Running</job1:JState>
            </job:JobGetListReq>
        </soapenv:Body>
    </soapenv:Envelope>"""

PAUSED = """<soapenv:Envelope
    xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:job="JobGetList" xmlns:job1="JobGlobal">
        <soapenv:Header/>
        <soapenv:Body>
            <job:JobGetListReq Cmd="Start" OpV="01.00.00" >
                <job1:JState>Paused</job1:JState>
            </job:JobGetListReq>
        </soapenv:Body>
    </soapenv:Envelope>"""

COMPLETED = """<soapenv:Envelope
    xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:job="JobGetList" xmlns:job1="JobGlobal">
        <soapenv:Header/>
        <soapenv:Body>
            <job:JobGetListReq Cmd="Start" OpV="01.00.00" >
                <job1:JState>Completed</job1:JState>
            </job:JobGetListReq>
        </soapenv:Body>
    </soapenv:Envelope>"""

ABORTED = """<soapenv:Envelope
    xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:job="JobGetList" xmlns:job1="JobGlobal">
        <soapenv:Header/>
        <soapenv:Body>
            <job:JobGetListReq Cmd="Start" OpV="01.00.00" >
                <job1:JState>Aborted</job1:JState>
            </job:JobGetListReq>
        </soapenv:Body>
    </soapenv:Envelope>"""

JOBID = """<soapenv:Envelope
    xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:job="JobGetList" xmlns:job1="JobGlobal">
        <soapenv:Header/>
        <soapenv:Body>
            <job:JobGetListReq Cmd="Start" OpV="01.00.00" JId="13872"/>
        </soapenv:Body>
    </soapenv:Envelope>
"""

