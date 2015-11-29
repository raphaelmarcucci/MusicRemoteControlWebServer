function htmlEncode(value) {
  //create a in-memory div, set it's inner text(which jQuery automatically encodes)
  //then grab the encoded contents back out.  The div never exists on the page.
  return $('<div/>').text(value).html();
}

function htmlDecode(value) {
  return $('<div/>').html(value).text();
}

var messagereply='';

// function waitForValue() {
//     if(messagereply=='') {
//         window.setTimeout('waitForValue();',100);
//     }
// }

function sendToMrcServer(messagequery) {

    var xhr = new XMLHttpRequest();
    messagereply = '';
    messagequery = htmlEncode(messagequery)
    messagequery += '\n';

    xhr.onreadystatechange=function() {
        if(xhr.readyState == 4) {
            if (xhr.status == 200 || xhr.status == 0) {
                messagereply = xhr.responseText;
                messagereply = htmlDecode(messagereply)
            }
        }
    }
				
    // leave synchronous communication for the moment, even if not recommended
    // TODO: find a better usage later
    xhr.open('POST', 'http://192.168.1.36:61666/', false);
    xhr.send(messagequery);
 
    //waitForValue();
    
    return messagereply;
}
