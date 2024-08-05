# Aeris Project

This project is to display common statistics (mean, standard deviation, and sum) and visualization via a REST endpoint. This project is designed to run platforms that support Docker or a Linux OS that can install the python libraries in the requirements.txt file. **THIS PROGRAM USES THE DEFAULT WSGI SERVER FOR FLASK ENDPOINTS.**

# Requirements
- Docker
- Git (Windows can use Git Bash for git commands)
- VSCode (for DevContainer use)
- Python (3.12+ has been tested, may work with earlier)

# Getting Started (Docker Container)

1. Ensure the Docker Daemon is running. For MacOS and Windows, use Docker Desktop. For Linux, start the docker daemon (sudo dockerd), if it isn't already running.

2. Clone the repo in terminal using: ```git clone https://github.com/Kizitor/Aeris_Project.git```

3. Build the image from the terminal after navigating to the cloned git repo's top level folder. **(On Windows and MacOS, open Docker Desktop and use the following docker related commands in its terminal. Linux can use any terminal.)**

    - ```docker build -t Aeris_Image . ```

4. Run the container

    - ```docker run -it -p 80:80 Aeris_Image```

5. With the container running, the following endpoints are available to you:

    - get-mean: Returns the mean of the concentration
    - get-std-deviation: Returns the standard deviation of the concentration
    - get-sum: Returns the sum of the concentration
    - get-image: Returns 3D scatter plot visualization of the concentration

    To access these endpoints, go to your browser and go to the localhost URL ````http://127.0.0.1/<desired_endpoint>````

6. An alternative to this method that still takes advantage of Docker is to use a DevContainer (requires VSCode). If you use the preconfigured DevContainer in the project, build and open it. Then run this in the DevContainer: ```bash ./start.sh``` 

# Getting Started (No Containerization Linux)

1. Clone the repo in terminal using: ```git clone https://github.com/Kizitor/Aeris_Project.git```

2. Navigate to the top level of the git repo and install the required python libraries.
    ````
    cd Aeris_Project
    pip3.12 install --no-cache-dir -r requirements.txt
    ````

3. Edit the `start.sh` script and change the environment variable, `FLASK_RUN_HOST` , to use the localhost IP, `127.0.0.1`.

4. Run this: `bash ./start.sh`

5. With the app running, the following endpoints are available to you:

    - get-mean: Returns the mean of the concentration
    - get-std-deviation: Returns the standard deviation of the concentration
    - get-sum: Returns the sum of the concentration
    - get-image: Returns 3D scatter plot visualization of the concentration

    To access these endpoints, go to your browser and go to the localhost URL ````http://127.0.0.1/<desired_endpoint>````
