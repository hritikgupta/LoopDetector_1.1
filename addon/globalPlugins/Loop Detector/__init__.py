
import keyboardHandler
import mouseHandler
import eventHandler
import review
import controlTypes
import api
import textInfos
import speech
import sayAllHandler
from NVDAObjects import NVDAObject, NVDAObjectTextInfo
import appModuleHandler
import treeInterceptorHandler
import scriptHandler
import ui
import globalPluginHandler
from NVDAObjects import NVDAObject, NVDAObjectTextInfo
from NVDAObjects.IAccessible import IAccessible
from NVDAObjects.window.scintilla import Scintilla


class myClass(IAccessible):

	def script_func(self, gesture):
		obj=api.getFocusObject()
		treeInterceptor=obj.treeInterceptor
		if isinstance(treeInterceptor, treeInterceptorHandler.DocumentTreeInterceptor) and not treeInterceptor.passThrough:
			obj = treeInterceptor
		try:
			info = obj.makeTextInfo(textInfos.POSITION_CARET)
		except:
			info = obj.makeTextInfo(textInfos.POSITION_FIRST)
		info.expand(textInfos.UNIT_LINE)
		scriptCount = scriptHandler.getLastScriptRepeatCount()
		if scriptCount == 0:
			#tinker here
			#discover speechTextInfo
			ui.message("here:%s"%info)
			#speech.speakTextInfo(info, unit=textInfos.UNIT_LINE, reason=controlTypes.REASON_CARET)
		else:
			#on pressing gesture more than once
			speech.spellTextInfo(info, useCharacterDescriptions=scriptCount>1) 

	def speaker(self, gesture):
			selected = info.text
			k = info.text.split(" ")
			countIndent = 0
			ctr = 0
			for i in range(0, len(k)):
				if k[i] == "for":
					for j in range(i, len(k)):
						if k[j] == "in":
							flag = 1
							countIndent = re.search('\S', selected).start()
							ui.message("For loop starts")
				elif k[i] == "while":
					ui.message("While loop starts")

	__gestures={
		"kb:NVDA+h":"func"
	}

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def chooseNVDAObjectOverlayClasses(self,obj,clsList):
		if obj.windowClassName == u'Scintilla' and obj.windowControlID == 0:
			clsList.insert(0, myClass)