# -*- coding: utf-8 -*-
from lxml import etree
import uuid

def createXmemlDocument():
    return etree.Element('xmeml', version='5')

def createBinNode(parent, week):
    element = etree.SubElement(parent, 'bin')
    etree.SubElement(element, 'uuid').text = str(uuid.uuid4()).upper()
    etree.SubElement(element, 'updatebehavior').text = 'add'
    etree.SubElement(element, 'name').text = week
    return element

def createChildrenNode(parent):
    return etree.SubElement(parent, 'children')

def addSequence(parent, settings):
    sequence = etree.SubElement(parent, 'sequence', id=settings['name'])
    etree.SubElement(sequence, 'uuid').text = str(uuid.uuid4()).upper()
    etree.SubElement(sequence, 'updatebehavior').text = 'add'
    etree.SubElement(sequence, 'name').text = settings['name']
    etree.SubElement(sequence, 'duration').text = settings['duration']
    addRateNode(sequence)
    addTimecodeNode(sequence)
    etree.SubElement(sequence, 'in').text = '-1'
    etree.SubElement(sequence, 'out').text = '-1'
    addMediaNode(sequence, settings)
    return sequence

def addMediaNode(parent, settings):
    media = etree.SubElement(parent, 'media')
    addVideoNode(media, settings)
    addAudioNode(media, settings)

def addVideoNode(parent, settings):
    video = etree.SubElement(parent, 'video')
    setVideoFormatNode(video, settings)
    addVideoTrackNode(video, settings)

def addVideoTrackNode(parent, settings):
    track = etree.SubElement(parent, 'track')
    addGenerator(track, settings)
    etree.SubElement(track, 'enabled').text = 'TRUE'
    etree.SubElement(track, 'locked').text = 'FALSE'

def addGenerator(parent, settings):
    element = etree.SubElement(parent, 'generatoritem', id='generator_'+settings['name'])
    etree.SubElement(element, 'name').text = 'generator_'+settings['name']
    etree.SubElement(element, 'duration').text = settings['duration']
    addRateNode(element)
    etree.SubElement(element, 'in').text = '0'
    etree.SubElement(element, 'out').text = '325'
    etree.SubElement(element, 'start').text = '0'
    etree.SubElement(element, 'end').text = '325'
    etree.SubElement(element, 'anamorphic').text = 'FALSE'
    etree.SubElement(element, 'alphatype').text = 'straight'
    logginginfo = etree.SubElement(element, 'logginginfo')
    etree.SubElement(logginginfo, 'scene')
    etree.SubElement(logginginfo, 'shottake')
    etree.SubElement(logginginfo, 'lognote')
    etree.SubElement(logginginfo, 'good').text = 'FALSE'
    labels = etree.SubElement(element, 'labels')
    etree.SubElement(labels, 'label2')
    comments = etree.SubElement(element, 'comments')
    etree.SubElement(comments, 'mastercomment1')
    etree.SubElement(comments, 'mastercomment2')
    etree.SubElement(comments, 'mastercomment3')
    etree.SubElement(comments, 'mastercomment4')

    addEffectForGenerator(element, settings)

    addFilterNode(element, 'Basic Motion')

    addFilterNode(element, 'Distort')

    sourcetrack = etree.SubElement(element, 'sourcetrack')
    etree.SubElement(sourcetrack, 'mediatype').text = 'video'
    etree.SubElement(element, 'fielddominance').text = 'lower'

def addFilterNode(parent, effect, value=None):
    filterNode = etree.SubElement(parent, 'filter')
    if effect == 'Basic Motion':
        addBasicMotionEffectNode(filterNode)
    if effect == 'Distort':
        addDistortEffectNode(filterNode)
    if effect == 'Audio Levels':
        addAudioLevelsEffectNode(filterNode, value)
    if effect == 'Audio Pan':
        addAudioPanEffectNode(filterNode, value)

