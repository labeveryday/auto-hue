-- Stream Deck launcher that runs rotate_scenes.py without opening Terminal.
-- Keep this file in the repo root and compile it to an app:
--   osacompile -o streamdeck_rotate_scenes.app streamdeck_rotate_scenes.applescript

set appPath to POSIX path of (path to me)
set repoDir to do shell script "dirname " & quoted form of appPath

set py to repoDir & "/venv/bin/python"
set scriptPath to repoDir & "/rotate_scenes.py"
set logPath to repoDir & "/streamdeck_rotate_scenes.log"

try
	-- Note: do shell script uses /bin/sh; quoting is important.
	do shell script ("echo " & quoted form of ("[run] " & (do shell script "date")) & " >> " & quoted form of logPath)
	do shell script (quoted form of py & " " & quoted form of scriptPath & " >> " & quoted form of logPath & " 2>&1")
on error errMsg number errNum
	-- Avoid popups; log the error instead.
	do shell script ("echo " & quoted form of ("[AppleScript error " & errNum & "] " & errMsg) & " >> " & quoted form of logPath)
end try


