FROM python:3.12-slim


# Docker Build time
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install my project force not to search for dependencies and rely on reqs.txt, 
# dont cache old versikons to save space on the container
COPY pyproject.toml README.md ./
COPY src/ ./src/
RUN pip install --no-deps --no-cache-dir .

# Setup the env
# confusing syntax, docker build reads this as use BUILD_SHA if sent as arg, else use "dev":
ARG BUILD_SHA=dev
# back to 'sensible' syntax assign docker container var ENV to the dockerfiles local var $BUILD_SHA:
ENV BUILD_SHA=$BUILD_SHA 
# make a non root user account with no interactive login
RUN useradd -m -u 10001 -s /usr/sbin/nologin appuser
USER appuser

# Add a field to the docker config so can tell from docker inspect what port it uses
EXPOSE 8000

# Docker Run time - creates json array to pass as shell command to give the WSGI
# flask_ci:main:app as a callable
# Need to give is flask_ci:main:app because flask_ci:main would fall over
# when if __name__ == "__main__" returned flask_ci.main not main
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "flask_ci.main:app" ]