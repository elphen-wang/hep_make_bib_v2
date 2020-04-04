# -*- coding: utf-8 -*
import numpy as np
import random as rdm
import urllib
import asyncio
from pyppeteer import launch
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import re
import os
#note: this script now just for literature
# PhantomJS
def rreplace(self, old, new, *max):
  count = len(self)
  if max and str(max[0]).isdigit():
    count = max[0]
  return new.join(self.rsplit(old, count))


print("Please input your keyword...");
keyword=input();
#keyword="JUNO+PRD+neutrino+2020";
#keyword="JUNO + IceCube +2019+ 1911.06745"
#keyword="JUNO+PRD+1609.07403"
#keyword="JUNO + IceCube +2020+1908.07249"
print("Your are searching: ",keyword);
keyword=urllib.parse.quote_plus(keyword);

search_what="literature";# authors, jobs, conferences
sort="mostrecent"; #or mostcited, sort method
size="25"; # maximum number of search results per page.
page_index="1";#  Page index of current search results.
domain_name="https://inspirehep.net/";
my_url=domain_name+search_what+"?sort="+sort+"&size="+size+"&page="+page_index+"&q="+keyword;

options = webdriver.FirefoxOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
browser = webdriver.Firefox(executable_path ="/usr/local/bin/geckodriver",options=options)
########driver download link: https://github.com/mozilla/geckodriver/releases


#options = webdriver.ChromeOptions()
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')
#browser = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver",options=options)
#########driver download link: https://sites.google.com/a/chromium.org/chromedriver/home


#browser = webdriver.Safari()

browser.get(my_url)
content = browser.page_source
#print(content)



#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
#data=requests.get(my_url,headers=headers)
#print(data.content)


async def main(url):
    #browser = await launch(headless = 0, args=['--disable-infobars','--no-sandbox'],dumpio=True)
    browser = await launch({'headless': True, 'args': ['--disable-infobars'],'dumpio':False, 'slowMo': 30})  #dumpio':True就不会卡住了
    # headless = False (or 0 ,namely non headless,有头模式), default ture (or 1, default value, headless ,无头模式）
    # args=['--disable-infobars']: close chrome tips
    #
    page = await browser.newPage()
    await page.setViewport({'width': 1200, 'height': 800})
    await page.goto(url,{'timeout': 1000*180})#'https://www.baidu.com/'
    #await page.screenshot({'path': 'example.png'})
    content=await page.content();
    #print(await page.title())
    await browser.close()
    return content

#content=asyncio.get_event_loop().run_until_complete(main(my_url));

bsObj = BeautifulSoup(content, "lxml")
#print(bsObj)

record_body=bsObj.findAll("div", {"class":{"mv2"}});
resultsnum=len(record_body);
if(resultsnum>0):
  result_total_str=bsObj.findAll("div", {"class":{"ant-col ant-col-xs-24 ant-col-lg-8"}})[0].find('span').get_text();
  result_total_num = int(re.sub("\D","",result_total_str),10)
else:
  result_total_num=0;
  result_total_str="0 result"
  
print("You got ",resultsnum," result(s) in the index -",page_index," page. Total: ",result_total_str,".");
print("\n");

