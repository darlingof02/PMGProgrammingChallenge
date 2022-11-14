# CSV Combiner

## Environment Requirement
Before you start, a python3-environment is needed. Run the command below to get necessary package for the program.
```shell script
pip3 install pandas
```
## Running Command
Given the filenames, you are able to get the desired file in a very fast speed. Here you can test the correctness of the program using small data set.

Of course, the content of the files and the number of input files can be changed and the program still works.
```shell script
$ ./csv-combiner.py ./fixtures/accessories_small.csv ./fixtures/clothing_small.csv ./fixtures/household_cleaners_small.csv > combined_small.csv
```

## Performance Tested
Using the ***generatefixtures*** file, we have three files whose total size is more than 2 GB and you can run the same command above to get the desired file. With a simpler running time clock provided by module 
***datetime***, the overall run time of the program is measured to be 1 min 5 seconds.

You can get desired file using command below.
```shell script
$ ./generatefixtures.py 
$ ./csv-combiner.py ./fixtures/accessories.csv ./fixtures/clothing.csv ./fixtures/household_cleaners.csv > combined.csv
```
