# BlackWatch Recon v2.0 - Scanner de Rede com Nmap
# Desenvolvido por: Davi Menezes Vasques
# IA Hacker System™

import nmap
import datetime

def scan_network(target):
    print("[*] Iniciando escaneamento com Nmap...")
    print(f"[*] Alvo: {target}")
    
    # Inicializa o scanner
    nm = nmap.PortScanner()
    
    try:
        # Executa o scan (ex: -sV detecta versões de serviços)
        nm.scan(hosts=target, arguments='-sV -O')
        
        report = f"\n=== RELATÓRIO BLACKWATCH RECON ===\n"
        report += f"Data: {datetime.datetime.now()}\n"
        report += f"Alvo: {target}\n\n"
        
        for host in nm.all_hosts():
            report += f"HOST: {host} ({nm[host].hostname()})\n"
            report += f"Estado: {nm[host].state()}\n"
            
            if 'osmatch' in nm[host]:
                for os in nm[host]['osmatch']:
                    report += f"Sistema: {os['name']} (Confiança: {os['accuracy']}%)\n"
            
            for proto in nm[host].all_protocols():
                ports = nm[host][proto].keys()
                for port in ports:
                    state = nm[host][proto][port]['state']
                    service = nm[host][proto][port]['name']
                    version = nm[host][proto][port].get('product', '')
                    report += f"  Porta: {port}/{proto} | Estado: {state} | Serviço: {service} | Versão: {version}\n"
            report += "\n"
        
        # Salva o relatório
        with open(f"blackwatch_scan_{target}_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}.txt", "w") as f:
            f.write(report)
        
        print("[✓] Escaneamento concluído!")
        print(f"[✓] Relatório salvo: blackwatch_scan_{target}.txt")
        print(report)
        
    except Exception as e:
        print(f"[!] Erro ao escanear: {e}")

# === EXECUÇÃO DO SCRIPT ===
if __name__ == "__main__":
    print("🔹 BLACKWATCH RECON v2.0 - Scanner de Rede")
    print("🔹 Desenvolvido por Davi MV | IA Hacker System™\n")
    
    alvo = input("Digite o IP ou rede para escanear (ex: 192.168.1.1 ou 192.168.1.0/24): ")
    scan_network(alvo)