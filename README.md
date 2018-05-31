# PxevarsToLmod
lmod is a lua based enviroment modules managemt system.
lmod add and remove directories from paths such as PATH, LD_LIBRARY_PATH, etc.

when using intel parallel studio one must configure the user environment by
sourcing files such as psxevars.sh .

since intel parallel studio does not provide lmod module file this script
will source the intel variable file and create a lmod lua file.

The script was tested with python3 3.6.3
and the following Intel Parallel Studio XE Editions:

2015_update3
2016
2016_update3
2017_update1
2017_update2
2017_update4
2018_update1
2018_update2
2018_update3

./PxevarsToLmod/run.py <INTEL_PSXE_ROOT_DIR>

for example:

./PxevarsToLmod/run.py /software/x86_64/intel/parallel_studio_xe_2018_update3/

