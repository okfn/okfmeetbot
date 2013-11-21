import writers
import re
class Config(object):
    logFileDir = '/home/okfn/okfmeetbot/meetinglogs'
    filenamePattern = '%(channel)s/%%Y/%(channel)s.%%F-%%H.%%M'

    logUrlPrefix = 'http://meetinglogs.okfn.org'
    MeetBotInfoURL = 'https://wiki.ubuntu.com/meetingology'
    writer_map = {
        #'.log.html':writers.HTMLlog,
        #'.1.html': writers.HTML,
        '.html': writers.HTML2,
        #'.rst': writers.ReST,
        '.txt': writers.Text,
        #'.rst.html':writers.HTMLfromReST,
        #'.moin.txt':writers.Moin,
        #'.mw.txt':writers.MediaWiki,
        }
    command_RE = re.compile(r'[#|\[]([\w]+)[\]]?[ \t]*(.*)')