for index in range(0,resultsnum):#resultsnum
    b_elements=record_body[index].findAll("b");
    href_list=record_body[index].findAll("a");
    #i=0;
    title_link="";
    article_title="";
    arXiv_pdf_link="";
    arXiv_abs_link="";
    publish_year="";
    arXiv_title=""
    doi_title=""
    latex_us_links="";
    doi_link="";
    collaborations=[];
    authors=[];
    collaborations_str="";
    authors_str="";
    
    article_title=record_body[index].findAll("a",{"data-test-id":{"literature-result-title-link"}})[0].find('span').get_text();
    cite=article_title
    
    mt1=record_body[index].findAll("div",{"class":{"mt1"}})
    mt1_a=mt1[0].findAll("a")
    mt1_b=mt1[1].findAll("ul")
    for mt1a in mt1_a:
      #print(mt1a)
      if("collaboration" in str(mt1a)):
        collaborations.append(mt1a.text)
      else:
        authors.append(mt1a.text)
    #print(collaborations,authors)
    for i in range(0,len(authors)):
      letters=authors[i].split(" ")
      author=""
      #print(letters)
      for l in range(0,len(letters)-1):
        author=author+letters[l][0]+".~"
      author=author+letters[len(letters)-1]
      #print(author)
      authors[i]=author
    #print(collaborations,authors)
    #print(mt1[0].get_text())
    p_braket=re.compile(r'[(](.*?)[)]', re.S)
    brakets=re.findall(p_braket, mt1[0].get_text())
    publish_date=brakets[-1];
    publish_dates=publish_date.split(", ")
    
    if(len(publish_dates)==1):
      publish_year=publish_date;
    else:
      publish_year=publish_dates[1];
    #print(publish_year)
    
    ############ old school style, if your like arVix style, please annotation below cite ############
    first_au_arr=authors[0].split("~")
    first_family_name=first_au_arr[len(first_au_arr)-1]
    cite=first_family_name+":"+publish_year+''.join(rdm.sample('zyxwvutsrqponmlkjihgfedcba',3));
    #print(cite)
    ###################################################################################################
    
    
    #print(mt1[1].get_text())
    publish_info=(mt1[1].get_text()).split(" •")
    #print(publish_info)
    
    for info in publish_info:
      if("Published in:" in info):
        doi_title=info.split("Published in:")[1]
      elif("e-Print:" in info):
        arXiv_title=info.split("e-Print:")[1]
        
    #cite="aiXiv:"+re.sub("[^0-9.]","",arXiv_title)###########aiVix style
    #print(doi_title,arXiv_title,cite)
    
    for link in href_list:
      if("title-link" in str(link)):
        title_link=domain_name+link.attrs['href']
      elif("doi" in str(link)):
        doi_link="https:"+(link.attrs['href'])[1:]
      elif("arxiv.org/abs" in str(link)):
        arXiv_abs_link="https:"+link.attrs['href']
      elif("arxiv.org/pdf" in str(link)):
        arXiv_pdf_link=link.attrs['href']
        
    #print(title_link)
    #print(doi_link)
    #print(arXiv_abs_link)
    #print(arXiv_pdf_link)
    ###############################################
    cite_str="%\cite{"+cite+"}"
    bib_str="\\bibitem{"+cite+"}"
    authors_str=""
    collaborations_str=""
    if(len(authors)==1):
      authors_str=authors[0]
    elif(len(authors)==2):
      authors_str=authors[0]+" and "+authors[1]
    else:
      for k in range(0,len(authors)-1):
        authors_str=authors_str+authors[k]+", "
      authors_str=authors_str[:-2]+" and "+authors[len(authors)-1]
    if(len(collaborations)==1):
      collaborations_str="["+collaborations[0]+"]"
      authors_str=authors_str+"\\textit{~et al.}"
    elif(len(collaborations)>1):
      collaborations_str=", ".join(collaborations)
      collaborations_str="["+collaborations_str+"]"
      authors_str=authors_str+"\\textit{~et al.}"
      
    #print(authors_str,collaborations_str)
    
    if(doi_title!=""):
      space_pos=[m.start() for m in re.finditer(" ", doi_title)]
      left_braket_pos=doi_title.find("(")
      #print(space_pos,"----",left_braket_pos)
      bold_str=doi_title[space_pos[space_pos.index(left_braket_pos-1)-1]:space_pos[space_pos.index(left_braket_pos-1)]]
      #print(bold_str)
      doi_title=rreplace(doi_title, bold_str, "\\textbf{"+bold_str+"}", 1);
      #doi_title.replace(bold_str,"\\textbf{"+bold_str+"}")
      #print(doi_title)
    newlatex=cite_str+"\n"+bib_str+"\n"+authors_str+"~"+collaborations_str+",\n"+"{\it{"+article_title+"}},{\color{blue}\href{"+doi_link+"}{~"+doi_title+"}\href{"+arXiv_abs_link+"}{~[arVix:"+arXiv_title+"]}[\href{"+title_link+"}{\scriptsize IN\\normalsize SPIRE}]}";
    print("Index. ",index,", ---------->title: ",article_title);
    print("\n");
    print(newlatex);
    print("\n");
      
    
        
    
    
    