def addDistortEffectNode(parent):
    effectNode = etree.SubElement(parent, 'effect')
    etree.SubElement(effectNode, 'name').text = 'Distort'
    etree.SubElement(effectNode, 'effectid').text = 'deformation'
    etree.SubElement(effectNode, 'effectcategory').text = 'motion'
    etree.SubElement(effectNode, 'effecttype').text = 'motion'
    etree.SubElement(effectNode, 'mediatype').text = 'video'
    parameter = etree.SubElement(effectNode, 'parameter')
    etree.SubElement(parameter, 'parameterid').text = 'ulcorner'
    etree.SubElement(parameter, 'name').text = 'Upper Left'
    value = etree.SubElement(parameter, 'value')
    etree.SubElement(value, 'horiz').text = '-0.5'
    etree.SubElement(value, 'vert').text = '-0.5'
    parameter = etree.SubElement(effectNode, 'parameter')
    etree.SubElement(parameter, 'parameterid').text = 'urcorner'
    etree.SubElement(parameter, 'name').text = 'Upper Right'
    value = etree.SubElement(parameter, 'value')
    etree.SubElement(value, 'horiz').text = '0.5'
    etree.SubElement(value, 'vert').text = '-0.5'
    parameter = etree.SubElement(effectNode, 'parameter')
    etree.SubElement(parameter, 'parameterid').text = 'lrcorner'
    etree.SubElement(parameter, 'name').text = 'Lower Right'
    value = etree.SubElement(parameter, 'value')
    etree.SubElement(value, 'horiz').text = '0.5'
    etree.SubElement(value, 'vert').text = '0.5'
    parameter = etree.SubElement(effectNode, 'parameter')
    etree.SubElement(parameter, 'parameterid').text = 'llcorner'
    etree.SubElement(parameter, 'name').text = 'Lower Left'
    value = etree.SubElement(parameter, 'value')
    etree.SubElement(value, 'horiz').text = '-0.5'
    etree.SubElement(value, 'vert').text = '0.5'
    parameter = etree.SubElement(effectNode, 'parameter')
    etree.SubElement(parameter, 'parameterid').text = 'aspect'
    etree.SubElement(parameter, 'name').text = 'Aspect'
    etree.SubElement(parameter, 'valuemin').text = '-10000'
    etree.SubElement(parameter, 'valuemax').text = '10000'
    etree.SubElement(parameter, 'value').text = '42.2222'

def addBasicMotionEffectNode(parent):
    effectNode = etree.SubElement(parent, 'effect')
    etree.SubElement(effectNode, 'name').text = 'Basic Motion'
    etree.SubElement(effectNode, 'effectid').text = 'basic'
    etree.SubElement(effectNode, 'effectcategory').text = 'motion'
    etree.SubElement(effectNode, 'effecttype').text = 'motion'
    etree.SubElement(effectNode, 'mediatype').text = 'video'
    parameter = etree.SubElement(effectNode, 'parameter')
    etree.SubElement(parameter, 'parameterid').text = 'scale'
    etree.SubElement(parameter, 'name').text = 'Scale'
    etree.SubElement(parameter, 'valuemin').text = '0'
    etree.SubElement(parameter, 'valuemax').text = '1000'
    etree.SubElement(parameter, 'value').text = '100'
    parameter = etree.SubElement(effectNode, 'parameter')
    etree.SubElement(parameter, 'parameterid').text = 'rotation'
    etree.SubElement(parameter, 'name').text = 'Rotation'
    etree.SubElement(parameter, 'valuemin').text = '-8640'
    etree.SubElement(parameter, 'valuemax').text = '8640'
    etree.SubElement(parameter, 'value').text = '0'
    parameter = etree.SubElement(effectNode, 'parameter')
    etree.SubElement(parameter, 'parameterid').text = 'center'
    etree.SubElement(parameter, 'name').text = 'Center'
    value = etree.SubElement(parameter, 'value')
    etree.SubElement(value, 'horiz').text = '0'
    etree.SubElement(value, 'vert').text = '0'
    parameter = etree.SubElement(effectNode, 'parameter')
    etree.SubElement(parameter, 'parameterid').text = 'centerOffset'
    etree.SubElement(parameter, 'name').text = 'Anchor Point'
    value = etree.SubElement(parameter, 'value')
    etree.SubElement(value, 'horiz').text = '0'
    etree.SubElement(value, 'vert').text = '0'
    
