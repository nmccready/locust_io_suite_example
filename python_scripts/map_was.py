from locust import Locust, TaskSet


def map_was(l):
    l.client.get("/city/was")

class UserBehavior(TaskSet):
    tasks = {map}

    def on_start(map_was):
        pass


class WebsiteUser(Locust):
    task_set = UserBehavior
    min_wait = 10
    max_wait = 10
