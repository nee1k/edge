# Edge Device Simulation

Before you begin, ensure you have met the following requirements:
- Docker installed on your machine.

### Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/nee1k/edge.git
    ```

2. **Navigate to the project directory**
    ```bash
    cd edge
    ```

3. **Create a Docker volume**
    Before building the Docker image, create a Docker volume named `icicle` to persist logs:

    ```bash
    docker volume create icicle
    ```

4. **Build the Docker image**

    Build the Docker image with the tag `edge`:

    ```bash
    docker build -t edge .
    ```

5. **Run the Docker container**

    Finally, run your Docker container named `edge`, mounting the `icicle` volume to `/app/logs`:

    ```bash
    docker run --name edge -v icicle:/app/logs edge
    ```

### Usage

Once the application is running, it will start producing messages to your Kafka cluster based on its configuration. You can customize the behavior of the producer by modifying environment variables or the `main.py` script according to your needs.

## Configuration

This project uses environment variables for configuration. You can modify these variables in the Docker run command using the `-e` flag. For example:

- `KAFKA_BOOTSTRAP_SERVERS`: Specifies the Kafka brokers to connect to.
- `TOPIC_NAME`: The name of the Kafka topic to produce messages to.

## Development

For development purposes, you can make changes to the `main.py` script to alter the message production logic. Ensure to rebuild the Docker image and rerun the container to test your changes:

```bash
docker build -t edge . && docker run --name edge -v icicle:/app/logs edge
```