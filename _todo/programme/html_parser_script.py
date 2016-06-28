# coding: cp1252
"""recherche de mot-clés dans des pages HTML, 
ce programme ne peut lire pour l'instant que le format HTML 2.0
et pas HTML 4.01, format utilisé par la plupart des sites."""

import HTMLParser       # parcourir un fichier HTML
import re
import markupbase

starttagopen = re.compile('<[a-zA-Z]')

attrfind = re.compile(
    r'\s*([a-zA-Z_][-.:a-zA-Z_0-9]*)(\s*=\s*'
    r'(\"[a-z]+\"#[a-zA-Z.  ]+[.][a-zA-Z]+|\"[0-9]+\"\"|\'[^\']*\'|"[^"]*"'\
     '|([a-zA-Z_:.]+\s*\([0-9/a-zA-Z\"\',.  &;éèàùûâêîô\-_\?:!=@]*\))'\
     '(;void\(0\);)?|\"\"|[-a-zA-Z0-9./,:;+*%?!&$\(\)_#=~]*))?')

# si locatestarttagend est modifié, il faut penser à modifier
# également attrfind
locatestarttagend = re.compile(r"""
  <[a-zA-Z][-.a-zA-Z0-9:_]*          # tag name
  (?:\s+                             # whitespace before attribute name
    (?:[a-zA-Z_][-.:a-zA-Z0-9_]*     # attribute name
      (?:\s*=\s*                     # value indicator
        (?:([a-zA-Z_:.]+\s*\([0-9/a-zA-Z\"',.  &;éèàùûâêîô\-_\?:!=@]*\))(;void\(0\);)? #                
          |\"[0-9]+\"\"              # colspan = "2""
          |\"[a-z]+\"\#[a-zA-Z.  ]+[.][a-zA-Z]+   # "rect"#Le Monde.fr
          |\"\"                      # alt = ""
          |\"[^\"]*\"                # LIT-enclosed value
          |'[^']*'                   # # LITA-enclosed value
          |[^'\">\s]+                # bare value
         )
       )?
     )
   )*
  \s*                                # trailing whitespace
""", re.VERBOSE)

entityref = re.compile('&([a-zA-Z][-.a-zA-Z0-9]*)[^a-zA-Z0-9]')
charref = re.compile('&#@(?:[0-9]+|[xX][0-9a-fA-F]+)[^0-9a-fA-F]')
incomplete = re.compile('&[a-zA-Z#]')

commentclose = re.compile(r'--\s*>|/\s*>|-- /\s*>|-\s*>')


