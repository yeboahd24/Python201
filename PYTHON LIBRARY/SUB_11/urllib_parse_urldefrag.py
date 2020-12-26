# To simply strip the fragment identifier from a URL, such as when finding a base page
# name from a URL, use urldefrag().


from urllib.parse import urldefrag

original = 'http://netloc/path;param?query=arg#frag'
print('original:', original)
d = urldefrag(original)
print('url :', d.url)
print('fragment:', d.fragment)