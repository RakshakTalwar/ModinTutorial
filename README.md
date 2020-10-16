Run the data/generate_random_csv.py code 3 times.
Each time set the size_selection variable to a new value.
Values are: 
- small
- medium
- large

(This will take over 1GB of space on your drive)

Then run the modin_pandas.py and vanilla_pandas.py scripts.
The wall time of each respective program will be printed to STDOUT.
Experiment by changing which data you use to compute on on line 7.

You will notice that Modin, for the most part, is actually slower than regular 'vanilla' pandas