videos=json.loads((D/'videos.json').read_text())
def video_links(indices):
 return '<ul class="video-links">'+''.join(f'<li><a href="{esc(v["url"])}">{esc(v["title"])}</a> <span class="video-duration">{esc(v["duration"])}</span></li>' for v in videos['items'] if v['order'] in indices)+'</ul>'
content=head('Family voices / Video conversations','Reminiscing<br>with Luba.','Mark, Natalie and Luba remember family life: Mayfair and Florida Lake, the shop, schooldays and the people who shaped their lives.')
content+=p('Seventeen short clips and the full conversation, shared by Mark Cohen. The titles below are those used in his YouTube playlist. These excerpts belong to the same conversation as the supplied transcript; recollections remain family testimony.','recent-videos','recent')
content+=p('<a class="button" href="'+esc(videos['url'])+'">Open the complete YouTube playlist</a>')
full=videos['items'][-1]
content+=section('The full conversation',f'<article class="video-full" id="clip-18"><h3><a href="{esc(full["url"])}">{esc(full["title"])}</a></h3><p>{esc(full["duration"])} · Opens on YouTube</p></article>')
content+=section('Choose a story','<p>Watch any clip on YouTube, or use the playlist to continue through the collection.</p><ol class="video-catalogue">'+''.join(f'<li id="clip-{v["order"]}"><h3><a href="{esc(v["url"])}">{esc(v["title"])}</a></h3><p>{esc(v["duration"])} · Opens on YouTube</p></li>' for v in videos['items'][:-1])+'</ol>')
content+=section('Follow the family story',p('<a href="gilinsky.html">The Gilinsky family</a> connects the memories of Max and Riva with photographs and records. <a href="johannesburg.html">Life in southern Africa</a> covers the Milstein household, Arke and later family life. <a href="voices.html">The listening archive</a> preserves the earlier family tapes.'))
page('videos.html','Reminiscing with Luba — videos',content)
