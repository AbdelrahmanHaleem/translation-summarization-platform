FROM confluentinc/cp-kafka:latest
COPY config/server.properties /etc/kafka/server.properties
COPY config/zookeeper.properties /etc/kafka/zookeeper.properties
CMD ["sh", "-c", "bin/zookeeper-server-start.sh /etc/kafka/zookeeper.properties & bin/kafka-server-start.sh /etc/kafka/server.properties"]

