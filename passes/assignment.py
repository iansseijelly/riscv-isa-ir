# given a @instr, determine whether an register assignment exists in the body

import ast


def extract_assignments(tree: ast.Module):
    assignments = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            assignments.append(node)
    return assignments


def extract_conditionals(tree: ast.Module):
    conditionals = []
    for node in ast.walk(tree):
        if isinstance(node, ast.If):
            conditionals.append(node)
    return conditionals


def extract_subscripts(tree: ast.Module):
    subscripts = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Subscript):
            subscripts.append(node)
    return subscripts


def is_valid_instruction(node: ast.AST):
    if node is not None:
        return "Y"
    else:
        return "N"


# is there a register assignment in the body?
def has_register_assignment(tree: ast.Module):
    assignments = extract_assignments(tree)
    for assignment in assignments:
        if len(assignment.targets) == 1 \
                and isinstance(assignment.targets[0], ast.Subscript) \
                and assignment.targets[0].value.id == "regfile":
            return True
    return False


def has_register_read_rs1(tree: ast.Module):
    subscripts = extract_subscripts(tree)
    for subscript in subscripts:
        if subscript.value.id == "regfile" \
                and subscript.slice.id == "rs1" \
                and subscript.value.ctx == ast.Load():
            return "OP1_RS1"
    return "OP1_X"


def test_register_assignment(tree: ast.Module):
    assignments = extract_assignments(tree)
    for assignment in assignments:
        if len(assignment.targets) == 1 \
                and isinstance(assignment.targets[0], ast.Subscript) \
                and isinstance(assignment.targets[0].value, ast.Name) \
                and assignment.targets[0].value.id == "regfile":
            print(assignment.value)
            return True
    print("0")
    return False


def has_pc_assignment(tree: ast.Module):
    assignments = extract_assignments(tree)
    for assignment in assignments:
        if len(assignment.targets) == 1 \
                and isinstance(assignment.targets[0], ast.Name) \
                and assignment.targets[0].id == "pc":
            print("1")
            return True
    print("0")
    return False


def test_conditional_assignment(tree: ast.Module):
    conditionals = extract_conditionals(tree)
    for conditional in conditionals:
        if len(conditional.test.ops) != 1:
            continue
        if isinstance(conditional.test.ops[0], ast.Eq):
            return "BR_EQ"
        elif isinstance(conditional.test.ops[0], ast.NotEq):
            return "BR_NE"
        elif isinstance(conditional.test.ops[0], ast.Lt):
            return "BR_LT"
        elif isinstance(conditional.test.ops[0], ast.LtE):
            return "BR_LE"
        elif isinstance(conditional.test.ops[0], ast.Gt):
            return "BR_GT"
    return "BR_N"