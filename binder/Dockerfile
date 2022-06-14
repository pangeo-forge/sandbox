FROM python:3.9-slim

ENV CONDA_ENV=pangeo-forge \
    CONDA_DIR=/srv/conda
ENV ENV_PYTHON_PREFIX=${CONDA_DIR}/envs/${CONDA_ENV}

# Add both our pangeo-forge env as well as default conda installation to $PATH
# Thus, when we start a `python` process, it loads the python in the pangeo-forge
# conda environment, as that comes first here.
ENV PATH=${ENV_PYTHON_PREFIX}/bin:${CONDA_DIR}/bin:${PATH}

# Install latest mambaforge in ${CONDA_DIR}
RUN apt-get update \
    && apt-get install -y wget \
    && rm -rf /var/lib/apt/lists/*
RUN echo "Installing Mambaforge..." \
    && URL="https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh" \
    && wget --quiet ${URL} -O installer.sh \
    && /bin/bash installer.sh -u -b -p ${CONDA_DIR} \
    && rm installer.sh \
    && mamba clean -afy \
    # After installing the packages, we cleanup some unnecessary files
    # to try reduce image size - see https://jcristharif.com/conda-docker-tips.html
    && find ${CONDA_DIR} -follow -type f -name '*.a' -delete \
    && find ${CONDA_DIR} -follow -type f -name '*.pyc' -delete

# Install deps.
RUN mamba create --name ${CONDA_ENV} python=3.9
RUN mamba install -n ${CONDA_ENV} -y \
    pangeo-forge-recipes>=0.9.0 \
    aiohttp \
    apache-beam \
    boto3 \
    cftime \
    dask \
    distributed \
    fsspec>=2022.1.0 \
    gcsfs>=2022.1.0 \
    h5netcdf \
    h5py>=3.3.0 \
    hdf5 \
    intake \
    intake-xarray \
    kerchunk>=0.0.6 \
    matplotlib \
    netcdf4 \
    numcodecs \
    numpy \
    pandas \
    pip \
    prefect \
    rasterio \
    requests \
    rechunker>=0.4.2 \
    scipy \
    s3fs>=2022.1.0 \
    setuptools \
    xarray>=0.18.0 \
    zarr>=2.6.0
 
