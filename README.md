# Getting Started

## Installation

> **Tip:**
> First, you need to install Docker Desktop to run our application

1. Go to [Docker Desktop Download Page](https://www.docker.com/products/docker-desktop/)
2. Download the version for your system (Windows or Mac)
3. Install Docker Desktop by following the installation wizard
4. Start Docker Desktop and wait until it's fully running

## Running the Application

### Windows 

**Using Docker Desktop interface:**
1. Open Docker Desktop
2. Click on the "Search" box
3. Type: `gaspardmacaux/singlenucleus:other_processor`
4. Click "Pull" to download the image
5. Once downloaded, click "Run"
6. In your web browser, go to: `http://localhost:3838`

**Using command line:**
1. Press `Windows + X` and click "Windows PowerShell" or "Terminal"
2. Type: `docker pull gaspardmacaux/singlenucleus:other_processor`
3. Then: `docker run -p 3838:3838 gaspardmacaux/singlenucleus:other_processor`
4. Access the application at `http://localhost:3838`

### Mac

**For Mac with Intel chip:**

*Using Docker Desktop interface:*
1. Open Docker Desktop
2. Click on the "Search" box
3. Type: `gaspardmacaux/singlenucleus:other_processor`
4. Click "Pull" to download the image
5. Once downloaded, click "Run"
6. In your web browser, go to: `http://localhost:3838`

*Using command line:*
1. Open Terminal (Applications > Utilities > Terminal)
2. Type: `docker pull gaspardmacaux/singlenucleus:other_processor`
3. Then: `docker run -p 3838:3838 gaspardmacaux/singlenucleus:other_processor`
4. Access the application at `http://localhost:3838`

**For Mac with Apple Silicon chip:**

*Using Docker Desktop interface:*
1. Open Docker Desktop
2. Click on the "Search" box
3. Type: `gaspardmacaux/singlenucleus:apple_processor`
4. Click "Pull" to download the image
5. Once downloaded, click "Run"
6. In your web browser, go to: `http://localhost:3838`

*Using command line:*
1. Open Terminal (Applications > Utilities > Terminal)
2. Type: `docker pull gaspardmacaux/singlenucleus:apple_processor`
3. Then: `docker run -p 3838:3838 gaspardmacaux/singlenucleus:apple_processor`
4. Access the application at `http://localhost:3838`

## Accessing the Application

Once you have run the Docker container using either the Docker Desktop interface or the command line, you can access the application by opening your web browser and navigating to `http://localhost:3838`.

> **Note:**
> `http://localhost:3838` is the URL where the application is hosted on your local machine. 
> - `localhost` refers to your own computer 
> - `3838` is the port number where the application is running
>
> If the application doesn't load, make sure that the Docker container is running and that you have typed the URL correctly in your web browser.