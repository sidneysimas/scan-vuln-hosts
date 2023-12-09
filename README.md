Muitas vezes precisamos verificar em uma rede com muitos hosts, quais estão vivos e quais portas e serviços estão em execução. Dessa forma eu automatizei o processo, facilitando e trazendo de forma organizada os resultados.
  
1.  **Como instalar?**

    Navegue dentro de seu sistema, escolha o local e execute no terminal o comando abaixo.

    ``` 
        git clone https://github.com/sidneysimas/scan-vuln-hosts.git
        Cloning into 'scan'...
        remote: Enumerating objects: 10, done.
        remote: Counting objects: 100% (10/10), done.
        remote: Compressing objects: 100% (10/10), done.
        remote: Total 10 (delta 1), reused 0 (delta 0), pack-reused 0
        Receiving objects: 100% (10/10), 19.14 KiB | 612.00 KiB/s, done.
        Resolving deltas: 100% (1/1), done.
      ```

2.  **Conceda permissão para o arquivo!**
```
chmod +x scan-vuln-hosts.sh
```
OBS: Uma outra boa dica é mover o arquivo do script para o diretório /usr/bin , dessa forma podemos utilizar de forma direta no terminal.
## 🧐 Como usar o script?
Caso digite sem o argumento da rede, recebe a seguinte resposta:

![image](https://github.com/sidneysimas/scan-vuln-hosts/assets/3409713/b5c3b44f-edc4-4953-b715-d213d0132f22)

Você irá digitar ```./scan_hosts.sh 192.168.0``` 
Ele vai perguntar o nome do projeto:
Em seguida o script faz o scan de hosts vivos.
![image](https://github.com/sidneysimas/scan-hosts/assets/3409713/232efccb-31b3-435a-aff6-46c3d68c373f)
<img alt="faciltech" src="20230118_194341.gif"/>

Também pode ser utilizado a opçao -l para passar uma lista de ips.
# scan-vuln-hosts

<!-- AUTO-GENERATED-CONTENT:END -->
<!-- AUTO-GENERATED-CONTENT:END -->
