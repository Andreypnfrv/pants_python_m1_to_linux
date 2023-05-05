docker_environment(
    name="linux_docker",
    platform="linux_x86_64",
    image="python:3.11",
    docker_env_vars=[
      "POSTGRES_HOST=localhost",
      "POSTGRES_PORT=5432",
      "POSTGRES_USER=postgres",
      "POSTGRES_PASSWORD=postgrespass",
      "POSTGRES_NAME=gochi"
  ]
)

local_environment(
  name="macos_laptop",
  compatible_platforms=["macos_x86_64"],
)