import re
from argparse import ArgumentParser

table_pat = re.compile(r"DropsLine\|name=([^|]+)\|quantity=(\d+)\|rarity=(\d+)/(\d+)")
dose_pat = re.compile(r".+\((\d)\)")
rune_pat = re.compile(r"(.+)\Wrune")
herb_pat = re.compile(r"HerbDropLines\|(\d+)/(\d+)")
rdt_pat = re.compile(r"GemDropTable\|(\d+)/(\d+)")

name_remap = {
    "Bronze bolts (p)": "bolt_p",
}


def _fix_dose(old_name):
    try:
        resp = re.findall(dose_pat, old_name)[0]
    except IndexError:
        return old_name
    else:
        new_name = old_name.replace('Super', '2')
        return f"{resp}dose{new_name[:-3]}"


def _fix_runes(old_name):
    try:
        resp = re.findall(rune_pat, old_name)[0]
    except IndexError:
        return old_name
    else:
        return f"{resp}rune"


def _name_remapping(old_name: str):
    old_name = _fix_dose(old_name)
    old_name = _fix_runes(old_name)
    try:
        return name_remap[old_name]
    except KeyError:
        return old_name.replace(" ", "_").replace("(p)", "_p").replace("Grimy", "unidentified").replace("'", "").lower()


def _parse_file(path):
    drop_table = []
    overall_base = None
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            resp = re.findall(table_pat, line)
            if len(resp) == 0:
                resp = re.findall(herb_pat, line)
                if len(resp) == 0:
                    resp = re.findall(rdt_pat, line)
                    if len(resp) == 0:
                        continue
                    else:
                        obj_name = "~randomjewel"
                        quantity = -1
                        rarity = resp[0][0]
                else:
                    obj_name = "~randomherb"
                    quantity = -1
                    rarity = resp[0][0]
            else:
                obj_name, quantity, rarity, base = resp[0]
            if overall_base is None:
                overall_base = base
            elif base != overall_base:
                raise ValueError("Base value changing in drop table")
            obj_name = _name_remapping(obj_name)
            drop_table.append({"name": obj_name, "quantity": quantity, "weight": rarity})

    if overall_base is None:
        raise ValueError("Unable to find the base value from the drop table")
    return overall_base, drop_table


def _generate_output(offset, weight, name, quantity):
    if offset == 0:
        new_offset = weight
        resp = f"if ($random < {weight})"
    else:
        new_offset = offset + int(weight)
        resp = f" else if ($random < {new_offset}) "
    resp += "{\n"
    if (quantity == -1):
        resp += f"    obj_add(npc_coord, {name}, ^lootdrop_duration);\n"
    else:
        resp += f"    obj_add(npc_coord, {name}, {quantity}, ^lootdrop_duration);\n"
    resp += "}"

    return resp, int(new_offset)


def build_rs2_file(in_file, out_file, npc_name):
    base, output = _parse_file(in_file)
    with open(out_file, 'w') as f:
        f.write(f"[ai_queue3,{npc_name}]\n")
        f.write("gosub(npc_death);\n")
        f.write("if (npc_findhero = false){\n")
        f.write("    return;\n")
        f.write("}\n\n")
        f.write("// Default drop from config\n")
        f.write("obj_add(npc_coord, npc_param(death_drop), 1, ^lootdrop_duration);\n\n")
        f.write(f"def_int $random = random({base});\n")

        offset = 0
        for obj in output:
            out, offset = _generate_output(offset, **obj)
            f.write(out)


if __name__ == "__main__":
    parser = ArgumentParser(
        description="Parse a wiki drop table into rs2",
        epilog="Any issues @gregf36665"
    )
    parser.add_argument('inputfile')
    parser.add_argument('outputfile')
    parser.add_argument('npcname')
    args = parser.parse_args()
    build_rs2_file(args.inputfile, args.outputfile, args.npcname)
