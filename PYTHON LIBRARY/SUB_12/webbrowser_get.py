# If for some reason your application needs to use a specific browser, you can access the set of
# registered browser controllers using the get() function. The browser controller has open(),
# open_new(), and open_new_tab() methods. The next example forces the use of the lynx
# browser.

import webbrowser

b = webbrowser.get('lynx')
b.open('https://docs.python.org/3/library/webbrowser.html')