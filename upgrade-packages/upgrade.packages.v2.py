import os
import requests
import re
from bs4 import BeautifulSoup
from pkg_resources import parse_version


url = "https://mirrors.slackware.com/slackware/slackware64/source/ap/"
url = "https://slackware.uk/slackware/slackware64-15.0/slackware64/ap/"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

source = response.text
soup = BeautifulSoup(response.text, "html.parser") # lxml is just the parser for reading the html
links = soup.find_all('a')

#print(response.text)

source_packages = []

for link in links:
    if "txz" in link.get_text() and ".asc" not in link.get_text():
        #print(f" >> [{link.get_text()}]")
        source_packages.append(link.get_text())



ssource = '''
<img src="/httpd-icons/tar.gif" alt="[TAR]" width="20" height="22"> <a href="jove-4.16.0.74-x86_64-3.txz">jove-4.16.0.74-x86_64-3.txz</a>                  2021-02-13 11:31  161K   
<img src="/httpd-icons/text.gif" alt="[TXT]" width="20" height="22"> <a href="jove-4.16.0.74-x86_64-3.txz.asc">jove-4.16.0.74-x86_64-3.txz.asc</a>              2021-02-13 11:31  163    
<img src="/httpd-icons/text.gif" alt="[TXT]" width="20" height="22"> <a href="ksh93-1.0_20220114_e569f23e-x86_64-1.txt">ksh93-1.0_20220114_e569f23e-x86_64-1.txt</a>     2022-01-16 20:31  532    
<img src="/httpd-icons/tar.gif" alt="[TAR]" width="20" height="22"> <a href="ksh93-1.0_20220114_e569f23e-x86_64-1.txz">ksh93-1.0_20220114_e569f23e-x86_64-1.txz</a>     2022-01-16 20:31  714K   
<img src="/httpd-icons/text.gif" alt="[TXT]" width="20" height="22"> <a href="ksh93-1.0_20220114_e569f23e-x86_64-1.txz.asc">ksh93-1.0_20220114_e569f23e-x86_64-1.txz.asc</a> 2022-01-16 20:31  163    
<img src="/httpd-icons/text.gif" alt="[TXT]" width="20" height="22"> <a href="libx86-1.1-x86_64-5.txt">libx86-1.1-x86_64-5.txt</a>                      2021-02-13 11:32  316    
<img src="/httpd-icons/tar.gif" alt="[TAR]" width="20" height="22"> <a href="libx86-1.1-x86_64-5.txz">libx86-1.1-x86_64-5.txz</a>                      2021-02-13 11:32   37K   
<img src="/httpd-icons/text.gif" alt="[TXT]" width="20" height="22"> <a href="libx86-1.1-x86_64-5.txz.asc">libx86-1.1-x86_64-5.txz.asc</a>                  2021-02-13 11:32  163    
<img src="/httpd-icons/text.gif" alt="[TXT]" width="20" height="22"> <a href="linuxdoc-tools-0.9.82-x86_64-3.txt">linuxdoc-tools-0.9.82-x86_64-3.txt</a>           2021-11-03 04:15  697    
<img src="/httpd-icons/tar.gif" alt="[TAR]" width="20" height="22"> <a href="linuxdoc-tools-0.9.82-x86_64-3.txz">linuxdoc-tools-0.9.82-x86_64-3.txz</a>           2021-11-03 04:15  4.7M   
<img src="/httpd-icons/text.gif" alt="[TXT]" width="20" height="22"> <a href="linuxdoc-tools-0.9.82-x86_64-3.txz.asc">linuxdoc-tools-0.9.82-x86_64-3.txz.asc</a>       2021-11-03 04:15  163    
<img src="/httpd-icons/text.gif" alt="[TXT]" width="20" height="22"> <a href="lm_sensors-3.6.0-x86_64-3.txt">lm_sensors-3.6.0-x86_64-3.txt</a>                2021-02-13 11:32  532    
<img src="/httpd-icons/tar.gif" alt="[TAR]" width="20" height="22"> <a href="lm_sensors-3.6.0-x86_64-3.txz">lm_sensors-3.6.0-x86_64-3.txz</a>                2021-02-13 11:32  137K   
<img src="/httpd-icons/text.gif" alt="[TXT]" width="20" height="22"> <a href="lm_sensors-3.6.0-x86_64-3.txz.asc">lm_sensors-3.6.0-x86_64-3.txz.asc</a>            2021-02-13 11:32  163    
<img src="/httpd-icons/text.gif" alt="[TXT]" width="20" height="22"> <a href="lsof-4.94.0-x86_64-3.txt">lsof-4.94.0-x86_64-3.txt</a>                     2021-02-13 11:32  331    
<img src="/httpd-icons/tar.gif" alt="[TAR]" width="20" height="22"> <a href="lsof-4.94.0-x86_64-3.txz">lsof-4.94.0-x86_64-3.txz</a>                     2021-02-13 11:32  298K   
<img src="/httpd-icons/text.gif" alt="[TXT]" width="20" height="22"> <a href="lsof-4.94.0-x86_64-3.txz.asc">lsof-4.94.0-x86_64-3.txz.asc</a>                 2021-02-13 11:32  163    
<img src="/httpd-icons/text.gif" alt="[TXT]" width="20" height="22"> <a href="lsscsi-0.32-x86_64-1.txt">lsscsi-0.32-x86_64-1.txt</a>                     2021-05-06 20:12  366    
<img src="/httpd-icons/tar.gif" alt="[TAR]" width="20" height="22"> <a href="lsscsi-0.32-x86_64-1.txz">lsscsi-0.32-x86_64-1.txz</a>                     2021-05-06 20:12   52K   
<img src="/httpd-icons/text.gif" alt="[TXT]" width="20" height="22"> <a href="lsscsi-0.32-x86_64-1.txz.asc">lsscsi-0.32-x86_64-1.txz.asc</a>                 2021-05-06 20:12  163    
<img src="/httpd-icons/text.gif" alt="[TXT]" width="20" height="22"> <a href="lxc-4.0.11-x86_64-3.txt">lxc-4.0.11-x86_64-3.txt</a>                      2021-11-17 20:08  504    
<img src="/httpd-icons/tar.gif" alt="[TAR]" width="20" height="22"> <a href="lxc-4.0.11-x86_64-3.txz">lxc-4.0.11-x86_64-3.txz</a>                      2021-11-17 20:08  1.8M   
<img src="/httpd-icons/text.gif" alt="[TXT]" width="20" height="22"> <a href="lxc-4.0.11-x86_64-3.txz.asc">lxc-4.0.11-x86_64-3.txz.asc</a>                  2021-11-17 20:08  163    
<img src="/httpd-icons/text.gif" alt="[TXT]" width="20" height="22"> <a href="madplay-0.15.2b-x86_64-7.txt">madplay-0.15.2b-x86_64-7.txt</a>                 2021-02-13 11:32  338    
<img src="/httpd-icons/tar.gif" alt="[TAR]" width="20" height="22"> <a href="madplay-0.15.2b-x86_64-7.txz">madplay-0.15.2b-x86_64-7.txz</a>                 2021-02-13 11:32   59K   
<img src="/httpd-icons/text.gif" alt="[TXT]" width="20" height="22"> <a href="madplay-0.15.2b-x86_64-7.txz.asc">madplay-0.15.2b-x86_64-7.txz.asc</a>             2021-02-13 11:32  163    
<img src="/httpd-icons/text.gif" alt="[TXT]" width="20" height="22"> <a href="maketag">maketag</a>                                      2020-12-07 21:44  6.3K   
<img src="/httpd-icons/binary.gif" alt="[BIN]" width="20" height="22"> <a href="maketag.ez">maketag.ez</a>                                   2020-12-07 21:44  6.3K   
<img src="/httpd-icons/text.gif" alt="[TXT]" width="20" height="22"> <a href="man-db-2.9.4-x86_64-3.txt">man-db-2.9.4-x86_64-3.txt</a>                    2022-01-19 04:55  532    
<img src="/httpd-icons/tar.gif" alt="[TAR]" width="20" height="22"> <a href="man-db-2.9.4-x86_64-3.txz">man-db-2.9.4-x86_64-3.txz</a>                    2022-01-19 04:55  542K   
<img src="/httpd-icons/text.gif" alt="[TXT]" width="20" height="22"> <a href="man-db-2.9.4-x86_64-3.txz.asc">man-db-2.9.4-x86_64-3.txz.asc</a>                2022-01-19 04:55  163    
<img src="/httpd-icons/text.gif" alt="[TXT]" width="20" height="22"> <a href="man-pages-5.13-noarch-1.txt">man-pages-5.13-noarch-1.txt</a>                  2021-08-29 03:36  489    
<img src="/httpd-icons/tar.gif" alt="[TAR]" width="20" height="22"> <a href="man-pages-5.13-noarch-1.txz">man-pages-5.13-noarch-1.txz</a>                  2021-08-29 03:36  3.3M   
<img src="/httpd-icons/text.gif" alt="[TXT]" width="20" height="22"> <a href="man-pages-5.13-noarch-1.txz.asc">man-pages-5.13-noarch-1.txz.asc</a>              2021-08-29 03:36  163    
<img src="/httpd-icons/text.gif" alt="[TXT]" width="20" height="22"> <a href="mariadb-10.5.13-x86_64-2.txt">mariadb-10.5.13-x86_64-2.txt</a>                 2021-11-20 19:18  369    
'''

