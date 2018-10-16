###################################################################
#                        Import Module
import json , sys , hashlib , os , time , marshal
###################################################################
'''
     Facebook Information 
'''
###################################################################
#                             COLOR
if sys.platform in ["linux","linux2"]:
	W = "\033[0m"
        G = '\033[32;1m'
        R = '\033[31;1m'
else:
	W = ''
	G = ''
	R = ''
###################################################################
#                      Exception
try:
	import requests
except ImportError:
	print R + '_     _'.center(44)
	print "o' \.=./ `o".center(44)
	print '(o o)'.center(44)
	print 'ooO--(_)--Ooo'.center(44)
	print W + ' '
	print ('O S I F').center(44)
	print ' '
	print "[!] Can't import module 'requests'\n"
	sys.exit()
####################################################################
#                    Set Default encoding
reload (sys)
sys . setdefaultencoding ( 'utf8' )

jml = []
jmlgetdata = []
n = []

def baliho():
	try:
		token = open('cookie/token.log','r').read()
		r = requests.get('https://graph.facebook.com/me?access_token=' + token)
		a = json.loads(r.text)
		name = a['name']
		n.append(a['name'])


	except (KeyError,IOError):
	 
		print ' ' + W
		print ('F B').center(44)
		print (W + '     [' + G +'Facebook Information'+ W + ']')
		print ' '
####################################################################
#		    Print In terminal
def show_program():

	print '''
                    %sINFORMATION%s
 ------------------------------------------------------

    Author     Luke Clegg
    Name       Facebook Information
    Version    Full Version
    Date       13/10/2018 

'''%(G,W)
def info_ga():

	print '''
     %sCOMMAND                      DESCRIPTION%s
  -------------       -------------------------------------

   get_data           fetching all friends data
   get_info           show information about your friend

   dump_id            fetching all id from friend list
   dump_phone         fetching all phone number from friend list
   dump_mail          fetching all emails from friend list
   dump_data          fetching all data from friend list
   dump_<id>_id       fetching all id from your friends <spesific>
		      ex: dump_username_id

   token              Generate access token
   cat_token          show your access token
   rm_token           remove access token


   clear              clear terminal
   help               show help
   about              Show information about this program
   exit               Exit the program
'''%(G,W)


####################################################################
#                     GENERATE ACCESS TOKEN
def get(data):
	print '[*] Generate access token '

	try:
		os.mkdir('cookie')
	except OSError:
		pass

	b = open('cookie/token.log','w')
	try:
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)

		b.write(a['access_token'])
		b.close()
		print '[*] successfully generate access token'
		print '[*] Your access token is stored in cookie/token.log'
		exit()
	except KeyError:
		print '[!] Failed to generate access token'
		print '[!] Check your connection / email or password'
		os.remove('cookie/token.log')
		main()
	except requests.exceptions.ConnectionError:
		print '[!] Failed to generate access token'
		print '[!] Connection error !!!'
		os.remove('cookie/token.log')
		main()
def id():
	print '[*] login to your facebook account         ';id = raw_input('[?] Username : ');pwd = raw_input('[?] Password : ');API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
	x = hashlib.new('md5')
        x.update(sig)

	data.update({'sig':x.hexdigest()})
        get(data)

#
###############################################################################

###############################################################################
#                         Dump Data

def dump_id():

	print '[*] Load Access Token'
	try:
		token = open("cookie/token.log",'r').read()
		print '[*] success load access token'
	except IOError:
		print '[!] failed load access token'
		print "[*] type 'token' to generate access token"
		main()

	try:
		os.mkdir('output')
	except OSError:
		pass

	print '[*] fetching all friends id'
	try:

		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
		a = json.loads(r.text)

		out = open('output/' + n[0].split(' ')[0] + '_id.txt','w')
		for i in a['data']:
			out.write(i['id'] + '\n')
			print '\r[*] %s retrieved'%(i['id']),;sys.stdout.flush();time.sleep(0.0001)

		out.close()
		print '\r[*] all friends id successfuly retreived'
		print '[*] file saved : output/' + n[0].split(' ')[0] + '_id.txt'
		main()

	except KeyboardInterrupt:
		print '\r[!] Stopped'
		main()
	except KeyError:
		print '[!] failed to fetch friend id'
		main()
	except (requests.exceptions.ConnectionError , requests.exceptions.ChunkedEncodingError):
		print '[!] Connection Error                 '
		print '[!] Stopped'
		main()

