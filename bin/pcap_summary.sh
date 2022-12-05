for i in *pcap
do
echo -e "\nFILENAME: ${i}\n"
tshark -r ${i} -z conv,ip | awk '/^IPv4/,/==/'
done
