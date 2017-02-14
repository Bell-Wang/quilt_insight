# Table of Contents

1. [Description] (README.md#description)
2. [Repo directory structure] (README.md#repo-directory-structure)

##Description

[Back to Table of Contents] (README.md#table-of-contents)

Rich Inman's Data Engineering Project for Insight-SV-Jan-2017.

##Repo directory structure
[Back to Table of Contents] (README.md#table-of-contents)

My Repo Structure

	├── README.md 
	├── __init__.py
	├── .gitignore
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
