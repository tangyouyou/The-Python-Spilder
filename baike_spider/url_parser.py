#coding:utf-8
#python
from bs4 import BeautifulSoup
import re
import urlparse
class Parser(object):
	# 获取url
	def _get_new_urls(self,page_url,soup):
		# 设置new_urls为一个集合
		# /view/123.htm
		new_urls = set()
		# r代表/更改为1个
		links = soup.find_all('a',href=re.compile(r"/view/\d+\.htm"))
		for link in links:
			new_url = link['href']
			# 将new_url 按照page_url的格式进行拼接
			new_full_url = urlparse.urljoin(page_url,new_url)
			new_urls.add(new_full_url)
		return new_urls

	# 解析数据
	def _get_new_data(self,page_url,soup):
		# <dd class="lemmaWgt-lemmaTitle-title"> lemmaWgt-lemmaTitle-title
		# <h1>Python</h1>
		res_data = {}
		res_data['url'] = page_url
		title_node = soup.find('dd',"lemmaWgt-lemmaTitle-title").find("h1")
		res_data['title'] = title_node.get_text()
		# <div class="lemma-summary" label-module="lemmaSummary">
		summary_node = soup.find('div',"lemma-summary")
		res_data['summary'] = summary_node.get_text()
		return res_data


	# 解析url
	def parse(self,page_url,html_cont):
		if page_url is None or html_cont is None :
			return 
		soup = BeautifulSoup(html_cont,'html.parser',from_encoding = 'utf-8')
		new_urls = self._get_new_urls(page_url,soup)
		new_data = self._get_new_data(page_url,soup)
		return new_urls,new_data