def dump_phone():
	print '[*] load access token'

	try:
		token = open('cookie/token.log','r').read()
		print '[*] Success load access token'
	except IOError:
		print '[!] failed load access token'
		print "[*] type 'token' to generate access token"
		main()

	try:
		os.mkdir('output')
	except OSError:
		pass

	print "[*] fetching all phone numbers"
	print '[*] start'

	try:
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
		a = json.loads(r.text)

		out = open('output/' + n[0].split(' ')[0] + '_phone.txt','w')

		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
			z = json.loads(x.text)

			try:
				out.write(z['mobile_phone'] + '\n')
				print W + '[' + G + z['name'] + W + ']' + R + ' >> ' + W + z['mobile_phone']
			except KeyError:
				pass
		out.close()
		print '[*] done'
		print "[*] all phone numbers successfuly retrieved"
		print '[*] file saved : output/'+n[0].split(' ')[0] + '_phone.txt'
		main()
	except KeyboardInterrupt:
		print '\r[!] Stopped'
		main()
	except KeyError:
		print "[!] failed to fetch all phone numbers"
		main()
	except (requests.exceptions.ConnectionError , requests.exceptions.ChunkedEncodingError):
		print '[!] Connection Error'
		print '[!] Stopped'
		main()

def dump_mail():
	print '[*] load access token'

	try:
		token = open('cookie/token.log','r').read()
                print '[*] Success load access token'
	except IOError:
		print '[!] failed load access token'
		print "[*] type 'token' to generate access token"
		main()

	try:
		os.mkdir('output')
	except OSError:
		pass

	print '[*] fetching all emails'
	print '[*] start'

	try:
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
                a = json.loads(r.text)

		out = open('output/' + n[0].split(' ')[0] + '_mails.txt','w')

		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
                        z = json.loads(x.text)

			try:
                                out.write(z['name'] + ' >> ' + z['email'] + '\n')
			        print W + '[' + G + z['name'] + W + ']' + R + ' >> ' + W + z['email']
			except KeyError:
				pass
		out.close()

                print '[*] done'
                print "[*] all emails successfuly retrieved"
		print '[*] file saved : output/' + n[0].split(' ')[0] + '_mails.txt'
		main()

	except KeyboardInterrupt:
		print '\r[!] Stopped'
		main()
	except KeyError:
		print "[!] failed to fetch all emails"
		main()
	except (requests.exceptions.ConnectionError , requests.exceptions.ChunkedEncodingError):
		print '[!] Connection Error'
		print '[!] Stopped'
		main()

		
