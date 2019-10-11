#/usr/bin/python
from z3 import *

flag = result = [0] * 19
for i in range(19):
	flag[i] = Int('flag[%d]'%i)

s = Solver()

s.add(flag[0x04] == 0x2d)
s.add(flag[0x09] == 0x2d)
s.add(flag[0x0e] == 0x2d)
s.add(flag[0x05] == flag[0x06] + 0x01)
s.add(flag[0x05] == flag[0x12])
s.add(flag[0x01] == (flag[0x12] % 0x04) * 0x16)
s.add(flag[0x0a] == flag[0x03] * flag[0x0f] / flag[0x11] - 0x01)
s.add(flag[0x01] == flag[0x0a])
s.add(flag[0x0d] == flag[0x0a] + 0x05)
s.add(flag[0x0a] == flag[0x05] - 0x09)
s.add(0x5a0 == (flag[0x00] % flag[0x07]) * flag[0x0b])
s.add(flag[0x02] - flag[0x08] + flag[0x0c] == flag[0x0a] - 0x09)
s.add(flag[0x10] == (flag[0x03] + flag[0x0c]) / 0x02)
s.add(flag[0x00] - flag[0x02] + flag[0x03] == flag[0x0c] + 0x0f)
s.add(flag[0x03] == flag[0x0d])
s.add(flag[0x10] == flag[0x00])
s.add(flag[0x07] + 0x01 == flag[0x02])
s.add(flag[0x0f] + 0x01 == flag[0x0b])
s.add(flag[0x0b] + 0x03 == flag[0x11])
s.add(flag[0x07] + 0x14 == flag[0x06])

if str(s.check()) == 'sat':
	m = s.model()
	for d in m.decls():
		_i, _v = int(d.name().strip('flag[]')), str(m[d])
		result[_i] = chr(int(_v))
	print('SERIAL : ' + ''.join(result))