# CoreML in Python 3.11

> **Note:** Ensure that your Python version is at most 3.11 to maintain compatibility with CoreML.

## Conda Setup for Python 3.11

To set up a Conda environment for Python 3.11, follow these steps:

1. **Install Anaconda or Miniconda**: If you haven't installed Anaconda or Miniconda, download and install it from the official website.

2. **Create a new Conda environment**:
    ```bash
    conda create -n myenv python=3.11
    ```

3. **Activate the environment**:
    ```bash
    conda activate myenv
    ```

4. **Deactivate the environment when done**:
    ```bash
    conda deactivate
    ```

Replace `myenv` with your desired environment name and `package_name` with the packages you need for your project.

5. **Set up with conda envrionment file**:
    ```bash
    conda env create -f environment.yml
    ```
environment will be made named witth **coreml**