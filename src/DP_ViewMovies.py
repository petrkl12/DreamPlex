# -*- coding: utf-8 -*-
"""
DreamPlex Plugin by DonDavici, 2012
 
https://github.com/DonDavici/DreamPlex

Some of the code is from other plugins:
all credits to the coders :-)

DreamPlex Plugin is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
(at your option) any later version.

DreamPlex Plugin is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
"""
#===============================================================================
# IMPORT
#===============================================================================
from Components.config import config

from DP_ViewCine import DP_ViewCine

from __common__ import printl2 as printl

#===============================================================================
# 
#===============================================================================
def getViewClass():
	printl("",__name__ , "S")
	
	printl("",__name__ , "C")
	return DPS_ViewMovies

#===============================================================================
# 
#===============================================================================
class DPS_ViewMovies(DP_ViewCine):

	#===========================================================================
	# 
	#===========================================================================
	def __init__(self, session, libraryName, loadLibrary, playEntry, viewName, select=None, sort=None, myFilter=None, cache=None):
		printl("", self , "S")

		self.session = session
		DP_ViewCine.__init__(self, session, libraryName, loadLibrary, playEntry, viewName, select, sort, myFilter, cache)

		printl("", self, "C")

	#===========================================================================
	# 
	#===========================================================================
	def getPictureInformationToLoad(self):
		printl("", self, "S")

		printl( "is playable content",self, "D")
		bname = self.details["ratingKey"]
		self.startPlaybackNow = False

		printl( "is movie",self, "D")
		self.changeBackdrop = True
		self.changePoster = True
		pname = self.details["ratingKey"]
		
		if not self.usePicCache:
			pname = "temp"
			bname = "temp"
			self.mediaPath = config.plugins.dreamplex.logfolderpath.value
		
		self.whatPoster = self.mediaPath + self.image_prefix + "_" + pname + self.poster_postfix
		self.whatBackdrop = self.mediaPath + self.image_prefix + "_" + bname + self.backdrop_postfix
		
		printl("", self, "C")