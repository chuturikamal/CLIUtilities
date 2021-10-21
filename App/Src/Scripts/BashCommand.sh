#! /bin/bash
cd ~/Downloads
dirList=`ls ${prefix}*.pdf`
set pdfList = $[]
set pdfName = $""
for dir in $dirList;
do
    #echo $dir
    
    if [[ "$pdfName" == "" ]];
    then
        pdfName = $dir
        echo "Empty value: "pdfName
    else
        pdfName = "${pdfName} ${dir}"
        echo "value: "pdfName
    fi

    echo $pdfName
    if [[ "$dir" == *".pdf" ]]; 
    then 
        echo "Document Names: ${pdfName}"
        pdfName = ""
    fi
done