def addEffectForGenerator(parent, settings):
    element = etree.SubElement(parent, 'effect')
    etree.SubElement(element, 'name').text = 'DALEE.PAL'
    etree.SubElement(element, 'effectid').text = \
            'QCMotionPatch:~/Library/Application Support/Final Cut Studio/Motion/Templates/TVC/DALEE.PAL.motn'
    etree.SubElement(element, 'effecttype').text = 'generator'
    etree.SubElement(element, 'mediatype').text = 'video'
    
    parameter = etree.SubElement(element, 'parameter')
    etree.SubElement(parameter, 'parameterid').text = 'inputFileName'
    etree.SubElement(parameter, 'name').text = 'File name'
    etree.SubElement(parameter, 'value').text = \
            '~/Library/Application Support/Final Cut Studio/Motion/Templates/TVC/DALEE.PAL.motn'
    addDropZone(element, settings, 1)
    addDropZone(element, settings, 2)
    addDropZone(element, settings, 3)
    addTextInput(element, settings, 1)
    addTextInput(element, settings, 2)
    addTextInput(element, settings, 3)
    addTextInput(element, settings, 4)
    addTextInput(element, settings, 5)
    addTextInput(element, settings, 6)

def addTextInput(parent, settings, numberOfInput):
    element1 = etree.SubElement(parent, 'parameter')
    etree.SubElement(element1, 'parameterid').text = 'textInput_'+str(numberOfInput)
    etree.SubElement(element1, 'name').text = settings['text_input'+str(numberOfInput)+'_name']
    title = settings['text_input'+str(numberOfInput)+'_value']
    etree.SubElement(element1, 'value').text = title if title == 'АБВГДейка' else title.upper()

    element2 = etree.SubElement(parent, 'parameter')
    etree.SubElement(element2, 'parameterid').text = 'textSize_'+str(numberOfInput)
    etree.SubElement(element2, 'name').text = 'Text Size'
    etree.SubElement(element2, 'valuemin').text = '6'
    etree.SubElement(element2, 'valuemax').text = '288'
    etree.SubElement(element2, 'value').text = settings['text_input'+str(numberOfInput)+'_size']

    element3 = etree.SubElement(parent, 'parameter')
    etree.SubElement(element3, 'parameterid').text = 'textTracking_'+str(numberOfInput)
    etree.SubElement(element3, 'name').text = 'Text Tracking'
    etree.SubElement(element3, 'valuemin').text = '-100'
    etree.SubElement(element3, 'valuemax').text = '100'
    etree.SubElement(element3, 'value').text = settings['text_input'+str(numberOfInput)+'_tracking']

def addDropZone(parent, settings, numberOfZone):
    element1 = etree.SubElement(parent, 'parameter')
    etree.SubElement(element1, 'parameterid').text = 'dropZone_'+str(numberOfZone)
    etree.SubElement(element1, 'name').text = 'DropZone'+str(numberOfZone)
    value = etree.SubElement(element1, 'value')
    addClipForDropZoneNode(value, settings, numberOfZone)
    
    element2 = etree.SubElement(parent, 'parameter')
    etree.SubElement(element2, 'parameterid').text = 'dropZone_'+str(numberOfZone)+'_x'
    etree.SubElement(element2, 'name').text = 'Position'
    value = etree.SubElement(element2, 'value')
    etree.SubElement(value, 'horiz').text = '0'
    etree.SubElement(value, 'vert').text = '0'

