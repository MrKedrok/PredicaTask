import requests
from datetime import datetime
from skidservice_lib.config_manager import ConfigManager
from skidservice_lib.exceptions import SkidServiceBaseException


class MetadataApiClientException(SkidServiceBaseException):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return "Metadata API call failed (#{self.status_code}): {self.message}"


class MetadataApiClient:
    date_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z")

    @staticmethod
    def get_token():
        try:
            access_token = MetadataApiClient.mi_token()
        except Exception as e:
            if "ManagedIdentityCredential authentication unavailable" in e.message:

                access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6ImppYk5ia0ZTU2JteFBZck45Q0ZxUms0SzRndyIsImtpZCI6ImppYk5ia0ZTU2JteFBZck45Q0ZxUms0SzRndyJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldC8iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8zNTk2MTkyYi1mZGY1LTRlMmMtYTZmYS1hY2I3MDZjOTYzZDgvIiwiaWF0IjoxNTk5NTc0NzI3LCJuYmYiOjE1OTk1NzQ3MjcsImV4cCI6MTU5OTU3ODYyNywiYWNyIjoiMSIsImFpbyI6IkUyQmdZRGc2SzBuemttajdmL0ZGWnpkL3ZCKzhNa0NjcS8xYnRLTElsdDZsQ1cyQllub0EiLCJhbXIiOlsicnNhIl0sImFwcGlkIjoiMDRiMDc3OTUtOGRkYi00NjFhLWJiZWUtMDJmOWUxYmY3YjQ2IiwiYXBwaWRhY3IiOiIwIiwiZGV2aWNlaWQiOiIwZWQ2YzNhNy0wOWQ2LTQ5N2QtYjExNy1hZGE3YWRlMTBjM2YiLCJmYW1pbHlfbmFtZSI6Ik1hamNoZXIiLCJnaXZlbl9uYW1lIjoiQWxiZXJ0IiwiZ3JvdXBzIjpbImIxZjk1NzY4LWQ1ODUtNGRlOC1iNTFhLWUwMGZmMzEzNjIxNSIsIjdjMjkyMDliLWU1NDAtNDI5YS1iYmJlLTg0MjA1OWNkMTJlOSIsIjgwMjY4ZGE5LWQxNDAtNDJlNy05ZDkyLTA1ZDg1NWJhZGIyZiIsIjY0NzA4MzA0LTRlYTMtNDE2OS05ZDY1LTIxNzU2NWI4YWU1NyIsImExMTIxYjFjLTllZjQtNDgwZC04MTFjLWQyODQ1MzdjZjIzNSIsIjA0MzkzZjBlLTYyZWYtNDlmMy1iYmRjLTIzMjJmYmVkNzkzNSIsIjhkMGM5MTRkLTQxNTAtNGEyYS1hZThjLTlhZWYwMDlmNzU4NyIsIjVkMjViYzdkLTBhZDItNDkxYS04MTYxLWQ3YjNlOTZkNjRhMiIsIjY4NzgwZmU5LTg1MmQtNDA2Ni1hMzljLTc0NDJlZWFhOTI4OCIsImJmMjI4OTMxLWFjMDgtNDliYy04ZjQ3LWIwMWE2NjE2M2Y1ZCIsIjYwYjM0Mjg4LWYyZmYtNDYxNy04NzgxLTY5Y2Y1OWZiOWI3YiIsImUzNGZjNDQ5LThkMjUtNGE4ZS1iMWY2LWM0ZTUxMzU0N2IwZCIsImEwZWY5NjY2LTI2NzctNDYwZi1hYmE3LTk1M2I3ZTA5ZDJhMCIsImQ4M2VlMTYyLTljYjMtNDJmNi1iNWFjLTUxYWU1MDAyNGQ5ZiIsIjI1NjYzNGE5LTRiMzAtNGFmZi1hZjBkLTRmZjA3NWRlZjJiYiIsImUyNzQyNzg5LWEzODUtNGVlNy05ZTRiLTI4ZGQwNTRjMzhhNCIsImZlMGJmNTE0LTliZWYtNDdmZC1hZGY3LTQ4NDQzMGYyZWVhYiIsIjNhYTU3MjQwLTkzZDYtNGQyMy1hZWQyLTAxZTMxMDE4ZTFjNCIsIjU5YTRhNjliLTIyOGUtNDcyZC1iMGY5LWNiMWE2ODAyNWNkZCIsIjU0MmViYmM3LThhYWEtNGJjMy1hM2U2LWNiYTE4MTJlNjRhMSIsIjU3MzYxNWVkLTJiNjUtNDBhOC1iOTQzLTAwOTNiZTMwZmY4ZiIsImY5MzAzNmY0LTMwMTctNDA1Zi05NTM4LTIzMzM3ZDJiYTM0ZCIsIjQ1YTBiOTQxLTBkMTYtNDg4ZS04ZTllLTk1ZjZlZWU0NDYyOSIsImUxNzRhNWFmLTIwZDYtNGZhMS05ZDQyLTQ4MTg5YmFlYjczNCIsImUwNWE5NGEwLTY5ZTItNDU1MS04NDc0LWFmNGNmNDIzNWZiZSIsIjY4M2I1NDcxLTJkZDItNGExNC1iY2I4LTU0NjdhMzllNGMxMiIsIjU3MGQ0OTEyLWJjZTUtNDBmMi05NDU5LTJiNTlhMjZiMGU0MiIsImYxNzdhOGU5LWVhNzgtNDI5Mi04MjQxLTExYjljOTk4OWI0OCIsIjQ3YTlhZjBhLTA1NGItNGU1Ny04MjYxLTU4Zjc1M2NiYWYwOCIsImQ4ZmEyZDI1LWI4NGQtNGQzYi1iZjczLTBhMGZjYThiYmY3NiIsIjc2MmI0YTBiLTBlNzUtNGZjZS04ODJlLTI4ZjRhMWU2YzRiMCIsIjVkMGE2ZGI4LWU5YTktNGZlZi1iYmYzLWU5ZjE0ODlmODNlNSIsIjcxZGE2ZGUxLTM5MWQtNGM3Yi04Njc2LTU4OTg1ZTkwNzVkZCIsIjZmNzdkNmU3LTY3ZTUtNGNmNy04NmQ3LWM0NmQxMDU1NTM1NCIsIjE0ZDEzYTI2LTMyODQtNGMxYS1iMDVjLTA5ZmQ3MDIwZDIyNiIsIjBkNTgyZWQ2LWQ3YzgtNDdjMC05ZGFmLWM3OGVmOWY4ZDY2NyIsImIzMDIzZWI2LTQ4MDItNGFkYy1hOTA0LTFmNTAyOWVlMjRhMCIsIjQwNTdlYjE3LWIzN2UtNGRlOS05NmJmLTIyZjcwNzRmNmE4YyIsIjZjMjkwMjQ2LTI2NDQtNDlkMS05NmQwLWI4MTM3MGQxOGJmZSIsIjQ1ZTRjOTE0LWNhNWYtNDAzNy04MTU3LWE2ZjRlMTk4MDQ1MyIsImRhZWYxODc3LWYzNTItNDIyNi05Mjg2LTY2Yzg2Njc4NjI5YyIsImM5NGU4MTk2LWRmZTMtNDhkNy04NDRhLTY5OTg0ZmU1Y2FiZSIsImY5NmYzYmRkLTYwOTItNGIyYy04Nzc2LWMxNzM4OGJmOWMyMSIsImE2OGZiZGNkLTA4MzEtNDBhOC04MmQ2LWUxNTA5MzRkNWNiZiIsIjY4NmY2N2NiLWNmMjUtNGVkNi1hM2JlLTFjNmU0MjgwOGQ2NiIsIjI4OTViMTM1LWVhM2QtNDdiNS05ZjRmLTFlYTQxYTcwYWJkOCIsIjBkMGZlMTdhLWRjYTYtNGY2My04NGUxLTM5OGRkMjZjMzk1MiIsImEwMGY4MGVkLWE2NmMtNGM1ZC04OWI2LWJlYmMyNDIwMmZiZiIsIjBlYjE3NDExLTQ1YmEtNDJiOC05MzgxLWQ5MDBlZWZhNmYxMSIsImFkYjBkNzI0LTVlZTMtNGVhZC05NjE2LTVhMmU0NjNjZmE1NSIsIjU3M2RlZjgzLTIxOGItNGE1NS1iNGFjLWUxYTYxMmZmZDUzZCIsIjQ2ZWFkYTNmLTI1M2MtNGIyMi05ZmE0LWMxYzc5Njg1ZjcyMSIsIjE0Y2JhN2U2LTNlNmMtNGUxMC1hZjBkLTBlYzkyMWM2OGMyZiIsIjljMjVjMGFjLTVhMDItNDMzMi1iMDEzLTMyMTUzYjY0ZGE3ZSIsImYzYWFmZjQ2LTg2MDAtNDEwYi04OTJlLTE1YjZiYjY3ZjU0MyIsImUwMzFkMjBiLWJiNWEtNDg3MS1hYzU0LTQ5NGI5MGVlYzJmOCIsIjJkYjVhNzQ3LTBlYzgtNDZlOS1hNDQzLTA4ZWZmMmFiYzcwYyIsIjMyNDMxMTdjLWNlMjMtNDRjMy04NjBhLTNhNzI3N2U0ZDdlZiIsImU1YzQ1OGMxLTE3OTYtNGEwMi04MTkxLTc0NTg2N2ExODgwZSIsImFhODhjYTlkLTdjOTItNDlmZC1hZDYzLWFmZDI2OTFmODE2MSIsImZkZjY1ODM2LTY0OTYtNDliZi1hOTdkLWJlOTk5MWFlOGE3NSIsImM0ZjJhZmQyLTI2NGYtNGYyMS1iZDY0LWZhMGIwOGIyZjVmMyIsIjRiYjdlYTQwLWM1YzMtNGU5MS05NDZjLTE2YmU0ZmY4YTg1NyIsIjZlZTUzNDVjLTBhODItNDllMi1iY2NhLWMwYTVmMWQ0YWEyOCIsIjQxYjExYjljLTMyNDgtNDE3Mi1iOWIyLTc4ODc5NThkNDE4MiIsImY5MzFlZGYwLTlmY2QtNGUzMi04NTFkLWEyMWVjZGFmMjU4MSIsIjMxZjZkYzhmLTkwYjQtNDUwNS1iNGVjLWZmOTI1OTM3YmQxMyIsIjZmYzE5NmMyLWQ4ZjgtNDllNC05NjUwLWE3Njc1MDkwZjkzNyIsImY4ZmEwMGIwLWZiYTQtNDgzNC1hNThiLTQ2ZjkyZjA0MzZjNiIsIjZkMmQ5NTE0LWE1MmMtNGY5Ny1hMTUyLWM4YjhlOWFmMjY0MiIsImY4NDAzNzljLWQxY2UtNDFiNi1iMjA4LWJlMTBlNWEzOGJiOCIsImU1ZWZmOTUxLWI0NGUtNDIzZC05MDY5LTk4MmY0NmQ2ZWVhZiIsImQzNGU4MzgwLTRhZjMtNDk5My05Mjg5LTA5ZWQxOTI3M2JmYyIsIjgyN2U0MjdmLWViNmYtNGMwOC1hMjVkLThlM2UxNWRhMGRiMCIsImE2MjA3NGY2LTMzNmYtNDhkYS05MWI4LTAyN2NkYzZkODM5NyIsIjU4ZTdmYWU2LTlmYzQtNGRiMi04YmRlLWNmOTI4Y2ZjNGVhMyIsIjJiYmY2N2MyLTZjZTQtNDQ3Yi05ZjI1LWU0NWY1ODcwMmZkOCIsImZhNTY5YTU3LWRkMzktNDU5ZC05Y2ZkLTdhZTRjMTk4ZmU1NiIsIjFhNDU5Y2ZhLTU1NDgtNDk5MC1iZjFkLWQ0Yzc2NTA3ODQ1YSIsIjJlNWY4YjZhLTU5OTktNDAyOS05MzJhLTk1YWUyNDQzMDNmYyIsIjAwNjA4ZjVjLThlMDUtNDc0NS1iZmYzLWZmMzA5MzE5ZGUyYyIsImYxMDgxMzZjLWFjNWUtNGIxNC1hZGUxLTVlYzI2NTYzNTVhMCIsIjNlZjk1NWRlLWZiYWUtNDBjOS1iMDc0LTRiY2RhYWJhMGNlOCIsIjJkOTZkMTExLTYxMDItNGI1ZS1hODhkLWRjMWQ4ODU0MmMwMiIsImQyMTIyMjhjLTY2MjYtNDA2NS1hZmNjLTUwNzEzMzQyYjVmOSIsIjEzOTUyZDQ0LTA4MTktNDUwMi05ZmY0LTRjZWEzODJiMGM3MCIsIjY4ODUxMmNjLWE4MGQtNGEzZi1iY2JjLTVkZjY5OWMyNTI2ZCIsIjhmYTFhNjMyLTYyMDEtNGU0OC1hYmY0LWZhOTkzMGM3MDlhNCIsImU3NTRlYTNjLTg4M2MtNDE2OS1hNzRjLTRjZTk3NTU0YzhkYyIsIjhiOWU3ZmIzLWQ1MDItNDQ0Mi1hMDJlLWFmZmNkMjY1YmE1MSIsIjY2MjZkOWIwLWRlYTQtNGUxMi1iNmY2LWU4ZmQ4NmE4MGNhOCIsImIzZTM2MGNlLWQ0ZjAtNDFkYy1hNWU5LThkOTg4Y2E3OWZhOCIsImMxMmU1OWUwLTBlNmYtNGY1OC05YTM5LWUzMWEyMmY4YzFlYyIsIjBjMWFmZGJkLTkxNmItNGM5ZC1iZTgzLTFiMGFhMWU3NmMwYyIsImE4MTYyNGQ4LTc5ZWMtNDIzMi1iMzkzLWQ0MDI2ZjdkNjc0YSIsImVlYjgxZThkLWU1OGUtNDQ5ZS1iMTZhLWQzMTNlNGNmNjMxZSIsIjdmNTQzYjBkLWNkODUtNDUxZi1iNzYxLWJiZGMyNTFmMTRlYyIsImVmOTA4ZWIwLTFiNWQtNDI0MC04ZDMyLWRhZjhhN2E1NjJkYiIsIjYzNTc3ZDZmLWFmMGEtNDRlOS05N2NhLTJlYzdlM2NmYWEzMyIsImIyY2ZjNmQ1LTMwNjgtNDEwYi04ZWQ4LTJhY2ZhOTA1MTk5YiIsImRkNDlmYWRhLTM3ZWMtNGRmNS04NDU5LWRmYTkyZDBmOTljYSIsIjgwMzI1Yzg3LWZlNzItNGY0My04ZGNhLTI3NTYxYzc1ODY1NCIsIjcwMzc2NTM4LTU4MGMtNDExMC04YjcxLTAxNmYwMjM1YjRmZiIsImU2YWEwNDRmLTRmMjktNDJmOC1iYTAyLTg3YTAxNDA5ZGFlMCIsImEzNzE5NzY5LTUyN2ItNDZkNy1hZDFhLTY4ZDkzNmMwMWEwZSIsIjc1OTdmZmFiLWUzYzQtNDg4MC1iMjgyLWYyYTBiZjJiNjIxOCIsIjBkNDI2ZjVkLTVhN2MtNGI2Ni1hOWFlLTAwODVkYjJlYmFmZSIsImM5MThjMTVkLTJjODctNDdlYS05OTI5LWEzNzA0ZGRiMzE0OSIsIjg4MDVlZDdjLTUyYzEtNDRmMC1hZDFmLTYzZDliYmUzYzE4MiIsImJlZmZlODQ0LTA4MjctNDVkOS1iODBjLWRjZGUzZDRkNzM2NiIsImYxY2EwY2FkLWFlYjAtNGQxYy05ZTYzLTJkZmY2YjhkMmY5YSIsIjg2ZmZiZGJjLWI5ZGUtNGQ4NC1iYzMyLTUyZmUxNzY3MGIyMyJdLCJpcGFkZHIiOiI3OS4xOTEuMjUuMTE5IiwibmFtZSI6Ik1hamNoZXIsIEFsYmVydCIsIm9pZCI6IjU1ZDk4MDg5LWMwNGItNGViOS1hMGFlLTQ0Y2E3YzhkM2U3YiIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS0xNTE5NjEwODI2LTIwNTI5NDYwNzctODc5OTcyMzYzLTMxMzYzOCIsInB1aWQiOiIxMDAzMjAwMEJGREFERUM3IiwicmgiOiIwLkFRZ0FLeG1XTmZYOUxFNm0tcXkzQnNsajJKVjNzQVRialJwR3UtNEMtZUdfZTBZSUFHMC4iLCJzY3AiOiJ1c2VyX2ltcGVyc29uYXRpb24iLCJzdWIiOiJOU0EtYU9EcTc4WS1ESXJoMkQxTWdFV0lDbnViNDE5WW5PUkpZUjZfSmZvIiwidGlkIjoiMzU5NjE5MmItZmRmNS00ZTJjLWE2ZmEtYWNiNzA2Yzk2M2Q4IiwidW5pcXVlX25hbWUiOiJtYWpjaGVyLmFtQHBnLmNvbSIsInVwbiI6Im1hamNoZXIuYW1AcGcuY29tIiwidXRpIjoiamNXZUhzWEszMENpaHhiM2ZkZ1RBQSIsInZlciI6IjEuMCIsInhtc190Y2R0IjoxMzcyNDQwMjg5fQ.uff-mMk2DgEZLIOYT502UDRsNboDcUGCg3Vp40kFOAu6nXZ1xIz2yermAknfrqg9QoPOKtSF44I6sNyv40MH_ytwU1c-hLSVfq0nPaNtDTi40Na-CiZo27Ah5mzxtphyP5icTN-03n5wkXUC2sDFGau0FnlSzssGxpITvD-tP0r4CNWQoucRIaZ1TGc97cMiKASa9XXRqPHv5eMy8bju0mHuWaQwokoCPU4EO72w43hqTd_YD3IDSmpwK77IwT--_4vVTRESOTdmoV2m4QybicIU4nHmLsuKWTz_iqG6hIlsRufo5rOfab92-vU6I7910Ndf0fBW0XxHBBwvk5axMg"
            else:
                raise Exception(e.message)
        return access_token

    @staticmethod
    def mi_token():
        from azure.identity import ManagedIdentityCredential
        resource_id = ConfigManager.get_config().metaapi_resource_id
        credentials = ManagedIdentityCredential()
        client_token = ManagedIdentityCredential.get_token(credentials, resource_id)
        access_token = getattr(client_token, "token")
        return access_token

    def _call(self, endpoint, payload=None, method="GET"):
        url = f"{ConfigManager.get_config().metadata_api_url}{endpoint}"
        headers = {"Authorization": f"Bearer {self.get_token()}", "Content-Type": "application/json"}
        if method == "GET":
            response = requests.get(url=url, headers=headers)
        elif method == "POST":
            response = requests.post(url=url, json=payload, headers=headers)
        elif method == "PUT":
            response = requests.put(url=url, json=payload, headers=headers)
        else:
            raise SkidServiceBaseException("this method of calling is not supported")

        if response.status_code not in range(200, 300):
            message = response.json()["message"] if response.text.startswith("{") else "call failed"
            raise MetadataApiClientException(
                status_code=response.status_code,
                message=message)
        return response if response.text != "" else response.status_code

    def get_process_run_parameter(self, process_run_key: int):
        return self._call(
            endpoint=f"/api/v1/runParameters/{process_run_key}/variables/PROCESS_RUN_OBJECT_PARAMETER/")

    def add_dataset_assoc(self, object_key: int, process_run_key: int):
        payload = {
            "objectKey": object_key,
            "processRunKey": process_run_key,
            "processRunObjectAssocTypeCode": "INPUT"
        }
        return self._call(
            method="POST",
            endpoint="/api/v1/process-run/dataset-assocs",
            payload=payload)

    def add_process_execution(self, process_key: int):
        payload = {"lastUpdateDatetime": self.date_time,
                   "parentProcessRunKey": 0,
                   "priorityNum": 0,
                   "processKey": process_key,
                   "processStatus": "PREPARING",
                   "processType": "EXECUTABLE",
                   "scheduleDatetime": self.date_time,
                   "scheduleStatus": "PENDING",
                   "startDatetime": self.date_time}
        return self._call(
            method="POST",
            endpoint="/api/v1/processExecutions",
            payload=payload)

    def update_process_execution_status(self, process_key: int, process_run_key: int):
        payload = {"processKey": process_key,
                   "processRunKey": process_run_key,
                   "processStatus": "COMPLETED"}
        return self._call(
            method="PUT",
            endpoint="/api/v1/processExecutions",
            payload=payload)

    def add_physical_datasets(self, object_name: str, infra_key: int, partition_definition_value: str,
                              process_run_key: int):
        payload = {
            "objectTypeCode": "PHYSICAL_TABLE_PARTITION",
            "parentLogicalObject": None,
            "objectName": object_name,
            "objectDescription": "inc_surrogate_key_lkp",
            "fileTypeCode": "parquet",
            "statusCode": "STAGING",
            "dataProviderCode": "MDM",
            "dataTypeCode": "CDL",
            "owningApplicationName": "MDM Refined",
            "infrastructureKey": infra_key,
            "partitionDefinitionValue": partition_definition_value,
            "objectSizeInKb": None,
            "processRunKey": process_run_key,
            "secureGroupKey": 0
        }
        return self._call(
            method="POST",
            endpoint="/api/v1/datasets/physical",
            payload=payload)

    def add_parameters_post(self, object_key: int, process_run_key: int):
        payload = {
            "processRunKey": process_run_key,
            "processRunParameterKey": 1,
            "processRunParameterName": "PROCESS_RUN_OBJECT_PARAMETER",
            "processRunParameterType": "VARIABLE",
            "processRunParameterValue": str([{"object_key": object_key, "parameter_value": "INCREMENTAL", "parameter_name": "RELOAD_TYPE"}])
        }
        return self._call(
            method="POST",
            endpoint="/api/v1/runParameters",
            payload=payload)

    def add_parameters_put(self, object_key: int, process_run_key: int):
        payload = {
            "processRunKey": process_run_key,
            "processRunParameterKey": 1,
            "processRunParameterName": "PROCESS_RUN_OBJECT_PARAMETER",
            "processRunParameterType": "VARIABLE",
            "processRunParameterValue": str([
                {"object_key": object_key, "parameter_value": "INCREMENTAL", "parameter_name": "RELOAD_TYPE"},
                {"object_key": object_key, "parameter_value": "FULL", "parameter_name": "RELOAD_TYPE"}])
        }
        return self._call(
            method="PUT",
            endpoint="/api/v1/runParameters",
            payload=payload)

    def trigger_process(self):
        # TODO:  implement this method correctly
        return self._call("/test")
