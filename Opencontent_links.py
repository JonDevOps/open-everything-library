#!/usr/bin/python3
from urllib.parse import urlparse, urlunparse
import codecs
import fileinput
import json
import os.path
import pprint
import requests
#import results
import six
import sys
import time
import urllib.request, urllib.parse, urllib.error, urllib.request, urllib.error, urllib.parse
from filelock import FileLock
import pymongo
import funcs
import re
refs = {}
links = {}

from multiprocessing import Process, Pool
skip = (       
    '3dml',
    '3g2',
    '3gp',
    '7z',
    'aab',
    'aac',
    'aam',
    'aas',
    'abw',
    'ac',
    'acc',
    'ace',
    'acu',
    'adp',
    'aep',
    'afp',
    'ahead',
    'ai',
    'aif',
    'air',
    'ait',
    'ami',
    'apk',
    'application',
    'apr',
    'asf',
    'aso',
    'atc',
    'atomcat',
    'atomsvc',
    'atx',
    'au',
    'avi',
    'aw',
    'azf',
    'azs',
    'azw',
    'bcpio',
    'bdf',
    'bdm',
    'bed',
    'bh2',
    'bin',
    'bmi',
    'bmp',
    'box',
    'btif',
    'bz',
    'bz2',
    'c11amc',
    'c11amz',
    'c4g',
    'cab',
    'car',
    'cat',
    'ccxml',
    'cdbcmsg',
    'cdkey',
    'cdmia',
    'cdmic',
    'cdmid',
    'cdmio',
    'cdmiq',
    'cdx',
    'cdxml',
    'cdy',
    'cer',
    'cgm',
    'chat',
    'chrt',
    'cif',
    'cii',
    'cil',
    'cla',
    'class',
    'clkk',
    'clkp',
    'clkt',
    'clkw',
    'clkx',
    'clp',
    'cmc',
    'cmdf',
    'cml',
    'cmp',
    'cmx',
    'cod',
    'cpio',
    'cpt',
    'crl',
    'cryptonote',
    'csh',
    'csml',
    'csp',
    'cu',
    'curl',
    'cww',
    'dae',
    'daf',
    'davmount',
    'dcurl',
    'dd2',
    'ddd',
    'deb',
    'der',
    'dfac',
    'dir',
    'dis',
    'djvu',
    'dna',
    'docm',
    'dotm',
    'dp',
    'dpg',
    'dra',
    'dsc',
    'dssc',
    'dtb',
    'dts',
    'dtshd',
    'dvi',
    'dwf',
    'dwg',
    'dxf',
    'dxp',
    'ecelp4800',
    'ecelp7470',
    'ecelp9600',
    'edm',
    'edx',
    'efif',
    'ei6',
    'eml',
    'emma',
    'eol',
    'eot',
    'epub',
    'es',
    'es3',
    'esf',
    'etx',
    'exe',
    'exe',
    'exi',
    'ext',
    'ez2',
    'ez3',
    'f',
    'f4v',
    'fbs',
    'fcs',
    'fdf',
    'fe_launch',
    'fg5',
    'fh',
    'fig',
    'xdf',
    'fli',
    'flo',
    'flv',
    'flv',
    'flw',
    'flx',
    'fly',
    'fm',
    'fnc',
    'fpx',
    'fsc',
    'fst',
    'ftc',
    'fti',
    'fvt',
    'fxp',
    'fzs',
    'g2w',
    'g3',
    'g3w',
    'gac',
    'gdl',
    'geo',
    'gex',
    'ggb',
    'ggt',
    'ghf',
    'gif',
    'gim',
    'gmx',
    'gnumeric',
    'gph',
    'gqf',
    'gram',
    'grv',
    'grxml',
    'gsf',
    'gtar',
    'gtm',
    'gtw',
    'gv',
    'gxt',
    'h261',
    'h263',
    'h264',
    'hal',
    'hbci',
    'hdf',
    'hlp',
    'hpgl',
    'hpid',
    'hps',
    'hqx',
    'htke',
    'hvd',
    'hvp',
    'hvs',
    'i2g',
    'icc',
    'ice',
    'ico',
    'ief',
    'ifm',
    'igl',
    'igm',
    'igs',
    'igx',
    'iif',
    'imp',
    'ims',
    'ipfix',
    'ipk',
    'irm',
    'irp',
    'itp',
    'ivp',
    'ivu',
    'jad',
    'jam',
    'jar',
    'jisp',
    'jlt',
    'jnlp',
    'joda',
    'jpeg, .jpg',
    'jpgv',
    'jpm',
    'karbon',
    'kfo',
    'kia',
    'kml',
    'kmz',
    'kne',
    'kon',
    'kpr',
    'ksp',
    'ktx',
    'ktz',
    'kwd',
    'lasxml',
    'latex',
    'lbd',
    'lbe',
    'les',
    'link66',
    'lrm',
    'ltf',
    'lvp',
    'lwp',
    'm21',
    'm3u',
    'm3u8',
    'm4v',
    'ma',
    'mads',
    'mag',
    'mathml',
    'mbk',
    'mbox',
    'mc1',
    'mcd',
    'mcurl',
    'mdb',
    'mdi',
    'meta4',
    'mets',
    'mfm',
    'mgp',
    'mgz',
    'mid',
    'mif',
    'mj2',
    'mlp',
    'mmd',
    'mmf',
    'mmr',
    'mny',
    'mods',
    'movie',
    'mp3',
    'mp4',
    'mp4',
    'mp4a',
    'mpc',
    'mpeg',
    'mpga',
    'mpkg',
    'mpm',
    'mpn',
    'mpp',
    'mpy',
    'mqy',
    'mrc',
    'mrcx',
    'mscml',
    'mseq',
    'msf',
    'msh',
    'msl',
    'msty',
    'mts',
    'mus',
    'musicxml',
    'mvb',
    'mwf',
    'mxf',
    'mxl',
    'mxml',
    'mxs',
    'mxu',
    'n-gage',
    'n3',
    'nbp',
    'nc',
    'ncx',
    'ngdat',
    'nlu',
    'nml',
    'nnd',
    'nns',
    'nnw',
    'npx',
    'nsf',
    'oa2',
    'oa3',
    'oas',
    'oda',
    'odb',
    'odc',
    'odf',
    'odft',
    'odg',
    'odi',
    'odm',
    'odp',
    'ods',
    'odt',
    'oga',
    'ogg',
    'ogv',
    'ogx',
    'opf',
#    'org',
    'osf',
    'osfpvg',
    'otc',
    'otf',
    'otg',
    'oth',
    'oti',
    'otp',
    'ots',
    'ott',
    'oxt',
    'p',
    'p10',
    'p12',
    'p7b',
    'p7m',
    'p7r',
    'p7s',
    'p8',
    'par',
    'paw',
    'pbd',
    'pbm',
    'pcf',
    'pcl',
    'pclxl',
    'pcurl',
    'pcx',
    'pdb',
#    'pdf',
    'pfa',
    'pfr',
    'pgm',
    'pgn',
    'pgp',
    'pic',
    'pki',
    'pkipath',
    'plb',
    'plc',
    'plf',
    'pls',
    'pml',
    'png',
    'pnm',
    'portpkg',
    'potm',
    'ppam',
    'ppd',
    'ppm',
    'ppsm',
    'ppt',
    'pptm',
    'prc',
    'pre',
    'prf',
    'psb',
    'psd',
    'psf',
    'pskcxml',
    'ptid',
    'pub',
    'pvb',
    'pwn',
    'pya',
    'pyv',
    'qam',
    'qbo',
    'qfx',
    'qps',
    'qt',
    'qxd',
    'ram',
    'rar',
    'ras',
    'rcprofile',
    'rdf',
    'rdz',
    'rep',
    'res',
    'rgb',
    'rif',
    'rip',
    'rl',
    'rlc',
    'rld',
    'rm',
    'rmp',
    'rms',
    'rnc',
    'rp9',
    'rpss',
    'rpst',
    'rq',
    'rs',
    'rsd',
    'rtx',
    's',
    'saf',
    'sbml',
    'sc',
    'scd',
    'scm',
    'scq',
    'scs',
    'scurl',
    'sda',
    'sdc',
    'sdd',
    'sdkm',
    'sdp',
    'sdw',
    'see',
    'seed',
    'sema',
    'semd',
    'semf',
    'ser',
    'setpay',
    'setreg',
    'sfd-hdstx',
    'sfs',
    'sgl',
    'shar',
    'shf',
    'sis',
    'sit',
    'sitx',
    'skp',
    'sldm',
    'slt',
    'sm',
    'smf',
    'smi',
    'snf',
    'spf',
    'spl',
    'spot',
    'spp',
    'spq',
    'src',
    'sru',
    'srx',
    'sse',
    'ssf',
    'ssml',
    'st',
    'stc',
    'std',
    'stf',
    'sti',
    'stk',
    'stl',
    'str',
    'stw',
    'sub',
    'sus',
    'sv4cpio',
    'sv4crc',
    'svc',
    'svd',
    'svg',
    'swf',
    'swi',
    'sxc',
    'sxd',
    'sxg',
    'sxi',
    'sxm',
    'sxw',
    't',
    'tao',
    'tar',
    'tcap',
    'tcl',
    'teacher',
    'tei',
    'tfi',
    'tfm',
    'tiff',
    'tmo',
    'torrent',
    'tpl',
    'tpt',
    'tra',
    'trm',
    'tsd',
    'tsv',
    'ttf',
    'ttl',
    'twd',
    'txd',
    'txf',
    'ufd',
    'umj',
    'unityweb',
    'uoml',
    'uri',
    'ustar',
    'utz',
    'uu',
    'uva',
    'uvh',
    'uvi',
    'uvm',
    'uvp',
    'uvs',
    'uvu',
    'uvv',
    'vcd',
    'vcf',
    'vcg',
    'vcs',
    'vcx',
    'vis',
    'viv',
    'vsd',
    'vsf',
    'vtu',
    'vxml',
    'wad',
    'wav',
    'wax',
    'wbmp',
    'wbs',
    'wbxml',
    'weba',
    'webm',
    'webp',
    'wg',
    'wgt',
    'wm',
    'wma',
    'wmd',
    'wmf',
    'wml',
    'wmlc',
    'wmls',
    'wmlsc',
    'wmv',
    'wmx',
    'wmz',
    'woff',
    'wpd',
    'wpl',
    'wqd',
    'wrl',
    'wsdl',
    'wspolicy',
    'wtb',
    'wvx',
    'x3d',
    'xap',
    'xar',
    'xbap',
    'xbd',
    'xbm',
    'xdm',
    'xdp',
    'xdssc',
    'xdw',
    'xenc',
    'xer',
    'xfdf',
    'xfdl',
    'xif',
    'xo',
    'xop',
    'xpi',
    'xpm',
    'xpr',
    'xps',
    'xpw',
    'xslt',
    'xsm',
    'xspf',
    'xul',
    'xwd',
    'xyz',
    'yang',
    'yin',
    'zaz'
    'zip',
    'zip',
    'zir',
    'zmm',
)