def addClipForDropZoneNode(parent, settings, numberOfZone):
    clip = etree.SubElement(parent, 'clip', id=settings['media'+str(numberOfZone)]+'_dalee'+str(numberOfZone)+'_clip_'+settings['name'])
    etree.SubElement(clip, 'uuid').text = str(uuid.uuid4()).upper()
    etree.SubElement(clip, 'updatebehavior').text = 'add'
    etree.SubElement(clip, 'name').text = settings['media'+str(numberOfZone)]+'_dalee'+str(numberOfZone)
    etree.SubElement(clip, 'duration').text = '103'
    addRateNode(clip)
    addTimecodeNode(clip)
    etree.SubElement(clip, 'in').text = '-1'
    etree.SubElement(clip, 'out').text = '-1'
    etree.SubElement(clip, 'anamorphic').text = 'FALSE'
    etree.SubElement(clip, 'ismasterclip').text = 'TRUE'
    labels = etree.SubElement(clip, 'labels')
    etree.SubElement(labels, 'label2')
    media = etree.SubElement(clip, 'media')
    video = etree.SubElement(media, 'video')
    track = etree.SubElement(video, 'track')
    addClipitemForDropZoneNode(track, settings, numberOfZone)
    etree.SubElement(track, 'enabled').text = 'TRUE'
    etree.SubElement(track, 'locked').text = 'FALSE'

def addClipitemForDropZoneNode(parent, settings, numberOfZone):
    clipitem = etree.SubElement(parent, 'clipitem', id=settings['media'+str(numberOfZone)]+'_dalee'+str(numberOfZone)+'_clipitem_'+settings['name'])
    etree.SubElement(clipitem, 'name').text = settings['media'+str(numberOfZone)]+'_dalee'+str(numberOfZone)
    etree.SubElement(clipitem, 'duration').text = '103'
    addRateNode(clipitem)
    etree.SubElement(clipitem, 'in').text = '0'
    etree.SubElement(clipitem, 'out').text = '103'
    etree.SubElement(clipitem, 'start').text = '0'
    etree.SubElement(clipitem, 'end').text = '103'
    etree.SubElement(clipitem, 'pixelaspectratio').text = 'PAL-601'
    etree.SubElement(clipitem, 'anamorphic').text = 'TRUE'
    etree.SubElement(clipitem, 'alphatype').text = 'none'
    logginginfo = etree.SubElement(clipitem, 'logginginfo')
    etree.SubElement(logginginfo, 'scene')
    etree.SubElement(logginginfo, 'shottake')
    etree.SubElement(logginginfo, 'lognote')
    etree.SubElement(logginginfo, 'good').text = 'FALSE'
    labels = etree.SubElement(clipitem, 'labels')
    etree.SubElement(labels, 'label2')
    comments = etree.SubElement(clipitem, 'comments')
    etree.SubElement(comments, 'mastercomment1')
    etree.SubElement(comments, 'mastercomment2')
    etree.SubElement(comments, 'mastercomment3')
    etree.SubElement(comments, 'mastercomment4')
    addFileForDropZoneNode(clipitem, settings, numberOfZone)
    sourcetrack = etree.SubElement(clipitem, 'sourcetrack')
    etree.SubElement(sourcetrack, 'mediatype').text = 'video'
    etree.SubElement(clipitem, 'fielddominance').text = 'lower'

