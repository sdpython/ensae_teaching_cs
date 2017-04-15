/*
 Javascript animated menu
  Copyright (c), Jean-Damien POGOLOTTI
  see http://www.sunyday.net/article-Menu-anime-en-javascript.html for help

 function AttachEvent(obj,evt,fnc,useCapture)
  Copyright (c), Gavin Kistner (gavin@refinery.com)
*/

 var millisec = 500; 
 var Speed    = Math.round(millisec / 100);
 DivsStatus   = new Array();
 DivCount     = 0;
 TimerID      = -1;

 function pInit()
  {
   // Parse the DIVs to register them & add events callbacks
   Divs = document.getElementsByTagName("div");
   for (i = 0; i < Divs.length; i++)
    {
     className = Divs[i].className;
     if ( className == "pMenu" )
      {
       DivID     = Divs[i].id;
       DivObject = document.getElementById(DivID);

       AttachEvent(DivObject,"mouseover",pMouseOver,false);
       AttachEvent(DivObject,"mouseout",pMouseOut,false);

       DivsStatus[DivCount]    = new Array(3);
       DivsStatus[DivCount][0] = DivID;
       DivsStatus[DivCount][1] = 0;
       DivsStatus[DivCount][2] = 0;
       DivCount++;
      }
    }
  }

 // Event handler for MouseOver events
 function pMouseOver(e)
  {
   DivID = GetEventSource(e);
   if ( GetDivAnimationStatus(DivID) == 0 )
    {
     SetDivAnimationStatus(DivID,1)
     ValidateTimer();
    }
  }

 // Event handler for MouseOut events
 function pMouseOut(e)
  {
   DivID = GetEventSource(e);
   if ( GetDivAnimationStatus(DivID) == 1 || GetDivAnimationStatus(DivID) == 2 )
    {
     SetDivAnimationStatus(DivID,3)
     ValidateTimer();
    }
  }

 // Perform the animation & kill the timer when all DIVs are idle
 function IndentDivContent()
  {
   ProcessEnded = true;

   for (i = 0; i < DivsStatus.length; i++)
    {
     DivID     = DivsStatus[i][0];
     DivObject = document.getElementById(DivID);

     if ( DivsStatus[i][1] == 1 )
      {
       DivsStatus[i][2] = DivsStatus[i][2] + 1;
       TextHColor = (DivsStatus[i][2]+5).toString(16);
       TextColor = "#" + TextHColor + "1" + TextHColor + "9" + TextHColor + "C";

       DivObject.style.color        = TextColor;
       DivObject.style.marginLeft  = DivsStatus[i][2];
       DivObject.style.marginRight = 10 - DivsStatus[i][2];

       if ( DivsStatus[i][2] == 10 ) { DivsStatus[i][1] = 2; } else { ProcessEnded = false; }
      }

     if ( DivsStatus[i][1] == 3 )
      {
       DivsStatus[i][2] = DivsStatus[i][2] - 1;
       TextHColor = (DivsStatus[i][2]+5).toString(16);
       TextColor = "#" + TextHColor + "1" + TextHColor + "9" + TextHColor + "C";

       DivObject.style.color        = TextColor;
       DivObject.style.marginLeft  = DivsStatus[i][2];
       DivObject.style.marginRight = 10 - DivsStatus[i][2];

       if ( DivsStatus[i][2] <= 0 ) { DivsStatus[i][1] = 0; DivsStatus[i][2] = 0; } else { ProcessEnded = false; }
      }
    }

   if ( ProcessEnded )
    { clearInterval(TimerID); TimerID = -1; }
  }

 // Retrieve a DIV animation status
 function GetDivAnimationStatus(DivID)
  {
   for (i = 0; i < DivsStatus.length; i++)
    {
     if ( DivsStatus[i][0] == DivID )
      return(DivsStatus[i][1]);
    }
  }

 // Change a DIV animation status
 function SetDivAnimationStatus(DivID,Status)
  {
   for (i = 0; i < DivsStatus.length; i++)
    {
     if ( DivsStatus[i][0] == DivID )
      {
       DivsStatus[i][1] = Status;
       return(0);
      }
    }
  }

 // Is the timer already started ?
 function ValidateTimer()
  {
   if ( TimerID == -1 )
   TimerID = setInterval("IndentDivContent();",1);
  }

 // Cross browser event source retriever
 function GetEventSource(e)
  {
   if (e.srcElement)
    return(e.srcElement.id);
   else
    return(e.target.id);
  }

 // Cross browser event attacher comming from http://phrogz.net/JS/AttachEvent_js.txt
 function AttachEvent(obj,evt,fnc,useCapture)
  {
   if (!useCapture) useCapture=false;
   if (obj.addEventListener)
    {
     obj.addEventListener(evt,fnc,useCapture);
     return true;
    }
   else if (obj.attachEvent)
    return obj.attachEvent("on"+evt,fnc);
   else
    {
     MyAttachEvent(obj,evt,fnc);
     obj['on'+evt]=function(){ MyFireEvent(obj,evt) };
    }
  }
  
