# Don't change this - this is installing a base image with conda installed
FROM continuumio/miniconda3

# We are setting the working directory
WORKDIR /app

# Add your code here to make it work
# You will need to make the YML file and fq file available in the container
COPY fastqc_env.yml example.fq.gz .

# You will then need to create a conda environment with the correct name
RUN conda env create -f fastqc_env.yml

# Don't change this either (need to activate environment and add it to path)
# Note the name of the environment
RUN echo "source activate fastqc_env" > ~/.bashrc
ENV PATH=/opt/conda/envs/fastqc_env/bin:$PATH

# Add CMD here to run fastqc
CMD ["fastqc", "example.fq.gz"]