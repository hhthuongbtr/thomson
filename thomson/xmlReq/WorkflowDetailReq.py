HEADERS = {
    'content-type': 'text/xml; charset=utf-8',
    'SOAPAction': 'WorkflowGetPublicDesc'
}
BODY = """<soapenv:Envelope
    xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:wor="WorkflowGetPublicDesc" xmlns:mal="MalteseGlobal">
        <soapenv:Body>
            <wor:WorkflowGetPublicDescReq Cmd="Start" OpV="01.00.00">
                <wor:WInfReq WId="WorkflowID"/>
            </wor:WorkflowGetPublicDescReq>
        </soapenv:Body>
    </soapenv:Envelope>"""


