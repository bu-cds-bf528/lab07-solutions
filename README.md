# Lab 06 - Docker

## Objectives

- Gain familiarity with common Docker commands: FROM, RUN, COPY, WORKDIR, CMD

- Understand Docker build cache

- Learn how to run docker containers non-interactively and interactively

- Follow general best practices to make containers reproducible, and lightweight

- Use a bind-mount to persist files generated in a container on the host

## Accept the github classroom repository

Instead of cloning this repo to the SCC, we are instead going to use the github 
codespaces functionality, which allows you to open an integrated development
environment in the cloud using the repository as a template. By default, this
environment is created from an Ubuntu image and pre-installed with a selection 
of popular tools and utilities. 

After you accept the github classroom link, please go directly to the github
repository and click on the large green `code` button. Switch tabs and open a 
codespace. 


## Creating a simple Docker image and container

If you navigate to the simple_with_errors/ directory, you'll notice that we have three
files: a Dockerfile, a requirements.txt, and a genome fasta file. 

Briefly take a look at each file, based on the lecture, you should be able to get a rough
sense for what the Dockerfile is doing. We are creating an image with python and biopython
installed, copying a script located in the current directory into the container image, and
then running the script. 

Please use the following command to build a docker image from this Dockerfile:

```
docker build -t python_script:latest .
```

Upon completion, you should be able to see your docker image if you use the following command:

```
docker images
```

Take note of th difference between REPOSITORY and TAG as well as the size of the created
image.

## Running a container from this image

We have only built the image, we still need to create a container or instance from this
image. 

Run the following command:

```
docker run --name test1 python_script
```

What do you expect the output to be? What is the output?

That was an example of running a docker container non-interactively. We can choose to run 
containers `interactively`, which you'll often use to debug or troubleshoot commands. The
following command will attach your terminal to the containers stdin/stdout so that you can 
interact with a bash shell or other program. 

```
docker run -it python_script bash
```

Use the `ls` command and take note of what files are present. Try to open a python 
interpreter and `import Bio`. This is the environment that your container created and
you should have access to the same files you copied and the tools you installed in the
Dockerfile.

## A slightly more advanced version

Navigate to the advanced/ directory and use what we've just done, LLMs, or the internet,
and try to complete the files in this directory to build an image with FastQC, create containers,
and run fastqc on the provided fastq. 

Once you've successfully completed the Dockerfile, recall that containers are isolated and by default
store any files non-persistently inside the container unless otherwise specified. We will quickly
explore one way you could persist files from a docker container by using a bind-mount. 

Add the following flag to your docker run command for this new container:

```
--volume $(pwd):/app
```

This will enable you to create files in the container and persist the files onto the host filesystem. In 
this case, you can see that we are binding the present working directory on the host to the /app directory
inside the container where FastQC is running and producing its outputs. 

After you run this command, you should now see the outputs of FastQC appear in your current directory. 

## BF528 Containers

Navigate to the class_containers/ directory. You do not need to do anything for this part, but take a look
at the files contained within. 

These are how the containers we use for this class were built. Try to understand the purpose of each line on
your own. We'll go through it together and talk about the specific considerations that were necessary. 

## Commonly used commands

docker build -t

docker run --name

docker ps -a

docker rm

docker images

docker run -it