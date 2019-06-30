FROM python:3.6

ARG project_dir=/app/
COPY . $project_dir
WORKDIR $project_dir

RUN apt-get update && \
    apt-get install -y locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ Asia/Tokyo

COPY scripts/docker/startup.sh /startup.sh
RUN chmod 744 /startup.sh
CMD ["/startup.sh"]
