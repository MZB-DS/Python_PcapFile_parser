import json
import os
import datetime
import pandas as pd

path=input("Enter path of pcap file: ")
filename= input("Enter pcap filename: ")

wireshark_expression = '' # Enter the wireshark search expression for the post call and content type is json

command="tshark -r '{}/{}' -x -l -Y ''".format(path,filename,wireshark_expression)

print(command)

filename='{}_wireshark_capture.txt'.format(str(datetime.datetime.now()).split(" ")[1].split('.')[0])

os.system(command+ '>>' +filename)

f = open(filename)

data=''

for line in f:
    fields=[]
    if "Uncompressed" in line or "Frame" in line or line.startswith('\n'):
        data= data + '<break>'
        continue

    fields = line.strip().split('   ')
    data=data + str(fields[-1])

data_array = data.split('<break>') # data_array is the list of all the json parsed based on the given wireshark search expression

for i in range(0, len(data_array)-1):
    data_array[i] = data_array[i].replace('....{', '<break>{')
    if '<break>{' in data_array[i]:
        one,two = data_array[i].split('<break>')
        data_array[i]=two

os.remove(filename)
