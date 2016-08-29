#!/usr/bin/env python

import cgi
import cgitb
import httplib

cgitb.enable()
form = cgi.FieldStorage()

#### FUNCS ####

def mrcDisplayError(message):
    print '    <div id="mrcError">'
    print '      <p align="right">&nbsp;<button onclick="var mrcErrorDiv=document.getElementById(\'mrcError\');mrcErrorDiv.innerHTML=\'\';">X</button>&nbsp;</p>'
    print '      <p>&nbsp;Error!&nbsp;<br/>&nbsp;'+message+'&nbsp;</p>'
    print '    </div>'

def mrcDisplayPost(postParamName):
    output=''
    if postParamName in form.keys():
        output=form.getvalue(postParamName)
    else:
        output='not found'
    print '    <p>POST parameter "'+postParamName+'" = '+output+'</p>'

def mrcDisplayDirFromPost(postParamName):
    output=''
    if postParamName in form.keys():
        output=form.getvalue(postParamName)
    print '    <script type="text/javascript">';
    print '      $(document).ready(function () {';
    print '        mrcBrowse("'+output+'");';
    print '      });';
    print '    </script>';
 
def analyseServerSideLine(line):
    line=line.lstrip()
    if line.startswith('<!--'):
        return

    functionAttrIndex = line.find('function="')
    if functionAttrIndex==-1:
        return
    
    functionName=''
    functionParam=''

    startFunctionAttrIndex = line[functionAttrIndex:].find('"')+functionAttrIndex+1
    endFunctionAttrIndex = line[startFunctionAttrIndex:].find('"')+startFunctionAttrIndex
    functionName = line[startFunctionAttrIndex:endFunctionAttrIndex]
    # print '    <p>functionName '+functionName+'</p>'

    paramAttrIndex = line.find('param="')
    if paramAttrIndex>-1:
        startParamAttrIndex = line[paramAttrIndex:].find('"')+paramAttrIndex+1
        endParamAttrIndex = line[startParamAttrIndex:].find('"')+startParamAttrIndex
        functionParam = line[startParamAttrIndex:endParamAttrIndex]
        # print '    <p>functionParam '+functionParam+'</p>'

    if functionName=='mrcDisplayError' and functionParam:
        mrcDisplayError(functionParam)
        return

    if functionName=='mrcDisplayPost' and functionParam:
        mrcDisplayPost(functionParam)
        return

    if functionName=='mrcDisplayDirFromPost' and functionParam:
        mrcDisplayDirFromPost(functionParam)
        return
        
#### MAIN ####
with open('start.py.html') as f:
    for line in f:
        line = line.rstrip('\r\n')
        if line.find('<python')==-1:
            print line
        else:
            analyseServerSideLine(line)

