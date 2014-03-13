from locust import Locust, TaskSet
import random

def bounds_was(l):
    l.client.get("/bounds/?sw_lat=38.75140585784823&sw_lon=-77.3736190795899&ne_lat=39.07197839072956&ne_lon=-76.6814804077149&is_temp_dis=true")

def bounds_nyc(l):
    l.client.get("/bounds/?sw_lat=40.51337536952665&sw_lon=-74.26519009765627&ne_lat=40.82585855240282&ne_lon=-73.62248990234377&is_temp_dis=true")

def map_was(l):
    l.client.get("/city/was")

def map_nyc(l):
    l.client.get("/city/nyc")

def token(l):
    l.client.get("/token/url/%i" % random.randint(1,100))

class UserBehavior(TaskSet):
    tasks = {map_was:4,map_nyc:4,get_bounds_was:3,bounds_nyc:3,token:2}

    def on_start(self):
        pass

class WebsiteUser(Locust):
    task_set = UserBehavior
    min_wait = 10
    max_wait = 10
