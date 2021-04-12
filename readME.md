# Tentative Design


## State Representation
numpy array for state, w/ 1 elem. as 9 => indicating empty space

## Initial State

A scrambled 3x3 array with a 9 indicating the blank space. Here is 3x3 matrix we must provide the solution for:
/


1  9  3
4  2  6
7  5  8

Here we can see that the empty slot is marked 9 and is at (1,2) in matrix notation.

## Goal State

The goal state is obviously:

1  2  3
4  5  6
7  8  9



## Operators

We can move the -1 within the array. It cannot go diagonal, but it can go up,down,left or right depneding on the position.

### Move empty slot up

#### Precondition
The there is a # above the 9 (Not a boundary).

#### Instruction

The 9 and # above swap. For example, if we execute this in the goal state, the state will be:

1  2  3\
4  5  9\
7  8  6\



## Path Cost

The path cost in this problem is 1 for every operation. We want to minimize this obviously.

