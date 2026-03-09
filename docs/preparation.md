# Preparation
## System Requirements
Minimum Specifications:
- CPU: 12 physical cores (e.g. AMD Ryzen 9 5900X, Intel Xeon Silver 4310)
- Memory (RAM): 64 GB DDR4 or DDR5
- Storage:
    - Primary drive: 1 TB NVMe SSD
    - Secondary driv(*Optional*) : 2 TB HDD for additional storage
- Operating System: Linux (e.g. Ubuntu 22.04 LTS or compatible distribution)

Recommended Specifications:
- CPU: 24 physical cores (e.g. AMD Threadripper PRO 5975WX, Intel Xeon Gold 6338)
- Memory (RAM): 128 GB DDR4 or DDR5
- Storage: 
    - Primary drive: 2 TB NVMe Gen4 SSD
    - Secondary drive (*Optional*): 4 TB SSD or HDD (RAID 1 optional for redundancy)
- Operating System: Linux (e.g. Ubuntu 22.04 LTS or compatible distribution)

## Docker
The BaseCode Processing Pipeline is distributed as a Docker image. To install Docker, please follow the instructions found at https://www.docker.com/.

The only platforms we are currently supporting are the various Linux distributions (e.g. CentOS, Debian, Fedora, RHEL, and Ubuntu). Running the BaseCode Processing Pipeline using Docker on MacOS or Windows may be successful but is not supported.

### Docker Desktop
If you have access to a window manager on your host machine running the BaseCode Processing Pipeline, it is possible to install Docker Desktop to manager your containers using a graphical user interface: https://www.docker.com/products/docker-desktop/.

### Docker Engine
If your host machine is command line only, Docker Engine provides all the needed tools to run Docker. The instructions to install Docker Engine can be found here: https://docs.docker.com/engine/install/. Additionally, you are encouraged to proceed with the post-installation steps detailed here: https://docs.docker.com/engine/install/linux-postinstall/. This documentation assume you have enabled the management of Docker as a non-root user.
 
> **IMPORTANT**The Docker daemon runs as root by default and files created by the Docker container are owned by root. Therefore, the user which runs the BaseCode Processing Pipeline need root access (either using sudo or by knowing the password to the root user) to change file permissions of the final output.