class HTMLParserScript (HTMLParser.HTMLParser) :
    
    def parse_comment(self, i, report=1):
        rawdata = self.rawdata
        #assert rawdata[i:i+4] == '<!--', 'unexpected call to parse_comment()'
        match = commentclose.search(rawdata, i+4)
        if not match:
            print "-------------------------------------------------------"
            print rawdata[i:i+250]
            print "-------------------------------------------------------"
            print end
            print "-------------------------------------------------------"
            return -1
        if report:
            j = match.start()
            self.handle_comment(rawdata[i+4: j])
        j = match.end()
        return j
        
    def _scan_name(self, i, declstartpos):
        rawdata = self.rawdata
        n = len(rawdata)
        if i == n:
            return None, -1
        m = markupbase._declname_match(rawdata, i)
        if m:
            s = m.group()
            name = s.strip()
            if (i + len(s)) == n:
                return None, -1  # end of buffer
            return name.lower(), m.end()
        else:
            self.updatepos(declstartpos, i)
            print "-------------------------------------------------------"
            print rawdata[i:i+250]
            print "-------------------------------------------------------"
            print end
            print "-------------------------------------------------------"
            self.error("expected name token")
            
    def parse_starttag(self, i):
        self.__starttag_text = None
        endpos = self.check_for_whole_start_tag(i)
        if endpos < 0:
            return endpos
        rawdata = self.rawdata
        self.__starttag_text = rawdata[i:endpos]

        # Now parse the data between i+1 and j into a tag and attrs
        attrs = []
        match = HTMLParser.tagfind.match(rawdata, i+1)
        assert match, 'unexpected call to parse_starttag()'
        k = match.end()
        self.lasttag = tag = rawdata[i+1:k].lower()

        while k < endpos:
            m = attrfind.match(rawdata, k)
            if not m:
                break
            attrname, rest, attrvalue = m.group(1, 2, 3)
            if not rest:
                attrvalue = None
            elif attrvalue[:1] == '\'' == attrvalue[-1:] or \
                 attrvalue[:1] == '"' == attrvalue[-1:]:
                attrvalue = attrvalue[1:-1]
                attrvalue = self.unescape(attrvalue)
            attrs.append((attrname.lower(), attrvalue))
            k = m.end()

        end = rawdata[k:endpos].strip()
        if end not in (">", "/>"):
            lineno, offset = self.getpos()
            if "\n" in self.__starttag_text:
                lineno = lineno + self.__starttag_text.count("\n")
                offset = len(self.__starttag_text) \
                         - self.__starttag_text.rfind("\n")
            else:
                offset = offset + len(self.__starttag_text)
            print "-------------------------------------------------------"
            print rawdata[i:i+250]
            print "-------------------------------------------------------"
            print end
            print "-------------------------------------------------------"
            self.error("junk characters in start tag: %s"
                       % `rawdata[k:endpos][:20]`)
        if end.endswith('/>'):
            # XHTML-style empty tag: <span attr="value" />
            self.handle_startendtag(tag, attrs)
        else:
            self.handle_starttag(tag, attrs)
            if tag in self.CDATA_CONTENT_ELEMENTS:
                self.set_cdata_mode()
        return endpos
        
    def check_for_whole_start_tag(self, i):
        rawdata = self.rawdata
        m = locatestarttagend.match(rawdata, i)
        if m:
            j = m.end()
            next = rawdata[j:j+1]
            if next == ">":
                return j + 1
            if next == "/":
                if rawdata.startswith("/>", j):
                    return j + 2
                if rawdata.startswith("/", j):
                    # buffer boundary
                    return -1
                # else bogus input
                self.updatepos(i, j + 1)
                self.error("malformed empty start tag")
            if next == "":
                # end of input
                return -1
            if next in ("abcdefghijklmnopqrstuvwxyz=/"
                        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
                # end of input in or before attribute value, or we have the
                # '/' from a '/>' ending
                return -1
            #if next in "'" :
            #    return -1
            print "------------------------------------"
            print next
            print m.groups ()
            print "------------------------------------"
            print rawdata [i: i + 250]
            print "...................................."
            print rawdata [j: j + 30]
            self.updatepos(i, j)
            self.error("malformed start tag")
        raise AssertionError("we should not get here!")
        
    def goahead(self, end):
        if not self.__dict__.has_key ("_script") :
            self._script    = False         # ajout
            self._nb_script = 0             # ajout
        rawdata = self.rawdata
        i = 0
        n = len(rawdata)
        while i < n:
            match = self.interesting.search(rawdata, i) # < or &
            if match:
                j = match.start()
            else:
                j = n
            if i < j: self.handle_data(rawdata[i:j])
            i = self.updatepos(i, j)
            if i == n: break
            startswith = rawdata.startswith

            if self._script :                           # ajout
                if startswith('</script>', i):          # ajout
                    k = i + len ('</script>')           # ajout
                    self._script = False                # ajout
                    i = self.updatepos(i, k)
                elif startswith('</SCRIPT>', i):       # ajout
                    k = i + len ('</SCRIPT>')           # ajout
                    self._script = False                # ajout
                    i = self.updatepos(i, k)
                else:
                    k = i + 1
                    i = self.updatepos(i, k)
            elif startswith('<', i):
                if startswith("<script", i):
                    self._nb_script += 1
                    k = i + len ("<script")
                    self._script = True
                elif startswith("<SCRIPT", i):
                    self._nb_script += 1
                    k = i + len ("<SCRIPT")
                    self._script = True
                elif starttagopen.match(rawdata, i): # < + letter
                    k = self.parse_starttag(i)
                elif startswith("</", i):
                    k = self.parse_endtag(i)
                elif startswith("<!--", i):
                    k = self.parse_comment(i)
                elif startswith("<!-", i):
                    k = self.parse_comment(i)
                elif startswith("<!/", i):
                    k = self.parse_comment(i)
                elif startswith("<!-- /", i):
                    k = self.parse_comment(i)
                elif startswith("<?", i):
                    k = self.parse_pi(i)
                elif startswith("<!", i):
                    k = self.parse_declaration(i)
                elif (i + 1) < n:
                    self.handle_data("<")
                    k = i + 1
                else:
                    break
                if k < 0:
                    if end:
                        print "######################################### (1)"
                        print rawdata [i:i+250]
                        self.error("EOF in middle of construct")
                    break
                i = self.updatepos(i, k)
            elif startswith("&#", i):
                match = charref.match(rawdata, i)
                if match:
                    name = match.group()[2:-1]
                    self.handle_charref(name)
                    k = match.end()
                    if not startswith(';', k-1):
                        k = k - 1
                    i = self.updatepos(i, k)
                    continue
                else:
                    break
            elif startswith('&', i):
                match = entityref.match(rawdata, i)
                if match:
                    name = match.group(1)
                    self.handle_entityref(name)
                    k = match.end()
                    if not startswith(';', k-1):
                        k = k - 1
                    i = self.updatepos(i, k)
                    continue
                match = incomplete.match(rawdata, i)
                if match:
                    # match.group() will contain at least 2 chars
                    if end and match.group() == rawdata[i:]:
                        print "######################################### (2)"
                        print rawdata [i:i+250]
                        self.error("EOF in middle of entity or char ref")
                    # incomplete
                    break
                elif (i + 1) < n:
                    # not the end of the buffer, and can't be confused
                    # with some other construct
                    self.handle_data("&")
                    i = self.updatepos(i, i + 1)
                else:
                    break
            else:
                assert 0, "interesting.search() lied"
        # end while
        if end and i < n:
            self.handle_data(rawdata[i:n])
            i = self.updatepos(i, n)
        self.rawdata = rawdata[i:]
