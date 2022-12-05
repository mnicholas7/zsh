#!/bin/bash -x
#
ARG=("$@")

echo "ARG LIST IS: ${ARG[@]}"
#
for file in ${ARG[@]}
do
  perl -wpl -i -e "s///g;" ${file}
done
#
#
