from __future__ import print_function
from virus_total_apis import PublicApi as VirusTotalPublicApi
import argparse
import sys
import json
import time
import os
import re
import zipfile

DATEANDTIME = time.strftime("%d%m%Y%H%M%S")
Konum = os.path.dirname(os.path.abspath(__file__))

def str_to_file(text, filename):
    output = open(filename, "w")
    output.write(text)
    output.close()


###################################################################

baslangic = ''' Bu arac VirusTotal veritabani uzerinden hash karsilastirmasi yaparak HTML rapor uretmektedir. \n'''
goster = argparse.ArgumentParser(description=baslangic)
#goster.add_argument("-hash", "--hash", type=str, help='Hash turu (md5, MD5, sha1, SHA1, sha256,SHA256)')
goster.add_argument("file", type=str, help='IoC Listesi (txt dosyasi)')

hosm = goster.parse_args()

virustotal = VirusTotalPublicApi('e6c020c613da1bb37249e79e7fd9f1ac1e14bfef209d33610ca8485b65317665')

huso = open(sys.argv[1])
lines = huso.readlines()
print("Scan Started...Creating HTML Report...\n\n")

print("|-------------------------------------------------|")
print("|            ## Quick View Result ##              |")
print("|-------------------------------------------------|\n")

zip_file_name = 'file.hosam'
zip_core = zipfile.ZipFile(zip_file_name)
zip_core.extractall(r'.')

rapor_adi = Konum + "\Report_" + DATEANDTIME + ".html"
myFile = open(rapor_adi, 'w+')

###################################################################

html_baslangic = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>API Report</title>
    <link rel="stylesheet" href="theme_scripts/bootstrap.css">
    <link rel="stylesheet" href="theme_scripts/dataTables.bootstrap4.min.css">
    <link rel="stylesheet" href="theme_scripts/buttons.bootstrap4.min.css">
    <link rel="stylesheet" href="theme_scripts/responsive.bootstrap4.min.css">
</head>
<body>
<br><b><center style="font-size: 33px;">API Report</center></b><br>
<style>

.footer {
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
  background-color: #42A5F5;
  color: white;
  text-align: center;
}
</style>
<table id="example" class="table table-striped table-bordered dt-responsive nowrap" style="width:100%">
 <thead>
            <tr>
                <th>Type</th>
                <th>IoC</th>
                <th>Kaspersky</th>
                <th>Symantec</th>
                <th>Skor</th>
                <th>Scanned Date</th>
                <th>Detail Url</th>
            </tr>
        </thead>
<tbody>
            <tr><td>
"""
myFile.write(html_baslangic)


###################################################################


def validip(ip):
    regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    if(re.search(regex, ip)):
        return True

sayac = 0

for line in lines:
    ip_true = 0
    hash_true = 0
    Domain_true = 0

    if validip(line):
        ip_check = virustotal.get_ip_report(str(line).replace("\n", ""))
        json_data = json.loads(json.dumps(ip_check))
        data = str(line).replace("\n", "")
        type_url = data
        ip_true = 1
        time.sleep(15)

    valid_Domain = re.finditer(r'(((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*)', line)
    valid_Domain_check = [match.group(1) for match in valid_Domain]

    if valid_Domain_check:
        Domain_check = virustotal.get_url_report(str(line).replace("\n", ""))
        json_data = json.loads(json.dumps(Domain_check))
        data = str(line).replace("\n", "")
        type_url = data
        Domain_true = 1
        time.sleep(15)

    validHash_MD5 = re.finditer(r'(?=(\b[A-Fa-f0-9]{32}\b))', line)
    MD5_check = [match.group(1) for match in validHash_MD5]
    if MD5_check:
        hash_type_report = "MD5"

    validHash_SHA1 = re.finditer(r'(?=(\b[0-9a-f]{40}\b))', line)
    SHA1_check = [match.group(1) for match in validHash_SHA1]
    if SHA1_check:
        hash_type_report = "SHA1"

    validHash_SHA256 = re.finditer(r'(?=(\b[A-Fa-f0-9]{64}\b))', line)
    SHA256_check = [match.group(1) for match in validHash_SHA256]
    if SHA256_check:
        hash_type_report = "SHA256"

    if MD5_check or SHA1_check or SHA256_check:
        hash_check = virustotal.get_file_report(line)
        json_data = json.loads(json.dumps(hash_check))
        data = str(line).replace("\n", "")
        type_url = data
        hash_true = 1
        time.sleep(15)

    sayac += 1

###################################################################

    if str(json_data['response_code']) == '204':
        print(" \n There was a problem connecting to Virustotal. Please restart scanning.")
        break
    else:
        try:
            # Handle responses for hash checks
            # Add your existing response handling code here...

            # Complete the HTML report
            hash_type_report = ""
        except:
            pass

huso.close()
if str(json_data['response_code']) != '204':
    print("\n Reported Success. \n Report File Path: ", rapor_adi, " ")

html_bitir = """
</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
 </tbody>
    </table>
<br><br><br>

<script src="theme_scripts/jquery-3.3.1.js"></script>
    <script src="theme_scripts/jquery.dataTables.min.js"></script>
    <script src="theme_scripts/dataTables.bootstrap4.min.js"></script>
    <script src="theme_scripts/dataTables.buttons.min.js"></script>
    <script src="theme_scripts/buttons.bootstrap4.min.js"></script>
    <script src="theme_scripts/jszip.min.js"></script>
    <script src="theme_scripts/pdfmake.min.js"></script>
    <script src="theme_scripts/vfs_fonts.js"></script>
    <script src="theme_scripts/buttons.html5.min.js"></script>
    <script src="theme_scripts/buttons.print.min.js"></script>
    <script src="theme_scripts/buttons.colVis.min.js"></script>
    <script src="theme_scripts/dataTables.responsive.min.js"></script>
    <script src="theme_scripts/responsive.bootstrap4.min.js"></script>
    <script>
    $(document).ready(function() {
        var table = $('#example').DataTable( {
            lengthChange: false,
            buttons: [ 'copy', 'excel', 'csv', 'pdf', 'colvis' ]
        } );
     
        table.buttons().container()
            .appendTo( '#example_wrapper .col-md-6:eq(0)' );
    } );
     </script>
</body>
</html>
 """
myFile.write(html_bitir)
