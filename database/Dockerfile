FROM postgres:alpine

ENV POSTGRES_PASSWORD admin
ENV POSTGRES_DB flask

COPY init.sql /docker-entrypoint-initdb.d/