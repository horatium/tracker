# tracker

Description
-----------
a small tracking service that receives data from a GPS tracker device.

In the beginning of a track, it requests a route to be created, then continuously populates it with data points (WGS84 coordinates). Eventually a request to calculate the length of the route is made.
There is an additional endpoint that returns the longest route of the day.

To see all the available endpoints go to the homepage http://localhost:5000.

### System requirements

    docker

### Basic dev setup

* `git clone git@github.com:horatium/tracker.git`

* `cd tracker`

* run docker compose :

    `docker-compose up`

* you'll have to manually do a :

    `docker-compose run --rm web django-admin.py migrate`

* for accessing the app in browser go to http://localhost:5000

### Tests requirements

    virtualenv

* to be able to run the tests on local environment do:
    
    `virtualenv test`
    
    `source test/bin/activate`
    
    `pip install -r requirements.test.txt`
    
* to run the original test:    
    `pytest -vvv tests/initital_integration_test.py`
    
* to run the final form of the integration tests:
    `pytest -vvv tests/integration_test.py`


