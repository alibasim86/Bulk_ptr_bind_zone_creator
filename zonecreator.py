#!/usr/bin/python

# this script creates the zone file and the named.conf zone params.
#please confirm the zone file location so that the generate named.conf will have the right path value.
#please check the name server name and master IP


import binascii


# subnet range finder
def  range (subnet,mask,files_loc):
	v= subnet.split (".")
	if mask <8:
		offset=8-mask
		st="0b"+"1"*offset
		newmaxsub= str(int (v[0])+int(st,2))+"."+v[1]+"."+v[2]+"."+v[3]
		gen (subnet,int(st,2),0,files_loc)

	elif ((mask>8) and (mask <16)):
                offset =16-mask
                st="0b"+"1"*offset
                newmaxsub= v[0]+"."+str(int (v[1])+int(st,2))+"."+v[2]+"."+v[3]
		gen (subnet,int(st,2),1,files_loc)

		

	elif ((mask >16) and (mask <24)):
                offset =24-mask
                st="0b"+"1"*offset
                newmaxsub= v[0]+"."+v[1]+"."+str(int (v[2])+int(st,2))+"."+v[3]
		gen (subnet,int(st,2),2,files_loc)
											

	elif ((mask >24) and (mask <32)):
                offset =32-mask
                st="0b"+"1"*offset
                newmaxsub= v[0]+"."+v[1]+"."+v[2]+"."+str(int(v[3])+int(st,2))
		gen (subnet,int(st,2),3,files_loc)



	return(newmaxsub)

def gen (lowsub,sub,octet,files_loc):

	i=0
	v=lowsub.split(".")
	a= int (v[octet])
	c= a+sub
	while a <=c:
		if octet == 0:
			f= open (files_loc+v[3]+"."+v[2]+"."+v[1]+"."+str(a)+".zone","w")
			f.write("$TTL 86400\n$ORIGIN "+str(a)+".in-addr.arpa.\n@	IN	SOA	ns1.domain.com.	hostmaster.domain.com. (\n				2016070601      ; serial number\n				14400           ; refresh, 4 hours\n				3600            ; update retry, 1 hour\n				604800          ; expiry, 7 days\n				600             ; minimum, 10 minutes\n				)\n	IN	NS	ns1.domain.com.\n	IN      NS      ns2.domain.com.\n	IN      NS      ns3.domain.com.\n$ORIGIN "+str(a)+".in-addr.arpa.\n")
			f.close
			cf= open (files_loc+"named.conf-master","a")
			cf.write( 'zone "'+str(a)+'.in-addr.arpa"' +"{\n	type master;\n	file "+'"'+v[3]+"."+v[2]+"."+v[1]+"."+str(a)+'.zone";\n'+"	allow-query { any;};\n	};\n")
			cf.close
			cfs= open(files_loc+"named.conf-slave","a")
                        cfs.write('zone "'+str(a)+'.in-addr.arpa"' +"{\n	type slave;\n	masters { 192.168.10.1; };\nfile "+'"'+v[3]+"."+v[2]+"."+v[1]+"."+str(a)+'.zone";\n'+"	allow-query { any;};\n	};\n")
			cfs.close
                if octet == 1:
                        f= open (files_loc+v[3]+"."+v[2]+"."+str(a)+"."+v[0]+".zone","w")
                        f.write("$TTL 86400\n$ORIGIN "+str(a)+"."+v[0]+".in-addr.arpa.\n@      IN      SOA     ns1.domain.com.        hostmaster.domain.com. (\n                               2016070601      ; serial number\n                               14400           ; refresh, 4 hours\n                               3600            ; update retry, 1 hour\n                               604800          ; expiry, 7 days\n                               600             ; minimum, 10 minutes\n                               )\n       IN      NS      ns1.domain.com.\n       IN      NS      ns2.domain.com.\n       IN      NS      ns3.domain.com.\n$ORIGIN "+str(a)+"."+v[0]+".in-addr.arpa.\n")
                        f.close
                        cf= open (files_loc+"named.conf-master","a")
                        cf.write('zone "'+str(a)+"."+v[0]+'.in-addr.arpa"' +"{\n	type master;\n	file "+'"'+v[3]+"."+v[2]+"."+str(a)+"."+v[0]+'.zone";\n'+"	allow-query { any;};\n	};\n")
                        cf.close
                        cfs= open(files_loc+"named.conf-slave","a")
                        cfs.write('zone "'+str(a)+"."+v[0]+'.in-addr.arpa"' +"{\n	type slave;\n	masters { 192.168.10.1; };\n	file "+'"'+v[3]+"."+v[2]+"."+str(a)+"."+v[0]+'.zone";\n'+"	allow-query { any;};\n	};\n")
                        cfs.close
                if octet == 2:
                        f= open (files_loc+v[3]+"."+v[2]+"."+str(a)+"."+v[0]+".zone","w")
                        f.write("$TTL 86400\n$ORIGIN "+str(a)+"."+v[1]+"."+v[0]+".in-addr.arpa.\n@      IN      SOA     ns1.domain.com.        hostmaster.domain.com. (\n                               2016070601      ; serial number\n                               14400           ; refresh, 4 hours\n                               3600            ; update retry, 1 hour\n                               604800          ; expiry, 7 days\n                               600             ; minimum, 10 minutes\n                               )\n       IN      NS      ns1.domain.com.\n       IN      NS      ns2.domain.com.\n       IN      NS      ns3.domain.com.\n$ORIGIN "+vstr(a)+"."+v[1]+"."+v[0]+".in-addr.arpa.\n")
                        f.close
                        cf=open (files_loc+"named.conf-master","a")
                        cf.write('zone "'+str(a)+"."+v[1]+"."+v[0]+'.in-addr.arpa"' +"{\n	type master;\n	file "+'"'+v[3]+"."+str(a)+"."+v[1]+"."+v[0]+'.zone";\n'+"	allow-query { any;};\n	};\n")
                        cf.close
                        cfs= open(files_loc+"named.conf-slave","a")
                        cfs.write('zone "'+str(a)+"."+v[1]+"."+v[0]+'.in-addr.arpa"' +"{\n	type slave;\n	masters { 192.168.10.1; };\n	file "+'"'+v[3]+"."+str(a)+v[2]+"."+v[1]+"."+v[0]+'.zone";\n'+"	allow-query { any;};\n	};\n")
                        cfs.close
                if octet == 3:
                        f= open (files_loc+str(a)+"."+v[2]+"."+v[1]+"."+v[0]+".zone","w")
                        f.write("$TTL 86400\n$ORIGIN "+str(a)+"."+v[2]+"."+v[1]+"."+v[0]+".in-addr.arpa.\n@      IN      SOA     ns1.domain.com.        hostmaster.domain.com. (\n                               2016070601      ; serial number\n                               14400           ; refresh, 4 hours\n                               3600            ; update retry, 1 hour\n                               604800          ; expiry, 7 days\n                               600             ; minimum, 10 minutes\n                               )\n       IN      NS      ns1.domain.com.\n       IN      NS      ns2.domain.com.\n       IN      NS      ns3.domain.com.\n$ORIGIN "+str(a)+"."+v[2]+"."+v[1]+"."+v[0]+".in-addr.arpa.\n")
                        f.close
                        cf= open (files_loc+"named.conf-master","a")
                        cf.write('zone "'+ str(a)+"."+v[2]+"."+v[1]+"."+v[0]+'.in-addr.arpa"' +"{\n	type master;\n	file "+'"'+str(a)+"."+v[2]+"."+v[1]+"."+v[0]+'.zone";\n'+"	allow-query { any;};\n	};\n")
                        cf.close
                        cfs=open(files_loc+"named.conf-slave","a")
                        cfs.write('zone "'+str(a)+"."+v[2]+"."+v[1]+"."+v[0]+'.in-addr.arpa"' +"{\n	type slave;\n	masters { 192.168.10.1; };\n	file "+'"'+str(a)+"."+v[2]+"."+v[1]+"."+v[0]+'.zone";\n'+"	allow-query { any;};\n	};\n")
                        cfs.close

		a=a+1
	return()

