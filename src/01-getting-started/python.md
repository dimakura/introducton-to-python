# Installing Python

There are many possible ways to install Python on your system.
Here we will cover WSL installation on Windows 11.

## Installing Windows Subsystem for Linux (WSL)

WSL gives you a Linux environment running on Windows.

To install WSL, first open PowerShell as an adminstrator. For this, press the Windows key, type `powershell`, right-click on the `Windows PowerShell` app and select `Run as administrator`. Then enter the following command:

```powershell
$ wsl --install
```

and press `Enter`. This will install Ubuntu distribution and restart your computer.

Once restarted, open PowerSheel again, this time as a normal user. Then start your Linux session with:

```powershell
$ wsl ~
```

## Installing Miniconda

[Miniconda](https://docs.conda.io/en/latest/miniconda.html) is a package manager that allows you to install Python and other packages.

Execute the following commands in your terminal:

```sh
$ mkdir Downloads
$ cd Downloads
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

Once download is completed, run the installer, and follow the instructions:

```sh
$ bash Miniconda3-latest-Linux-x86_64.sh
```

To check that installation was successful, run:

```sh
$ conda --version
conda 23.3.1 # your version might be different
```

## Prepare your environment

It's usual for Python developers to create a virtual environment for each project. This allows you to install different versions of Python and packages for each project.

For this course, we will create a virtual environment called `pyinto`:

```sh
$ conda create -n pyinto python=3.11
```

When you need to use this environment, you can activate it with:

```sh
$ conda activate pyinto
```

You can check it with:

```sh
$ python --version
Python 3.11.3 # your version might be different
```