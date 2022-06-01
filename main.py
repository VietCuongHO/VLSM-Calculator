#Chương trình chia subnet sử dụng phương pháp VLSM
import ipaddress
import math
def ktrclass(ip):
    lst = ip[0].split('.')
    if int(lst[0]) >= 1 and int(lst[0]) <= 127:
        return 'Class A'
    elif int(lst[0]) >= 128 and int(lst[0]) <= 191:
        return 'Class B'
    elif int(lst[0]) >= 192 and int(lst[0]) <= 223:
        return 'Class C'
def buocnhay(function, value1, value2):
    lst = value1.split('.')
    if function == 'Class A':
        while (int(lst[3]) + value2) > 255:
            lst[3] = str(0)
            lst[2] = str(int(lst[2]) + 1)
            value2 = value2 - (256 - int(lst[3]))
            if int(lst[2]) > 255:
                lst[2] = str(0)
                lst[1] = str(int(lst[1]) + 1)
        if value2 > 0:
            lst[3] = str(int(lst[3]) + value2)
            value1new = str('.'.join(lst))
            return value1new
        else:
            value1new = str('.'.join(lst))
            return value1new
    elif function == 'Class B':
        while (int(lst[3]) + value2) > 255:
            lst[3] = str(0)
            lst[2] = str(int(lst[2]) + 1)
            value2 = value2 - (256 - int(lst[3]))
        if value2 > 0:
            lst[3] = str(int(lst[3]) + value2)
            value1new = str('.'.join(lst))
            return value1new
        else:
            value1new = str('.'.join(lst))
            return value1new
    elif function == 'Class C':
        lst[3] = str(int(lst[3]) + value2)      #cộng vào octet 2
        value1new = str('.'.join(lst))
        return value1new
def hienthism(value1, value2):
    lst = []
    lst.append(value1)
    lst.append(str(value2))
    lstnew = '/'.join(lst)
    ip = ipaddress.IPv4Network(lstnew)
    print('Subnet mask:',ip.netmask)
#mainprogram
a = input('Nhập địa chỉ IPv4: \nex: 192.168.1.0/24\n')
b = ipaddress.IPv4Network(a)
c = list(map(int, input('Nhập danh sách host mà bạn cần: ').split()))
c.sort(reverse=True)
print('-----------------------------------------------------------')
# Thông tin của host lớn nhất
print('Thông tin của mạng {} hosts:'.format(c[0]))
d0 = []
d0str = []
l0 = []
m0 = math.ceil(math.log((c[0] + 2), 2))        # số bit còn lại phần host
np0 = 32 - m0                                  # new prefix
jump0 = 2**m0
#print(jump0)
for j in b.subnets(new_prefix=np0):
    d0str.append(str(j.network_address))
#print(d0str)
for k in b.subnets(new_prefix=np0):
    d0.append(k)
next0str = buocnhay(ktrclass(d0str), d0str[0], jump0)
#print(next0str)
for i in d0[0].hosts():
    l0.append(str(i))
print('Network ID: ', d0[0])
print('Subnet mask:', d0[0].netmask)
print('Host range: {}/{} --> {}/{}'.format(l0[0], np0, l0[-1], np0))
print('Broadcast ID: {}/{}'.format((ipaddress.IPv4Address(next0str) - 1), np0))
print('Prefix length:', np0)
#print('Next ip:',next0str)
print('\n')
#Thông tin các host sau đó:
jump = 0
nextstr = next0str
for u in range(1, len(c)):
    print('Thông tin của mạng {} hosts:'.format(c[u]))
    dstr = []
    d = []
    l = []
    m = math.ceil(math.log((c[u] + 2), 2))       # số bit còn lại phần host
    np = 32 - m                                  # new prefix
    for jj in b.subnets(new_prefix=np):
        dstr.append(str(jj.network_address))
    #print(dstr)
    for kk in b.subnets(new_prefix=np):
        d.append(kk)
    jump = 2 ** m
    #print(jump)
    if nextstr not in dstr:
        print('Host range đã đầy')
        print('\n')
    #vitri = dstr.index(str(nextstr))
    else:
        vitri = dstr.index(str(nextstr))
        # print(vitri)
        for ii in d[vitri].hosts():
            l.append(ii)
        print('Network ID: {}/{} '.format(nextstr, np))
        hienthism(nextstr,np)
        print('Host range: {}/{}-->{}/{}'.format(l[0], np, l[-1], np))
        print('Broadcast ID: {}/{}'.format((ipaddress.IPv4Address(nextstr) + jump - 1), np))
        print('Prefix length:', np)
        nextstr = buocnhay(ktrclass(d0str), nextstr, jump)
        #print(nextstr)
        print('\n')



