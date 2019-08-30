#!/usr/bin/python
# encoding: utf-8

import sys
import os
import re
import string
from workflow import Workflow3, web

def createNew(wf):
    query = sys.argv[1]
    if query.endswith('/'):    
        path = os.popen("osascript ./getPath.scpt")
        for item in path:
            item = re.split("\n",item)[0]
            query = query[:-1]
            filePath = item+query
            wf.add_item(title=u"创建文件-->"+query, subtitle="文件路径-->"+item+"/"+query,arg=filePath,valid=True)
    else:
        wf.add_item(title=u"输入文件名,并以'/'结束")
    wf.send_feedback()

if __name__ == "__main__":
    wf = Workflow3()
    sys.exit(wf.run(createNew))