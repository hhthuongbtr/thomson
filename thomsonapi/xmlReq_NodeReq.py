HEADERS = {
    'content-type': 'text/xml; charset=utf-8',
    'SOAPAction': 'SystemGetNodesStats'
}

BODY = """<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
        <S:Body>
            <sGetNodesStats:SystemGetNodesStatsReq xmlns:sGetNodesStats="SystemGetNodesStats" Cmd="Start" OpV="00.00.00"/>
        </S:Body>
    </S:Envelope>"""
