const addScript=(path,callback)=>{const scriptElement=document.createElement('script')
scriptElement.src=path
scriptElement.async=true
document.head.appendChild(scriptElement)
scriptElement.onload=()=>{callback()}}
const addStyle=(url)=>{const styleElement=document.createElement('link')
styleElement.rel='stylesheet'
styleElement.type='text/css'
styleElement.href=url
document.getElementsByTagName('head')[0].appendChild(styleElement)}
const updateCode=(btnElement,code)=>{if(btnElement.classList.contains('btn--red')){return}else{const redBtnElement=document.querySelector('.btn--red')
if(redBtnElement){redBtnElement.classList.remove('btn--red')}
btnElement.classList.add('btn--red')}
const demoCodeElement=document.getElementById('vditorDemoCode')
demoCodeElement.firstElementChild.innerHTML=`<code>${code}
</code>`
Vditor.highlightRender({lineNumber:true,enable:true},demoCodeElement)
Vditor.codeRender(demoCodeElement)}
const autoType=()=>{const typeElement=document.getElementById('autoType')
if(!typeElement){return}
const texts=['å®žçŽ° CommonMark å’Œ GFM è§„èŒƒ','æ”¯æŒæ•°å­¦å…¬å¼ã€å›¾è¡¨ã€äº”çº¿è°±ã€è„‘å›¾ç­‰14+æ¸²æŸ“','æ‰€è§å³æ‰€å¾—ï¼ˆwysiwygï¼‰','å³æ—¶æ¸²æŸ“ï¼ˆirï¼‰','åˆ†å±é¢„è§ˆï¼ˆsvï¼‰','æ˜“äºŽä½¿ç”¨çš„ Markdown ç¼–è¾‘å™¨ï¼Œä¸ºé€‚é…ä¸åŒçš„åº”ç”¨åœºæ™¯è€Œç”Ÿ',]
let textLength=0
let time=0
texts.forEach((text,i)=>{if(i>0){textLength+=text[i-1].length+20}
for(let j=0;j<text.length;j++){time+=200
setTimeout(()=>{typeElement.innerHTML=text.substr(0,j+1)+
`<span class="caret" style="${(j===text.length-1?'animation-name:flash':'')}"></span>`},time)}
if(i!==texts.length-1){time+=2000
for(let k=0;k<text.length;k++){time+=50
setTimeout(()=>{typeElement.innerHTML=typeElement.textContent.substr(0,typeElement.textContent.length-1)+'<span class="caret"></span>'},time)}}else{setTimeout(()=>{document.querySelector('.caret').style.animationName='flash'},time+1)}})}
addStyle('https://cdn.jsdelivr.net/npm/vditor@3.8.12/dist/index.css')
document.addEventListener('DOMContentLoaded',function(){autoType();if(document.getElementById('vditorComments')){addScript('https://cdn.jsdelivr.net/npm/vditor@3.8.12/dist/index.min.js',()=>{const demoCodeElement=document.getElementById('vditorDemoCode')
if(demoCodeElement){Vditor.highlightRender({lineNumber:true,enable:true},demoCodeElement)
Vditor.codeRender(demoCodeElement)}
if(typeof vditorScript!=='undefined'){vditorScript()}
addScript('https://cdn.jsdelivr.net/npm/vcmt@1.3.1/dist/index.min.js',()=>{const vcomment=new Vcomment({id:'vditorComments',postId:'1549638745630',url:'https://ld246.com',userName:'Vanessa',currentPage:1,vditor:{hljsEnable:true,hljsStyle:'github',},after(){const commentCntElement=document.getElementById('commentsCount')
document.getElementById('commentCnt').innerText=commentCntElement.innerText+
' ä¸ªè®¨è®º'
commentCntElement.nextSibling.remove()
commentCntElement.remove()},error(){document.getElementById('comments').remove()},})
vcomment.render()})})}
const dynamicElement=document.getElementById('dynamic')
if(dynamicElement){const xhr=new XMLHttpRequest()
xhr.open('GET','https://ld246.com/api/v2/articles/tag/vditor?p=1')
xhr.withCredentials=true
xhr.onreadystatechange=()=>{if(xhr.readyState===XMLHttpRequest.DONE){if(xhr.status===200){const responseJSON=JSON.parse(xhr.responseText)
const articles=responseJSON.data.articles
if(responseJSON.code!==0||0===articles.length){dynamicElement.innerHTML='æ— æ–°é—»'
dynamicElement.style.backgroundImage='none'
return}
let listHTML='<ul class="fn-list">'
for(var i=0;i<articles.length;i++){const article=articles[i]
listHTML+='<li><a target=\'_blank\' href=\''+
article.articlePermalink+
'\'>'
+article.articleTitle+'</a>&nbsp;<small class="ft-fade">['+
article.cmtTimeAgo
+']</small></li>'}
listHTML+='</ul>'
dynamicElement.innerHTML=listHTML
dynamicElement.style.backgroundImage='none'}else{dynamicElement.innerHTML='åŠ è½½åˆ—è¡¨å¤±è´¥ :-('
dynamicElement.style.backgroundImage='none'}}}
xhr.send()}})