def extern(url):

    for x in skip:
        if url.endswith("." + x):
            print ("skip",url)
            return
        
    if url  in c.extern.data:
        print ("exists",url)
        return
    
    print ("loading link",url)

    try:
        resp = requests.head(url, timeout=1)
        head = {
            'code': resp.status_code,
            'text' : resp.text,
            'hdrs' :  resp.headers
        };

    except Exception as e:
        pprint.pprint(e)
        c.extern.add(url,
                     {
                         'data': None,
                         'url': url,
                         #'head' : head,
                         'error' : str(e),
                     })
        return None
    
    clen = 0
    tlen = 0
    if  'Content-Length' in resp.headers:
        tlen = resp.headers['Content-Length']
        g = re.match('(\d+)', tlen)
        clen = 0
        if  g:
            tp = g.groups()[0]
            print(tp, tlen)
            clen = int(tp)        

    print("getting size", url, clen, tlen)
          #, pprint.pformat(resp.headers))
        

    try:
        html = requests.get(url, timeout=1,verify=False, stream=True).text
        head = {
            'code': resp.status_code,
            'text' : resp.text,
            'hdrs' :  resp.headers
        };
        # truncat
        if len(html) <  20000:
            print ("Truncating html",len(html), url)
            html = None
            
        c.extern.add(url,
                     {
                         'data':html,
                         'url': url,
                         'head' : head
                     })
        

    except Exception as e:
        pprint.pprint(e)
        c.extern.add(url,
                     {
                         'data': None,
                         'url': url,
                         #'head' : head,
                         'error' : str(e),
                     } )
        return