def genoct(subnet,maski,files_loc):
	v = subnet.split(".")
	ma = mask/8
	if ma ==1:
		cf =open(files_loc+"named.conf-master","a")
		cf.write('zone "'+ v[0]+'.in-addr.arpa"' +"{\n   type master;\n   file "+'"'+v[0]+'.zone";\n'+"   allow-query { any;};\n  };\n")
		cf.close
		cfs=open(files_loc+"named.conf-slave","a")
		cfs.write('zone "'+v[0]+'.in-addr.arpa"' +"{\n   type slave;\n   masters { 192.168.10.1; };\n   file "+'"'+v[0]+'.zone";\n'+"   allow-query { any;};\n  };\n")
		cfs.close
	
		f= open ("./david-zones/"+v[0]+".zone","w")
		f.write("$TTL 86400\n$ORIGIN "+v[0]+".in-addr.arpa.\n@      IN      SOA     ns1.domain.com.        hostmaster.domain.com. (\n                               2016070601      ; serial number\n                               14400           ; refresh, 4 hours\n                               3600            ; update retry, 1 hour\n                               604800          ; expiry, 7 days\n                               600             ; minimum, 10 minutes\n                               )\n       IN      NS      ns1.domain.com.\n       IN      NS      ns2.domain.com.\n       IN      NS      ns3.domain.com.\n$ORIGIN "+v[0]+".in-addr.arpa.\n")
	if ma==2:
		cf =open(files_loc+"named.conf-master","a")
		cf.write('zone "'+v[1]+"."+v[0]+'.in-addr.arpa"' +"{\n   type master;\n   file "+'"'+v[1]+"."+v[0]+'.zone";\n'+"   allow-query { any;};\n  };\n")
		cf.close
		cfs=open(files_loc+"named.conf-slave","a")
		cfs.write('zone "'+v[1]+"."+v[0]+'.in-addr.arpa"' +"{\n   type slave;\n   masters { 192.168.10.1; };\n   file "+'"'+v[1]+"."+v[0]+'.zone";\n'+"   allow-query { any;};\n  };\n")
		cfs.close
	
		f= open (files_loc+v[1]+"."+v[0]+".zone","w")
		f.write("$TTL 86400\n$ORIGIN "+v[1]+"."+v[0]+".in-addr.arpa.\n@      IN      SOA     ns1.domain.com.        hostmaster.domain.com. (\n                               2016070601      ; serial number\n                               14400           ; refresh, 4 hours\n                               3600            ; update retry, 1 hour\n                               604800          ; expiry, 7 days\n                               600             ; minimum, 10 minutes\n                               )\n       IN      NS      ns1.domain.com.\n       IN      NS      ns2.domain.com.\n       IN      NS      ns3.domain.com.\n$ORIGIN "+v[1]+"."+v[0]+".in-addr.arpa.\n")
	if ma==3:
		cf =open(files_loc+"named.conf-master","a")
		cf.write('zone "'+v[2]+"."+v[1]+"."+v[0]+'.in-addr.arpa"' +"{\n   type master;\n   file "+'"'+v[2]+"."+v[1]+"."+v[0]+'.zone";\n'+"   allow-query { any;};\n  };\n")
		cf.close
		cfs=open(files_loc+"named.conf-slave","a")
		cfs.write('zone "'+v[2]+"."+v[1]+"."+v[0]+'.in-addr.arpa"' +"{\n   type slave;\n   masters { 192.168.10.1; };\n   file "+'"'+v[2]+"."+v[1]+"."+v[0]+'.zone";\n'+"   allow-query { any;};\n  };\n")
		cfs.close
	
		f= open (files_loc+v[2]+"."+v[1]+"."+v[0]+".zone","w")
		f.write("$TTL 86400\n$ORIGIN "+v[2]+"."+v[1]+"."+v[0]+".in-addr.arpa.\n@      IN      SOA     ns1.domain.com.        hostmaster.domain.com. (\n                               2016070601      ; serial number\n                               14400           ; refresh, 4 hours\n                               3600            ; update retry, 1 hour\n                               604800          ; expiry, 7 days\n                               600             ; minimum, 10 minutes\n                               )\n       IN      NS      ns1.domain.com.\n       IN      NS      ns2.domain.com.\n       IN      NS      ns3.domain.com.\n$ORIGIN "+v[2]+"."+v[1]+"."+v[0]+".in-addr.arpa.\n")
	if ma==4:
		cf =open(files_loc+"named.conf-master","a")
		cf.write('zone "'+v[3]+"."+v[2]+"."+v[1]+"."+v[0]+'.in-addr.arpa"' +"{\n   type master;\n   file "+'"'+v[3]+"."+v[2]+"."+v[1]+"."+v[0]+'.zone";\n'+"   allow-query { any;};\n  };\n")
		cf.close
		cfs=open(files_loc+"named.conf-slave","a")
		cfs.write('zone "'+v[3]+"."+v[2]+"."+v[1]+"."+v[0]+'.in-addr.arpa"' +"{\n  type slave;\n   masters { 192.168.10.1; };\n   file "+'"'+v[3]+"."+v[2]+"."+v[1]+"."+v[0]+'.zone";\n'+"   allow-query { any;};\n  };\n")
		cfs.close
	
		f= open (files_loc+v[3]+"."+v[2]+"."+v[1]+"."+v[0]+".zone","w")
		f.write("$TTL 86400\n$ORIGIN "+v[3]+"."+v[2]+"."+v[1]+"."+v[0]+".in-addr.arpa.\n@      IN      SOA     ns1.domain.com.        hostmaster.domain.com. (\n                               2016070601      ; serial number\n                               14400           ; refresh, 4 hours\n                               3600            ; update retry, 1 hour\n                               604800          ; expiry, 7 days\n                               600             ; minimum, 10 minutes\n                               )\n       IN      NS      ns1.domain.com.\n       IN      NS      ns2.domain.com.\n       IN      NS      ns3.domain.com.\n$ORIGIN "+v[3]+"."+v[2]+"."+v[1]+"."+v[0]+".in-addr.arpa.\n")
c=0
files_loc = raw_input ("please specify where you want the files to be stored please incuding the tailing /: ")
print files_loc	
while c!=3:
	print "please choose what you want to do:"
	print "1) generate reverse  zone for one octet based subnet"
	print "2) generate reverse zone for one none octect based submet"
	print "3) Exit"
	c= input ("choose by number: ")


# this part generates zone files based on none octed zone
	if c == 2:
		subnet =""
		subnet= raw_input (" please enter the subnet address: ")
		mask= input ("please enter the mask (bit number): ")
		print subnet+"/"+str(mask)
		maxsubnet= range(subnet,mask,files_loc)


	if c==1:
	        subnet =""
       		subnet= raw_input (" please enter the subnet address: ")
        	mask= input ("please enter the mask (bit number): ")
        	print subnet+"/"+str(mask)

		genoct(subnet,mask,files_loc)

print "Enjoy...bye!"
