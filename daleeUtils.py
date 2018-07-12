import xlrd
from roliki import getRoliki

def fday_to_hms(fday):
    seconds = round(fday * 86400.0)
    minutes = int(seconds / 60.0)
    seconds = seconds - (minutes * 60.0)
    hours = int(minutes / 60.0)
    minutes = minutes - (hours * 60.0)
    return int(hours), int(minutes), int(seconds)

def insertTimeString(time):
    timeTuple = fday_to_hms(time)
    hoursString = ''
    hoursDecline = ''
    minutesString = ''
    if timeTuple[0]:
        if 10 < timeTuple[0] < 20:
            hoursDecline = ' ЧАСОВ'
        elif timeTuple[0] % 10 == 1:
            hoursDecline = ' ЧАС'
        elif timeTuple[0] % 10 < 5:
            hoursDecline = ' ЧАСА'
        else:
            hoursDecline = ' ЧАСОВ'
        hoursString = hoursString + ' ' + str(timeTuple[0]) + hoursDecline
    if timeTuple[1]:
        minutesString = minutesString + ' ' + str(timeTuple[1]) + ' МИНУТ'
    return 'ЧЕРЕЗ'+hoursString+minutesString

def getListFromFile(XLSfile):
    rb = xlrd.open_workbook(XLSfile, formatting_info=True)
    sheet = rb.sheet_by_index(0)
    vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
    vals.pop(0)
    vals.pop(0)
    if not len(vals[-1][0]):
        vals.pop()
    list1 = []
    for item in vals:
        itemList = []
        itemList.append(item[0])
        name = item[1].rpartition(' ')
        name = list(name)[0].rpartition(' ')
        name = list(name)[0].partition(' ')
        name = name[2]
        itemList.append(name.split('-')[0])
        itemList.append(name.split('-')[1])
        itemList.append(name.split('-')[2])
        itemList.append(insertTimeString(item[3]))
        itemList.append(insertTimeString(item[4]))
        list1.append(itemList)
    return list1

def createListVariors(listFromXLS):
    ROLIKI = getRoliki()
    listVariors = []
    listLost = []
    for item in listFromXLS:
        # print(item)
        itemList = []
        try:
            itemList.append(item[0])
            itemList.append(ROLIKI.get(item[1])[0])
            itemList.append(ROLIKI.get(item[1])[1])
            itemList.append(ROLIKI.get(item[1])[2])
            itemList.append(ROLIKI.get(item[2])[0])
            itemList.append(ROLIKI.get(item[2])[1])
            itemList.append(ROLIKI.get(item[2])[2])
            itemList.append(ROLIKI.get(item[3])[0])
            itemList.append(ROLIKI.get(item[3])[1])
            itemList.append(ROLIKI.get(item[3])[2])
            itemList.append(item[4])
            itemList.append(item[5])
            itemList.append(ROLIKI.get(item[1])[3])
            itemList.append(ROLIKI.get(item[1])[4])
            itemList.append(ROLIKI.get(item[2])[3])
            itemList.append(ROLIKI.get(item[2])[4])
            itemList.append(ROLIKI.get(item[3])[3])
            itemList.append(ROLIKI.get(item[3])[4])
        except Exception as e:
            # print(e)
            # print(item[1] + ' ' + item[2] + ' ' + item[3])
            listLost.append(item[1])
            listLost.append(item[2])
            listLost.append(item[3])
        else:
            pass
        finally:
            pass
        # print(itemList)
        listVariors.append(itemList)
    setLost = set(listLost)
    if len(setLost):
        listRolik = []
        for item in ROLIKI:
            listRolik.append(item)
        setRolik = set(listRolik)
        listLost = list(setLost.difference(setRolik))
        listLost.sort()
        for item in listLost:
            print(item)
    
    return listVariors

def getSequenceSettings():
    settings = {'name':'SEQUENCE_NAME',
                'duration':'325',
                'videoWidth':'720',
                'videoHeight':'576',
                'anamorphic':'TRUE',
                'pixelaspectratio':'PAL-601',
                'fielddominance':'lower',
                'colordepth':'24',
                'media1':'Notkin1',
                'media2':'Notkin1',
                'media3':'Notkin1',
                'media1_single':'CYCLES',
                'media2_single':'CYCLES',
                'media3_single':'CYCLES',
                'text_input1_name':'СЕЙЧАС',
                'text_input1_value':'СЕЙЧАС',
                'text_input1_size':'60',
                'text_input1_tracking':'0',
                'text_input2_name':'ДОКУМЕНТАЛЬНОЕ КИНО',
                'text_input2_value':'TEXT_INPUT1_VALUE',
                'text_input2_size':'60',
                'text_input2_tracking':'0',
                'text_input3_name':'ЧЕРЕЗ 1 ЧАС 20 МИНУТ',
                'text_input3_value':'TIME2_VALUE',
                'text_input3_size':'60',
                'text_input3_tracking':'0',
                'text_input4_name':'ВСЕМИРНАЯ ИСТОРИЯ',
                'text_input4_value':'TEXT_INPUT2_VALUE',
                'text_input4_size':'60',
                'text_input4_tracking':'0',
                'text_input5_name':'ЧЕРЕЗ 2 ЧАСА',
                'text_input5_value':'TIME3_VALUE',
                'text_input5_size':'60',
                'text_input5_tracking':'0',
                'text_input6_name':'ИМЯ. ЗАШИФРОВАННАЯ',
                'text_input6_value':'TEXT_INPUT3_VALUE',
                'text_input6_size':'60',
                'text_input6_tracking':'0'}
    # print(settings)
    return settings
