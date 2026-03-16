#!/usr/bin/env python3
import shutil
from tools.low.glob import *
from tools.low.utilsVersion import *
from tools.pypstem.manSetup import check_wibo

def sayHi():
    my_color = "\033[38;5;221m\033[48;2;150;75;0m"
    echo (f"{my_color}{cfg.project_name} v{getVersion().upper()}")

def exec_check(version, clear=False, stop=False):

    # decide which version to use
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

        write_ver(version)

    # assert version
    if not is_ver_exist(version):
        write_ver(old_version)
        fail (f"data/ver/{version}/code.bin missing. Please provide the code.bin from the {version} version.")
    if not is_ver_valid(version):
        write_ver(old_version)
        fail (f"code.bin for {version} is invalid. Did you dump the right version, correctly?")
    if not is_ver_configured(version):
        write_ver(old_version)
        fail (f"Current version {version} is not configured. Try again later, por favor.")

    # hi
    setVersion(version)
    sayHi()

    # clear on change
    if clear or (old_version != version):
        if getBuildPath().exists():
            shutil.rmtree(getBuildObjPath(), ignore_errors=True) # rem objects
            if getBuildLibPath().exists():
                for item in getBuildLibPath().iterdir(): # only keep split
                    if item.is_file() and not getSplitLibName() in item.name: 
                        item.unlink()
            for item in getBuildPath().iterdir():
                if item.is_file():
                    item.unlink()
        if not clear and not stop:
            print(f"Version changed, rebuilding. ({old_version.upper()} -> {version.upper()})")

    if not getBuildObjPath().exists():
        getBuildObjPath().mkdir(parents=True, exist_ok = True)
    if not getBuildLibPath().exists():
        getBuildLibPath().mkdir(parents=True, exist_ok = True)

    # misc
    check_wibo()

    if stop:
        exit(0)
