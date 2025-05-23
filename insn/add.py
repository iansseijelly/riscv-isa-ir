from isa.operations import *

@instr
def beq(rs1: int, rs2: int, bimm12: int):
    if regfile[rs1] == regfile[rs2]:
        pc = pc + bimm12

