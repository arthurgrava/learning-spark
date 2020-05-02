FROM python:3.6.10-alpine

####
# Working with Spark 2.4.5 and Hadoop 2.7
####

LABEL author="Arthur Grava"
LABEL version="0.0.1"

RUN apk update \
    && apk add ca-certificates \
    && update-ca-certificates \
    && apk add openssl
RUN apk add tzdata gcc bash linux-headers vim
RUN apk add musl-dev
RUN apk add openjdk8
RUN pip install awscli

RUN echo "syntax enable\nset number\nset hlsearch" > /root/.vimrc

# getting spark
RUN wget http://archive.apache.org/dist/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz
RUN tar -xzf spark-2.4.5-bin-hadoop2.7.tgz \
    && mv spark-2.4.5-bin-hadoop2.7 spark \
    && rm spark-2.4.5-bin-hadoop2.7.tgz

RUN wget https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/2.7.3/hadoop-aws-2.7.3.jar && \
    mv hadoop-aws-2.7.3.jar /spark/jars

RUN wget https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk/1.7.4/aws-java-sdk-1.7.4.jar && \
    mv aws-java-sdk-1.7.4.jar /spark/jars

RUN wget https://repo1.maven.org/maven2/net/java/dev/jets3t/jets3t/0.9.4/jets3t-0.9.4.jar && \
    mv jets3t-0.9.4.jar /spark/jars

# Install python requirements
RUN mkdir /image-config
COPY spark-base/requirements.txt /image-config/requirements.txt
RUN pip install -r /image-config/requirements.txt

ENV PATH="/spark/bin:${PATH}"
ENV PYTHONHASHSEED 1
