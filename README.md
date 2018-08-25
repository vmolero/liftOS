# liftOS
Lift management. 

Run the server:

```bash
$ python -m LiftOS
```
Run the clients:

```bash
$ python -m LiftClient < LiftClient/input1.txt
```
```bash
$ python -m LiftClient < LiftClient/input2.txt
```
## Inputs
------

Input file format as follows:

```
<IdUser> <StartingFloor> <UserWeight>
<NumberOfLinesToProcess>
<FloorToMove> <TimeInSecBeforeCallingAgain>
<FloorToMove> <TimeInSecBeforeCallingAgain>
...
```