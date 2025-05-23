from isa.operations import *

@instr
def add(rd: int, rs1: int, rs2: int):
    regfile[rd] = regfile[rs1] + regfile[rs2]

@instr
def addi(rd: int, rs1: int, imm12: int):
    regfile[rd] = regfile[rs1] + imm12

@instr
def sub(rd: int, rs1: int, rs2: int):
    regfile[rd] = regfile[rs1] - regfile[rs2]

@instr
def beq(rs1: int, rs2: int, bimm12: int):
    if regfile[rs1] == regfile[rs2]:
        pc = pc + bimm12

@instr
def bne(rs1: int, rs2: int, bimm12: int):
    if regfile[rs1] != regfile[rs2]:
        pc = pc + bimm12

@instr
def jalr(rd: int, rs1: int, imm12: int):
    regfile[rd] = pc + 4
    pc = regfile[rs1] + imm12

@instr
def lw(rd: int, imm12: int, rs1: int):
    tmp = load(addr=x(rs1) + imm12, size=4, rd=rd)
    regfile[rd] = tmp

@instr
def lh(rd: int, imm12: int, rs1: int):
    tmp = load(addr=x(rs1) + imm12, size=2, rd=rd)
    regfile[rd] = tmp

@instr
def lhu(rd: int, imm12: int, rs1: int):
    tmp = zero_extend(load(addr=x(rs1) + imm12, size=2, rd=rd))
    regfile[rd] = tmp

@instr
def sw(rs1: int, imm12: int, rs2: int):
    store(addr=regfile[rs1] + imm12, size=4, data=regfile[rs2])

@instr
def sh(rs1: int, imm12: int, rs2: int):
    store(addr=regfile[rs1] + imm12, size=2, data=regfile[rs2])

@instr
def sb(rs1: int, imm12: int, rs2: int):
    store(addr=regfile[rs1] + imm12, size=1, data=regfile[rs2])