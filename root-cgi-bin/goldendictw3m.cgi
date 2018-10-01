#!/bin/bash
#search words in goldendict
#Use this script when goldendict is running, because w3m freezes
#in "URL of dictionary lookup command" in OPTIONS 
#put file:///$LIB/goldendictw3m.cgi
goldendict $QUERY_STRING
printf "W3m-control: BACK\n\n"
