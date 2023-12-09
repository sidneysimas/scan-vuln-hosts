#!/bin/bash
figlet SCAN-VULN-HOSTS
echo "Autor: Sidney Giovanni Simas"
# echo "You Tube : https://www.youtube.com/faciltech"
# echo "github   : https://github.com/faciltech"
echo "Linkedin : https://www.linkedin.com/in/sidneygiovannisimas/"
if [ -z "$1" ]
then
        echo "Modo de Uso: ./scan-vuln-hosts.sh 192.168.0"
        echo "Apenas ID da rede (3 primeiros numeros, exemplo 192.168.0)."
        echo "ATENÇÃO: Só portas TCP"
        echo "OBS: Necessita de Nmap"
        exit 1
fi
echo ""
echo -e "\e[31m#### SCANEANDO HOSTS ####\e[0m"
echo "DIGITE O NOME DO PROJETO: "
read diretorio
mkdir $diretorio
#cd $diretorio
if [ $1 == "-l" ]
then
        hosts=$2
        for i in $(cat $hosts);
        do
                echo $i
                mkdir $diretorio/$i
        done
        for i in $(cat $hosts);
        do
                echo ""
                echo -e "\e[31m#### SCANEANDO PORTAS DO HOST $i ####\e[0m"
                portas=$(sudo nmap -sS --open --source-port 443 -p- -Pn $i | grep '^[0-9]' | awk -F'/' '{print $1}'| xargs | sed 's/ /,/g')

                if [ -z "$portas" ]; then
                        echo "Sem portas abertas no Host $i"
                else
                        printf "\e[1;33;40mPortas abertas do Host $i \e[0m: \e[1;32m$portas\e[0m"
                        echo " "
                        echo -e "\e[31m#### Informações dos serviços das Portas do Host $i ####\e[0m"
                        nmap -sC -sV -p $portas -Pn $i > $diretorio/$i/portas_servicos.txt
                        echo "Os serviços das portas foram salvos no arquivo $diretorio/$i/portas_servicos.txt"
                        echo -e "\e[31m#### Escaneando Vulnerabilidades no Host $i ####\e[0m"
                        nmap --script vuln -p $portas -Pn $i > $diretorio/$i/vulnerabilidades.txt
                        echo "As vulnerabilidades foram salvas no arquivo $diretorio/$i/vulnerabilidades.txt"
                fi
        done 

else
        hosts=$(sudo nmap -sn $1.0/24 | grep -oE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b')
        for i in $hosts;
        do
                echo $i
                mkdir $diretorio/$i
        done
        for i in $hosts;
        do
                echo ""
                echo -e "\e[31m#### SCANEANDO PORTAS DO HOST $i ####\e[0m"
                portas=$(sudo nmap -sS --open --source-port 443 -p- -Pn $i | grep '^[0-9]' | awk -F'/' '{print $1}'| xargs | sed 's/ /,/g')

                if [ -z "$portas" ]; then
                        echo "Sem portas abertas no Host $i"
                else
                        printf "\e[1;33;40mPortas abertas do Host $i \e[0m: \e[1;32m$portas\e[0m"
                        echo " "
                        echo -e "\e[31m#### Informações dos serviços das Portas do Host $i ####\e[0m"
                        nmap -sC -sV -p $portas -Pn $i > $diretorio/$i/portas_servicos.txt
                        echo "Os serviços das portas foram salvos no arquivo $diretorio/$i/portas_servicos.txt"
                        echo -e "\e[31m#### Escaneando Vulnerabilidades no Host $i ####\e[0m"
                        nmap --script vuln -p $portas -Pn $i > $diretorio/$i/vulnerabilidades.txt
                        echo "As vulnerabilidades foram salvas no arquivo $diretorio/$i/vulnerabilidades.txt"
                fi
        done
fi
