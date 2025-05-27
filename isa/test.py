from insn.instruction import instr
from insn.operations import ArchState, load, zero_extend


@instr
def beq(rs1: int, rs2: int, bimm12: int, state: ArchState):
    if state.regfile[rs1] == state.regfile[rs2]:
        state.pc = state.pc + bimm12


@instr
def lw(rd: int, imm12: int, rs1: int, state: ArchState):
    addr = state.regfile[rs1] + imm12
    tmp = state.mem[addr] << 24 | state.mem[addr + 1] << 16 | state.mem[addr + 2] << 8 | state.mem[addr + 3]
    state.regfile[rd] = tmp


@instr
def lh(rd: int, imm12: int, rs1: int, state: ArchState):
    addr = state.regfile[rs1] + imm12
    tmp = state.mem[addr]
    tmp = (tmp << 8) | state.mem[addr + 1]
    state.regfile[rd] = tmp


# @instr
# def lhu(rd: int, imm12: int, rs1: int, state: ArchState):
#     tmp = zero_extend(load(addr=state.regfile[rs1] + imm12, size=2, state=state))
#     state.regfile[rd] = tmp

@instr
def sb(rs1: int, imm12: int, rs2: int, state: ArchState):
    addr = state.regfile[rs1] + imm12
    state.mem[addr] = state.regfile[rs2] & 0xff
