from locust import Locust, TaskSet


def bounds_was(l):
    l.client.get("/bounds/?sw_lat=38.75140585784823&sw_lon=-77.3736190795899&ne_lat=39.07197839072956&ne_lon=-76.6814804077149&is_temp_dis=true")

class UserBehavior(TaskSet):
    tasks = {bounds_was}

    def on_start(self):
        pass


class WebsiteUser(Locust):
    task_set = UserBehavior
    min_wait = 10
    max_wait = 10
