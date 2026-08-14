# FLASK CI/CD Practice

### Building the requirements / requirements-dev files
- Used the small sh script in project root dir make_reqs_uv.sh
- Uses uv to build from the pyprojects.toml file - no hands on

### pytest unit testing
- Very simple test against bad urls (whitespaces) in the GETS and the outputs of an internal 'normalise name' func

### github actions workflow
- Spins up an ubuntu VM
- Clones my repo and installs a py interpreter
- installs my repo using -dev requirements again using uv
- runs pytest -v
- If passes builds a docker image and tags it with the github session sha

### Testing the docker image
- The socket/port is listed in the dockerfile so run docker inspect to find (8000)

#### From GHCR:
````bash
# get the SHA from an existing container if running on /healthz or off the packages tab on github
docker pull ghcr.io/cm-hobbs/flask-ci:$SHA

docker run -rm -p 8000:8000
````

### Deploying the image on a second box with docker compose

#### On the prod box
markdown
```
opt/
├── flask-ci/
│   ├── compose.yaml
│   └── .env
```
- store the $IMAGE_TAG=commit sha in the .env
- Then docker copose has everything it needs to setup the app on the new box

##### The full workflow to setup a new box with the flask-ci app
'''bash
# 1. Docker
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER
# log out, log back in

# 2. Deployment directory
sudo mkdir -p /opt/flask-ci
sudo chown $USER:$USER /opt/flask-ci
cd /opt/flask-ci

# 3. Add the two above files
# compose.yaml — copy from repo
# .env — IMAGE_TAG=<sha>

# 4. Check substitution resolved
docker compose config

# 5. Deploy
docker compose pull
docker compose up -d

# 6. Verify
curl localhost:8000/healthz
'''