def addFileForDropZoneNode(parent, settings, numberOfZone):
    file = etree.SubElement(parent, 'file', id=settings['media'+str(numberOfZone)]+'_dalee'+str(numberOfZone)+'_file_'+settings['name'])
    etree.SubElement(file, 'name').text = settings['media'+str(numberOfZone)]+'_dalee'+str(numberOfZone)+'.mov'
    etree.SubElement(file, 'pathurl').text = 'file://localhost/Volumes/TVCi_Store/Broadcast%20Masters/%D0%9D%D0%BE%D0%B2%D0%B0%D1%8F%20%D0%BF%D0%B0%D0%BF%D0%BA%D0%B0/CG_DALEE/SHOTS/'+settings['media'+str(numberOfZone)+'_single']+'/'+settings['media'+str(numberOfZone)]+'_dalee'+str(numberOfZone)+'.mov'
    rate = etree.SubElement(file, 'rate')
    etree.SubElement(rate, 'timebase').text = '25'
    etree.SubElement(file, 'duration').text = '103'
    metadata = etree.SubElement(file, 'metadata')
    etree.SubElement(metadata, 'storage').text = 'QuickTime'
    etree.SubElement(metadata, 'key').text = 'com.apple.finalcutstudio.media.uuid'
    etree.SubElement(metadata, 'size').text = '36'
    etree.SubElement(metadata, 'type').text = 'UTF8'
    etree.SubElement(metadata, 'value').text = str(uuid.uuid4()).upper()
    timecode = etree.SubElement(file, 'timecode')
    rate = etree.SubElement(timecode, 'rate')
    etree.SubElement(rate, 'timebase').text = '25'
    etree.SubElement(timecode, 'string').text = '00:00:00:00'
    etree.SubElement(timecode, 'frame').text = '0'
    etree.SubElement(timecode, 'displayformat').text = 'NDF'
    etree.SubElement(timecode, 'source').text = 'source'
    media = etree.SubElement(file, 'media')
    video = etree.SubElement(media, 'video')
    etree.SubElement(video, 'duration').text = '103'
    samplecharacteristics = etree.SubElement(video, 'samplecharacteristics')
    etree.SubElement(samplecharacteristics, 'width').text = '720'
    etree.SubElement(samplecharacteristics, 'height').text = '576'

def setVideoFormatNode(parent, settings):
    node = etree.SubElement(parent, 'format')
    samplecharacteristics = etree.SubElement(node, 'samplecharacteristics')
    etree.SubElement(samplecharacteristics, 'width').text = settings['videoWidth']
    etree.SubElement(samplecharacteristics, 'height').text = settings['videoHeight']
    etree.SubElement(samplecharacteristics, 'anamorphic').text = settings['anamorphic']
    etree.SubElement(samplecharacteristics, 'pixelaspectratio').text = settings['pixelaspectratio']
    etree.SubElement(samplecharacteristics, 'fielddominance').text = settings['fielddominance']
    addRateNode(samplecharacteristics)
    etree.SubElement(samplecharacteristics, 'colordepth').text = settings['colordepth']
    codec = etree.SubElement(samplecharacteristics, 'codec')
    etree.SubElement(codec, 'name').text = 'Apple DVCPRO - PAL'
    addAppspecificdataNode(codec, True)

    addAppspecificdataNode(node, False)

def addAppspecificdataNode(parent, qtcodec):
    element = etree.SubElement(parent, 'appspecificdata')
    etree.SubElement(element, 'appname').text = 'Final Cut Pro'
    etree.SubElement(element, 'appmanufacturer').text = 'Apple Inc.'
    etree.SubElement(element, 'appversion').text = '7.0'
    data = etree.SubElement(element, 'data')
    if qtcodec:
        addQtCodecNode(data)
    else:
        addFcpimageprocessingNode(data)

def addQtCodecNode(parent):
    qtcodec = etree.SubElement(parent, 'qtcodec')
    etree.SubElement(qtcodec, 'codecname').text = 'Apple DVCPRO - PAL'
    etree.SubElement(qtcodec, 'codectypename').text = 'DVCPRO - PAL'
    etree.SubElement(qtcodec, 'codectypecode').text = 'dvpp'
    etree.SubElement(qtcodec, 'codecvendorcode').text = 'appl'
    etree.SubElement(qtcodec, 'spatialquality').text = '1023'
    etree.SubElement(qtcodec, 'temporalquality').text = '0'
    etree.SubElement(qtcodec, 'keyframerate').text = '0'
    etree.SubElement(qtcodec, 'datarate').text = '0'

def addFcpimageprocessingNode(parent):
    fcpimageprocessing = etree.SubElement(parent, 'fcpimageprocessing')
    etree.SubElement(fcpimageprocessing, 'useyuv').text = 'TRUE'
    etree.SubElement(fcpimageprocessing, 'usesuperwhite').text = 'FALSE'
    etree.SubElement(fcpimageprocessing, 'rendermode').text = 'YUV8BPP'

