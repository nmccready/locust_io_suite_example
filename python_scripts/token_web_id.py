from locust import Locust, TaskSet


def token(l):
    l.client.get("/token/url/20")

class UserBehavior(TaskSet):
    tasks = {token}

    def on_start(self):
        pass


class WebsiteUser(Locust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 1000  # hitting at 10 persecond
