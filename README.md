# Local kafka lab

Some commands to deal with the docker environment:

### Create a topic
``` shell
docker compose exec broker \
  kafka-topics --create \
    --topic purchases \
    --bootstrap-server 172.19.79.239:9092 \
    --replication-factor 1 \
    --partitions 1
```

### List topics

``` shell
docker-compose exec broker kafka-topics --list --bootstrap-server localhost:9092
```

### Consume from a topic from beginning

``` shell

docker-compose exec broker kafka-console-consumer --topic "com.test.purchases" --bootstrap-server PLAINTEXT://localhost:9092 --from-beginning

```

When using a producer in a machine away from kafka, run this conda parameter on terminal before executing consumer.

``` shell
set CONDA_DLL_SEARCH_MODIFICATION_ENABLE=1
```