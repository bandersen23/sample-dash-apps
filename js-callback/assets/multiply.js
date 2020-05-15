if(!window.dash_clientside) {window.dash_clientside = {};}
window.dash_clientside.clientside = {
    multiply: function (a, b) {
        if (a == null | b == null | isNaN(a) | isNaN(b)) {
          return null;
        }
        else {
          x = a * b;
          return 'Client says ' + a + ' times ' + b + ' is ' + x + ' .';
        }
    }
}
