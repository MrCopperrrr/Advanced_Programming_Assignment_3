from StaticError import *
from Symbol import *
from functools import reduce


def simulate(list_of_commands):
    def is_valid_identifier(name):
        return (
            isinstance(name, str) and len(name) > 0 and name[0].islower() and
            all(c.isalnum() or c == '_' for c in name[1:])
        )

    def is_redeclared(name, current_scope):
        return any(sym.name == name for sym in current_scope)

    def insert_symbol(name, typ, table):
        if is_redeclared(name, table[-1]):
            raise Redeclared(f"INSERT {name} {typ}")
        return table[:-1] + [[Symbol(name, typ)] + table[-1]]

    def lookup(name, table):
        found = [sym.typ for scope in reversed(table) for sym in scope if sym.name == name]
        return found[0] if found else None

    def lookup_level(name, table):
        found_levels = [(i, sym) for i, scope in enumerate(reversed(table)) for sym in scope if sym.name == name]
        if not found_levels:
            raise Undeclared(f"LOOKUP {name}")
        return len(table) - 1 - found_levels[0][0]

    def get_type_of_value(val, table, cmd):
        if val.isdigit():
            return "number"
        if val.startswith("'") and val.endswith("'"):
            content = val[1:-1]
            if not all(c.isalnum() or c == ' ' for c in content) and content != "":
                raise InvalidInstruction(f"ASSIGN {cmd[7:]}")
            return "string"
        if is_valid_identifier(val):
            typ = lookup(val, table)
            if typ is None:
                raise Undeclared(f"ASSIGN {cmd[7:]}")
            return typ
        raise InvalidInstruction(f"ASSIGN {cmd[7:]}")

    def flatten_table(table):
        def helper(scopes, seen):
            return [] if not scopes else (
                [(sym.name, len(scopes) - 1) for sym in scopes[-1] if sym.name not in seen] +
                helper(scopes[:-1], seen | set(sym.name for sym in scopes[-1]))
            )
        return list(reversed(helper(table, set())))

    def flatten_table_reverse(table):
        def reducer(seen_names_levels, pair):
            scope, level = pair
            seen, acc = seen_names_levels
            filtered = [(sym.name, level) for sym in scope if sym.name not in seen]
            new_seen = seen.union(sym[0] for sym in filtered)
            return (new_seen, acc + filtered)
        
        _, result = reduce(reducer, zip(reversed(table), reversed(range(len(table)))), (set(), []))
        return result
    
    def process_command(table_result, cmd):
        table, results = table_result
        tokens = cmd.strip().split()

        if tokens[0] == "INSERT" and len(tokens) == 3:
            name, typ = tokens[1], tokens[2]
            if not is_valid_identifier(name) or typ not in ["number", "string"]:
                raise InvalidInstruction(cmd)
            new_table = insert_symbol(name, typ, table)
            return (new_table, results + ["success"])

        if tokens[0] == "ASSIGN" and len(tokens) == 3:
            name, val = tokens[1], tokens[2]
            val_type = get_type_of_value(val, table, cmd)
            id_type = lookup(name, table)
            if id_type is None:
                raise Undeclared(f"ASSIGN {cmd[7:]}")
            if id_type != val_type:
                raise TypeMismatch(f"ASSIGN {cmd[7:]}")
            return (table, results + ["success"])

        if tokens[0] == "BEGIN" and len(tokens) == 1:
            return (table + [[]], results)

        if tokens[0] == "END" and len(tokens) == 1:
            if len(table) == 1:
                raise UnknownBlock()
            return (table[:-1], results)

        if tokens[0] == "LOOKUP" and len(tokens) == 2:
            name = tokens[1]
            if not is_valid_identifier(name):
                raise InvalidInstruction(f"LOOKUP {name}")
            level = lookup_level(name, table)
            return (table, results + [str(level)])

        if tokens[0] == "PRINT" and len(tokens) == 1:
            flattened_print = flatten_table(table)
            print_line = ' '.join([f"{name}//{level}" for name, level in flattened_print])
            return (table, results + [print_line])

        if tokens[0] == "RPRINT" and len(tokens) == 1:
            flattened_rprint = flatten_table_reverse(table)
            rprint_line = ' '.join([f"{name}//{level}" for name, level in flattened_rprint])
            return (table, results + [rprint_line])


        raise InvalidInstruction(cmd)

    try:
        final_table, outputs = reduce(process_command, list_of_commands, ([[]], []))
        if len(final_table) > 1:
            raise UnclosedBlock(len(final_table) - 1)
        return outputs
    except StaticError as e:
        return [str(e)]
