if (navigator && navigator.platform) {
    var sasIsIosUiwebview = false;
    if (navigator.platform.substr(0,2) === 'iP') {
      var lte9 = /constructor/i.test(window.HTMLElement);
      var nav = window.navigator, ua = nav.userAgent, idb = !!window.indexedDB;
      if (ua.indexOf('Safari') !== -1 && ua.indexOf('Version') !== -1 && !nav.standalone) {      
        sasIsIosUiwebview = false;
      } else if ((!idb && lte9) || !window.statusbar.visible) {
        sasIsIosUiwebview = true;
      } else if ((window.webkit && window.webkit.messageHandlers) || !lte9 || idb) {
        sasIsIosUiwebview = true;
      }
    }
    if (!sasIsIosUiwebview) {
        var smartCsync=document.createElement('IFRAME');smartCsync.src='//csync.smartadserver.com/rtb/csync/CookieSync.html?nwid=104&dcid=3&gdpr=1&gdprc=BOo9tNnOqqLbNAKAbBENCw-AAAAsxr_7__7-_9_-_f__9uj3Or_v_f__30ccL59v_B_zv-_7fi_20jV4u_1vft9yfk1-5ctDztp505iakivHmqdeb9v_mz3_5pxP78k89r7337Ew_v8_v8b7BCKNgA';
        smartCsync.scrolling = 'no';smartCsync.frameBorder = 0;smartCsync.width = 0;smartCsync.height = 0;smartCsync.style.margin = 0;smartCsync.style.padding = 0;smartCsync.style.display = 'none';smartCsync.style.width = '0px';smartCsync.style.height = '0px';smartCsync.style.visibility = 'hidden';
        if(document.body != null)document.body.appendChild(smartCsync);
    }
}/*_hs_*/;var sas = sas || {};
if(sas && sas.events && sas.events.fire && typeof sas.events.fire === "function" )
        sas.events.fire("ad", { tagId: "sas_1391", formatId: 1391 }, "sas_1391");;/*_hs_*/var sas=sas||{};sas.utils=sas.utils||{},sas.events=sas.events||{},sas.rev=sas.rev||20110214,function(){sas.utils.cdns?(sas.utils.cdns["http:"]&&0!=sas.utils.cdns["http:"].length||(sas.utils.cdns["http:"]="http://ak-ns.sascdn.com"),sas.utils.cdns["https:"]&&0!=sas.utils.cdns["https:"].length||(sas.utils.cdns["https:"]="https://ec-ns.sascdn.com")):sas.utils.cdns={"http:":"http://ak-ns.sascdn.com","https:":"https://ec-ns.sascdn.com"};var t=function(){};sas.utils.getIEVersion=function(){var t=navigator.userAgent.match(/(?:MSIE |Trident\/.*; rv:)(\d+)/);return t?parseInt(t[1]):void 0},sas.events.addEvent=function(t,s,a){if(t&&s&&a)return t.attachEvent?t.attachEvent("on"+s,a):t.addEventListener&&t.addEventListener(s,a,!1),{removeEvent:function(){t.detachEvent?t.detachEvent("on"+s,a):t.removeEventListener&&t.removeEventListener(s,a,!1)}}},sas.events.addLoadEvent=function(t,s){if(t&&s){var a="load",n=function(){return!0};(sas.utils.getIEVersion()<11||t==document)&&(a="readystatechange",n=function(){if(!t.readyState||"complete"==t.readyState||"loaded"==t.readyState||4==t.readyState)return!0});var e=sas.events.addEvent(t,a,function(){n()&&(e.removeEvent(),s.apply(this,arguments))})}},sas.utils.Latch=function(t){for(var s=[],a={},n=t=t||[],e=!1,i=0;i<n.length;i++)a[t[i]]={};var l=function(){if(!e){for(var t in a)if(!a[t].status)return;e=!0;for(var n=c(),i=0;i<s.length;i++)s[i].apply(this,n)}},c=function(){for(var t=[],s=0;s<n.length;s++)t.push(a[n[s]].result);return t};this.notify=function(t,s){a[t]&&(a[t].status=!0,a[t].result=s,l())},this.addListener=function(t){null!=t&&(e?t():s.push(t))},l()},sas.utils._libs=sas.utils._libs||{};var s=function(t){"string"==typeof t&&(t=[t]);for(var s,a,n="https:"==document.location.protocol||"about:"==document.location.protocol?sas.utils.cdns["https:"]:sas.utils.cdns[document.location.protocol]||sas.utils.cdns["http:"],e=0;e<t.length;e++)t[e]=(s=n,a=t[e],"/"==s.charAt(s.length-1)&&(s=s.slice(0,-1)),"/"==a.charAt(0)&&(a=a.slice(1)),s+"/"+a);return t};sas.utils.loadLinkCdn=function(t){t=s(t);for(var a=0;a<t.length;a++)e(t[a],!0)},sas.utils.loadScriptCdn=function(t,a){t=s(t),sas.utils.loadScript(t,a)};var a=Math.floor(1e6*Math.random()),n=1;sas.utils._callbacks=sas.utils._callbacks||{};var e=function(t,s,e,i){var l,c=(s?"link":"script")+"-"+a+"-"+n++,r=document.createElement(s?"link":"script");r.id=c,r.setAttribute("type",s?"text/css":"text/javascript"),r.setAttribute(s?"href":"src",t),s&&r.setAttribute("rel","stylesheet"),!s&&e&&r.setAttribute("async","true"),sas.utils._libs[t]={loaded:!1,callbacks:[]},null!=i&&sas.utils._libs[t].callbacks.push(i),sas.utils._callbacks[c]=(l=t,function(){sas.utils._libs[l].loaded=!0;for(var t=0;t<sas.utils._libs[l].callbacks.length;t++)sas.utils._libs[l].callbacks[t]()}),s||e?(document.getElementsByTagName("head")[0].appendChild(r),sas.events.addLoadEvent(document.getElementById(c),sas.utils._callbacks[c])):(document.write(r.outerHTML),document.write("<script type='text/javascript'>(function() { sas.utils._callbacks['"+c+"'](); })();<\/script>"))};sas.utils.loadScript=function(s,a){(a=a||{}).async=null==a.async||a.async;var n=a.onLoad||t;"string"==typeof s&&(s=[s]);var i=new sas.utils.Latch(s);i.addListener(n);for(var l=0;l<s.length;l++){var c=s[l],r=function(t){return function(){i.notify(t)}}(c);sas.utils._libs[c]?sas.utils._libs[c].loaded?i.notify(c):sas.utils._libs[c].callbacks.push(r):e(c,!1,a.async,r)}}}();

