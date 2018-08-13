from datetime import datetime
import requests


SERVICE_ENDPOINT = 'http://localhost:5000/'
ROUTE_ENDPOINT = "{}route/".format(SERVICE_ENDPOINT)
ROUTE_ADD_WAY_POINT_ENDPOINT = "{}{}/way_point/".format(ROUTE_ENDPOINT, "{}")
ROUTE_LENGTH_ENDPOINT = '{}{}/length/'.format(ROUTE_ENDPOINT, "{}")
LONGEST_ROUTE = '{}longest/{}/'.format(ROUTE_ENDPOINT, "{}")


class TestRoute(object):
    wgs84_coordinates = [
        {"lat": -25.4025905, "lon": -49.3124416},
        {"lat": 59.3258414, "lon": 17.70188},
        {"lat": 53.200386, "lon": 45.021838}
    ]
    cluj_wgs84_coordinates = {
        'lat': 46.7833643,
        'lon': 23.546473
    }
    def setup(self):
        self.route_post = requests.post(ROUTE_ENDPOINT)
        route = self.route_post.json()
        self.route_id = route['route_id']
        self._push_route(self.route_id, self.wgs84_coordinates)
        self.length_get = requests.get(ROUTE_LENGTH_ENDPOINT.format(self.route_id))
        self.longest_route_id = None

    def _push_route(self, route_id, waypoints):
        for coordinates in waypoints:
            requests.post(ROUTE_ADD_WAY_POINT_ENDPOINT.format(route_id), json=coordinates)

    def test_length_calculation(self):
        length = self.length_get.json()
        assert 12975 < length['km'] < 13025

    def get_longest_route_of_the_day(self):
        # get today's longest route
        today = datetime.strftime(datetime.today(), "%Y-%m-%d")
        longest_get = requests.get(LONGEST_ROUTE.format(today))
        return longest_get.json()

    def test_longest_route(self):
        longest_route = self.get_longest_route_of_the_day()
        longest_route_waypoints = longest_route['longest_route']['way_points']
        waypoints = [{'lat': float(wp[0]), 'lon': float(wp[1])} for wp in
                     longest_route_waypoints]
        longest_route_id = longest_route['longest_route']['route_id']
        # create new route
        new_route_post = requests.post(ROUTE_ENDPOINT)
        new_route = new_route_post.json()
        new_route_id = new_route['route_id']
        # add new waypoint
        waypoints.append(self.cluj_wgs84_coordinates)
        self._push_route(new_route_id, waypoints)
        # get the longest route again
        new_longest_route = self.get_longest_route_of_the_day()
        # assert that newly created route is the new longest route of the day
        assert new_longest_route['longest_route']['route_id'] != longest_route_id
        assert new_longest_route['longest_route']['route_id'] == new_route_id
        self.longest_route_id = new_route_id

    def teardown(self):
        requests.delete("{}{}/".format(ROUTE_ENDPOINT, self.route_id))
        requests.delete("{}{}/".format(ROUTE_ENDPOINT, self.longest_route_id))
