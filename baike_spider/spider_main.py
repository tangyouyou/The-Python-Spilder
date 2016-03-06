
#coding:utf-8
import url_manger,url_parser,html_downloader,html_outputer

class SpiderMain(object):
	# 初始化
	def __init__(self):
		# url管理器
		self.urls = url_manger.UrlManger()
		# html下载器
		self.downloader = html_downloader.HtmlDownloader()
		# html输出器
		self.outputer = html_outputer.Outputer()
		# URL解析器
		self.parser = url_parser.Parser()

	def craw(self,root_url):
		count = 1
		# 增加一个url进入url管理器
		self.urls.add_new_url(root_url)
		while self.urls.has_new_url():
			try : 
				new_url = self.urls.get_new_url()
				print 'craw %d :%s'  %(count,new_url)
				html_cont = self.downloader.download(new_url)
				new_urls,new_data = self.parser.parse(new_url,html_cont)
				self.urls.add_new_urls(new_urls)
				self.outputer.collect_data(new_data)
				if count == 10:
					break
				count = count + 1
			except:
				print 'craw falied'
		self.outputer.output_html()


if __name__ ==  "__main__":
	# 入口url
	root_url = "http://baike.baidu.com/view/21087.htm"
	# create a spider object
	obj_spider = SpiderMain()
	# start a spider
	obj_spider.craw(root_url)
