import pytest
from flask_ci.main import app, normalise

### PYTEST UNIT TESTING ##########################################################################
'''
Add 'client' to the pytest fixture (pytests 'plumbing' that runs tests for us)

Set the Flask app to TESTING (for debug msgs) and setup a generator context to yield the app.test_client() for the 
rest of the pytest functions

When pytest runs (triggered by pyproject.tomnl on build) it sees the pytest.fixture, creates the test_client
and pytest then one by one goes through the test functions sending it the test_client()

The "with, yield app.test_client()" creates a new test client for each test and breaks it down gracefully for us

LIMITATION: Only tests known errors structures. py hypothesis module can be used to suto generate
multiple other inputs for test.

As project develops and errors occur - make the pytest first - confirm it captures the error - then fix the error
'''


### SETUP THE TEST CLIENT

'''
Create our testing fixture. 

Pytest looks for fixtures when params are passed to each test
ie my test(greet(client) - pytest then looks for a pytest fixture: client

Cant just pass a func calling
the app.test_client() - pytest wont accept it
'''
@pytest.fixture
def client():
    app.config["TESTING"] = True # set the flask app to TESTING for debug output
    with app.test_client() as c:
        yield c


### TESTING THE NORMALISE FUNCTION

'''
pytest.mark manages pytest metadata/params
here params is used to send the test data to test_normalise() - could have just hard coded but learning
'''
@pytest.mark.parametrize("raw, expected", [("Chester ", "chester"), ("CHESTER MAYNARD","chester maynard"),("Hobbs","hobbs"),]) # my set of test pairs: (test entry,correct result)
def test_normalise(raw, expected):
    # use an assert test to see if the normalised raws == expected
    # better than a loop because if one fails doesnt just end
    # why not a loop with try/exceptions?
    assert normalise(raw) == expected

# Test if send wrong type
def test_normalise_rejects_non_string():
    with pytest.raises(TypeError):
        normalise(42)

# Test if send white space only
def test_normalise_rejects_non_string():
    with pytest.raises(ValueError):
        normalise("   ")

### TEST THE HTTP GETS

def test_greet(client):
    '''
    Send put some whitespace around entered name, 
    send app.greet and assert it returns a 200 OK http response and that the json retuned is correct
    '''
    r = client.get("/greet/%20%20Chester%20%20") # %20 is http for whitespace
    assert r.status_code == 200
    assert r.get_json()["timmy"] == "awesome" # remember: get_json() returns a dict (json in - py dict out)

def test_healthz(client):
    '''
    No tricks here - just test healthz
    '''
    r = client.get("/healthz")
    assert r.get_json()["status"] == "ok"

def test_greet_empty_name_returns_400(client):
    '''
    Send app.get("greet/<name>") but send it some whitespace
    '''
    r = client.get("/greet/%20%20%20")
    assert r.status_code == 400
    assert "error" in r.get_json()


