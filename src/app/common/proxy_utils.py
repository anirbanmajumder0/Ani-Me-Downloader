# coding:utf-8
import requests
from concurrent.futures import ThreadPoolExecutor
from .constants import Constants as constants
from queue import Queue
from .config import cfg


def get_proxies():
    response = requests.get(constants.proxy_url)
    with open(cfg.testProxy.value, "wb") as f:
        f.write(response.content)
    li=["216.215.125.182:48324","72.195.114.184:4145","212.72.134.26:35010","72.195.114.169:4145","80.232.253.108:4153","109.94.182.128:4145","91.222.147.56:5678","179.1.110.77:5678","77.235.23.130:5678","89.151.251.50:32000","190.2.115.208:4153","92.84.56.10:47054","181.209.106.188:1080","37.187.91.192:27898","176.236.37.132:1080","186.97.144.98:5678","188.95.20.138:5678","202.131.159.58:5678","72.206.181.97:64943","72.221.232.152:4145","184.178.172.18:15280","98.170.57.231:4145","184.181.217.206:4145","176.113.157.149:37417","50.235.92.65:32100","88.84.62.5:4153","181.205.68.210:35010","50.236.148.246:31699","190.239.24.69:5678","202.40.181.220:31247","103.160.201.76:1080","184.178.172.26:4145","199.102.106.94:4145","186.211.199.118:4145","31.42.6.125:5678","103.56.206.65:4996","14.161.14.106:5678","103.181.250.242:4145","106.245.183.58:4145","94.181.33.149:40840","167.172.224.178:40176","138.197.134.114:40331","184.178.172.11:4145","192.252.208.67:14287","184.105.134.166:48324","185.43.249.148:39316","175.144.198.226:31694","201.221.134.74:5678","72.210.208.101:4145","94.130.54.158:43664","82.207.20.247:5678","200.85.169.18:50577","194.85.135.243:4145","24.37.245.42:51056","38.113.171.88:57775","116.255.137.220:17989","190.4.62.10:4153","192.111.137.35:4145","185.161.186.133:54321","154.26.133.235:41279","218.26.101.226:53813","192.252.211.197:14921","123.253.124.28:5678","138.97.221.0:35010","59.45.13.219:3629","182.253.40.55:4153","202.162.212.163:4153","92.249.219.47:59587","60.190.195.146:10800","178.128.88.72:10000","192.252.216.81:4145","197.232.47.102:52567","36.67.14.5:5678","113.53.247.221:4153","103.146.26.31:5678","68.71.247.130:4145","190.110.165.124:5678","194.28.91.10:5678","187.62.89.252:4153","103.172.17.7:5678","80.26.111.141:3000","72.37.216.68:4145","182.16.171.65:51459","192.252.220.89:4145","137.184.60.101:56624","103.148.225.6:5678","177.66.43.189:4145","199.58.184.97:4145","202.162.219.12:1080","58.215.218.170:10800","198.89.91.42:5678","154.72.78.146:5678","180.180.124.248:49992","67.201.33.10:25283","81.30.204.218:1080","190.216.56.1:4153","41.162.162.140:4153","5.188.64.79:5678","142.54.236.97:4145","90.188.40.61:3629","162.14.135.190:10800","1.179.148.9:36476","161.35.50.185:49025","114.4.200.222:5678","109.232.106.150:52435","83.234.76.155:4145","203.160.61.104:4145","105.208.44.53:5678","1.179.147.5:52210","138.97.200.69:35010","213.6.68.94:5678","186.219.215.147:4153","197.159.130.134:5678","94.247.241.70:51006","184.170.249.65:4145","103.110.89.78:5678","124.90.45.58:10800","192.111.134.10:4145","45.234.100.102:1080","112.14.47.6:57545","103.37.82.134:39873","188.95.20.139:5678","102.39.113.232:5678","98.181.137.80:4145","202.131.234.107:5678","178.212.54.137:5678","184.178.172.3:4145","181.209.106.189:1080","98.162.96.41:4145","109.188.86.168:4145","89.185.212.198:32000","181.143.21.146:4153","36.66.203.163:5678","45.228.147.204:4153","192.252.214.20:15864","61.7.138.74:4145","181.229.38.117:5678","107.181.168.145:4145","109.75.34.152:59341","213.6.38.50:59422","208.76.170.51:52545","46.172.75.51:5678","178.212.48.23:1080","201.20.79.182:5678","190.145.37.5:65409","202.166.218.99:57775","212.115.232.79:10800","142.93.118.220:43840","103.160.201.23:1080","188.134.1.49:3629","103.191.44.39:5678","184.178.172.17:4145","192.111.135.17:18302","195.191.13.12:5678","98.162.25.23:4145","178.35.177.242:3629","46.107.230.122:1080","98.162.25.4:31654","162.240.10.224:44228","212.42.99.22:4145","192.141.236.10:5678","175.139.179.65:41527","192.111.137.34:18765","141.105.107.34:5678","218.83.201.226:10800","201.140.116.170:4153","185.51.92.108:51327","103.134.239.210:5678","94.72.158.129:4153","98.162.25.7:31653","200.105.173.250:65425","124.41.240.203:37704","1.9.167.35:60489","77.241.20.215:55915","70.80.75.236:5678","192.252.209.155:14455","179.108.158.204:4145","154.79.248.156:5678","213.171.44.82:3629","50.250.205.21:32100","64.90.52.0:31878","45.5.119.86:4153","85.196.151.2:4153","185.47.184.253:45463","200.0.247.84:4153","93.105.40.62:51327","92.255.164.166:4145","114.108.177.104:60984","111.68.31.134:40385","170.247.43.142:32812","82.114.92.222:4145","213.16.81.182:35559","184.181.217.201:4145","110.34.28.109:1080","139.59.124.215:48455","37.57.56.38:5678","103.150.110.202:9969","190.12.95.170:37209","162.240.71.176:43416","47.180.63.37:54321","1.116.184.2:12580","200.118.122.6:4153","150.220.8.228:64312","189.203.181.34:1080","103.123.250.179:38362","114.134.90.43:5678","181.209.106.190:1080","115.85.72.202:5678","192.111.139.162:4145","174.64.199.79:4145","201.234.24.89:4153","202.151.163.10:1080","201.184.239.75:5678","176.197.103.58:4145","49.156.38.126:5678","211.21.125.32:4153","181.129.74.58:30431","184.178.172.23:4145","200.0.247.82:4153","196.0.113.10:31651","202.137.31.155:5678","72.195.34.59:4145","190.54.120.86:5678","46.98.192.233:5678","205.185.117.119:17465","222.252.25.9:1080","162.243.148.156:51790","76.81.6.107:31008","179.40.75.1:61362","72.195.34.41:4145","116.196.124.43:8899","72.206.181.123:4145","103.11.193.163:35010","82.114.68.42:5678","178.150.188.118:1099","182.52.58.44:4153","115.85.86.114:5678","84.2.233.239:4153","98.162.96.52:4145","143.137.116.72:1080","95.134.113.250:5678","51.89.68.78:9050","212.231.197.29:4145","103.102.26.1:7469","112.78.138.163:5678","91.203.114.71:42905","198.211.110.125:63720","72.210.252.137:4145","72.217.216.239:4145","36.67.27.189:49524","71.40.17.29:33651","202.40.188.92:55103","41.223.108.13:1080","83.220.46.106:4145","102.217.205.117:5678","82.103.70.227:4145","142.54.228.193:4145","31.173.251.198:40547","24.249.199.4:4145","201.234.24.1:4153","36.89.251.210:5678","41.223.234.116:37259","74.119.147.209:4145","181.174.85.78:5678","91.213.119.246:46024","144.91.95.238:58237","201.174.73.70:11337","103.124.139.178:4145","184.178.172.25:15291","103.112.253.23:5678","186.225.194.78:34110","187.188.58.173:4153","110.77.145.159:4145","182.34.213.100:1080","221.230.77.10:10800","93.184.7.26:1080","183.88.240.53:4145","103.114.96.125:8291","103.150.115.186:4153","192.111.130.5:17002","31.43.33.56:4153","77.65.50.118:34159","182.52.67.122:36378","41.160.6.186:9898","190.144.224.182:44550","182.71.146.148:5678","72.221.164.34:60671","50.250.75.153:39593","98.162.25.16:4145","103.110.59.3:35294","41.180.70.2:4153","185.89.65.170:33744","188.92.110.174:1080","80.191.40.41:5678","197.250.15.87:5678","72.221.171.130:4145","89.28.32.203:57391","181.129.62.2:47377","95.9.217.137:5678","36.37.189.64:5678","104.248.250.110:7510","213.91.128.99:10801","50.235.117.234:39593","46.171.28.162:59311","192.111.139.163:19404","218.93.48.26:10800","201.158.120.44:45504","50.235.92.14:32100","31.210.225.135:4153","85.172.66.254:1099","14.97.246.241:35010","207.180.235.47:24215","94.42.200.58:5678","38.133.200.94:31596","104.200.135.46:4145","49.156.42.186:5678","172.99.187.33:4145","68.71.254.6:4145","197.234.58.102:32767","1.20.95.95:5678","81.12.157.98:5678","85.172.5.74:3629","72.221.196.157:35904","197.211.24.206:5678","174.77.111.198:49547","80.63.107.90:4153","107.181.161.81:4145","187.177.30.154:4145","36.91.45.11:51299","186.103.133.91:5678","105.214.28.39:5678","128.199.113.127:62877","218.75.69.50:56430","92.249.122.108:58749","182.53.96.56:4145","187.32.20.249:5678","181.113.59.188:35010","176.99.2.43:1080","190.216.56.177:4153","5.58.33.187:5678","103.140.35.11:4145","45.73.0.118:5678","192.111.138.29:4145","120.138.0.205:5678","95.31.35.210:3629","51.83.184.241:9191","105.29.93.193:4145","119.82.251.250:31678","91.199.93.32:4153","140.206.81.178:1080","31.146.97.254:5678","117.220.229.148:5678","72.49.49.11:31034","189.124.138.137:5678","130.193.123.34:5678","138.68.109.12:7077","98.175.31.195:4145","198.8.84.3:4145","124.109.44.126:4145","192.158.15.201:50877","184.181.217.213:4145","31.131.135.247:4153","213.6.36.146:5678","72.221.232.155:4145","103.221.254.102:54409","72.206.181.103:4145","113.190.253.76:5678","184.181.217.220:4145","181.113.135.254:50083","209.94.84.65:1080","139.255.97.156:14888","64.124.191.98:32688","187.49.207.65:4153","186.219.96.47:49923","213.79.115.146:32767","89.151.134.157:3629","46.23.141.142:5678","179.159.134.228:4153","186.145.192.251:5678","98.188.47.132:4145","213.145.134.174:3629","50.237.206.138:64312","109.167.134.253:44788","199.102.107.145:4145","203.189.159.33:35010","185.87.121.35:8975","1.9.167.36:60489","208.102.51.6:58208","190.2.115.64:4153","213.165.185.211:4153","201.220.140.6:30575","192.111.135.18:18301","185.213.156.226:51971","192.252.208.70:14282","58.34.34.186:10800","192.111.130.2:4145","103.139.246.166:5678","167.71.241.136:33299","170.80.71.78:5678","82.103.118.42:1099","212.31.100.138:4153","184.181.217.210:4145","85.206.188.116:5678","72.195.34.35:27360","117.205.67.43:4153","193.105.62.11:58973","154.16.116.166:44003","109.248.236.150:9898","105.214.2.80:5678","184.178.172.14:4145","104.200.152.30:4145","185.139.56.133:4145","66.42.224.229:41679","188.247.39.14:43032","95.170.201.34:43018","86.110.189.154:4145","50.199.46.20:32100","61.148.199.206:4145","105.214.28.83:5678","180.180.171.113:4145","37.17.53.108:3629","203.76.112.68:5678","110.78.149.216:4145","192.111.139.165:4145","104.37.135.145:4145","174.77.111.196:4145","181.209.106.187:1080","125.70.227.214:10800","212.103.118.77:5678","68.1.210.163:4145","200.105.192.6:5678","192.111.137.37:18762","200.24.148.132:3629","109.197.55.234:1080","103.124.190.130:5678","91.121.48.221:55348","201.206.141.102:6969","155.0.181.254:41174","217.66.206.156:5678","186.87.179.54:5678","72.195.34.58:4145","119.235.50.5:4145","154.118.241.86:35010","103.221.254.59:1088","118.136.82.136:5678","203.205.34.58:5678","50.255.17.229:32100","81.7.86.154:4145","80.80.164.164:10801","103.247.23.82:1080","46.173.35.229:3629","72.210.252.134:46164","210.61.216.66:33990","185.97.114.179:3629","162.253.68.97:4145","177.55.247.181:5678","98.162.96.53:10663","118.70.126.245:5678","188.64.113.104:1080","184.181.217.194:4145","36.91.139.82:5678","72.210.221.223:4145","202.84.76.190:5678","94.253.95.241:3629","131.221.120.196:5678","123.231.230.58:31196","95.31.42.199:3629","70.82.75.118:4153","184.170.248.5:4145","154.66.120.80:57775","103.60.214.18:51754","174.64.199.82:4145","213.14.19.252:1080","159.224.243.185:61303","221.224.140.140:51080","213.32.252.134:5678","200.32.105.86:4153","62.89.31.216:3629","213.89.53.85:1080","46.227.36.152:1080","95.165.163.188:36496","63.151.9.74:64312","181.48.70.30:4153","46.40.60.108:52088","95.158.174.111:1080","83.151.4.172:47036","186.97.172.178:5678","61.164.58.66:10800","103.118.47.74:4145","81.16.1.71:5678","103.26.209.206:11080","200.41.60.33:4153","121.139.218.165:43295","200.218.240.9:5678","181.209.106.186:1080","178.215.163.218:4145","194.226.164.214:1080","156.0.229.194:42692","193.200.151.158:8192","107.152.98.5:4145","196.61.46.114:4145","58.75.126.235:4145","186.251.209.121:35010","98.181.137.83:4145","190.109.2.89:4145","103.87.81.86:5678","190.96.97.202:4153","82.137.245.41:1080","98.178.72.21:10919","200.116.227.98:33337","45.128.135.65:1080","142.54.235.9:4145","186.178.10.78:35010","103.1.105.10:4153","135.125.244.133:42165","5.189.129.186:48229","176.197.91.178:4153","118.172.47.97:51327","5.58.47.25:3629","85.217.192.39:4145","202.137.141.26:5678","77.238.79.111:5678","174.77.111.197:4145","5.141.87.135:3629","109.110.78.70:5678","193.141.65.48:8975","142.54.226.214:4145","91.243.192.17:3629","88.99.150.167:29425","91.194.239.122:5678","184.170.245.148:4145","134.209.105.160:30217","216.154.201.132:54321","197.210.217.66:60896","95.188.82.147:3629","85.245.254.22:57775","202.141.242.3:55544","103.17.90.6:5678","194.233.78.142:49653","5.178.217.227:31019","185.87.121.5:8975","176.118.52.129:3629","50.236.148.254:31699","177.36.185.182:5678","177.104.87.23:5678","95.31.5.29:51528","183.88.212.167:4153","89.39.114.31:4153","192.111.129.145:16894","109.87.130.6:5678","64.64.152.248:39593","95.143.8.182:50285","70.166.167.55:57745","24.249.199.12:4145","142.54.239.1:4145","74.57.41.242:4153","203.202.253.186:58309","174.75.211.222:4145","31.210.134.114:13080","159.69.153.169:5566","181.15.154.156:52033","185.95.199.103:1099","122.252.179.66:5678","200.170.203.90:1080","181.13.198.90:4153","213.186.202.149:5678","190.180.35.149:5678","213.190.26.158:1080","129.205.244.158:1080","190.104.26.227:33638","142.54.237.34:4145","91.193.125.123:3629","184.74.140.38:39593","36.67.63.239:38071","185.43.189.182:3629","74.95.1.114:33108","27.72.122.228:51067","69.75.122.146:39593","98.170.57.249:4145","182.253.152.234:5678","171.223.214.191:8098","201.236.203.180:4153","115.164.146.10:5678","190.184.144.222:5678","104.192.202.11:1080","92.241.87.14:5678","72.221.171.135:4145","177.101.228.52:4153","72.37.217.3:4145","80.26.56.66:4153","98.162.25.29:31679","84.236.185.247:61710","184.178.172.5:15303","222.165.215.117:52667","177.136.124.36:3629","213.19.205.18:54321","45.128.133.197:1080","112.133.192.231:5678","186.159.3.193:45524","93.182.76.244:5678","102.89.12.203:7599","184.178.172.28:15294","103.127.23.10:5678","77.238.209.58:5678","12.218.209.130:13326","202.131.246.250:5678","76.26.114.253:39593","203.210.235.91:5678","193.176.41.32:5678","189.5.147.124:4145","98.188.47.150:4145","79.143.225.152:31270","197.210.186.226:1080","72.195.34.42:4145","118.97.107.65:5430","103.152.104.228:1080","222.165.223.140:41541","177.10.150.3:4145","94.232.11.178:58028","85.237.62.189:3629","182.160.115.234:5678","187.86.153.254:30660","205.240.77.164:4145","46.98.191.58:5678","103.195.141.47:1080","94.101.55.201:4153","50.62.56.97:54702","72.210.221.197:4145","199.229.254.129:4145","213.208.146.80:5678","168.194.224.36:4153","203.205.29.108:5678","103.111.225.244:1088","82.142.147.174:4145","138.68.24.185:33994","185.253.233.173:35010","68.71.249.153:48606","36.37.251.171:5678","202.160.175.78:35010","138.59.177.117:5678","109.75.42.82:3629","50.197.210.138:32100","199.102.104.70:4145","134.209.154.177:7878","200.85.52.254:5678","220.132.33.150:4145","212.252.78.40:1080","85.143.252.94:9100","69.61.200.104:36181","27.72.59.99:5678","131.196.180.1:4153","45.235.87.66:49997","72.221.172.203:4145","188.163.170.130:35578","62.122.201.246:50129","159.65.225.229:49772","142.54.232.6:4145","139.59.43.165:29933","206.220.175.2:4145","221.4.161.201:51080","74.119.144.60:4145","202.29.226.134:32241","178.210.131.61:5678","142.54.229.249:4145","170.244.0.179:4145","72.195.34.60:27391","118.69.109.222:1080","192.162.232.15:1080","178.176.193.56:1080","198.8.94.170:4145","202.51.103.154:5678","199.58.185.9:4145","103.235.199.100:25566","177.234.192.44:32213","143.255.141.113:5678","188.75.186.152:4145","148.77.34.200:54321","27.115.33.94:4153","27.72.73.143:4153","192.141.232.12:33998"]
    with open(cfg.testProxy.value, 'r') as f:
        for line in f:
            li.append(line.strip())

    li=list(set(li))
    with open(cfg.testProxy.value, 'w') as f:
        for line in li:
            f.write(line+'\n')
    print(f"Fresh Proxies downloaded\nTotal proxies: {len(li)}")


def check_proxy(proxy):
    try:
        session = requests.Session()
        session.proxies = {'https': f'socks4://{proxy}'}
        response = session.get('https://nyaa.si', timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.RequestException:
        return False

def check_proxies():
    working_proxies = []
    max_threads = cfg.maxThread.value * 20

    def worker(queue):
        while not queue.empty():
            proxy = queue.get()
            if check_proxy(proxy):
                working_proxies.append(proxy)
            queue.task_done()

    queue = Queue()
    with open(cfg.testProxy.value, 'r') as f:
        for line in f:
            proxy = line.strip()
            queue.put(proxy)

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        for _ in range(max_threads):
            executor.submit(worker, queue)

    queue.join()

    with open(cfg.proxyPath.value, 'w') as f:
        for proxy in working_proxies:
            f.write(proxy + '\n')

    print(f"Proxy check Done\nTotal working proxies: {len(working_proxies)}")