res = []
dir_path = '/mnt/user/jonathan/git/unRAID/plugins/unRAID-NerdPack/packages/6.11'
dir_path = '/packages/6.11'

for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        #print(path)

        #print(path.split("-")[0])
        try:
                

            package = re.match('^(.+?)-\d.*', path)[1]
            version = re.match('^(.+?)-(\d.+?)(:?-|_).*', path)[2]
            
            #print(re.match('^(.+?)-\d.*', path)[1])

            #print(source.find(source_packages = []))
            
            update = parse_version('2.1-rc2') < parse_version('2.1')
            #update = parse_version(version) < parse_version('20200608')


            for pack in source_packages:
                if package in pack:
                    version2 = re.match('^(.+?)-(\d.+?)(:?-|_).*', pack)[2]
                    update = parse_version(version) < parse_version(version2)
                    if update:
                        print(f"   UPDATE  [*] [{package}] -->   [{path}] [{version}]  >>> [{pack}] [{version2}][{update}]")
                    else:
                        print(f"   [*] [{package}] -->   [{path}] [{version}]  >>> [{pack}] [{version2}][{update}]")


            #print(f"   >>>  [{path}]  [{package}]")
        except Exception as e:
            print(f"   [!] Exception [{e}]")


#print(len(res))
#print(res)


