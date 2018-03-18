import time
import threading
import re
import urllib
print time.ctime()
baidu_name = []
name_web = raw_input('input web name:')
def scan_web(url):
    try:
        print '\n',time.ctime(),url,'\n'
        txt_name = url[7:] + '.html'
        urllib.urlretrieve(url, txt_name)
        time.sleep(1)
        return 1
    except:
        print '\n',time.ctime(),url,'fail','\n'
        return 0

match_str = 'http://(\w+\.){0,3}\w+\.com'
a = scan_web(name_web)
if a:
    txt_name = name_web[7:] + '.html'
    b = open(txt_name, 'r')
    for i in b:
        web_scan_1 = re.search(match_str, i)
        if web_scan_1:
            web_scan = web_scan_1.group()
            if web_scan in baidu_name:
                pass
                # print 'pass'
            else:
                baidu_name.append(web_scan)
                # print web_scan
threads = []
c =range(len(baidu_name))
for j in c:
    d = str(baidu_name[j])
    t = threading.Thread(target=scan_web,args=(d,))
    threads.append(t)
    # print j

for z in c:
    threads[z].start()

for z in c:
    threads[z].join()
print time.ctime()
# for j in c:
    # t = str(baidu_name[j])
    # scan_web(t)