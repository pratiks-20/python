
server_ip = ("192", "168", "1", "10")  
allowed_ips = ["192.168.1.2", "192.168.1.3"]  

def update_allowed_ips(new_ip):
    if new_ip not in allowed_ips:
        allowed_ips.append(new_ip)
        print(f"IP {new_ip} added to allowed list.")
    else:
        print(f"IP {new_ip} is already allowed.")

def display_config():
    print("=== Server Configuration ===")
    print("Server IP (unchangeable):", ".".join(server_ip))
    print("Allowed IPs (modifiable):", allowed_ips)

display_config()
update_allowed_ips("192.168.1.4")
update_allowed_ips("192.168.1.2")  

try:
    server_ip[0] = "10"  
except TypeError:
    print("Error: Cannot change server_ip. It is fixed.")

display_config()