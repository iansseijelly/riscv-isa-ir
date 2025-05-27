import ast


def extract_mem_reads(tree: ast.Module):
    mem_reads = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Subscript):
            match node:
                case ast.Subscript(
                    value=ast.Attribute(
                        value=ast.Name(id="state"),
                        attr="mem",
                    ),
                    ctx=ast.Load()
                ):
                    mem_reads.append(node.slice)
    return mem_reads


def extract_mem_writes(tree: ast.Module):
    mem_writes = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Subscript):
            match node:
                case ast.Subscript(
                    value=ast.Attribute(
                        value=ast.Name(id="state"),
                        attr="mem",
                    ),
                    ctx=ast.Store()
                ):
                    mem_writes.append(node.slice)
    return mem_writes


def coalesce_mem_ops(mem_ops: list[ast.Subscript]):
    coalescing: dict[str, set[int]] = {}
    for mem_op in mem_ops:
        match mem_op:
            case ast.Name(ctx=ast.Load()):
                coalescing[mem_op.id] = coalescing.get(mem_op.id, set()) | {0}
            case ast.BinOp(
                op=ast.Add(),
                left=ast.Name(ctx=ast.Load()),
            ):
                coalescing[mem_op.left.id] = coalescing.get(mem_op.left.id, set()) | {mem_op.right.value}
    # print(f"coalescing: {coalescing}")
    assert len(coalescing) <= 1, "At most one memory read is allowed"
    if len(coalescing) == 1:
        read_ops = coalescing.popitem()[1]
        # assert this is consecutive and start from 0
        assert read_ops == set(range(max(read_ops) + 1)), "Memory read size must be consecutive"
        return len(read_ops)
    else:
        return 0


def get_mem_read_size(tree: ast.Module):
    mem_reads = extract_mem_reads(tree)
    return coalesce_mem_ops(mem_reads)


def get_mem_write_size(tree: ast.Module):
    mem_writes = extract_mem_writes(tree)
    return coalesce_mem_ops(mem_writes)
