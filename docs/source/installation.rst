==========================
Getting Started
==========================

**Install Docker Desktop**

.. tip:: 
  First, you need to install Docker Desktop to run our application

1. Go to `Docker Desktop Download Page <https://www.docker.com/products/docker-desktop/>`_
2. Download the version for your system (Windows or Mac)
3. Install Docker Desktop by following the installation wizard
4. Start Docker Desktop and wait until it's fully running

**Run Our Application**

.. tip::
  Once Docker Desktop is running, you can get our application using the Docker Desktop interface

1. Open Docker Desktop
2. Click on the "Search" box
3. Type: ``gaspardmacaux/singlenucleus:latest``
4. Click "Pull" to download the image
5. Once downloaded, click "Run"
6. In your web browser, go to: ``http://localhost:3838``

**Troubleshooting**

If the above method doesn't work, try using the command line:

**For Windows:**
  1. Press ``Windows + X`` and click "Windows PowerShell" or "Terminal"
  2. Type: ``docker pull gaspardmacaux/singlenucleus:latest``
  3. Then: ``docker run -p 3838:3838 gaspardmacaux/singlenucleus:latest``
  4. Access the application at ``http://localhost:3838``

**For Mac:**
  1. Open Terminal (Applications > Utilities > Terminal)
  2. Type: ``docker pull gaspardmacaux/singlenucleus:latest``
  3. Then: ``docker run -p 3838:3838 gaspardmacaux/singlenucleus:latest``
  4. Access the application at ``http://localhost:3838``