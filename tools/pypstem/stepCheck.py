#!/usr/bin/env python3
import shutil
from tools.low.glob import *
from tools.low.__utilsVersion import *

def sayHi(ver):
    my_color = "\033[38;5;221m\033[48;2;150;75;0m"
    echo (f"{my_color}{cfg.project_name} v{ver.upper()}")

def exec_check(version, clear=False):
    version = version
    found_version = sort_bin_if_exist()
    old_version = get_ver(version)

    if not version or found_version or ("code.bin" in version):
        version = found_version or old_version
    else:
        if not is_ver_name(version):
            fail_ex (f"Passed argument \'{version}\' is not a valid version!", f"Available versions: {get_versions()}")
        if found_version and (found_version is not version):
            fail_ex ("found unsorted code.bin in data/, but parameter version differs.", "data/code.bin: " + found_version + ", specified: " + version)

        set_ver(version)

    if not is_ver_exist(version):
        set_ver(old_version)
        fail (f"data/ver/{version}/code.bin missing. Please provide the code.bin from the {version} version.")
    if not is_ver_valid(version):
        set_ver(old_version)
        fail (f"code.bin for {version} is invalid. Did you dump the right version, correctly?")
    if not is_ver_configured(version):
        set_ver(old_version)
        fail (f"Current version {version} is not configured. Try again later, por favor.")

    sayHi(version)

    if clear or (old_version != version):
        shutil.rmtree(getBuildPath(), ignore_errors=True)
        if clear:
            exit(0)
        else:
            print(f"Version changed, rebuilding. ({old_version.upper()} -> {version.upper()})")
    elif not getBuildPath().exists():
        getBuildPath().mkdir(parents=True, exist_ok = True)

    return version
