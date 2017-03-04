function mrcDisplayControls(isPaused, paragraph) {
    var r = '<button onclick="mrcVolumeDown();">vol &#45;</button> ';
    r += '<button onclick="mrcPrev();">&lt;&lt;</button> ';
    if(isPaused)
        r += '<button id="playpause" onclick="mrcUnpause();">&#32;&gt;&#32;</button>';
    else
        r += '<button id="playpause" onclick="mrcPause();">&#32;&#124;&#124;&#32;</button>';
    r += ' <button onclick="mrcNext();">&gt;&gt;</button> ';
    r += '<button onclick="mrcVolumeUp();">vol &#43;</button>';
    paragraph.innerHTML = r;
}
