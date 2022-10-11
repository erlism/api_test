*** Settings ***
Documentation       Run the robot which will call the python file and get the value of skipped
Library  get_api.py


*** Variables ***
#${URL_link}=   'https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow'



*** Tasks ***
| Example that calls a Python keyword
| | ${result}= | return skipped value  |
| | ${end_value}= | Convert To String  |  ${result}  |
| | Should be equal | ${end_value} | 0  |
