import requests,csv
from lxml import etree
import json
def save(info):
	with open('info.csv','a+',encoding='utf-8',newline='')as f:
		write = csv.writer(f)
		write.writerow(info)

def save_detail(info):
	with open('kinfo.json', 'a+', encoding='utf-8', newline='\n')as f:
		f.write(json.dumps(info, ensure_ascii=False))
# 页面获取
def gethtml(url):
	headers = {'Cookie': 'security_session_verify=eda1c93addc1c227a32009d0e20f0803; security_session_high_verify=b502686fa4bd5cd2456f054610962802; ASP.NET_SessionId=dcamzp31q201xytlv0xixugm; Hm_lvt_83853859c7247c5b03b527894622d3fa=1587436517; Hm_lpvt_83853859c7247c5b03b527894622d3fa=1587436517; security_session_mid_verify=bbedb6b8988e89512fbf15e0d44996a4'}
	response = requests.get(url=url,headers=headers)
	# print(response.text)
	return response.text

#页面解析
def paser(content):
	select = etree.HTML(content)
	trs = select.xpath('//table[@id="TAB_contentTable"]//tr')
	# print(trs)
	for tr in trs[1:]:
		tds = tr.xpath('.//td')
		number = tds[0].xpath('./text()')[0]
		local = tds[1].xpath('./text()')[0]
		detail_href = 'https://www.landchina.com/'+tds[2].xpath('./a/@href')[0]
		# print(detail_href)
		if tds[2].xpath('./a/span'):
			address = tds[2].xpath('./a/span/@title')[0]

		else:
			address = tds[2].xpath('./a/text()')[0]
		area = tds[3].xpath('./text()')[0]
		use = tds[4].xpath('./text()')[0]
		use_method = tds[5].xpath('./text()')[0]
		date = tds[6].xpath('./text()')[0]
		#详情页解析
		detail_response = gethtml(detail_href)
		items = etree.HTML(detail_response)
		trs = items.xpath('//table/tbody//tr')[1:]
		# print(trs)
		title = trs[1].xpath('./td/span/text()')[0]
		# 行政区
		dq = trs[2].xpath('.//td[2]/span/text()')[0]
		# 电子监管号
		hao = trs[2].xpath('.//td[4]/span/text()')[0]
		# 项目名称
		name = trs[3].xpath('.//td[2]/span/text()')[0]
		# 项目位置
		plocal_name = trs[4].xpath('.//td[2]/span/text()')[0]
		# 面积(公顷
		darea_nu = trs[5].xpath('.//td[2]/span/text()')[0]
		# 土地来源
		dfromd = trs[5].xpath('.//td[4]/span/text()')[0]
		# 土地用途
		duse_n = trs[6].xpath('.//td[2]/span/text()')[0]
		# 供地方式
		duse_name = trs[6].xpath('.//td[4]/span/text()')[0]
		#print(duse_name)
		# 土地使用年限
		use_time_name = trs[7].xpath('.//td[2]/span/text()')
		if use_time_name:
			use_time_name=use_time_name[0]
		else:
			use_time_name = ' '
		# 行业分类
		type_name = trs[7].xpath('.//td[4]/span/text()')[0]
		# 土地级别
		jb_name = trs[8].xpath('.//td[2]/span/text()')[0]
		# 成交价格(万元)
		price = trs[8].xpath('.//td[4]/span/text()')
		if price:
			price=price[0]
		else:
			price = ''
		zhifus_trs = trs[9].xpath('.//td[2]/table/tbody//tr')[1:]
		for zhifus_tr in zhifus_trs:
			zhifus_time = zhifus_tr.xpath('./td/span/text()')
		# 支付期号
			if zhifus_time:
				zhi_hao = zhifus_time[0]
			else:
				zhi_hao= ''
		# 约定支付日期
			if zhifus_time:
				zhi_time = zhifus_time[1]
			else:
				zhi_time= ''

		# 约定支付金额(万元)
			if zhifus_time:
				zhi_price = zhifus_time[2]
			else:
				zhi_price= ''

		# 下限
		xiaxian = trs[16].xpath('.//td[2]/span/text()')
		if xiaxian:
			xiaxian=xiaxian[0]
		else:
			xiaxian = ''
		# 上限
		shangxian = trs[16].xpath('.//td[4]/span/text()')
		if shangxian:
			shangxian = shangxian[0]
		else:
			shangxian = ''
		# 约定交地时间
		jiaodi_time = trs[19].xpath('.//td[4]/span/text()')
		if jiaodi_time:
			jiaodi_time=jiaodi_time[0]
		else:
			jiaodi_time = ''
		# 批准单位
		danwei = trs[-1].xpath('.//td[2]/span/text()')
		het = trs[-1].xpath('.//td[4]/span/text()')
		# print(het)

		kinfo = {
			'行政区:':dq,
			'电子监管号:': hao,
			'项目名称:':name,
			'项目位置:': plocal_name,
			'面积(公顷):': darea_nu,
			'土地来源:': dfromd,
			'土地用途:': duse_n,
			'供地方式:': duse_name,
			'土地使用年限:':use_time_name ,
			'行业分类:':type_name,
			'土地级别:': jb_name,
			'成交价格(万元):': price,
			'支付期号': zhi_hao,
			'约定支付日期': zhi_time,
			'约定支付金额(万元)': zhi_price,
			'土地使用权人:': name,
			'下限:': xiaxian,
			'上限:': shangxian,
			'约定交地时间:': jiaodi_time,
			'约定开工时间:': jiaodi_time,
			'约定竣工时间:': jiaodi_time,
			'批准单位:': danwei,
			'合同签订日期:': het,
		}
		print(kinfo)# 输出所有详情信息
		save_detail(kinfo)

		info = [number,local,address,area,use,use_method,date]
		save(info)


if __name__ == '__main__':
	tite = ['序号','行政区','土地坐落','总面积','土地用途','供应方式','签定日期']
	save(tite)
	url = 'https://www.landchina.com/default.aspx?tabid=263'
	content = gethtml(url)
	paser(content)

