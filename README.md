## Overview

This is a Python implementation to find the closest pair of points in a three-dimensional space using divide and conquer
algorithm.

The program takes two inputs: the number of points to be generated, and the number of dimensions of the points.

After clicking <kbd>Start</kbd>, the program finds the closest pair of points with divide-and-conquer algorithm and
brute-force algorithm. After both algorithms done executing, the program compares said algorithms based on the number
of Euclidean distance operations and the execution time.

Data visualization is also implemented, but only if the number of dimensions is three.

[![proximate.png](https://i.postimg.cc/PfWWZs3Y/proximate.png)](https://postimg.cc/F1Kk5qQH)

## Prerequisites

- [Python 3.11.2](https://www.python.org/downloads/release/python-3112/)
- Required packages as specified
  in [`requirements.txt`](https://github.com/noelsimbolon/Tucil2_13521046_13521096/blob/main/requirements.txt)

## Directory Structure

```
├── doc        # Contains report for the project
├── src        # Contains source code for the program
...
```

## How To Use

1. Download this repository as a ZIP file and extract it
2. Open your terminal in the root directory of the project
3. Activate the virtual environment in which you want to install packages
4. Install required packages using `pip`

   ```shell
   pip install -r requirements.txt
   ```
5. Run `main.py` using `python` from the root directory

    ```shell
    python src/main.py
    ```
6. Input the number of points and the number of dimensions
7. Click <kbd>Start</kbd>
