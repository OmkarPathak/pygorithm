@echo off
setlocal EnableExtensions EnableDelayedExpansion

for %%f in (*.py) do (
    set fn="%%~nf"
    if not "x!fn:test=!" == "x!fn!" (
        echo "exporting !fn!.."
        py "!fn!.py" --export
    )
)
endlocal