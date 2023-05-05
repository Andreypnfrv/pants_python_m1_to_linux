python_sources(
    name="helloworld",
)

pex_binary(
    name="helloworld_pex",
    entry_point="helloworld.__init__:main",
    dependencies=[
        ":helloworld"
    ],
    output_path="helloworld.pex",
    environment="linux_docker",
)

docker_image(
    name="helloworld_docker",
    dependencies=[
        ":helloworld_pex"
    ]
)
