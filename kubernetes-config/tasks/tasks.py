import uuid

from datetime import datetime
from locust import HttpLocust, TaskSet, task


class MetricsTaskSet(TaskSet):
    _deviceid = None

    def on_start(self):
        self._deviceid = str(uuid.uuid4())

    @task(1)
    def getApiValues(self):
        self.client.get('/api/values')
        #self.client.get('/api/v1/consentData/101')

class MetricsLocust(HttpLocust):
    task_set = MetricsTaskSet

