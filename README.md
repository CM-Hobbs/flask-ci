# FLASK CI/CD Practice

### Building the requirements / requirements-dev files
- Used the small sh script in project root dir make_reqs_uv.sh
- Uses uv to build from the pyprojects.toml file - no hands on

# pytest unit testing
- Very simple test against bad urls (whitespaces) in the GETS and the outputs of an internal 'normalise name' func

# github actions workflow
- Spins up an ubuntu VM
- Clones my repo and installs a py interpreter
- installs my repo using -dev requirements again using uv
- runs pytest -v
- If passes builds a docker image and tags it with the github session sha

# Running the docker image
- The socket/port is listed in the dockerfile so run docker inspect to find (8000)

## From GHCR:
````bash
# get the SHA from an existing container if running on /healthz or off the packages tab on github
docker pull ghcr.io/cm-hobbs/flask-ci:$SHA

docker run -rm -p 8000:8000
````