def dump_data():
	print '[*] load access token'

	try:
		token = open('cookie/token.log','r').read()
                print '[*] Success load access token'
	except IOError:
		print '[!] failed load access token'
		print "[*] type 'token' to generate access token"
		main()

	try:
		os.mkdir('output')
	except OSError:
		pass

	print '[*] fetching database'
	print '[*] start'

	
	try:
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
                a = json.loads(r.text)

		out = open('output/' + n[0].split(' ')[0] + '_data.txt','w')
		
		
		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
                        z = json.loads(x.text)
						

			try:
								
			        print ''
				print ''					
			except KeyError:
				pass
				
			try:
				print G + '[-------- ' + z['name'] + ' INFORMATION --------]'
				out.write('\n\n' + '[-------- ' + z['name'] + ' INFORMATION --------]' + '\n')
			except KeyError:
				pass
			try:
				print W + '[' + G + 'Username' + W + ']' + R + ' >> ' + W + z['username']
				out.write('Username = ' + z['username'] + '\n')
			except KeyError:
				pass
			try:
				print W + '[' + G + 'ID' + W + ']' + R + ' >> ' + W + i['id']
				out.write('ID = ' + z['id'] + '\n')
			except KeyError:
				pass
			try:
				print W + '[' + G + 'Email' + W + ']' + R + ' >> ' + W + z['email']
				out.write('Email = ' + z['email'] + '\n')
			except KeyError:
				pass
			try:
				print W + '[' + G + 'DOB' + W + ']' + R + ' >> ' + W + z['birthday'].replace('/','-')
				out.write('DOB = ' + z['birthday'] + '\n')
			except KeyError:
				pass
			try:
				print W + '[' + G + 'Number' + W + ']' + R + ' >> ' + W + z['mobile_phone']
				out.write('Number = ' + z['mobile_phone'] + '\n')
			except KeyError:
				pass
			try:
				print W + '[' + G + 'Locale' + W + ']' + R + ' >> ' + W + z['locale'].split('_')[0]
				out.write('Locale = ' + z['locale'].split('_')[0] + '\n')
			except KeyError:
				pass
			try:
				print W + '[' + G + 'Location' + W + ']' + R + ' >> ' + W + z['location']['name']
				out.write('Location = ' + z['location']['name'] + '\n')
			except KeyError:
				pass
			try:
				print W + '[' + G + 'Hometown' + W + ']' + R + ' >> ' + W + z['hometown']['name']
				out.write('Hometown = ' + z['hometown']['name'] + '\n')
			except KeyError:
				pass
			try:
				print W + '[' + G + 'Gender' + W + ']' + R + ' >> ' + W + z['gender']
				out.write('Gender = ' + z['gender'] + '\n')
			except KeyError:
				pass
			try:
				print W + '[' + G + 'Religion' + W + ']' + R + ' >> ' + W + z['religion']
				out.write('Religion = ' + z['religion'] + '\n')
			except KeyError:
				pass
			try:
				print W + '[' + G + 'Relationship' + W + ']' + R + ' >> ' + W + z['relationship_status']
				out.write('Relationship = ' + z['relationship_status'] + '\n')
			except KeyError:
				pass
			try:
				print W + '[' + G + 'Political' + W + ']' + R + ' >> ' + W + z['political']
				out.write('Political = ' + z['political'] + '\n')
			except KeyError:
				pass
			try:
				print W + '[' + G + 'Link' + W + ']' + R + ' >> ' + W + z['link']
				out.write('Link = ' + z['link'] + '\n')
			except KeyError:
				pass
			try:
				print W + '[' + G + 'Quotes' + W + ']' + R + ' >> ' + W + z['quotes']
				out.write('\n' + 'Quotes' + '\n' + '----------------' + '\n' + z['quotes'] + '\n')
			except KeyError:
				pass
			try:
				print W + '[' + G + 'Bio' + W + ']' + R + ' >> ' + W + z['bio']
				out.write('\n' + 'Bio = ' + '\n' + '----------------' + '\n' + z['bio'] + '\n')
			except KeyError:
				pass
			try:	
				print '[' + R + '*' + W + ']' + G + 'Favourite teams' + W
				out.write('\n' + 'Favourite teams' + '\n' + '----------------' + '\n')
				for i in z['favorite_teams']:
					try:
						print ' ~  '+i['name']
						out.write(' ~  '+i['name'] + '\n')
					except KeyError:
						pass
					except KeyError:
						pass
			except KeyError:
				pass
			try:			
				print '[' + R + '*' + W + ']' + G + 'School' + W
				out.write('School' + '\n' + '----------------' + '\n')
				for i in z['education']:
					try:
						print ' ~  '+i['school']['name']
						out.write(' ~  '+i['school']['name'] + '\n')
					except KeyError:
						pass
					except KeyError:
						pass
			except KeyError:
				pass
			try:		
				print '[' + R + '*' + W + ']' + G + 'Work' + W
				out.write('Work = ' + '\n' + '----------------' + '\n')
				for i in z['work']:
					try:
						print '   [-] position : '+i['position']['name']
						out.write('   [-] position : '+i['position']['name'] + '\n')
					except KeyError:
						pass
					try:
						print '   [-] employer : '+i['employer']['name']
						out.write('   [-] employer : '+i['employer']['name'] + '\n')
					except KeyError:
						pass
					try:
						if i['start_date'] == "0000-00":
							print '   [-] start date : ---'
							out.write('   [-] start : ---' + '\n')
						else:
							print '   [-] start date : '+i['start_date']
							out.write('   [-] start date : '+i['start_date'] + '\n')
					except KeyError:
						pass
					try:
						if i['end_date'] == "0000-00":
							print '   [-] end date : ---'
							out.write('   [-] end date : ---' + '\n')
						else:
							print '   [-] end date : '+i['end_date']
							out.write('   [-] end date : '+i['end_date'] + '\n')
					except KeyError:
						pass
					try:
						print '   [-] location : '+i['location']['name']
						out.write('   [-] location : '+i['location']['name'] + '\n')
					except KeyError:
						pass
					print ' '
			except KeyError:
				pass
			try:	
				print '[*] Updated time : '+z['updated_time'][:10]+' '+z['updated_time'][11:19]
				out.write('[*] Updated time : '+z['updated_time'][:10]+' '+z['updated_time'][11:19] + '\n')
			except KeyError:
				pass
		
		out.close()
		
                print '[*] done'
                print "[*] all data successfuly retrieved"
		print '[*] file saved : output/' + n[0].split(' ')[0] + '_data.txt'
		main()

	except KeyboardInterrupt:
		print '\r[!] Stopped'
		main()
	except KeyError:
		print "[!] failed to fetch database"
		main()
	except (requests.exceptions.ConnectionError , requests.exceptions.ChunkedEncodingError):
		print '[!] Connection Error'
		print '[!] Stopped'
		main()