pool = Pool(processes=20)

c = funcs.Context()
cname = 'Category:'
name = 'Open content'
seen = {
    # dont care about open access right now
    'Category:Creative Commons-licensed journals':1,
    'Category:Android (operating system) games':1,
    'Category:Android (operating system) software' :1,
    'Category:Articles with imported Creative Commons Attribution 2.5 text':1,
    'Category:Articles with imported Creative Commons Attribution 3.0 text' :1,
    'Category:Citizen media' : 1,
    'Category:Debian people' :1 ,
    'Category:Firefox OS software' :1,
    'Category:Free software companies' : 1,
    'Category:Free software people': 1,
    'Category:FreeBSD people': 1,
    'Category:FreeDOS people': 1,
    'Category:GNOME companies' :1,
    'Category:GNU people':1,
    'Category:Inferno (operating system) people' : 1,
    'Category:Linux companies': 1,
    'Category:Linux people': 1,
    'Category:Linux software' : 1,  # dont process this because it is full of non free software
    'Category:Mozilla people' : 1,
    'Category:NetBSD people': 1,
    'Category:Netscape people': 1,
    'Category:Open access (publishing)' :1,
    'Category:Open content activists':1,
    'Category:Open hardware organizations and companies': 1,
    'Category:Open source people': 1,
    'Category:OpenBSD people' : 1,
    'Category:People associated with Bitcoin': 1,
    'Category:Perl people': 1,
    'Category:Plan 9 people': 1,
    'Category:Public commons' : 1,
    'Category:Public domain books' :1,
    'Category:Public domain music' :1,
    'Category:Red Hat people': 1,
    'Category:Single-board computers':1,
    'Category:Ubuntu (operating system) people' :1,
    'Category:WikiProject Open Access articles':1, # tons of articles, not relevant
    'Category:WikiProject Open Access' :1,
    'Category:Wikimedia Foundation people': 1,
    'Category:Wikipedia people':1,
    'Category:X Window System people': 1,
    'Category:X Window programs':1,
}

