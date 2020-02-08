FROM amazon/dynamodb-local

EXPOSE 8000/tcp

VOLUME ["/local/dynamodb:/data/"]

CMD ["-jar", "DynamoDBLocal.jar", "-sharedDb", "-dbPath", "/data"]