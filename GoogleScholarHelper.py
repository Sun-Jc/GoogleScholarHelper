# -*- coding:utf-8 -*-

# expired: http://laod.cn/journal/google-hosts-share-strategies.html
# please go to hosts provider's website
# thank LAOD.CN very much!
# appologies if cause any inconvenience to you

# @Author SunJc
# @Date 2015-07
# only helps to access Google Scholar in Chengdu
# very vulnerable now, expected to be outdated in Dec. 2015
# thanks to 'laod.cn'!

import urllib2,re,os,time,platform

osx = platform.platform().startswith('Darwin')

# find the address of hosts file from pageUrl with specific Regex
pageUrl = "http://laod.cn//hosts//2015-google-hosts.html"
regex = r'''(下载.*)(?<=href=")(http://laod.cn/wp-content/uploads/.*?.txt)(?=" target="_blank">)'''
timeLimit = 5

def nowToStr():
	now = int(time.time()) 
	timeArray = time.localtime(now)
	return time.strftime("-%Y-%m-%d-%H-%M-%S", timeArray)
# backup the older hosts file with filename of 'hosts-YY-MM-HH-MM-SS.txt'

if osx:
	newpath = ur"/etc/hosts"+ nowToStr() +'.txt'
	hostspath = ur'/etc/hosts'
else:
	newpath = ur"C:/Windows/System32/drivers/etc/hosts"+ nowToStr() +'.txt'
	hostspath = ur'C:/Windows/System32/drivers/etc/hosts'

def echoWelcome():
	if osx:
		os.system('clear')
	else:
		os.system('cls') 
	print '''Google Scholar Helper
			\nTHANKS to "laod.cn" !
			\nThis will take a minute and won't delete or upload any file from your computer
			\nYou are free to change the file source if safe and necessary
			\nPlease make sure to observe the law\n'''

def echoError():
	print '''Failed
			\nYou may run me again, and
			\nRun as administrator
			\nCheck if the source is outdated\n'''

#return the content of object page/file
def fetchTxt(targetUrl):
	return urllib2.urlopen(targetUrl, timeout = timeLimit).read()

#file operation
def readFile(fp):
	f = open(fp, "rb")
	txt = f.read()
	f.close()
	return txt
def writeFile(fp,txt):
	f = open(fp, "wb")
	f.write(txt)
	f.close()

def main():
	try:
		echoWelcome()
		#find new hosts path
		print 'Fetching from ',pageUrl,'\n'
		pageContent = fetchTxt(pageUrl)
		print 'Target Found\n'

		writeFile('pc.txt',pageContent)

		matchedAddress = re.search(regex,pageContent)
		#download new hosts
		print "Downloading from ",matchedAddress.group(2),'\n'
		hostsContent = fetchTxt(matchedAddress.group(2))
		#backup
		writeFile(newpath,readFile(hostspath)) 
		#build new hosts
		writeFile(hostspath,hostsContent)
		print 'Done\n'

	except Exception, e:
		print str(e)+'\n'
		echoError()
		
	if 'false'==osx:
		os.system('pause')

if __name__ == "__main__":
	main()