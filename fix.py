#!/usr/bin/python2.7

def convert_hashforge(hash_at,beginning,end):

	hexstuff = ""
	for i in range(0, len(hash_at)):
		if(hash_at[i] == "\\"):
			hexstuff = hash_at[:(i+4)]


	hexstuff = hexstuff[len(beginning):]
	converted = ""
	for j in range(0,len(hexstuff)-3,4):
		converted += chr(int(str(hexstuff[j+2:j+4]), 16))

	return(beginning+converted+end)
