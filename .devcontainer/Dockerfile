FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

# El repo apt de Yarn viene preconfigurado en la imagen base y su clave GPG está
# rota; no lo usamos, así que lo quitamos antes de actualizar.
RUN rm -f /etc/apt/sources.list.d/yarn.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
         ffmpeg libimage-exiftool-perl \
    && rm -rf /var/lib/apt/lists/*

ARG POETRY_VERSION=2.1.3
RUN pipx install poetry==${POETRY_VERSION}

ENV POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1