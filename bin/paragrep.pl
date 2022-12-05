#!/bin/bash
#
#

echo "args: $@"
#perl -wpl -i -e "s///g;" $@;
#perl -wpl -i -e "s/edit/\n\nedit/g;" $@;

for i in $@
do
    if [[ -e ${i} ]]
    then
        echo -e "\n<!-- file: ${i} -->\n"
        perl -wnl -00 -e "/$1|\nconfig/ and print;" ${i} 
    fi
done
