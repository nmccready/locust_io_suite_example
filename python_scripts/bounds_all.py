from locust import Locust, TaskSet


def bounds(l):
    l.client.get("/bounds/?sw_lat=-90&sw_lon=-180&ne_lat=90&ne_lon=180&is_temp_dis=true")

class UserBehavior(TaskSet):
    tasks = {bounds}

    def on_start(self):
        pass


class WebsiteUser(Locust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 1000  # hitting at 10 persecond
