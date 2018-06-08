name = "Thomson"
from .thomson import Thomson
from .node import Node, NodeDetail
from .job import Job, JobDetail
from .workflow import Workflow, WorkflowDetail
from .log import Log

help = """Web Service Operations can be performed at the following levels:
 - System (Thomson, Nodes, NodeDetail)
 - Workflows (Workflow, WorrkflowDetail)
 - Jobs (Job, Job Detail)
 - Logs (Logs, LogDetail)


* Workflow Web Service Operations
 - instant class Workflow(host = "ip-vs700", user = "username", passwd = "password")
   + function:  get_workflow(): Returns the whole list of
    workflow identifiers that you are
    entitled to see and provides their
    current version

 - instant class WorkflowDetail(host = "ip-vs700", user = "username", passwd = "password", wid = int(workflow id))
   + get_param(): Returns the list of public
    parameters that shall be filled to
    create a job


* Job Web Service Operations
 - instant class Job(host = "ip-vs700", user = "username", passwd = "password")
 - funtion:
   + get_job(): Gets the whole list of jobs that you are entitled to see
   + get_waiting(): Gets the whole list of waiting jobs that you are entitled to see
   + get_running(): Gets the whole list of running jobs that you are entitled to see
   + get_paused(): Gets the whole list of paused jobs that
you are entitled to see
   + get_completed(): Gets the whole list of completed jobs that you are entitled to see
   + get_abort(): Gets the whole list of abort jobs that you are entitled to see
   + get_job_status(): Count qty job by state

 - instant class JobDetail(host = "ip-vs700", user = "username", passwd = "password", jid = int(job id))
 - Function:
   + get_param(): Returns information about job
    parameters in terms of
    instantiation
   + start(): Starts a job
   + abort(): Abort a job
   + delete(): Delete a job
   + restart(): Restart a job


* System Web Service Operations
- instant class Thomson(host = "ip-vs700", user = "username", passwd = "password")
- funtions:
   + get_datetime(): Gets the system date and time
   + get_mountpoint(): Retrieves the network storage
settings
   + get_system_status(): Get performmance hardwarre
   + get_license(): get license info

- instant class Node(host = "ip-vs700", user = "username", passwd = "password")
- functuons:
   + get_info() get performmance for each node(blade)

- instant class NodeDetail(host = "ip-vs700", user = "username", passwd = "password", jid = int(job id))
   + get_list_job() get performmance for node(blade) by id and job running list on node


* Log Web Service Operations
- instant class Log(host = "ip-vs700", user = "username", passwd = "password")
   + get_log(): Retrieves logs in update mode
    (i.e. only the new log operations
    are transmitted)
   + get_by_jobID(): get logs on job by jobid"""
