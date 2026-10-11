from datetime import datetime
import argparse


timestamp =datetime.now().strftime("%d-%m-%Y %H:%M:%S") #Buscar data de registro
#Definir parâmetros de entrada no terminal
parser =argparse.ArgumentParser()
parser.add_argument("--service",required=True)
parser.add_argument("--status",choices=["SUCCESS","WARNING", "ERROR"],required=True)
parser.add_argument("--msg",required=True)

t_argp =parser.parse_args()
log = f"[{timestamp}][{t_argp.service}] [{t_argp.status}]:{t_argp.msg}\n"
#Aguardar registro em doc txt
with open("audit.log","a") as arquivo:
    arquivo.write(log)

print("REGISTRO ANEXADO👍.")
print(f"==Resumo==\nService:{t_argp.service} \nSTATUS:{t_argp.status} \nMESSAGE:{t_argp.msg}")
if t_argp.status == "ERROR":
    print("!!! ALERTA : ERRO DETECTADO!!!")


