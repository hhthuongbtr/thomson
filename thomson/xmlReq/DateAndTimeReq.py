HEADERS = {
    'content-type': 'text/xml; charset=utf-8',
    'SOAPAction': 'GetDateAndTime'
}
BODY = """<soapenv:Envelope
    xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:get="GetDateAndTime" xmlns:mal="MalteseGlobal">
        <soapenv:Body>
            <get:GetDateAndTimeReq Cmd="Start" OpV="01.00.00"/>
        </soapenv:Body>
    </soapenv:Envelope>"""