def  catpage(data, n, p):
    #pprint.pprint(data)
    #print( "cat",data['title'])
    #pprint.pprint(data.keys())
    pass




                

def page(data, n, p ):
    #print( "page",n,p ) 
    todo = []
    
    for l in data['links']:
        if 'http' in l:
            if l not in links :
                links[l]=1
                todo.append(l)
                
    for l in data['references']:
        if 'http' in l:
            if l not in links :
                links[l]=1
                todo.append(l)

    pool.apply_async(extern, todo)   


def recurse(n, p):
    if n not in seen:
        seen[n]=1
    else:
        return

    #print("Process:", n, p)
    if n not in c.pages.pages.data:
        print("TODO1 add :", n, p)      
        c.pages.get(n)
        pass
    else:
        data = c.pages.pages.data[n]
        catpage(data, n, p )
                    
    if n not in c.cats.data:
        print("Missing cat", n)
        exit(0)
    else:
        s = c.cats.data[n]
        subcats = s['subcats']
        if subcats:
            for sc in subcats:
                p2 = list(p)
                p2.append(n)
                recurse(sc, p2)

        pages = s['pages']
        if pages:
            for pg in pages:
                p2 = list(p)
                p2.append(n)
                if pg not in c.pages.pages.data:
                    if pg not in c.redirs.data:
                        print("TODO2", pg, p, n)
                        c.pages.get(pg)
                    else:
                        pg = c.redirs.data[pg]['to']
                        if pg not in c.pages.pages.data:
                            print("TODO3", pg, p, n)
                            c.pages.get(pg)
                        else:
                            data = c.pages.pages.data[pg]
                            page(data, pg, p)
                else:
                    data = c.pages.pages.data[pg]
                    page(data, pg, p)
        # pages
    
#Category:Open Content and all subcats.
recurse(cname + name,[])
pool.close()

print ("waiting")
pool.join()
