HEADERS = {
    'content-type': 'text/xml; charset=utf-8',
    'SOAPAction': 'LogsGet'
}

BODY = """<soapenv:Envelope
    xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:log="LogsGet" xmlns:mal="MalteseGlobal"
    xmlns:job="JobGlobal">
        <soapenv:Body>
            <log:LogsGetReq Cmd="Start" OpV="01.00.00" Open="true"
            Close="true" Sys="true" Sev="Info to critical" Nb="500"
            PastCloseNb="500"/>
        </soapenv:Body>
    </soapenv:Envelope>"""

OPEN = """<soapenv:Envelope
    xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:log="LogsGet" xmlns:mal="MalteseGlobal"
    xmlns:job="JobGlobal">
        <soapenv:Body>
            <log:LogsGetReq Cmd="Start" OpV="01.00.00" Sev="Info to critical" />
        </soapenv:Body>
    </soapenv:Envelope>"""

ID = """<soapenv:Envelope
     xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
     xmlns:log="LogsGet" xmlns:mal="MalteseGlobal" xmlns:job="JobGlobal">
        <soapenv:Body>
            <log:LogsGetReq Cmd="Start" OpV="01.00.00" Open="true"
             Close="true" Sys="false" JSelect="Selected jobs"
             Sev="Info to critical" Nb="500" PastCloseNb="500">
                <job:JId>JobID</job:JId>
            </log:LogsGetReq>
        </soapenv:Body>
    </soapenv:Envelope>"""

SYSTEM = """<soapenv:Envelope
     xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
     xmlns:log="LogsGet" xmlns:mal="MalteseGlobal" xmlns:job="JobGlobal">
        <soapenv:Body>
            <log:LogsGetReq Cmd="Start" OpV="01.00.00" Sys="true" Nb="30" PastCloseNb="500"/>
        </soapenv:Body>
    </soapenv:Envelope>"""
