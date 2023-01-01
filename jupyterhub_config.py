import os

c = get_config()

c.JupyterHub.spawner_class = "dockerspawner.DockerSpawner"
c.DockerSpawner.image = "jupyter/minimal-notebook:latest"

c.DockerSpawner.network_name = "jupyterhub-network"
c.DockerSpawner.notebook_dir = "/home"
c.DockerSpawner.volumes = {"jupyterhub-user-admin": "/home"}


c.JupyterHub.hub_ip = "jupyterhub"
c.JupyterHub.hub_port = 8080

c.JupyterHub.db_url = "sqlite:////data/jupyterhub.sqlite"

c.JupyterHub.authenticator_class = "dummy"
c.DummyAuthenticator.password = "admin"
