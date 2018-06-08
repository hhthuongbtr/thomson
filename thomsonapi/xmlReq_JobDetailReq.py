HEADERS = {
    'content-type': 'text/xml; charset=utf-8',
    'SOAPAction': 'JobGetParams'
}

BODY = """<soapenv:Envelope
    xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:job="JobGetParams">
        <soapenv:Body>
            <job:JobGetParamsReq Cmd="Start" OpV="01.00.00" JId="JobID"/>
        </soapenv:Body>
    </soapenv:Envelope>"""

START_HEADERS = {
    'content-type': 'text/xml; charset=utf-8',
    'SOAPAction': 'JobStart'
}

START_BODY ="""<soapenv:Envelope
    xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:job="JobStart">
      <soapenv:Body>
        <job:JobStartReq Cmd="Start" OpV="01.00.00" JId="JobID"/>
      </soapenv:Body>
    </soapenv:Envelope>"""

ABORT_HEADERS = {
    'content-type': 'text/xml; charset=utf-8',
    'SOAPAction': 'JobAbort'
}

ABORT_BODY ="""<soapenv:Envelope
    xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:job="JobAbort">
      <soapenv:Body>
        <job:JobAbortReq Cmd="Start" OpV="01.00.00" JId="JobID"/>
      </soapenv:Body>
    </soapenv:Envelope>"""

DELETE_HEADERS = {
    'content-type': 'text/xml; charset=utf-8',
    'SOAPAction': 'JobDeleteReq'
}

DELETE_BODY ="""<soapenv:Envelope
    xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:job="JobDelete">
      <soapenv:Body>
        <job:JobDeleteReq Cmd="Start" OpV="01.00.00" JId="JobID"/>
      </soapenv:Body>
    </soapenv:Envelope>"""