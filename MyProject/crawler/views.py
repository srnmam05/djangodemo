from django.shortcuts import render,HttpResponse
from django.template.defaultfilters import register
from django.contrib.auth.decorators import login_required
from bs4 import BeautifulSoup
import requests
import time
import re
import csv
import datetime
import numpy as np 

@login_required(login_url='/signin/')
def simple_crawl(request):
	articlenumber = 0
	return render(request, 'crawl.html',locals())



def get_web_page(url):
	resp = requests.get(
		url=url,
		cookies={'over18': '1'}
	)
	if resp.status_code != 200:
		print('Invalid url:', resp.url)
		return None
	else:
		return resp.text


def get_articles(dom, date):
	soup = BeautifulSoup(dom, 'html5lib')

	# 取得上一頁的連結
	paging_div = soup.find('div', 'btn-group btn-group-paging')
	prev_url = paging_div.find_all('a')[1]['href']

	articles = []  # 儲存取得的文章資料
	authortotal=[]
	divs = soup.find_all('div', 'r-ent')
	for d in divs:
		if d.find('div', 'date').text.strip() == date:  # 發文日期正確
			# 取得推文數
			push_count = 0
			push_str = d.find('div', 'nrec').text
			if push_str:
				try:
					push_count = int(push_str)  # 轉換字串為數字
				except ValueError:
					# 若轉換失敗，可能是'爆'或 'X1', 'X2', ...
					# 若不是, 不做任何事，push_count 保持為 0
					if push_str == '爆':
						push_count = 99
					elif push_str.startswith('X'):
						push_count = -10

			# 取得文章連結及標題
			if d.find('a'):  # 有超連結，表示文章存在，未被刪除
				href = d.find('a')['href']
				title = d.find('a').text
				author = d.find('div', 'author').text if d.find('div', 'author') else ''
				articles.append({
					'title': title,
					'href': href,
					'push_count': push_count,
					'author': author
				})
				authortotal.append(author)
	return articles, prev_url,authortotal


def POST_crawl(request):

	PTT_URL = 'https://www.ptt.cc'

	data = request.POST.get('title', None)
	if int(data) > 5:
		error = "最多一次爬取5頁!!"
		articlenumber = 0
		return render(request, 'crawl.html',locals())
	print(data)
	number=data
	print('取得今日文章列表...')
	current_page = get_web_page(PTT_URL + '/bbs/Gossiping/index.html')
	if current_page:
		articles = []  # 全部的今日文章
		author=[]
		title=[]
		total =[]
		today = time.strftime('%m/%d').lstrip('0')
		current_articles, prev_url,authortotal = get_articles(current_page, today)  # 目前頁面的今日文章
		
		for i in range(int(number)):
			articles += current_articles
			current_page = get_web_page(PTT_URL + prev_url)
			current_articles, prev_url,authortotal = get_articles(current_page, today)
		print('共 %d 篇文章' % (len(articles)))

		for article in articles[:len(articles)]:
			page = get_web_page(PTT_URL + article['href'])
			author.append(article['author'])
			title.append(article['title'])
			total.append([article['author'],article['title'],PTT_URL + article['href']])

		articlenumber=len(articles)

	return render(request, 'crawl.html',locals())



