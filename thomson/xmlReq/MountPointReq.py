HEADERS = {
    'content-type': 'text/xml; charset=utf-8',
    'SOAPAction': 'GetMountPoints'
}
BODY = """<soapenv:Envelope
    xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:get="GetMountPoints">
      <soapenv:Body>
        <get:GetMountPointsReq Cmd="Start" OpV="01.00.00"/>
      </soapenv:Body>
    </soapenv:Envelope>"""
