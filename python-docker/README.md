# python-docker

This repo contains a simple python docker project with the following features:
* Support for `requirements.txt` file
* Passing environment variables in via file
* Logging back to host machine

## Running locally
To run the file locally:
1. Add the environement variables by coping `.env_example` to `.env` and setting the values.
2. (Optional) Setup a virtual environment and activate it.
3. Run `python main.py`

## Running in Docker
To run the file in docker:
1. Build the image using:
    ```bash
    docker build -t python-docker .
    ```
    
2. Run the image using:
    ```bash
    docker run --name python-docker-example --env-file .env -v /<path>/<to>/<log>/<dir>/log:/usr/src/app/log --rm -d python-docker
    ```

## Explaination
Below is an explaintion of the docker commands above:
```bash
docker build -t python-docker .
```
|Command| Explaination
|--|--
|`docker build`| build an image from a Dockerfile
|`-t python-docker`| set name (tag). Short for `--tag`
|`.`| location of the Dockerfile
[docker build docs](https://docs.docker.com/engine/reference/commandline/build/)

```bash
docker run --name python-docker-example --env-file .env -v /<path>/<to>/<log>/<dir>/log:/usr/src/app/log --rm -d python-docker
```
|Command| Explaination
|--|--
|`docker run` | create and run a container
|`--name python-docker-example` | set name of container
|`--env-file .env` | read in a file of environment variables
|`-v /<path>/<to>/<log>/<dir>/log : /usr/src/app/log`| read in a file of environment variables
|`--rm` | delete the container after exiting
|`-d` | detach container from terminal. Allows it to run in the background
|`python-docker`| name of the image
[docker run docs](https://docs.docker.com/engine/reference/commandline/run/)