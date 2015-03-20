import urllib2
from lxml import html
from nose.tools import assert_equals
from lettuce import world, before, step
from lettuce.django import django_url
from django.test.client import Client

@before.all
def set_client():
	world.browser = Client()
	
@step(r'I access the url "(.*)"')
def given_i_access_the_url(step, url):
	url = django_url(url)
	raw = urllib2.urlopen(url).read()
	world.dom = html.fromstring(raw)
	
@step(r'I see the title "(.*)"')
def see_title(step, text):
	assert text == world.dom.find(".//title").text
