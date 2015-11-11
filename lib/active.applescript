tell application "System Events"
  set activeApp to name of first application process whose frontmost is true
  do shell script "echo " & activeApp
end tell