def dump_id_id():
	global target_id

	print '[*] load access token'

	try:
		token = open('cookie/token.log','r').read()
		print '[*] Success load access token'
	except IOError:
		print '[!] failed load access token'
		print "[*] type 'token' to generate access token"
		main()

	try:
		os.mkdir('output')
	except OSError:
		pass

	print '[*] fetching all id from your friend'

	try:
		r = requests.get('https://graph.facebook.com/{id}?fields=friends.limit(5000)&access_token={token}'.format(id=target_id,token=token))
		a = json.loads(r.text)

		out = open('output/' + n[0].split(' ')[0] + '_' + target_id + '_id.txt','w')

		for i in a['friends']['data']:
			out.write(i['id'] + '\n')
			print '\r[*] %s retrieved'%(i['id']),;sys.stdout.flush();time.sleep(0.0001)
		out.close()

		print '\r[*] all friends id successfuly retreived'
		print '[*] file saved : output/' + n[0].split(' ')[0] + '_' + target_id + '_id.txt'
		main()
	except KeyboardInterrupt:
		print '\r[!] Stopped'
		main()
	except KeyError:
		print '[!] failed to fetch friend id'
		try:
			os.remove('output/' + n[0].split(' ')[0] + '_' + target_id + '_id.txt')
		except OSError:
			pass
		main()
	except (requests.exceptions.ConnectionError , requests.exceptions.ChunkedEncodingError):
		print '[!] Connection Error                      '
		print '[!] Stopped'
#
###############################################################################

###############################################################################
#                         Main

def main():
  global target_id

  try:
	cek = raw_input(R + 'luke clegg' + W +' >> ')

	if cek.lower() == 'get_data':
		if len(jml) == 0:
			getdata()
		else:
			print '[*] You have retrieved %s friends data'%(len(jml))
			main()
	elif cek.lower() == 'get_info':
		print '\n'+'[*] Information Gathering [*]'.center(44) + '\n'
		search()
	elif cek.lower() == "cat_token":
		try:
			o = open('cookie/token.log','r').read()
			print '[*] Your access token !!\n\n' + o + '\n'
			main()
		except IOError:
			print '[!] failed to open cookie/token.log'
			print "[!] type 'token' to generate access token"
			main()

	elif cek.lower() == 'clear':
		if sys.platform == 'win32':
			os.system('cls')
			baliho()
			main()
		else:
			os.system('clear')
			baliho()
			main()

	elif cek.lower() == 'token':
		try:
			open('cookie/token.log')
			print '[!] an access token already exists'
			cek = raw_input('[?] Are you sure you want to continue [Y/N] ')
			if cek.lower() != 'y':
				print '[*] Canceling '

		except IOError:
			pass

		print '\n' + '[*] Generate Access token facebook [*]'.center(44) + '\n'
		print '[Warn] please turn off your VPN before using this feature !!!'
		id()
	elif cek.lower() == 'rm_token':
		print '''
[Warn] you must create access token again if 
       your access token is deleted
'''
		a = raw_input("[!] type 'delete' to continue : ")
		if a.lower() == 'delete':
			try:
				os.system('rm -rf cookie/token.log')
				print '[*] Success delete cookie/token.log'
				main()
			except OSError:
				print '[*] failed to delete cookie/token.log'
				main()
		else:
			print '[*] failed to delete cookie/token.log'
			main()
	elif cek.lower() == 'about':
		show_program()
		main()
	elif cek.lower() == 'exit':
		print "[!] Exiting Program"
		sys.exit()
	elif cek.lower() == 'help':
		info_ga()
		main()
	elif cek.lower() == 'dump_id':
		dump_id()
	elif cek.lower() == 'dump_phone':
		dump_phone()
	elif cek.lower() == 'dump_mail':
		dump_mail()
	elif cek.lower() == 'dump_data':
		dump_data()

	if 'dump_' in cek.lower() and cek.lower().split('_')[2] == 'id':
		target_id = cek.lower().split('_')[1]
		dump_id_id()
	else:
		if cek == '':
			main()
		else:
			print "[!] command '"+cek+"' not found"
			print '[!] type "help" to show command'
			main()
  except KeyboardInterrupt:
	main()
  except IndexError:
	print '[!] invalid parameter on command : ' + cek
	main()
#
######################################################################################################################

################################################################################
#                          Get Data

