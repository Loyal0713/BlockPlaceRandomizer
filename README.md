# Block Place Randomizer

## About
Small python based tool used to randomize the blocks that are placed. 

## How to use
Have python installed (I use python 3.10). Open terminal and run the script via: ```script/location/BlockRandomizer.py start_slot end_slot {delay}``` where ```start_slot``` is the first slot to pick from and ```end_slot``` is the last slot to pick from.

To run with picking slots 3->8:
```script/location/BlockRandomizer.py 3 8```

The ```delay``` parameter is optional and determines how long (in seconds) to wait before picking a new slot. Default delay is .2 seconds.

To run with picking slots 2->9 with .25 second delay:
```script/location/BlockRandomizer.py 2 9 .25```

To run without a shell, change the extension from ```.py``` to ```.pyw```. This tells the python interpreter to run without a shell open.