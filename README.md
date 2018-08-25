# liftOS
Lift management. 

Run the server:

$ python -m LiftOS

Run the clients:

$ python -m LiftClient < LiftClient/input1.txt
$ python -m LiftClient < LiftClient/input2.txt

## Inputs
------

Input file format as follows:

<IdUser> <StartingFloor> <UserWeight>
<NumberOfLinesToProcess>
<FloorToMove> <TimeInSecBeforeCallingAgain>
<FloorToMove> <TimeInSecBeforeCallingAgain>
...
