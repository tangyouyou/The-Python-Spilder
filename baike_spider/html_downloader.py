#coding:utf-8
 # python
import urllib2
class HtmlDownloader(object):

 	def download(self,url):
 		if url is None:
 			return None
 		respnse = urllib2.urlopen(url)

 		if respnse.getcode() != 200 :
 			return None
 			
 		return respnse.read()
