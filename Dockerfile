FROM ubuntu:18.04

USER 0

RUN cat /etc/apt/sources.list
ENV DEBIAN_FRONTEND="noninteractive"
ENV TZ="Europe/London"
RUN apt-get update && \
    apt-get install -y gnupg software-properties-common wget && \
    apt-get install -y lsb-release && \
    wget -qO - https://qgis.org/downloads/qgis-2020.gpg.key | gpg --no-default-keyring --keyring gnupg-ring:/etc/apt/trusted.gpg.d/qgis-archive.gpg --import && \
    chmod a+r /etc/apt/trusted.gpg.d/qgis-archive.gpg

RUN add-apt-repository "deb https://qgis.org/debian-ltr `lsb_release -c -s` main" && \
    apt-get update && \
    apt-get install -y --allow-unauthenticated --no-install-recommends --no-install-suggests qgis-server python-qgis

COPY ch.so.agi.av.grundstuecke.rechtskraeftige_v3.qml /styles/

COPY mock.py /program/

COPY uid_entrypoint.sh /usr/local/bin/

ENV QT_QPA_PLATFORM=offscreen
ENV QGIS_PREFIX_PATH="/usr"
ENV QGIS_SERVER_TRUST_LAYER_METADATA=true

# ENTRYPOINT ["/usr/local/bin/uid_entrypoint.sh"]

# CMD ["/program/mock.py"]

ENTRYPOINT ["/usr/bin/python3", "/program/mock.py"]
