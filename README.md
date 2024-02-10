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

## Development

For development purposes, you can make changes to the `main.py` script to alter the message production logic. Ensure to rebuild the Docker image and rerun the container to test your changes:

```bash
docker build -t edge . && docker run --name edge -v icicle:/app/logs edge
```