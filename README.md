# Impact Analytics Assessment

## Question

In a university, your attendance determines whether you will be allowed to attend your graduation ceremony. 
You are not allowed to miss classes for four or more consecutive days. 
Your graduation ceremony is on the last day of the academic year, which is the Nth day.

Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.
Represent the solution in the string format as "Answer of (2) / Answer of (1)", don't actually divide or reduce the fraction to decimal

Test cases:

for 5 days: 14/29

for 10 days: 372/773


>> Solution for this is mentioned though a Rest Api call
> 
>> Also one more script solution for this is written in a script with test cases
> 
>> Run the Get Api by below commands and pass the params no_of_days more than 4 less is handled check the exceptions


## Follow these commands step by step 
>> pip install -r requirements.txt
> 
>> python manage.py runserver

Get api call
>> http://127.0.0.1:8000/api/v1/attendance_class_info?no_of_days=4

Test cases too written we can run to check the condition

## OR

You can run the individual script mentioning as other file too directly with these below commands

>> python independent_script.py
> 
>> python unit_independent_test_cases.py

