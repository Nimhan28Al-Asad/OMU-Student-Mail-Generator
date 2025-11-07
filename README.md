# OMU-Student-Mail-Generator
🧩 OMU Student Mail Generator

OMU Student Mail Generator is a simple Python tool that automatically generates official-style university email addresses for students of Ondokuz Mayıs University (OMU).

It reads student data (ID, name, surname) from a text file, cleans Turkish characters using the unidecode library, and formats standardized email addresses following the pattern:

name.surname@departement.omu.edu.tr


For foreign students with multiple given names (e.g., Nimhan Soubaneh, Elmi), the generator automatically uses the last two parts to create a valid email like:

soubaneh.elmi@bil.omu.edu.tr

⚙️ Features

Converts Turkish characters (e.g., Ç → C, Ş → S, Ü → U)

Handles both Turkish and international name structures

Generates valid OMU email addresses

Lightweight and customizable Python script

🧠 Example

Input (file.txt):

24572011, Deniz, Yılmaz
22212808, Nimhan Soubaneh, Elmi
22856987, Mohamed, Vall


Output:

24572011, deniz.yilmaz@departement.omu.edu.tr
22212808, soubaneh.elmi@departement.omu.edu.tr
22856987, mohamed.vall@departement.omu.edu.tr
