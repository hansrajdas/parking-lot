## Problem Statement
Implement a parking lot that can hold up to 'n' vehicles at any given point in time. Each slot is given a number starting at 1 increasing with increasing distance from the entry point in steps of one. 
Create an automated ticketing system that allows customers to use my parking lot without human intervention.

Due to government regulation, the system should provide the ability to find out:
* Registration numbers of all cars of a particular colour.
* Slot number in which a car with a given registration number is parked.
* Slot numbers of all slots where a car of a particular colour is parked.

We interact with the system via a simple set of commands which produce a specific
output. Please take a look at the example below, which includes all the commands
supported. The system should allow input in two ways:
1) It should provide us with an interactive command prompt based shell where
commands can be typed in
2) It should accept a filename as a parameter at the command prompt and read the
commands from that file

## Prerequisites
* Python
* Python mock package

## Setup
From `parking_lot` directory execute:
```
parking_lot$ bin/setup
```
Setup installs all dependencies all executes unit test suite.

## Assumptions
* This is implemented for single-storey only.
* If parking lot created again, it will create a new instance of parking lot and previous details will be lost.
* Before creating parking lot, non of the command will be supported.
* To exit from interactive mode use `exit` command.


## Usage
* Below are the 2 methods to execute application
```
parking_lot$ bin/parking_lot file_inputs.txt
parking_lot$ bin/parking_lot
```
* Execute test suite using below command
```
parking_lot$ bin/run_functional_tests
```
## Example
### File mode
To run the code so it accepts input from a file
```
parking_lot$ bin/parking_lot file_inputs.txt
```
File can have commands like
```
create_parking_lot 6
park KA-01-HH-1234 White
park KA-01-HH-9999 White
park KA-01-BB-0001 Black
park KA-01-HH-7777 Red
park KA-01-HH-2701 Blue
park KA-01-HH-3141 Black
leave 4
status
park KA-01-P-333 White
park DL-12-AA-9999 White
registration_numbers_for_cars_with_colour White
slot_numbers_for_cars_with_colour White
slot_number_for_registration_number KA-01-HH-3141
slot_number_for_registration_number MH-04-AY-1111
```
Console logs after parsing and executing above commands
```
Created a parking lot with 6 slots
Allocated slot number: 1
Allocated slot number: 2
Allocated slot number: 3
Allocated slot number: 4
Allocated slot number: 5
Allocated slot number: 6
Slot number 4 is free
Slot No. Registration No Colour
1        KA-01-HH-1234   White
2        KA-01-HH-9999   White
3        KA-01-BB-0001   Black
5        KA-01-HH-2701   Blue
6        KA-01-HH-3141   Black
Allocated slot number: 4
Sorry, parking lot is full
KA-01-HH-1234, KA-01-HH-9999, KA-01-P-333
1, 2, 4
6
Not found
```
### Interactive mode
To run the program and launch the shell
```
parking_lot$ bin/parking_lot
user@parking-lot$ create_parking_lot 6
Created a parking lot with 6 slots
user@parking-lot$ park KA-01-HH-1234 White
Allocated slot number: 1
user@parking-lot$ park KA-01-HH-9999 White
Allocated slot number: 2
user@parking-lot$ park KA-01-BB-0001 Black
Allocated slot number: 3
user@parking-lot$ park KA-01-HH-7777 Red
Allocated slot number: 4
user@parking-lot$ park KA-01-HH-2701 Blue
Allocated slot number: 5
user@parking-lot$ park KA-01-HH-3141 Black
Allocated slot number: 6
user@parking-lot$ leave 4
Slot number 4 is free
user@parking-lot$ status
Slot No. Registration No Colour
1        KA-01-HH-1234   White
2        KA-01-HH-9999   White
3        KA-01-BB-0001   Black
5        KA-01-HH-2701   Blue
6        KA-01-HH-3141   Blac
user@parking-lot$ park KA-01-P-333 White
Allocated slot number: 4
user@parking-lot$ park DL-12-AA-9999 White
Sorry, parking lot is full
user@parking-lot$ registration_numbers_for_cars_with_colour White
KA-01-HH-1234, KA-01-HH-9999, KA-01-P-333
user@parking-lot$ slot_numbers_for_cars_with_colour White
1, 2, 4
user@parking-lot$ slot_number_for_registration_number KA-01-HH-3141
6
user@parking-lot$ slot_number_for_registration_number MH-04-AY-1111
Not found
user@parking-lot$ exit
```
