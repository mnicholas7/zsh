#!/bin/bash
#

echo "args: $@"

for i in $@
do
    if [[ -e $i ]]
    then
    echo -e "\n<!-- changed file ${i} ]] -->\n"
        perl -wpl -i -e "s///g;" $i;
        perl -wpl -i -e "s:(edit|config):\n\n\n\n\$1:g;" $i;
    fi
done