def addAudioNode(parent, settings):
    audio = etree.SubElement(parent, 'audio')
    formatNode = etree.SubElement(audio, 'format')
    samplecharacteristics = etree.SubElement(formatNode, 'samplecharacteristics')
    etree.SubElement(samplecharacteristics, 'depth').text = '16'
    etree.SubElement(samplecharacteristics, 'samplerate').text = '48000'

    outputs = etree.SubElement(audio, 'outputs')
    group = etree.SubElement(outputs, 'group')
    etree.SubElement(group, 'index').text = '1'
    etree.SubElement(group, 'numchannels').text = '2'
    etree.SubElement(group, 'downmix').text = '0'
    channel = etree.SubElement(group, 'channel')
    etree.SubElement(channel, 'index').text = '1'
    channel = etree.SubElement(group, 'channel')
    etree.SubElement(channel, 'index').text = '2'

    etree.SubElement(audio, 'in').text = '-1'
    etree.SubElement(audio, 'out').text = '-1'

    addAudioTrackNode(audio, settings, '1')
    addAudioTrackNode(audio, settings, '2')

    addFilterNode(audio, 'Audio Levels', '1.25893')

def addAudioTrackNode(parent, settings, numberOfTrack):
    track = etree.SubElement(parent, 'track')
    addAudioClipitemNode(track, settings, numberOfTrack)
    etree.SubElement(track, 'enabled').text = 'TRUE'
    etree.SubElement(track, 'locked').text = 'FALSE'
    etree.SubElement(track, 'outputchannelindex').text = numberOfTrack

def addAudioClipitemNode(parent, settings, numberOfTrack):
    clipitem = etree.SubElement(parent, 'clipitem', id='audiotrack_'+numberOfTrack+'_'+settings['name'])
    etree.SubElement(clipitem, 'name').text = 'DALEE'
    etree.SubElement(clipitem, 'duration').text = '325'
    addRateNode(clipitem)
    etree.SubElement(clipitem, 'in').text = '0'
    etree.SubElement(clipitem, 'out').text = '325'
    etree.SubElement(clipitem, 'start').text = '0'
    etree.SubElement(clipitem, 'end').text = '325'
    logginginfo = etree.SubElement(clipitem, 'logginginfo')
    etree.SubElement(logginginfo, 'scene')
    etree.SubElement(logginginfo, 'shottake')
    etree.SubElement(logginginfo, 'lognote')
    etree.SubElement(logginginfo, 'good').text = 'FALSE'
    labels = etree.SubElement(clipitem, 'labels')
    etree.SubElement(labels, 'label2')
    comments = etree.SubElement(clipitem, 'comments')
    etree.SubElement(comments, 'mastercomment1')
    etree.SubElement(comments, 'mastercomment2')
    etree.SubElement(comments, 'mastercomment3')
    etree.SubElement(comments, 'mastercomment4')
    addAudioFileNode(clipitem, settings, numberOfTrack)
    addFilterNode(clipitem, 'Audio Levels', '1')
    addFilterNode(clipitem, 'Audio Pan', str((-1)**int(numberOfTrack)))

    sourcetrack = etree.SubElement(clipitem, 'sourcetrack')
    etree.SubElement(sourcetrack, 'mediatype').text = 'audio'
    etree.SubElement(sourcetrack, 'trackindex').text = numberOfTrack

    link1 = etree.SubElement(clipitem, 'link')
    etree.SubElement(link1, 'linkclipref').text = 'audiotrack_1_'+settings['name']
    etree.SubElement(link1, 'mediatype').text = 'audio'
    etree.SubElement(link1, 'trackindex').text = '1'
    etree.SubElement(link1, 'clipindex').text = '1'
    etree.SubElement(link1, 'groupindex').text = '1'
    link2 = etree.SubElement(clipitem, 'link')
    etree.SubElement(link2, 'linkclipref').text = 'audiotrack_2_'+settings['name']
    etree.SubElement(link2, 'mediatype').text = 'audio'
    etree.SubElement(link2, 'trackindex').text = '2'
    etree.SubElement(link2, 'clipindex').text = '1'
    etree.SubElement(link2, 'groupindex').text = '1'

    itemhistory = etree.SubElement(clipitem, 'itemhistory')
    etree.SubElement(itemhistory, 'uuid').text = str(uuid.uuid4()).upper()

