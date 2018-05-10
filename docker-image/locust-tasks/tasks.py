import uuid

from datetime import datetime
from locust import HttpLocust, TaskSet, task


class MetricsTaskSet(TaskSet):
    _deviceid = None

    def on_start(self):
        self._deviceid = str(uuid.uuid4())

    @task(1)
    def getApiValues(self):
        self.client.get(
            '/api/values')

class MetricsLocust(HttpLocust):
    task_set = MetricsTaskSet

