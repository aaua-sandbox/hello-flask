FROM python:3.6

ARG project_dir=/app/
COPY . $project_dir
WORKDIR $project_dir

RUN pip install flask
# RUN pip install -r requirements.txt

COPY scripts/docker/startup.sh /startup.sh
RUN chmod 744 /startup.sh
CMD ["/startup.sh"]
