
# *  This Program is free software; you can redistribute it and/or modify
# *  it under the terms of the GNU General Public License as published by
# *  the Free Software Foundation; either version 2, or (at your option)
# *  any later version.
# *
# *  This Program is distributed in the hope that it will be useful,
# *  but WITHOUT ANY WARRANTY; without even the implied warranty of
# *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# *  GNU General Public License for more details.
# *
# *  You should have received a copy of the GNU General Public License
# *  along with XBMC; see the file COPYING.  If not, write to
# *  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
# *  http://www.gnu.org/copyleft/gpl.html

import xbmc,xbmcgui
import subprocess,os
import xbmcaddon
import subprocess

addon = xbmcaddon.Addon("service.playback.sleeptimer")

# helper function to get bool type from settings
def getSettingAsBool(setting):
	return getSetting(setting).lower() == "true"

while(not xbmc.abortRequested):
	if xbmc.getGlobalIdleTime() > (int(addon.getSetting('idle_time_min'))*60):
		if xbmc.Player().isPlaying() and getSettingAsBool('turn_off_cec'):
			xbmc.Player().stop()
			subprocess.call('echo "standby 0" | cec-client -s', shell=True)
		else:
			xbmc.Player().stop()
	xbmc.sleep(60000)
