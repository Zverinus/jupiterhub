ARG HUB_PATH
ARG NOTEBOOKS_FROM

FROM jupyterhub/jupyterhub:3.0.0

RUN python3 -m pip install --no-cache-dir dockerspawner==12.1
COPY ./jupyterhub_config.py /srv/jupyterhub/
COPY $NOTEBOOKS_FROM $HUB_PATH
EXPOSE 8000:8000
CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyterhub_config.py"]
