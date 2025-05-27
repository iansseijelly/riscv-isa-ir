# RISC-V ISA IR

A way to generate control signals from static analysis with ISA IR definition.

## Notes

Let's start by defining a very simple `add` instruction.

One may naively want to define add as:

```[python]
def add(rd: int, rs1: int, rs2: int):
    rd = rs1 + rs2
```

### Defining an Architectural State

Why do we need to define an arch state?

### Handling Implicit Arch State Changes

Handling things like PC+4 and TLB effects.

### Handling Memory Operations

### Connections?

Specifying connection is absent in the current settings.

### More Complex signals

Handling things like memory flushing and synchronization.
