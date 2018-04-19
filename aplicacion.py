import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import io
import fileinput

archivo = open("configuracion.json")
config = json.load(archivo)

for documentId in config["documentIds"]:
    url = config["urlBase"].format(
        protocol=config["protocol"],
        host=config["host"],
        idempresa=config["idEmpresa"],
        documentid=documentId)
    print(
        "Descargando documento {documentId}... ".format(documentId=documentId),
        end=" ")
    f = urllib.request.urlopen(url)
    data = f.read()
    with open("{documentId}.xml".format(documentId=documentId)) as code:
        code.write(data)
        dte3 = ET.parse(code).getroot()

        print("OK!")
print("Proceso finalizado")