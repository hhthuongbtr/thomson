MODIFY_HEADERS = {
    'content-type': 'text/xml; charset=utf-8',
    'SOAPAction': 'JobModify'
}


ACTIVE_BACKUP_BODY =  """<soapenv:Envelope
 xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
 xmlns:job="JobModify" xmlns:wor="WorkflowDesc">
	<soapenv:Body>
		<job:JobModifyReq Cmd="Start" OpV="01.00.00" JId="[jid]"
		 ConsistencyBL="noerror_nowarning"
		 RebalancingMode="RebalancingNotAllowed">
			<wor:Job name="[job_name]" workflowIdRef="[wid]">
				<wor:ParamDesc value="[is_backup]" name="Define backup input" />
			</wor:Job>
		</job:JobModifyReq>
	</soapenv:Body>
</soapenv:Envelope"""

MAIN_IP_ADDRESS_BODY = """<soapenv:Envelope
 xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
 xmlns:job="JobModify" xmlns:wor="WorkflowDesc">
	<soapenv:Body>
		<job:JobModifyReq Cmd="Start" OpV="01.00.00" JId="[jid]"
		 ConsistencyBL="noerror_nowarning"
		 RebalancingMode="RebalancingNotAllowed">
			<wor:Job name="[job_name]" workflowIdRef="[wid]">
				<wor:ParamDesc value="[ip_address]" name="IP address" />
			</wor:Job>
		</job:JobModifyReq>
	</soapenv:Body>
</soapenv:Envelope"""

BACKUP_IP_ADDRESS_BODY = """<soapenv:Envelope
 xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
 xmlns:job="JobModify" xmlns:wor="WorkflowDesc">
	<soapenv:Body>
		<job:JobModifyReq Cmd="Start" OpV="01.00.00" JId="[jid]"
		 ConsistencyBL="noerror_nowarning"
		 RebalancingMode="RebalancingNotAllowed">
			<wor:Job name="[job_name]" workflowIdRef="[wid]">
				<wor:ParamDesc value="[ip_address]" name="Backup input IP address" />
			</wor:Job>
		</job:JobModifyReq>
	</soapenv:Body>
</soapenv:Envelope"""

MAIN_UDP_PORT_BODY = """<soapenv:Envelope
 xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
 xmlns:job="JobModify" xmlns:wor="WorkflowDesc">
	<soapenv:Body>
		<job:JobModifyReq Cmd="Start" OpV="01.00.00" JId="[jid]"
		 ConsistencyBL="noerror_nowarning"
		 RebalancingMode="RebalancingNotAllowed">
			<wor:Job name="[job_name]" workflowIdRef="[wid]">
				<wor:ParamDesc value="[udp_port]" name="UDP port" />
			</wor:Job>
		</job:JobModifyReq>
	</soapenv:Body>
</soapenv:Envelope"""

BACKUP_UDP_PORT_BODY = """<soapenv:Envelope
 xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
 xmlns:job="JobModify" xmlns:wor="WorkflowDesc">
	<soapenv:Body>
		<job:JobModifyReq Cmd="Start" OpV="01.00.00" JId="[jid]"
		 ConsistencyBL="noerror_nowarning"
		 RebalancingMode="RebalancingNotAllowed">
			<wor:Job name="[job_name]" workflowIdRef="[wid]">
				<wor:ParamDesc value="[udp_port]" name="Backup input UDP port" />
			</wor:Job>
		</job:JobModifyReq>
	</soapenv:Body>
</soapenv:Envelope"""




