#!/usr/bin/env python3
#
import os
import sys
import subprocess as sp
from files import Files

psxe_dir = sys.argv[1]
arch = 'intel64'
f = Files()

gcc = f.files['gcc']
env = f.files['env']

if not os.path.isdir(psxe_dir):
    print(f"""
{psxe_dir} is not a valid directory
""")
    exit()

dir = [ file for file in os.listdir(psxe_dir) if "parallel_studio_xe_" in file ]
psxe_major_version = min(dir)
psxe_minor_version = max(dir)
modulespath = '/software/x86_64/modulefiles/intel_parallel_studio_xe/'

vars_script = f"{psxe_dir}/{psxe_minor_version}/psxevars.sh"

if not os.path.isfile(vars_script):
    print(f"""
could not find a valid psxevars.sh file in {psxe_dir}/{psxe_minor_version}
""")
    exit()

env_cmd = f'{env} -i bash -f -c \'export PATH={os.path.dirname(gcc)}:$PATH;source {vars_script} {arch};{env}\''
clean_env_cmd = f'env -i bash -f -c env'
show_env = sp.getoutput(env_cmd)
clean_env = sp.getoutput(clean_env_cmd).splitlines()

vars = {}
for line in show_env.splitlines():
    if "=" not in line:
        #print(f"Skipping line : \"{line}\"")
        continue
    if line in clean_env:
        continue
    var = line.split("=")[0]
    values = line.split("=")[1]

    vars[var] = [ v for v in values.split(":") ] 

lua_module = ''
for var, values in vars.items():
    for value in values:
        lua_module += f"prepend_path(\"{var}\",\"{value}\")\n"

lua_module = f"""-- -*_ lua module file for {psxe_minor_version}

help([[Ensures that you have the path to {psxe_minor_version} in your path]])

family("intel_compiler")

whatis("{psxe_minor_version}")
{lua_module}
setenv("CC","icc")
setenv("CXX","icpc")
setenv("FC","ifort")
setenv("F90","ifort")
setenv("F77","ifort")

load("gcc")"""
print(lua_module)
