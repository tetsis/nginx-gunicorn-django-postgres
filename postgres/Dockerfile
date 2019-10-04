FROM postgres:9.6.9-alpine
COPY postgres/postgresql.conf /etc/postgresql.conf
ADD postgres/init_db.sh .
RUN chown postgres /etc/postgresql.conf