function html_entity_decode(texte) {
    texte = unescape (texte) ;
    return texte ;
}
  
function extractUrlParams(){	
	var t = location.search.substring(1).split('&');
	var f = [];
	for (var i=0; i<t.length; i++){
		var x = t[ i ].split('=');
		f[x[0]]=html_entity_decode (x[1]);
	}
	return f;
}

function nodeName( elem, name ) 
{
    return elem.nodeName && elem.nodeName.toUpperCase() === name.toUpperCase();
}

function evalScript( elem ) 
{
    data = ( elem.text || elem.textContent || elem.innerHTML || "" );

    var head = document.getElementsByTagName("head")[0] || 
                  document.documentElement ;
    var script = document.createElement("script");
    script.type = "text/javascript";
    
   try {
      // doesn't work on ie...
      script.appendChild(document.createTextNode(data));      
    } catch(e) {
      // IE has funky script nodes
      script.text = data;
    }
    
    head.insertBefore( script, head.firstChild );
    head.removeChild( script );

    if ( elem.parentNode ) {
        elem.parentNode.removeChild( elem );
    }
}

function processEventText(pageElement, linkurl, titleElement, keywordsElement, body)
{
    var bodyp = body.indexOf("<body>");
    var bodype = body.lastIndexOf("</body>")+7;
    var page = body.substring(bodyp, bodype);
    var titp = body.indexOf("<title>")+7;
    var titpe = body.indexOf("</title>");
    var title = body.substring(titp, titpe);
    if ((linkurl != "") && (keywordsElement == null) && 
        (page.indexOf("<!-- CUT PAGE HERE -->") > 0))
    {
        var temp = page.split("<!-- CUT PAGE HERE -->") ;
        page = temp[0] + "<br /><p><a href=\"" + linkurl + "\"><i>more...</i></a></p></body></html>" ;
    }
    pageElement.innerHTML = page ;
    titleElement.innerHTML += " <b>" + title +"</b>";
    if (keywordsElement != null)
    {
        var keywords = getKeywords(body) ;
        keywordsElement.innerHTML = keywords ;
    }
    
    // on execute les scripts de la page
    var scripts = [];

    ret = pageElement.childNodes;
    for ( var i = 0; ret[i]; i++ ) {
      if ( scripts && nodeName( ret[i], "script" ) && 
          (!ret[i].type || ret[i].type.toLowerCase() === "text/javascript") ) 
        {
            scripts.push( ret[i].parentNode ? ret[i].parentNode.removeChild( ret[i] )
                               : ret[i] );
        }
    }

    for(script in scripts)
    {
      evalScript(scripts[script]);
    }    
}
  
function loadDoc(urlPage, linkurl, pageElement, titleElement, keywordsElement)
{
    var xmlhttp = null; 
    if (window.XMLHttpRequest)
    {// code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp=new XMLHttpRequest();
    }
    else
    {// code for IE6, IE5
        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange=function()
    {
        if (xmlhttp.readyState==4 && xmlhttp.status==200)
        {
            processEventText(pageElement, linkurl, titleElement, keywordsElement, xmlhttp.responseText) ;
        }
    }
    xmlhttp.open("GET",urlPage,true);
    xmlhttp.send(null);
}

function getKeywords (text)
{
    // one way of the other
    var patt=new RegExp('<meta +content=\\"(.*?)\\" +name=\\"keywords\\"/>','i');
    var keywords = patt.exec(text) ;
    return keywords[1] ;
}
    
