# Intel Psxevars To Lmod Converter
==================================

*Takes intel parallel studio psxevars.sh script and converts it into lmod lua module file.*

lmod is a lua based enviroment modules managemt system and can be found here https://lmod.readthedocs.io/
lmod add and remove directories from paths such as PATH, LD_LIBRARY_PATH, etc.

since intel parallel studio does not provide lmod module file this script
will source the intel variable file and create an lmod lua file.

The script was tested using python3 3.6.3
and the following Intel Parallel Studio XE Editions:

* 2015_update3
* 2016
* 2016_update3
* 2017_update1
* 2017_update2
* 2017_update4
* 2018_update1
* 2018_update2
* 2018_update3

Usage
-----
```
./PxevarsToLmod/run.py <INTEL_PSXE_ROOT_DIR>
```
```
./PxevarsToLmod/run.py /software/x86_64/intel/parallel_studio_xe_2018_update3/
```
