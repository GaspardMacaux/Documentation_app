==========================
Installation with Docker
==========================

### Overview

Docker allows you to containerize the application, making it easy to deploy and run in any environment. This guide will walk you through the steps to install Docker, pull the Docker image for the application, and run the application using Docker.

### Step 1: Install Docker

First, you need to install Docker on your machine. Docker is available for various operating systems, including Windows, macOS, and Linux. Follow the steps below to install Docker based on your operating system:

#### For Windows:

1. **Download Docker Desktop**:  
   - Visit the Docker Desktop download page: [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/).
   - Download the installer and run it.

2. **Install Docker Desktop**:  
   - Follow the on-screen instructions to install Docker Desktop.
   - During installation, make sure to enable "Use WSL 2 instead of Hyper-V" if prompted. This allows Docker to run on Windows Subsystem for Linux (WSL 2).

3. **Start Docker Desktop**:  
   - Once installed, launch Docker Desktop. You may need to sign in with a Docker account, which you can create for free if you don't already have one.

#### For macOS:

1. **Download Docker Desktop**:  
   - Visit the Docker Desktop download page: [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/).
   - Download the `.dmg` file and open it.

2. **Install Docker Desktop**:  
   - Drag and drop the Docker icon into the Applications folder to install it.
   - Open Docker from the Applications folder. You may need to grant it permission to run and install any required components.

3. **Start Docker Desktop**:  
   - Launch Docker Desktop. You may need to sign in with a Docker account.
### Step 2: Pull and Run the Docker Image Using Docker Desktop

Once Docker Desktop is installed and running, you can pull and run the application without using the command line.

1. **Open Docker Desktop**:  
   - Launch Docker Desktop on your system.

2. **Pull the Docker Image**:  
   - In Docker Desktop, navigate to the **Images** tab.
   - In the search bar, enter the name of the Docker image you need to pull (e.g., `username/your-app-name`) and pull it from Docker Hub.
   - Alternatively, you can use the **Pull Image** option in Docker Desktop to download the image by providing the image name.

3. **Run the Docker Container**:  
   - After the image is downloaded, go to the **Images** tab in Docker Desktop.
   - Find the pulled image in the list, and click the **Run** button.
   - A dialog will appear where you can configure container settings, such as ports and environment variables.
   - Set the **Host Port** to `3838` (or another port if your application uses a different one). The **Container Port** should match the port the application runs on inside the container (e.g., `3838`).
   - Click **Run** to start the container.

4. **Access the Application**:  
   - Open a web browser and go to `http://localhost:3838` (or the port you specified) to access the application.

### Managing Containers with Docker Desktop

Docker Desktop provides an easy interface for managing running containers:

- **Start, Stop, and Restart Containers**:  
  - In the **Containers/Apps** tab, you can see the list of running containers.
  - Use the **Start**, **Stop**, and **Restart** buttons to control the state of each container.


.. image:: /_static/images/introduction.png
   :width: 90%
   :align: center



