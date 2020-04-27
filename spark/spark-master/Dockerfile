FROM spark-base:latest

COPY spark-master/start.sh /

# Copying local data added for testing purposes
RUN mkdir /data
COPY ./data/* /data/

ENV SPARK_MASTER_PORT 7077
ENV SPARK_MASTER_WEBUI_PORT 8080
ENV SPARK_MASTER_LOG /spark/logs

# Setting some vimrc configs
RUN echo "syntax enable" >> /root/.vimrc
RUN echo "set number" >> /root/.vimrc
RUN echo "set hlsearch" >> /root/.vimrc

EXPOSE 8080 7077 6066

CMD ["/bin/bash", "/start.sh"]
