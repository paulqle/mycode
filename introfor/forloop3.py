#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
   learning about for logic"""

# create the list called vendors
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]



# loop across the list vendors
for x in farms:
    print("The farms are:" + x)  # each time through the loop print value of x
print("\nOur loop has ended.")  # when the loop ends print this

