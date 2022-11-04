o

�V�b��	@svddlmZddlmZddlmZddlZddlZddlZddl	Z	ddl
mZmZddl
mZe	��Ze�d�edd	Zedd
ZdZdZd
ZdZee�Zee�Ze�ejZejZej Z!ej"Z#ej$Z%ej&Z'ej(Z)ee!e#e%e'e)gZ*zddl+Z+Wne,y�e-e�de���e�.d�Ynwdd�Z/dd�Z0	e0�e/�e-ede�e-ede�e-ede�e-ede�e-ede�e-ede�ee1d��Z2e2dk�r}gZ3e4dd���Z5ee1d e)�d!e!����Z6e7e6�D]!Z8ee1d e'�d"e!����Z9d#�:e9�;��Z<e�=e<ge5�e3�>e<�q�e-d e%�d$��e0�e-d e)�d%��e3D]6Z?ed&e?��ee�Z@e@�Ae?�e-e'�d'��e@ed(��ed)�e@ed*��ed)�e@ed+��e@�B��q,e1d,�Wd�n	1�srwYe5�C��n�e2d)k�r_gZDgZEe4dd-�ZF	z
eD�>e�GeF��Wn
eH�y�Ynw�q�eF�C�eIeD�dk�r�e-e!d.�ed/��n�eDD]LZJeeJd�ZKed&eK��ee�ZLeL�M�eL�N��szeL�OeK�e-eP�d0eK�d1e���W�q�e�ye-e!eeK�d2e�eE�>eJ�Y�q�w�q�eIeE�dk�re-ed3�e1d4��neED]ZQeD�ReQ��qe4dd5��ZSeDD]Z2e2dZTe�=eTgeS��q/Wd�n	1�sIwYeS�C�e-ed6e�e1d4�n�e2d/k�rgZUe4dd-�ZV	z
eU�>e�GeV��Wn
eH�y�Ynw�qleV�C�dZ8e-e'�d7��eUD]ZWe-e�d8e8�d9eWd�e���e8d7Z8�q�ee1d e�d:e����ZXeeUeXd�ZKeKd;ZYejZd<k�r�e�.d=eY���ne�.d>eY���eUeX=e4dd5�ZVeUD]	ZJe�=eJeV��q�e-d e�d?e���e1d4�eV�C�n:e2d@k�re-dA�e�.dB�e-dC�e1dD�e�.dE�ne2dFk�r,e0�e/�e1dG�ne2dHk�r:e0�e/�e[�q�)I�)�TelegramClient)�PhoneNumberBannedError)�JoinChannelRequestN)�init�Fore)�sleepz
setapi.iniZRex�input_api_id�input_api_hashz[1;31mz[1;32mz[1;36mz[1;35mz#[i] Installing module - requests...zpip install requestscCsVddl}gd�}|D]}t|�t��|�t���q
tdt���tdt�d��dS)Nr)uK╔═══╗──────────────────╔╗uN║╔═╗║─────────────────╔╝╚╗u]║║─║╠═╗╔═╗╔╗╔╦═╗╔══╦╦═╩╗╔╬══╦═╗u]║╚═╝║╔╗╣╔╗╣║║║╔╗╣╔═╬╣╔╗║║║╔╗║╔╝uZ║╔═╗║║║║║║║╚╝║║║║╚═╣║╔╗║╚╣╚╝║║uZ╚╝─╚╩╝╚╩╝╚╩══╩╝╚╩══╩╩╝╚╩═╩══╩╝z&==========BAN PROBLEM SOLVED==========z%   Version: 1.0 | Author: Annunciator�
)�random�print�choice�colors�gm�re�n)r�b�char�r�%/storage/emulated/0/nt/annunciator.py�banner(srcCs&tjdkrt�d�dSt�d�dS)N�nt�cls�clear)�os�name�systemrrrr�clr;s
rTz[1] ~Add New Accounts~z [2] ~Filter All Banned Accounts~z[3] ~Delete specific accounts~z[4] ~Member Adder~z[5] ~Credit~z
[6] ~Exit~z
Enter Your Choice: �zvars.txt�abr
z& [~] Enter number of accounts to add: z [~] Enter Phone Number: �z# [i] Saved all accounts in vars.txtz" [*] Logging in from new accounts
z	sessions/u>[+] 𝐋𝐨𝐠𝐢𝐧 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮Lz@The_Hacking_Zone�z@TeleModsApkz@Techno_Trickopz"
 Press enter to goto main menu...�rbz4[!] There are no accounts! Please add some and retry�z[+] z is not bannedz is banned!zCongrats! No banned accountsz!
Press enter to goto main menu...�wbz[i] All banned accounts removedz [i] Choose an account to delete
�[z] z[+] Enter a choice: z.sessionrz
del sessions\zrm sessions/z[+] Account Deleted�z[+] Openning Member Adderz
python xxx.pyz[+] Successfully Addedz#
 Press enter to goto main menu....zpython annunciator.py�zg
 All Credit goes to Astra/Cryptonion
 Ban solution --> @TG_STARWORLD
 
 Press enter to goto main menu....�)\Z
telethon.syncrZtelethon.errors.rpcerrorlistrZtelethon.tl.functions.channelsr�picklerZcsvZconfigparserZcoloramarr�timerZConfigParserZconfig�readrr	rr�coZwi�intZapi_id�strZapi_hashZRESETrZBLUEZlgZRED�rZWHITE�wZCYAN�cyZYELLOWZyeZGREENZgrrZrequests�ImportErrorrrrr�input�aZnew_accs�open�gZ
number_to_add�range�iZphone_number�join�splitZ
parsed_number�dump�appendZnumber�c�startZ
disconnect�closeZaccountsZbanned_accs�h�load�EOFError�lenZaccountZphoneZclientZconnectZis_user_authorizedZsend_code_requestZblue�m�remove�kZPhoneZaccs�fZacc�indexZsession_filer�quitrrrr�<module>s8
�


�

��

����


�� 






