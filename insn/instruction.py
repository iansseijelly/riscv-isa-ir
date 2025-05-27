from typing import Callable
import inspect
import ast
import passes.register
import passes.mem

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

    # print(ast.dump(tree, indent=2))

    # Valid
    valid = passes.register.is_valid_instruction(tree)
    print(f"Valid: {valid}")

    # BR_TYPE
    br_type = passes.register.test_conditional_assignment(tree)
    print(f"BR_TYPE: {br_type}")

    # has_register_read_rs1
    rs1 = passes.register.has_register_read_rs1(tree)
    print(f"has_register_read_rs1: {rs1}")

    # has_register_read_rs2
    rs2 = passes.register.has_register_read_rs2(tree)
    print(f"has_register_read_rs2: {rs2}")

    # has_register_write_rd
    rd = passes.register.has_register_write_rd(tree)
    print(f"has_register_write_rd: {rd}")

    # get_mem_read_size
    mem_read_size = passes.mem.get_mem_read_size(tree)
    print(f"get_mem_read_size: {mem_read_size}")

    # get_mem_write_size
    mem_write_size = passes.mem.get_mem_write_size(tree)
    print(f"get_mem_write_size: {mem_write_size}")
