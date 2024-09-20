==========================
Installation with Docker
==========================

### Overview

Docker allows you to containerize the application, making it easy to deploy and run in any environment. This guide provides instructions on how to install Docker, pull the Docker image for the application, and run the application using Docker Desktop.

### Step 1: Install Docker Desktop

Docker Desktop is an easy-to-install application that includes Docker Engine and Docker CLI, allowing you to build, share, and run containerized applications on your local machine. Follow the steps below to install Docker Desktop based on your operating system:

#### For Windows and macOS:

1. **Download Docker Desktop**:  
   - Visit the Docker Desktop download page: [Docker Desktop](https://www.docker.com/products/docker-desktop/).
   - Download the installer for your operating system (Windows or macOS).

2. **Install Docker Desktop**:  
   - Run the installer and follow the on-screen instructions.
   - On Windows, ensure that "Use WSL 2 instead of Hyper-V" is enabled if prompted. This allows Docker to run on Windows Subsystem for Linux (WSL 2).

3. **Start Docker Desktop**:  
   - After installation, launch Docker Desktop. You might need to sign in with a Docker account, which you can create for free if you don't have one.

4. **Verify Installation**:  
   - Docker Desktop will run automatically after installation. You can verify that Docker is running by looking for the Docker icon in your system tray (Windows) or menu bar (macOS).

#### For Linux:

1. **Install Docker Engine**:  
   Docker Desktop is not available for Linux, but you can install Docker Engine directly. Follow the official Docker Engine installation guide for your Linux distribution: [Docker Engine Installation](https://docs.docker.com/engine/install/).

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

- **View Logs**:  
  - Click on a running container to view its logs and output directly within Docker Desktop.

- **Remove Containers**:  
  - To remove a container, first stop it, then click the **Delete** button.

### Optional: Running Containers with Additional Settings

- **Port Mapping**:  
  - If you need to change the port mapping, you can do this in the configuration dialog when running the container.
- **Environment Variables**:  
  - Set environment variables if your application requires them, using the **Environment Variables** section in the run configuration dialog.

### Conclusion

Using Docker Desktop simplifies the process of managing containerized applications. With Docker Desktop, you can pull images, run containers, and manage your application using a graphical interface without needing to use command-line tools.
