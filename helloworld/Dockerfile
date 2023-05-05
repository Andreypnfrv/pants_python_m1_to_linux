# Dockerfile
FROM --platform=linux/amd64 python:3.11

WORKDIR /app

# Copy the Pants-produced PEX file to the container
COPY helloworld.pex .

# Set the entrypoint to the PEX file
ENTRYPOINT ["./helloworld.pex"]