# Functional Suite

`functional_spec/` contains the unittest based automated testing suite  to verify correctness of program for the sample input and output.

## Setup

First, install [Python](https://www.python.org/downloads/). Then run the following commands under the `functional_spec` dir.

```
functional_spec$ python -V  # Confirm Python is installed
Python 2.7.15rc1

functional_spec$ pip install mock  # Install mock python package
Collecting mock
  Using cached https://files.pythonhosted.org/packages/e6/35/f187bdf23be87092bd0f1200d43d23076cee4d0dec109f195173fd3ebc79/mock-2.0.0-py2.py3-none-any.whl
Collecting funcsigs>=1; python_version < "3.3" (from mock)
  Using cached https://files.pythonhosted.org/packages/69/cb/f5be453359271714c01b9bd06126eaf2e368f1fddfff30818754b5ac2328/funcsigs-1.0.2-py2.py3-none-any.whl
Collecting six>=1.9 (from mock)
  Using cached https://files.pythonhosted.org/packages/67/4b/141a581104b1f6397bfa78ac9d43d8ad29a7ca43ea90a2d863fe3056e86a/six-1.11.0-py2.py3-none-any.whl
Collecting pbr>=0.11 (from mock)
  Using cached https://files.pythonhosted.org/packages/f3/04/fddc1c2dd75b256eda4d360024692231a2c19a0c61ad7f4a162407c1ab58/pbr-5.1.1-py2.py3-none-any.whl
Installing collected packages: funcsigs, six, pbr, mock
Successfully installed funcsigs-1.0.2 mock-2.0.0 pbr-5.1.1 six-1.11.0
```

## Usage

Run the full test suite from `parking_lot` by doing
```
parking_lot$ bin/run_functional_specs
```
