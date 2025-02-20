# Don't change this
FROM continuumio/miniconda3

# Or this
WORKDIR /app

# Add your code here to make it work
# You will need to make the YML file and fq file available in the container


# You will then need to create a conda environment


# Don't change this either (need to activate environment and add it to path)
# Note the name of the environment
RUN echo "source activate fastqc" > ~/.bashrc
ENV PATH=/opt/conda/envs/fastqc/bin:$PATH

# Add CMD here to run fastqc
CMD