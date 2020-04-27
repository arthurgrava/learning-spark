FROM openjdk:8

LABEL author="Arthur Grava"
LABEL version="0.0.1-beta"

ENV SCALA_VERSION=2.12.4
ENV SCALA_HOME=/usr/share/scala

ARG SPARK_VERSION
ARG HADOOP_VERSION

RUN apt update && apt install -y curl vim wget software-properties-common ssh net-tools ca-certificates jq

# Scala
RUN cd "/tmp" && \
    wget --no-verbose "https://downloads.typesafe.com/scala/${SCALA_VERSION}/scala-${SCALA_VERSION}.tgz" && \
    tar xzf "scala-${SCALA_VERSION}.tgz" && \
    mkdir "${SCALA_HOME}" && \
    rm "/tmp/scala-${SCALA_VERSION}/bin/"*.bat && \
    mv "/tmp/scala-${SCALA_VERSION}/bin" "/tmp/scala-${SCALA_VERSION}/lib" "${SCALA_HOME}" && \
    ln -s "${SCALA_HOME}/bin/"* "/usr/bin/" && \
    rm -rf "/tmp/"*
RUN export PATH="/usr/local/sbt/bin:$PATH" \
    && apt update \
    && apt install ca-certificates wget tar \
    && mkdir -p "/usr/local/sbt" \
    && wget -qO - --no-check-certificate "https://github.com/sbt/sbt/releases/download/v1.2.8/sbt-1.2.8.tgz" \
    | tar xz -C /usr/local/sbt --strip-components=1 && sbt sbtVersion

# Get Spark
RUN echo "Getting SPARK ${SPARK_VERSION}"
RUN wget http://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz
RUN tar -xzf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz
RUN mv spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} spark
RUN rm spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz

# Get useful jars and add to lib
RUN wget https://repo1.maven.org/maven2/org/elasticsearch/elasticsearch-hadoop/7.6.2/elasticsearch-hadoop-7.6.2.jar && \
    mv elasticsearch-hadoop-7.6.2.jar /spark/jars

RUN wget https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/2.7.3/hadoop-aws-2.7.3.jar && \
    mv hadoop-aws-2.7.3.jar /spark/jars

RUN wget https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk/1.7.4/aws-java-sdk-1.7.4.jar && \
    mv aws-java-sdk-1.7.4.jar /spark/jars

# Add Dependencies for PySpark and install requirements.txt
RUN apt install -y python3 python3-pip python3-numpy python3-matplotlib python3-scipy python3-pandas python3-simpy
RUN update-alternatives --install "/usr/bin/python" "python" "$(which python3)" 1
RUN mkdir /config
COPY spark-base/requirements.txt /config/requirements.txt
RUN pip3 install -r /config/requirements.txt

# Useful simbolic links
ENV PATH="/spark/bin:${PATH}"

ENV PYTHONHASHSEED 1
