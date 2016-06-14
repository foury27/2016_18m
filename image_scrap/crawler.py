# coding:utf-8
from selenium import webdriver
import time  
import urllib.request
  
# 爬取页面地址  
url = 'https://www.google.com/search?q=car+dent&espv=2&rlz=1C5CHFA_enCN505CN506&biw=1280&bih=628&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiZ0Peq_YPNAhUQ0WMKHUrKDa0Q_AUIBigB'
  
# 目标元素的xpath  
xpath = '//div[@id="imgid"]/ul/li/a/img'  
  
# 启动Firefox浏览器  
driver = webdriver.Chrome('./chromedriver')
#driver = webdriver.Chrome()
  
# 最大化窗口，因为每一次爬取只能看到视窗内的图片  
driver.maximize_window()  
  
# 记录下载过的图片地址，避免重复下载  
img_url_dic = {}  
  
# 浏览器打开爬取页面  
driver.get(url)  
  
# 模拟滚动窗口以浏览下载更多图片  
pos = 0  
m = 0 # 图片编号  

for i in range(10):  
    pos += i*500 # 每次下滚500  
    js = "document.documentElement.scrollTop=%d" % pos  
    driver.execute_script(js)  
    time.sleep(1)     
      
    for element in driver.find_elements_by_class_name("rg_i"):  
        element.click()
        i=0
        time.sleep(5)
        img = driver.find_element_by_class_name("irc_mi")  
        img_url=img.get_attribute('src')
        print(img_url)
        while i<3 and not img_url:
            time.sleep(5)
            img_url=img.get_attribute('src')
            print(img_url)
            i+=1
        m += 1  
        # 保存图片到指定路径  
        if img_url and img_url not in img_url_dic:  
            img_url_dic[img_url] = ''  
            ext = img_url.split('.')[-1]  
            filename = str(m) + '.' + ext  
            #保存图片数据  
            try:
                data = urllib.request.urlopen(img_url, timeout=120).read()  
                f = open('/Users/foury/Documents/github/2016_18m/image_scrap/car/' + filename, 'wb')
                f.write(data)  
                f.close()  
                print("download >> "+img_url)
            except Exception:
                print("error")
            
driver.close()  