(function () {
    var config = {
        insertionId: Number(9133348),
        pageId: "708231",
        sessionId: new Date().getTime(),
        baseUrl: String("https://www.smartadserver.com"),
        formatId: Number(1391),
        tagId: String("sas_1391"),
        oba: Number(0),
        isAsync: window.sas_ajax || false,
        customScript: String(''),
        creative: {
            id: Number(24705159),
            url: String(''),
            type: Number(0),
            width: Number(('0' === '100%') ? 0 : '0'),
            height: Number(('0' === '100%') ? 0 : '0'),
            alt: String(''),
            clickUrl: String('https://www.smartadserver.com/click?imgid=24705159&insid=9133348&pgid=708231&ckid=9058983589001757824&uii=235697771422899336&acd=1574949891717&pubid=8&tmstp=4186368031&tgt=%24dt%3d1t%3b%24dt%3d1t%3b%24hc&systgt=%24qc%3d1312468581%3b%24ql%3dUnknown%3b%24qpc%3d75013%3b%24qt%3d184_1903_42652t%3b%24dma%3d0%3b%24b%3d12680%3b%24o%3d99999%3b%24sw%3d1280%3b%24sh%3d768%3b%24wpc%3d20%3b%24wpc%3d165%3b%24wpc%3d79&envtype=0&imptype=0&pgDomain=https%3a%2f%2fkorben.info%2f&go='),
            clickUrlArray: ["https://www.smartadserver.com/click?imgid=24705159&insid=9133348&pgid=708231&ckid=9058983589001757824&uii=235697771422899336&acd=1574949891717&pubid=8&tmstp=4186368031&tgt=%24dt%3d1t%3b%24dt%3d1t%3b%24hc&systgt=%24qc%3d1312468581%3b%24ql%3dUnknown%3b%24qpc%3d75013%3b%24qt%3d184_1903_42652t%3b%24dma%3d0%3b%24b%3d12680%3b%24o%3d99999%3b%24sw%3d1280%3b%24sh%3d768%3b%24wpc%3d20%3b%24wpc%3d165%3b%24wpc%3d79&envtype=0&imptype=0&pgDomain=https%3a%2f%2fkorben.info%2f&go="],
            oryginalClickUrl: String(''),
            clickTarget: String('_blank'),
            agencyCode: String('<scr'+'ipt type="application/javascript">\r\n'+'function cgSkin(background,clic,color,height){\r\n'+'cgAnchor=top.document.getElementsByClassName(\'app-main\')[0].getElementsByTagName(\'article\')[0];\r\n'+'if(!cgAnchor.getElementsByClassName(\'entry-format\')[0]){\r\n'+'cgClassName=cgAnchor.className.split(\' \')[0];\r\n'+'cgSkinCSS=\'.\'+cgClassName+\'{background-image:url("\'+background+\'")!important;background-repeat:no-repeat!important;background-attachment:scroll!important;background-position:center 352px!important;background-size:contain!important;} .\'+cgClassName+\' .entry-container{margin-top:\'+height+\'px!important;} .\'+cgClassName+\' .entry-thumbnail{margin-bottom:0px!important;} .\'+cgClassName+\',.\'+cgClassName+\' .entry-thumbnail,.\'+cgClassName+\' .text-center,.\'+cgClassName+\' .entry-container,.\'+cgClassName+\' .entry-footer,.\'+cgClassName+\' .comments,#comments{position:relative!important;z-index:2;} #sas_1391, #sas_1391 > iframe {display:none;}\';\r\n'+'(function(a,b,c,d){var f=document.createElement(b);f.type=c;if(f.styleSheet)f.styleSheet.cssText=d;else f.appendChild(document.createTextNode(d));a.parentNode.appendChild(f)}(top.document.getElementsByTagName(\'script\')[0],\'style\',\'text/css\',cgSkinCSS));\r\n'+'(function(a,b,c){var d=document.createElement(b);d.id=c;d.style.position=\'absolute\';d.style.height=\'100%\';d.style.width=\'100%\';d.style.top=0;d.style.left=0;d.style.zIndex=1;d.style.cursor=\'pointer\';d.onclick=function(){window.open(\'https://www.smartadserver.com/diffx/countgo?9133348;708231;9058983589001757824;4186368031;S;target=%24dt%3d1t%3b%24dt%3d1t;systemtarget=%24qc%3d1312468581%3b%24ql%3dUnknown%3b%24qpc%3d75013%3b%24qt%3d184_1903_42652t%3b%24dma%3d0%3b%24b%3d12680%3b%24o%3d99999%3b%24sw%3d1280%3b%24sh%3d768%3b%24wpc%3d20%3b%24wpc%3d165%3b%24wpc%3d79;envtype=0;imptype=0;24705159;URL=\'+clic);};a.insertBefore(d,a.firstChild)}(cgAnchor,\'a\',\'cg_skin\'));}}\r\n'+'try{cgSkin(\'//do69ll745l27z.cloudfront.net/Gameforge/KUF2/2019-11-13_KUF2_MKT_1140.jpg\',\'https://join.kingdomunderfire2.gameforge.com/fr_FR/landing/packages?kid=a-a9k08-88408-1911-e660006e&utm_source=cultureg&utm_medium=paid&utm_campaign=kuf_fr-fr_11-2019_launch_ua&utm_content=branding&gfsid=korben.info\',\'#000000\',185)}catch(e){}\r\n'+'</scr'+'ipt>'),
            creativeCountPixelUrl: String('https://www.smartadserver.com/h/aip?tmstp=4186368031&ckid=9058983589001757824&pubid=8&systgt=%24qc%3d1312468581%3b%24ql%3dUnknown%3b%24qpc%3d75013%3b%24qt%3d184_1903_42652t%3b%24dma%3d0%3b%24b%3d12680%3b%24o%3d99999%3b%24sw%3d1280%3b%24sh%3d768%3b%24wpc%3d20%3b%24wpc%3d165%3b%24wpc%3d79&uii=235697771422899336&acd=1574949891717&envtype=0&visit=S&statid=6&tgt=%24dt%3d1t%3b%24dt%3d1t%3b%24hc&imptype=0&pgDomain=https%3a%2f%2fkorben.info%2f&capp=1&mcrdbt=1&insid=9133348&siteid=120606&imgid=24705159&pgid=708231&fmtid=1391'),
            creativeClickCountPixelUrl: (24705159 ? 'https://www.smartadserver.com/h/cp?imgid=24705159&insid=9133348&pgid=708231&ckid=9058983589001757824&uii=235697771422899336&acd=1574949891717&pubid=8&tmstp=4186368031&tgt=%24dt%3d1t%3b%24dt%3d1t%3b%24hc&systgt=%24qc%3d1312468581%3b%24ql%3dUnknown%3b%24qpc%3d75013%3b%24qt%3d184_1903_42652t%3b%24dma%3d0%3b%24b%3d12680%3b%24o%3d99999%3b%24sw%3d1280%3b%24sh%3d768%3b%24wpc%3d20%3b%24wpc%3d165%3b%24wpc%3d79&envtype=0&imptype=0&pgDomain=https%3a%2f%2fkorben.info%2f' : 'https://www.smartadserver.com/h/micp?imgid=0&insid=9133348&pgid=708231&ckid=9058983589001757824&uii=235697771422899336&acd=1574949891717&pubid=8&tmstp=4186368031&tgt=%24dt%3d1t%3b%24dt%3d1t%3b%24hc&systgt=%24qc%3d1312468581%3b%24ql%3dUnknown%3b%24qpc%3d75013%3b%24qt%3d184_1903_42652t%3b%24dma%3d0%3b%24b%3d12680%3b%24o%3d99999%3b%24sw%3d1280%3b%24sh%3d768%3b%24wpc%3d20%3b%24wpc%3d165%3b%24wpc%3d79&envtype=0&imptype=0&pgDomain=https%3a%2f%2fkorben.info%2f') + '&rtb=1&rtbbid=&rtbet=&rtblt=&rtbnid=&rtbh=',
        },
        statisticTracking: {
            rtbbid: String(''),
            rtbet: String(''),
            rtblt: String(''),
            rtbnid: String(''),
            rtbh: String('')
        }
    };

    if (!document.getElementById("sas_1391")) {
        document.write('<div id="sas_1391"><div style="display:none"></div></div>');
    } else {
        var el = document.createElement('div');
        el.style.display = 'none';
        document.getElementById('sas_1391').appendChild(el);
    }

    var sas = window.sas;
    sas.utils.cdns["http:"] = "http://ced-ns.sascdn.com";
    sas.utils.cdns["https:"] = "https://ced-ns.sascdn.com";
    //sas.utils.cdns["http:"] = "http://demo.smartadserver.com";

    sas.utils.loadScriptCdn("/diff/templates/ts/dist/banner/sas-banner-1.2.js", {
        async: config.isAsync, onLoad: function () {
            newObj9133348 = new Banner(config);
            newObj9133348.init();
        }
    });
})();