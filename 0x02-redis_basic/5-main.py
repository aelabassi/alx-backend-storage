#!/usr/bin/env python3
get_page = __import__('web').get_page
result = get_page('http://slowwly.robertomurray.co.uk')
print(result)
