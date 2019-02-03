#!/bin/bash
(shopt -s globstar; for s in */**.py; do timeout 1 python2 -3 "$s"; done) 2> error.log > /dev/null
grep -i failed error.log && exit 1 || exit 0
