from typing import Callable
import inspect
import ast
import passes.assignment

from passes.assignment import has_register_assignment


def instr(fn: Callable):
    src = inspect.getsource(fn)
    tree = ast.parse(src)

    # extract the function definition
    func_def = next(node for node in ast.walk(tree)
                    if isinstance(node, ast.FunctionDef))
    func_name = func_def.name
    # args = [(arg.arg, arg.annotation.id) for arg in func_def.args.args]
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
