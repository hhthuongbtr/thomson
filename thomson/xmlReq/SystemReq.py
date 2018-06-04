HEADERS = {
    'content-type': 'text/xml; charset=utf-8',
    'SOAPAction': 'SystemGetStatus'
}

BODY = """<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
        <s:Body>
            <sGetStatus:SystemGetStatusReq xmlns:sGetStatus="SystemGetStatus" Cmd="Start" OpV="00.00.00"/>
        </s:Body>
    </s:Envelope>"""

LICENSE_HEADERS = {
    'content-type': 'text/xml; charset=utf-8',
    'SOAPAction': 'SystemGetVersions'
}

LICENSE_BODY = """<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
        <s:Body>
            <sGetVersions:SystemGetVersionsReq xmlns:sGetVersions="SystemGetVersions" Cmd="Start" OpV="00.00.00"/>
        </s:Body>
    </s:Envelope>"""