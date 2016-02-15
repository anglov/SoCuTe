function generateKey(len) {
    var arr = new Uint8Array((len || 40) / 2);
    window.crypto.getRandomValues(arr);
    return [].map.call(arr, function(n) { return n.toString(16); }).join("");
}
function socute_encode() {
    var key = generateKey();
    window.alert("Your secure key is \'" + key + "\'.\nSave it in secure place!");
    document.getElementById('id_text_hid').value = sjcl.encrypt(key, document.getElementById('id_text').value)
}
function socute_decode() {
    try {
        var query = getQueryParams(document.location.search);
        document.getElementById('id_text').value = sjcl.decrypt(query.key, document.getElementById('id_text_hid').value)
    }
    catch(err) {
        document.getElementById("id_text").value = "Wrong key!";
    }
}
function getQueryParams(qs) {
    qs = qs.split('+').join(' ');
    var params = {},
        tokens,
        re = /[?&]?([^=]+)=([^&]*)/g;
    while (tokens = re.exec(qs)) {
        params[decodeURIComponent(tokens[1])] = decodeURIComponent(tokens[2]);
    }
    return params;
}