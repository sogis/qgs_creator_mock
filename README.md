Utilized versions:
------------------

* QGIS 2.18
* Ubuntu 16.04
* python 2.7

Prerequisites:
--------------

You need a local and valid shp file to add. Because adding a layer to QGIS project means the layer has to be valid.
Therefor we need a dummy. To be flexible on input the appoach chosen is the simple one. Only rule: shp has to be 
named "input.shp".

Big picture:
------------

Everything runs in an Docker container. QGIS is used blank. Means without gui components. Python is invoked to use QGIS libs. Simple QGIS is spawned,
project loaded, layers added to QGIS-workspace and project, project is saved (to the same path where the input shp is stored).

Usage:
------

clone repository:
`https://github.com/simi-so/qgs_creator_mock.git`

walk into folder:
`cd qgs_creator_mock`

build image locally:
`docker build -t qgs_creator_mock:local_dev .`

run image:
`docker run --rm -v <path_to_local_shp>:/data qgs_creator_mock:local_dev`

where `<path_to_local_shp>` is the place where you keep your test shp.

Note:

> Means path of shp needs to be writeable for anybody!

Benchmark:
----------

For benchmarking on unix machines the simple to use GNU tool `time` can be utilized:

`/usr/bin/time -f "time result\ncmd:%C\nreal %es\nuser %Us \nsys  %Ss \nmemory:%MKB \ncpu %P" docker run --rm -v <path_to_local_shp>:/data qgs_creator_mock:local_dev`

This results in the following for 1000 iterations:

```
time result
cmd:docker run --rm -v /home/crud3_rt/tmp/:/data qgs_creator_mock:local_dev
real 3.68s
user 0.04s 
sys  0.02s 
memory:58860KB 
cpu 1%
```

On a System with:
* Intel® Core™ i7-8565U CPU (4 cores)

Pro of this benchmark method is, that all process time and mem usage is measures. Including eventually existing docker bottle necks.
