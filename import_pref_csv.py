tmpstr = '''{
    "model": "sugartsa.Pref",
    "fields": {
      "code": %code,
      "name": "%name"
    }
  },
'''

f = open('pref.csv', 'r')
datalist = f.readlines()
f.close()
wl = []
wl.append('[')
for dt in datalist:
    items = dt.split(',')
    vstr = tmpstr.replace('%code', items[0])
    vstr = vstr.replace('%name', items[1].strip())
    print(vstr)
    wl.append(vstr)
lstr = wl.pop(-1)
lstr = lstr.rstrip()
lstr = lstr.rstrip(',')
wl.append(lstr)
wl.append(']')
print(wl)
w = open('sugartsa/fixtures/100_Pref.json', 'w')

w.writelines(wl)

w.close()
