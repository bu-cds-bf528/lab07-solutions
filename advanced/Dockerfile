# Don't change this
FROM continuumio/miniconda3

# Or this
WORKDIR /app

# Add your code here to make it work


# Don't change this either (need to activate environment and add it to path)
RUN echo "source activate fastqc" > ~/.bashrc
ENV PATH=/opt/conda/envs/fastqc/bin:$PATH

# Add CMD here
CMD