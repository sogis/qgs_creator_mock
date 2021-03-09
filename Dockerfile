FROM ubuntu:16.04

USER 0

RUN cat /etc/apt/sources.list

RUN apt-get update && \
    apt-get install -y dirmngr && \
    apt-get install -y lsb-release && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-key CAEB3DC3BDF7FB45
RUN echo "deb http://qgis.org/debian `lsb_release -c -s` main" && \
    echo "deb http://qgis.org/debian `lsb_release -c -s` main" >> /etc/apt/sources.list && \
    cat /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y --allow-unauthenticated qgis python-qgis qgis-plugin-grass

# RUN mkdir /program && \
#     chown 1001 /program && \
#     chgrp 0 /program && \
#     chmod g=u /program && \
#     chgrp 0 /etc/passwd && \
#     chmod g=u /etc/passwd && \
#     mkdir /data && \
#     chown 1001 /data && \
#     chgrp 0 /data && \
#     chmod g=u /data

# USER 1001

COPY ch.so.agi.av.grundstuecke.rechtskraeftige_v3.qml /styles/

COPY mock.py /program/

COPY uid_entrypoint.sh /usr/local/bin/

# ENTRYPOINT ["/usr/local/bin/uid_entrypoint.sh"]

# CMD ["/program/mock.py"]

ENTRYPOINT ["/usr/bin/python", "/program/mock.py"]
