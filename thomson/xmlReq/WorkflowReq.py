HEADERS = {
    'content-type': 'text/xml; charset=utf-8',
    'SOAPAction': 'WorkflowGetList'
}

BODY = """<soapenv:Envelope
    xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:wor="WorkflowGetList">
        <soapenv:Body>
            <wor:WorkflowGetListReq Cmd="Start" OpV="01.00.00"/>
        </soapenv:Body>
    </soapenv:Envelope>"""



