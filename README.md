# lambdadata_yuanjinren
Python package for practice. It includes two helpers, two classes and a docker file. 

## Installation

```sh
pip install -i https://test.pypi.org/simple/ lambdadata-yuanjinren
```

## Usage

```py
from my_lambdata.optionsetting import setting
from my_lambdata.insertcolumn import insertcol
```

## Docker file usage:

Use the following command lines to open docker image in terminal: (ID of the docker image is 9cd4e9c8196e)

 + docker start 9cd4e9c8196e
 + docker attach 9cd4e9c8196e
 + python
 + from my_lambdata.optionsetting import setting
 + from my_lambdata.insertcolumn import insertcol


## Restaurant Class:

There are three methods in restaurant class, namely describe_restaurant, restaurant_open and restaurant_closed. 

## Unittest Scripts:

Unittest scripts were prepared for two functions (insertcolumn and optionsetting) and the restaurant class. 