set-psreadlineoption -editmode vi
set-psreadlinekeyhandler -chord = -function Complete -vimode Command
set-psreadlinekeyhandler -chord Tab -function Complete
$VIMRUNTIME = 'C:\tools\vim\'

Function t32 {bash -c "ls -lt"}
Set-Alias -Name t -Value t32

function plantUMLsvg {
  Param($File)
  java -DPLANTUML_LIMIT_SIZE=8192 -jar .\plantuml.jar -charset UTF-8 -svg $File
}

