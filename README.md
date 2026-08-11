# FLASK CI/CD Practice

### Building the requirements / requirements-dev files
- Used the small sh script in project root dir make_reqs_uv.sh
- Uses uv to build from the pyprojects.toml file - no hands on

# pytest unit testing
- Very simple test against bad urls (whitespaces) in the GETS and the outputs of an internal 'normalise name' func

# github workflow
- Spins up an ubuntu VM
- Clones my repo and installs a py interpreter
- installs my repo using -dev requirements
- runs pytest -v