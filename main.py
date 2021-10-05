message = input()

HemmigDict = {'r1': '',
              'r2': '',
              'i1': '',
              'r3': '',
              'i2': '',
              'i3': '',
              'i4': ''}

for i, byte in enumerate(list(message)):
    HemmigDict[list(HemmigDict.keys())[i]] = int(byte)

s1 = (HemmigDict['r1'] + HemmigDict['i1'] + HemmigDict['i2'] + HemmigDict['i4']) % 2
s2 = (HemmigDict['r2'] + HemmigDict['i1'] + HemmigDict['i3'] + HemmigDict['i4']) % 2
s3 = (HemmigDict['r3'] + HemmigDict['i2'] + HemmigDict['i3'] + HemmigDict['i4']) % 2

print('Синдром - ', (s1, s2, s3))

syndrome = str(s1) + str(s2) + str(s3)
incorrect_byte_num = int(syndrome[::-1], 2)
incorrect_byte = list(HemmigDict.keys())[incorrect_byte_num - 1]
print(f'Ошибка в {incorrect_byte}')
if HemmigDict[incorrect_byte] == 0:
    HemmigDict[incorrect_byte] = 1
else:
    HemmigDict[incorrect_byte] = 0
print(*list(HemmigDict.values()), end=' ')
