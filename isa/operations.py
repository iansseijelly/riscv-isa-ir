from dataclasses import dataclass
from enum import Enum
from typing import Callable
import inspect
import ast
import passes.assignment
# import gast
# import beniget

# import isa.register as register

from passes.assignment import has_register_assignment


class BinaryOperationType(Enum):
    ADD = '+'
    SUB = '-'


class MemOperationType(Enum):
    LOAD = 'load'
    STORE = 'store'


class Expr:
    pass


@dataclass
class BinaryOperation(Expr):
    op: BinaryOperationType
    left: Expr
    right: Expr


@dataclass
class MemOperation(Expr):
    op: MemOperationType
    addr: Expr
    data: Expr


class Stmt:
    pass


@dataclass
class Assign(Stmt):
    dest: int
    src: Expr


mem = {}
regfile = [0] * 32
pc = 0


# set the program counter to the value of target
def set_pc(target: int):
    global pc
    pc = target


# load the value from the memory at addr into the register rd
def load(addr: Expr, size: int, rd: int):
    global mem
    return mem[addr.val]


# store the value of data into the memory at addr
def store(addr: Expr, size: int, data: Expr):
    global mem
    mem[addr.val] = data.val


# get the value stored in the register at idx
def x(idx: int):
    global regfile
    return regfile[idx.idx]


# set the value of the register at idx to the value of target
def set_x(idx: int, target: Expr):
    pass


# zero extend the value of data to the size of the register
def zero_extend(data: Expr):
    pass


def instr(fn: Callable):
    src = inspect.getsource(fn)
    tree = ast.parse(src)

    # extract the function definition
    func_def = next(node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef))
    func_name = func_def.name
    args = [(arg.arg, arg.annotation.id) for arg in func_def.args.args]
    print(f"--- running on {func_name.upper()} ---")

    # convert the AST to a gast AST
    # duc = beniget.DefUseChains()
    # duc.visit(tree)

    print(ast.dump(tree, indent=2))

    # Valid
    valid = passes.assignment.is_valid_instruction(tree)
    print(f"Valid: {valid}")

    # BR_TYPE
    br_type = passes.assignment.test_conditional_assignment(tree)
    print(f"BR_TYPE: {br_type}")

    # has_register_read_rs1
    rs1 = passes.assignment.has_register_read_rs1(tree)
    print(f"has_register_read_rs1: {rs1}")

    has_register_assignment(tree)
