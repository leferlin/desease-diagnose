conda create -y -n labx 'python>=3'
source activate labx
conda config --env --add pinned_packages 'openjdk>8.0.121'
conda install -y -c conda-forge jupyterlab beakerx
jupyter labextension install @jupyter-widgets/jupyterlab-manager
jupyter labextension install beakerx-jupyterlab
