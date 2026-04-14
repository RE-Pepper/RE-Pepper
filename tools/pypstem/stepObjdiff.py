#!/usr/bin/env python3
from tools.low.glob import *
from tools.low.genComcom import *

def exec_objdiff(input=None):
    if not input:
        echo ("Objdiff step called but no input. Get out of here!")
        return

    if not input.endswith(".ctx"):
        return

    rel_path = Path(input).relative_to(getBuildObjPath())
    search_dir = getProjDir() / rel_path.parent
    matches = search_dir.glob(f"{rel_path.with_suffix('').name}.*")

    full_path = next(matches, None)

    if full_path is None:
        fail("File not found: " + str(rel_path))

    from tools.low.genContext import gen_ctx

    ctx, main = gen_ctx(full_path)

    if not Path(input).parent.exists():
        fail ("Directory not exist for output file: " + input)

    with open(input, "w") as f:
        f.write(ctx)
        f.write("\n\n")
        f.write(main)
