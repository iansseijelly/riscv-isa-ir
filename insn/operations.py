from dataclasses import dataclass


@dataclass
class ArchState:
    mem: dict[int, int]
    regfile: list[int]
    pc: int


# set the program counter to the value of target
def set_pc(target: int):
    global pc
    pc = target


# load the value from the memory at addr into the register rd
def load(addr: int, size: int, rd: int):
    global mem
    return mem[addr]


# store the value of data into the memory at addr
def store(addr: int, size: int, data: int):
    global mem
    mem[addr] = data


# zero extend the value of data to the size of the register
def zero_extend(data: int):
    pass