def getdata():
	global a , token

	print '[*] Load Access Token'

	try:
		token = open("cookie/token.log","r").read()
		print '[*] Success load access token '
	except IOError:
		print '[!] failed to open cookie/token.log'
		print "[!] type 'token' to generate access token"
		main()

	print '[*] fetching all friends data'

	try:
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
		a = json.loads(r.text)

	except KeyError:
		print '[!] Your access token is expired'
		print "[!] type 'token' to generate access token"
		main()

	except requests.exceptions.ConnectionError:
		print '[!] Connection Error'
		print '[!] Stopped'
		main()

	for i in a['data']:
		jml.append(i['id'])
		print '\r[*] fetching %s data from friends'%(len(jml)),;sys.stdout.flush();time.sleep(0.0001)

	print '\r[*] '+str(len(jml))+' data of friends successfully retrieved'
	main()

def search():

	if len(jml) == 0:
                print "[!] no friend data in the database"
                print '[!] type "get_data" to collect friends data'
                main()
        else:
                pass

	target = raw_input("[!] Search Name or Id : ")

	if target == '':
		print "[!] name or id can't be empty !!"
		search()
	else:
		info(target)

def info(target):
        global a , token

        print '[*] Searching'
	for i in a['data']:

	  if target in  i['name'] or target in i['id']:

		x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
		y = json.loads(x.text)

		print ' '
		print G + '[-------- INFORMATION --------]'.center(44)
		print W

		try:
			print '\n[*] Id : '+i['id']
		except KeyError:
			pass
		try:
			print '[*] Username : '+y['username']
		except KeyError:
			pass
		try:
			print '[*] Email : '+y['email']
		except KeyError:
			pass
		try:
			print '[*] Mobile Phone : '+y['mobile_phone']
		except KeyError:
			pass
		try:
			print '[*] Name : '+y['name']
		except KeyError:
			pass
		try:
			print '[*] First name : '+y['first_name']
		except KeyError:
			pass
		try:
			print '[*] Midle name : '+y['middle_name']
		except KeyError:
			pass
		try:
			print '[*] Last name : '+y['last_name']
		except KeyError:
			pass
		try:
			print '[*] Locale : '+y['locale'].split('_')[0]
		except KeyError:
			pass
		try:
			print '[*] location : '+y['location']['name']
		except KeyError:
			pass
		try:
			print '[*] hometown : '+y['hometown']['name']
		except KeyError:
			pass
		try:
			print '[*] gender : '+y['gender']
		except KeyError:
			pass
		try:
			print '[*] religion : '+y['religion']
		except KeyError:
			pass
		try:
			print '[*] relationship status : '+y['relationship_status']
		except KeyError:
			pass
		try:
			print '[*] political : '+y['political']
		except KeyError:
			pass
		try:
			print '[*] Work :'

			for i in y['work']:
				try:
					print '   [-] position : '+i['position']['name']
				except KeyError:
					pass
				try:
					print '   [-] employer : '+i['employer']['name']
				except KeyError:
					pass
				try:
					if i['start_date'] == "0000-00":
						print '   [-] start date : ---'
					else:
						print '   [-] start date : '+i['start_date']
				except KeyError:
					pass
				try:
					if i['end_date'] == "0000-00":
						print '   [-] end date : ---'
					else:
						print '   [-] end date : '+i['end_date']
				except KeyError:
					pass
				try:
					print '   [-] location : '+i['location']['name']
				except KeyError:
					pass
				print ' '
		except KeyError:
			pass
		try:
			print '[*] Updated time : '+y['updated_time'][:10]+' '+y['updated_time'][11:19]
		except KeyError:
			pass
		try:
			print '[*] Languages : '
			for i in y['languages']:
				try:
					print ' ~  '+i['name']
				except KeyError:
					pass
		except KeyError:
			pass
		try:
			print '[*] Bio : '+y['bio']
		except KeyError:
			pass
		try:
			print '[*] quotes : '+y['quotes']
		except KeyError:
			pass
		try:
			print '[*] birthday : '+y['birthday'].replace('/','-')
		except KeyError:
			pass
		try:
			print '[*] link : '+y['link']
		except KeyError:
			pass
		try:
			print '[*] Favourite teams : '
			for i in y['favorite_teams']:
				try:
					print ' ~  '+i['name']
				except KeyError:
					pass
		except KeyError:
			pass
		try:
			print '[*] School : '
			for i in y['education']:
				try:
					print ' ~  '+i['school']['name']
				except KeyError:
					pass
		except KeyError:
			pass
	  else:
		pass

        else:
		print W + ' '
		print '[*] Done '
		main()

#
##########################################################################

##########################################################################
#

if __name__ == '__main__':

	baliho()
	main()

#
##########################################################################


