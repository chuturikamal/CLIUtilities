#! /bin/bash
cd ~/Downloads



fileExtesion='*.mkv *.pdf'
dirList=`ls ${fileExtesion}`
pdfList=()
pdfName=''

echo $dirList
for dir in $dirList;
do
    if [[ "$pdfName" == "" ]];
    then
        pdfName=$dir
    else
        pdfName="${pdfName} ${dir}"
    fi

    if [[ "$pdfName" == $fileExtesion ]]; 
    then 
        pdfList+=",${pdfName}"
        pdfName=""
    fi
done

echo $pdfList
