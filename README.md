# Table of Contents

1. [Description] (README.md#description)
2. [Repo directory structure] (README.md#repo-directory-structure)

##Description

[Back to Table of Contents] (README.md#table-of-contents)

<img src="./images/quilt_data.png" width="500">

Rich Inman's Data Engineering Project for Insight-SV-Jan-2017.

The project was a consulting project for a company called [Quilt Data](https://www.quiltdata.com). 

Quilt is a data package manager. You can use data packages from the community, or publish packages for others to use.

`quilt` is the command-line client that builds, retrieves, and stores packages. 
Prior to my [Insight Data Engineering project](http://insightdataengineering.com/), `quilt` contained a Python client that allowed users working in python on a single machine to quickly and easily import data into Pandas DataFrames. For this purpose `quilt` stored data frames in a high-efficiency, memory-mapped binary format known as [HDF5](https://support.hdfgroup.org/HDF5/). This provided access to data frames [5X to 20X faster](http://wesmckinney.com/blog/pandas-and-apache-arrow/).

Realizing that distributed conputing is quickly growing in popularity, Quilt Data decided that they would like to extend `quilt` client support to the [Apache Spark framework](http://spark.apache.org/), which was the primary thrust of my project.

##Repo directory structure
[Back to Table of Contents] (README.md#table-of-contents)

My Repo Structure

	├── README.md 
	├── __init__.py
	├── .gitignore
	├── images
	|   └── quilt_logo.pdf
	└── data_tools
	|   └── cpr_annual_csv.m
	|   └── read_parquet.py
	└── quilt
	    └── __init__.py
	    └── data.py
	    └── test
	    |    └── __init__.py
	    |    └── build.yml
	    |    └── gen_data.py
	    |    └── test_build.py
	    |    └── test_command.py
	    |    └── test_gen_data.py
	    |    └── test_signature.py
	    |    └── data
	    |        └── 10KRows13Cols.csv
	    |        └── 10KRows13Cols.tsv
	    |        └── 10KRows13Cols.xlsx
	    |        └── foo.csv
	    |        └── nuts.csv
	    └── tools
	        └── __init__.py
	        └── build.py
	        └── command.py
	        └── const.py
	        └── hashing.py
	        └── sign.py
	        └── store.py
	        └── util.py
