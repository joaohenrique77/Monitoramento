import platform
import socket
import psutil


# Informações básicas do computador
def informacoes_sistema():
    try:
        memoria = psutil.virtual_memory()

        return {
            "nome": socket.gethostname(),
            "sistema": platform.system(),
            "versao": platform.release(),
            "arquitetura": platform.architecture()[0],
            "processador": platform.processor() or "Não identificado",
            "memoria_total": round(memoria.total / (1024 ** 3), 2)
        }

    except Exception as erro:
        return {"erro": str(erro)}


# Monitoramento do processador
def monitorar_cpu():
    try:
        uso = psutil.cpu_percent(interval=0.1)

        return {
            "uso_percentual": uso
        }

    except Exception as erro:
        return {"erro": str(erro)}


# Monitoramento da memória RAM
def monitorar_memoria():
    try:
        memoria = psutil.virtual_memory()

        return {
            "total_gb": round(memoria.total / (1024 ** 3), 2),
            "usada_gb": round(memoria.used / (1024 ** 3), 2),
            "disponivel_gb": round(memoria.available / (1024 ** 3), 2),
            "percentual": memoria.percent
        }

    except Exception as erro:
        return {"erro": str(erro)}


# Monitoramento do armazenamento
def monitorar_armazenamento():
    try:
        unidades = []

        for particao in psutil.disk_partitions():
            try:
                disco = psutil.disk_usage(particao.mountpoint)

                unidades.append({
                    "unidade": particao.device,
                    "total_gb": round(disco.total / (1024 ** 3), 2),
                    "usado_gb": round(disco.used / (1024 ** 3), 2),
                    "livre_gb": round(disco.free / (1024 ** 3), 2),
                    "percentual": disco.percent
                })

            except (PermissionError, OSError):
                continue

        if not unidades:
            return {"erro": "Nenhuma unidade disponível."}

        return unidades

    except Exception as erro:
        return {"erro": str(erro)}


# Reúne todas as informações
def atualizar_dados():
    return {
        "sistema": informacoes_sistema(),
        "cpu": monitorar_cpu(),
        "memoria": monitorar_memoria(),
        "armazenamento": monitorar_armazenamento()
    }


# Teste do backend
if __name__ == "__main__":
    from pprint import pprint

    dados = atualizar_dados()
    print(dados)
