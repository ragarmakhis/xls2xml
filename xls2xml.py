# -*- coding: utf-8 -*-
import xls2xmlHelper as xmeml
import io
# import sys
import argparse
import daleeUtils as DU
import roliki

def create_new_xml(args):
    NUMBER_OF_WEEK = args.week
    VARIORS = DU.createListVariors(DU.getListFromFile(args.xls))

    SEQUENCE_SETTINGS = DU.getSequenceSettings()

    root = xmeml.createXmemlDocument() 
    bin_node = xmeml.createBinNode(root, NUMBER_OF_WEEK)
    children_node = xmeml.createChildrenNode(bin_node)
    for item in VARIORS:
        SEQUENCE_SETTINGS['name'] = item[0]
        SEQUENCE_SETTINGS['media1'] = item[1]
        SEQUENCE_SETTINGS['media1_single'] = item[2]
        SEQUENCE_SETTINGS['text_input2_value'] = item[3]
        SEQUENCE_SETTINGS['text_input2_size'] = item[12]
        SEQUENCE_SETTINGS['text_input2_tracking'] = item[13]
        SEQUENCE_SETTINGS['media2'] = item[4]
        SEQUENCE_SETTINGS['media2_single'] = item[5]
        SEQUENCE_SETTINGS['text_input3_value'] = item[10]
        SEQUENCE_SETTINGS['text_input4_value'] = item[6]
        SEQUENCE_SETTINGS['text_input4_size'] = item[14]
        SEQUENCE_SETTINGS['text_input4_tracking'] = item[15]
        SEQUENCE_SETTINGS['media3'] = item[7]
        SEQUENCE_SETTINGS['media3_single'] = item[8]
        SEQUENCE_SETTINGS['text_input5_value'] = item[11]
        SEQUENCE_SETTINGS['text_input6_value'] = item[9]
        SEQUENCE_SETTINGS['text_input6_size'] = item[16]
        SEQUENCE_SETTINGS['text_input6_tracking'] = item[17]
        xmeml.addSequence(children_node, SEQUENCE_SETTINGS)
        
    fileName = 'output_' + NUMBER_OF_WEEK + '.xml'

    xmeml.createFile(root, fileName)

    with io.open(fileName,'r',encoding='utf8') as f:
        text = f.read()
    text = text.replace("&amp;", "&")
    with io.open(fileName,'w',encoding='utf8') as f:
        f.write(text)

def add_clip(args):
    roliki.addRolik(args.name, args.file, args.singles, args.title, args.size, args.tracking)

def change_clip(args):
    roliki.changeRolik(args.name, args.file, args.singles, args.title, args.size, args.tracking)

def remove_clip(args):
    roliki.removeRolik(args.name)

def list_clips(args):
    roliki.listRoliki()

def parser_args():
    parser = argparse.ArgumentParser(description='Clips DALEE utility')
    subparsers = parser.add_subparsers()

    parser_generate = subparsers.add_parser('generate', aliases=['g'], help='Create new Final Cut xml from Excel')
    parser_generate.add_argument('week', help='Number of week')
    parser_generate.add_argument('xls', help='Excel file')
    parser_generate.set_defaults(func=create_new_xml)
    
    parser_add = subparsers.add_parser('add', aliases=['a'], help='Add new clip')
    parser_add.add_argument('-n', '--name', required=True, help='Name of clip')
    parser_add.add_argument('-f', '--file', required=True, help='Name of file')
    parser_add.add_argument('-s', '--singles', default='SINGLES', help='SINGLES or CYCLES. Default = SINGLES')
    parser_add.add_argument('-t', '--title', required=True, help='Title of clip (&#10; - new line; &#8212; - mDash)')
    parser_add.add_argument('-S', '--size', default='60', help='Font size. Default = 60')
    parser_add.add_argument('-T', '--tracking', default='0', help='Font tracking. Default = 0')
    parser_add.set_defaults(func=add_clip)
    
    parser_change = subparsers.add_parser('change', aliases=['c'], help='Change clip')
    parser_change.add_argument('-n', '--name', required=True, help='Name of clip')
    parser_change.add_argument('-f', '--file', help='Name of file')
    parser_change.add_argument('-s', '--singles', help='SINGLES or CYCLES')
    parser_change.add_argument('-t', '--title', help='Title of clip (&#10; - new line; &#8212; - mDash)')
    parser_change.add_argument('-S', '--size', help='Font size. Default = 60')
    parser_change.add_argument('-T', '--tracking', help='Font tracking. Default = 0')
    parser_change.set_defaults(func=change_clip)

    parser_remove = subparsers.add_parser('remove', aliases=['r'], help='Remove clip')
    parser_remove.add_argument('-n', '--name', required=True, help='Name of clip')
    parser_remove.set_defaults(func=remove_clip)

    parser_list = subparsers.add_parser('list', aliases=['l'], help='List clips')
    parser_list.set_defaults(func=list_clips)

    return parser

def main():
    parser = parser_args()
    args = parser.parse_args()
    try:
        args.func(args)
    except Exception as e:
        # print('Usage: xls2xml.py generate NAME_OF_WEEK EXCEL_FILE')
        parser.print_help()
        print(e)
        # print(args)
        pass
    else:
        pass
    finally:
        pass

if __name__ == '__main__':
    main()