def addAudioFileNode(parent, settings, numberOfTrack):
    if numberOfTrack == '1':
        file = etree.SubElement(parent, 'file', id='audiofile_1_'+settings['name'])
        etree.SubElement(file, 'name').text = 'DALEE.wav'
        etree.SubElement(file, 'pathurl').text = 'file://localhost/Volumes/TVCi_Store/Broadcast%20Masters/%D0%9D%D0%BE%D0%B2%D0%B0%D1%8F%20%D0%BF%D0%B0%D0%BF%D0%BA%D0%B0/DALEE.wav'
        rate = etree.SubElement(file, 'rate')
        etree.SubElement(rate, 'timebase').text = '25'
        etree.SubElement(file, 'duration').text = '325'
        media = etree.SubElement(file, 'media')
        audio = etree.SubElement(media, 'audio')
        samplecharacteristics = etree.SubElement(audio, 'samplecharacteristics')
        etree.SubElement(samplecharacteristics, 'samplerate').text = '48000'
        etree.SubElement(samplecharacteristics, 'depth').text = '16'
        etree.SubElement(audio, 'channelcount').text = '2'
    else:
        etree.SubElement(parent, 'file', id='audiofile_1_'+settings['name'])

def addAudioLevelsEffectNode(parent, value):
    effectNode = etree.SubElement(parent, 'effect')
    etree.SubElement(effectNode, 'name').text = 'Audio Levels'
    etree.SubElement(effectNode, 'effectid').text = 'audiolevels'
    etree.SubElement(effectNode, 'effectcategory').text = 'audiolevels'
    etree.SubElement(effectNode, 'effecttype').text = 'audiolevels'
    etree.SubElement(effectNode, 'mediatype').text = 'audio'
    parameter = etree.SubElement(effectNode, 'parameter')
    etree.SubElement(parameter, 'name').text = 'Level'
    etree.SubElement(parameter, 'parameterid').text = 'level'
    etree.SubElement(parameter, 'valuemin').text = '0'
    etree.SubElement(parameter, 'valuemax').text = '3.98109'
    etree.SubElement(parameter, 'value').text = value

def addAudioPanEffectNode(parent, value):
    effectNode = etree.SubElement(parent, 'effect')
    etree.SubElement(effectNode, 'name').text = 'Audio Pan'
    etree.SubElement(effectNode, 'effectid').text = 'audiopan'
    etree.SubElement(effectNode, 'effectcategory').text = 'audiopan'
    etree.SubElement(effectNode, 'effecttype').text = 'audiopan'
    etree.SubElement(effectNode, 'mediatype').text = 'audio'
    parameter = etree.SubElement(effectNode, 'parameter')
    etree.SubElement(parameter, 'name').text = 'Pan'
    etree.SubElement(parameter, 'parameterid').text = 'pan'
    etree.SubElement(parameter, 'valuemin').text = '-1'
    etree.SubElement(parameter, 'valuemax').text = '1'
    etree.SubElement(parameter, 'value').text = value

def addTimecodeNode(parent):
    element = etree.SubElement(parent, 'timecode')
    addRateNode(element)
    etree.SubElement(element, 'string').text = '00:00:00:00'
    etree.SubElement(element, 'frame').text = '0'
    etree.SubElement(element, 'source').text = 'source'
    etree.SubElement(element, 'displayformat').text = 'NDF'

def addRateNode(parent):
    element = etree.SubElement(parent, 'rate')
    etree.SubElement(element, 'ntsc').text = 'FALSE'
    etree.SubElement(element, 'timebase').text = '25'

def createFile(root, fileName):
    doc = etree.ElementTree(root)
    outFile = open(fileName, 'wb')
    doc.write(outFile, xml_declaration=True, encoding='UTF-8', doctype="<!DOCTYPE xmeml>", pretty_print=True) 