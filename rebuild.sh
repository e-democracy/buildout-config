#! /bin/bash
./bin/buildout -N
cd parts/instance/etc
ln -vsf ../../../etc/gsconfig.ini .
