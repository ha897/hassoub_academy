import zipfile

compressZip = zipfile.ZipFile("flask.zip")

#يفك الضغط بمسار العمل الحالي
compressZip.extractall()
