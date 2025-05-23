from insn.instruction import instr
from insn.operations import ArchState


@instr
def beq(rs1: int, rs2: int, bimm12: int, state: ArchState):
    if state.regfile[rs1] == state.regfile[rs2]:
        state.pc = state.pc + bimm12
