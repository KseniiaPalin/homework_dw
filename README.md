# Steps for deploying the model
1. Build docker image from Dockerfile

    ```docker build --tag=homework .```

2. Run the docker container after build

    ```docker run -p 4000:80 homework```

# Example

### /predict (POST)
    Returns an array of predictions given a JSON object representing independent variables. Here's a sample input:
    ```
    [
      {
        "index": 0,
        "value": 0
      },
      {
        "index": 1,
        "value": 0
      },
      {
        "index": 2,
        "value": 0
      },
      ...
      ]
    ```
    
    and sample output:
    ```
    {"period": "346"}
    ```
    