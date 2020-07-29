# Python_PcapFile_parser
The repository contains python code for parsing the pcap file. For the network engineers, it is crucial to be able to parse the live traffic and draw some insights from it. A famous tool to view the pcap file is WireShark. Although it is a powerful tool, many a times some insights are tough to get from the manual search in this tool. The command line alternative of the WireShark is the "tshark" command. In this python code, we will be using the "tshark" linux command to parse the post calls having the content type as 'application/json'. After the execution of the program, we will have all the parsed json in the "data_array" list. We can do any analysis on that json. The json parsing to dataframe is not included in the code as the structure of the json will depend on the end user's pcap file.

## How to use this code
1. Install tshark in your linux with the help of the command
```sudo apt update;sudo apt install tshark```
2. If you are capturing the traffic directy in the wireshark then the file will be the pcap file. However if the capture is done on the server using the tcpdump then make sure to capture the traffic in the pcap file, with the help of option "-w".
3. In the code ```python_pcap_file_parser.py```, enter the wireshark search expression in the variable "wireshark_expression". Make sure to provide proper escapes in case there is mix of single and double quotes.
4. Execute ```python_pcap_file_parser.py```.
5. Enter the path where the input pcap file is stored.
6. Enter the pcap filename.
7. The code will start parsing the pcap file based on the given wireshark expression. And all the json will be stored in the python list "data_array". You can now do any analysis on the stored json.

## Future Features
Adding the support for parsing the GET calls and in case of POST calls also supporting Content-Type: text/xml

## Dependencies
- Python3 any version
- tshark: Network protocol analyser
- Wireshark: Network protocol analyser tool
- Python package: json, os, datetime
