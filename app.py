import socket
import select
import requests
import threading
import re
import time
import struct
import random
import urllib3
from datetime import datetime
####################################
bot_codes = b""
bot_true = False 
def Get_bot_Code():
    global bot_codes
    url_api = "https://projects-fox-apis.vercel.app/get_code"
    res = requests.get(url_api)  
    if res.status_code == 200:
        raw_data = res.text.strip()
        cleaned_codes = [code.strip('b"') for code in raw_data.split()]
        bot_codes = b" ".join(code.encode('utf-8') for code in cleaned_codes)
        print("تم جلب الأكواد بنجاح:", bot_codes)
    else:
        print("فشل في جلب الأكواد:", res.status_code)
####################################
def Decrypted_id(id_value):
    url = f"https://api-delta-two.vercel.app/decrypt_id?id={id_value}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("decrypted_id")
    else:
        return f"{id_value}"
def telegram(message):
    token = "7942911541:AAHcdHjMqscehzSAVfUkG4GW4VSHi0BFqhI"
    chat_id = "-4749183314"
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=payload)
def send_telegram_message(message):
    time.sleep(0.2)
    try:
        telegram(message)
    except KeyError as e:
        print("Error parsing data:", e)
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
def emotes(id, emote_nmbr=None):
    Fox_Emote = [
f"050000002008{id}100520162a1408aae2cafb0210d6fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210d2fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210d1fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210d0fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210cefbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210cdfbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210ccfbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210cbfbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210c4fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210c6fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210c7fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210c8fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210c9fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210cafbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210ccfbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210cbfbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210bdfbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210c1fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210c2fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210c3fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210cefbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210cdfbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210ccfbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210b9fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210c4fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210c6fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210c0fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210bbfbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210befbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210bdfbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210bffbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210bafbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210b8fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210affbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210b0fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210b1fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210b2fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210b3fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210b4fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210b5fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210b6fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210b7fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210a2fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210a3fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210a4fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210a5fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210a6fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210a7fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210a8fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210a9fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210aafbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210abfbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210acfbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210adfbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210aefbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb021099fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb02109afbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb02109bfbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb02109cfbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb02109dfbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb02109efbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb02109ffbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210a0fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb0210a1fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb021098fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb021097fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb021096fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb021095fbb8b1032a0608{id}",
 f"050000002008{id}100520162a1408aae2cafb021094fbb8b1032a0608{id}", 
    ]
    try:
        if isinstance(emote_nmbr, str) and emote_nmbr.isdigit():
            emote_nmbr = int(emote_nmbr)
        elif not isinstance(emote_nmbr, int):
            emote_nmbr = None
    except ValueError:
        emote_nmbr = None
    if emote_nmbr is not None and 1 <= emote_nmbr <= len(Fox_Emote):
        return Fox_Emote[emote_nmbr - 1]
    else:
        return random.choice(Fox_Emote)
def Danse_Players(id):
    Danse_Player = [ f"050000002008{id}100520162a1408{id}1084fbb8b1032a0608{id}",
        f"050000002008{id}100520162a1408{id}10a2fbb8b1032a0608{id}",
        f"050000002008{id}100520162a1408{id}10edbabbb1032a0608{id}",
        f"050000002008{id}100520162a1408{id}10d6c2bbb1032a0608{id}",
        f"050000002008{id}100520162a1408{id}109684bbb1032a0608{id}",
        f"050000002008{id}100520162a1408{id}109e84bbb1032a0608{id}",
        f"050000002008{id}100520162a1408{id}10ca9bbbb1032a0608{id}",
        f"050000002008{id}100520162a1408{id}10b9cabbb1032a0608{id}",
        f"050000002008{id}100520162a1408{id}108bfbb8b1032a0608{id}",
        f"050000002008{id}100520162a1408{id}10fffab8b1032a0608{id}",
        f"050000002008{id}100520162a1408{id}10ff8bbbb1032a0608{id}"
    ]
    return random.choice(Danse_Player)        
####################################
def get_player_info(player_id):
    url = f"https://projects-fox-apis.vercel.app/player_info?uid={player_id}"
    response = requests.get(url)    
    if response.status_code == 200:
        try:
            r = response.json()
            return {
                "Account Booyah Pass": f"{r.get('booyah_pass_level', 'N/A')}",
                "Account Create": f"{r.get('account_creation_date', 'N/A')}",
                "Account Level": f"{r.get('level', 'N/A')}",
                "Account Likes": f" {r.get('likes', 'N/A')}",
                "Name": f"{r.get('player_name', 'N/A')}",
                "UID": f" {r.get('player_id', 'N/A')}",
                "Account Region": f"{r.get('server', 'N/A')}",
                }
        except ValueError as e:
            pass
            return {
                "error": "Invalid JSON response"
            }
    else:
        pass
        return {
            "error": f"Failed to fetch data: {response.status_code}"
        }
####################################
def gen_msg(packet, content):
	content = content.encode("utf-8")
	content = content.hex()	
	header = packet[0:8]
	packetLength = packet[8:10]
	packetBody = packet[10:32]
	pyloadbodyLength = packet[32:34]
	pyloadbody2 = packet[34:62]
	pyloadlength = packet[62:64]	
	pyloadtext= re.findall(r"{}(.*?)28".format(pyloadlength) , packet[50:])[0]
	pyloadTile = packet[int(int(len(pyloadtext))+64):]	
	NewTextLength = (hex((int(f"0x{pyloadlength}", 16) - int(len(pyloadtext)//2) ) + int(len(content)//2))[2:])
	if len(NewTextLength) == 1:
		NewTextLength = "0"+str(NewTextLength)	
	NewpaketLength = hex(((int(f"0x{packetLength}", 16) - int((len(pyloadtext))//2) ) ) + int(len(content)//2) )[2:]
	NewPyloadLength = hex(((int(f"0x{pyloadbodyLength}", 16) - int(len(pyloadtext)//2)))+ int(len(content)//2) )[2:]
	NewMsgPacket = header + NewpaketLength + packetBody + NewPyloadLength + pyloadbody2 + NewTextLength + content + pyloadTile
	return str(NewMsgPacket)	
def gen_msgv2(packet , replay):
	replay = replay.encode('utf-8')
	replay = replay.hex()		
	hedar = packet[0:8]
	packetLength = packet[8:10] #
	paketBody = packet[10:32]
	pyloadbodyLength = packet[32:34]
	pyloadbody2= packet[34:60]	
	pyloadlength = packet[60:62]
	pyloadtext= re.findall(r'{}(.*?)28'.format(pyloadlength) , packet[50:])[0]
	pyloadTile = packet[int(int(len(pyloadtext))+62):]	
	NewTextLength = (hex((int(f'0x{pyloadlength}', 16) - int(len(pyloadtext)//2) ) + int(len(replay)//2))[2:])
	if len(NewTextLength) == 1:
		NewTextLength = "0"+str(NewTextLength)
	NewpaketLength = hex(((int(f'0x{packetLength}', 16) - int((len(pyloadtext))//2) ) ) + int(len(replay)//2) )[2:]
	NewPyloadLength = hex(((int(f'0x{pyloadbodyLength}', 16) - int(len(pyloadtext)//2)))+ int(len(replay)//2) )[2:]	
	finallyPacket = hedar + NewpaketLength +paketBody + NewPyloadLength +pyloadbody2+NewTextLength+ replay + pyloadTile	
	return str(finallyPacket)	
def send_msg(sock, packet, content, delay:int):
	time.sleep(delay)
	try:
		sock.send(bytes.fromhex(gen_msg(packet, content)))
		sock.send(bytes.fromhex(gen_msgv2(packet, content)))
	except Exception as e:
		print(e)
		pass
def adjust_text_length(text, target_length=22, fill_char="20"):
    if len(text) > target_length:
        return text[:target_length]
    elif len(text) < target_length:
        fill_length = target_length - len(text)
        return text + (fill_char * (fill_length // len(fill_char)))[:fill_length]
    else:
        return text
####################################
fake_friend = False
spam_room = False
spam_inv = False
get_room_code = None
bot_true = False
packet_start = None
recode_packet = False
#CLASS SOCKES5!
SOCKS_VERSION = 5
class Proxy:
    def __init__(self):
        self.username = "bot"
        self.password = "bot"
        self.website = f"https://besto-api-enc.vercel.app/Enc/{id}?Key=Besto-K7J9"
    def fake_friend(self, client, id: str):
        if len(id) == 8:
            packet = "060000007708d4d7faba1d100620022a6b08cec2f1051a1b5b3030464630305d2b2b20202020434f4445585b3030464630305d32024d454049b00101b801e807d801d4d8d0ad03e001b2dd8dae03ea011eefbca8efbca5efbcb2efbcafefbcb3efbca8efbca9efbcadefbca1efa3bf8002fd98a8dd03900201d00201"
            packet = re.sub(r'cec2f105', id, packet)
            client.send(bytes.fromhex(packet))
        elif len(id) == 10:            
            packet = "060000006f08d4d7faba1d100620022a6308fb9db9ae061a1c5b3030464630305d2b2be385a4434f44455820205b3030464630305d32024d454040b00113b801e71cd801d4d8d0ad03e00191db8dae03ea010a5a45522d49534b494e47f00101f801911a8002fd98a8dd03900201d0020ad80221"
            packet = re.sub(r'fb9db9ae06', id, packet)
            client.send(bytes.fromhex(packet))
        else:
            print(id)
    def Encrypt_ID(self, id):
            response = requests.get(f'https://besto-api-enc.vercel.app/Enc/{id}?Key=Besto-K7J9')
            if response.status_code == 200:
                match = re.search(r"EncryPted Id : (\S+)", response.text)
                if match:
                	Enc_Iddd = match.group(1)
                	return Enc_Iddd
    def spam_invite(self, dataS, remote):
         global invit_spam
         while invit_spam:
             try:
                 for _ in range(5):
                     remote.send(dataS)
                     time.sleep(0.03)
                 time.sleep(2.1)
             except:
                 pass
    def handle_client(self, connection):
        version, nmethods = connection.recv(2)
        methods = self.get_available_methods(nmethods, connection)
        if 2 not in set(methods):
            connection.close()
            return
        connection.sendall(bytes([SOCKS_VERSION, 2]))
        if not self.verify_credentials(connection):
            return
        version, cmd, _, address_type = connection.recv(4)
        if address_type == 1:
            address = socket.inet_ntoa(connection.recv(4))
        elif address_type == 3:
            domain_length = connection.recv(1)[0]
            address = connection.recv(domain_length)
            address = socket.gethostbyname(address)
        port = int.from_bytes(connection.recv(2), 'big', signed=False)
        try:
            if cmd == 1:
                remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                remote.connect((address, port))
                bind_address = remote.getsockname()
            else:
                connection.close()
            addr = int.from_bytes(socket.inet_aton(bind_address[0]), 'big', signed=False)
            port = bind_address[1]
            reply = b''.join([
                SOCKS_VERSION.to_bytes(1, 'big'),
                int(0).to_bytes(1, 'big'),
                int(0).to_bytes(1, 'big'),
                int(1).to_bytes(1, 'big'),
                addr.to_bytes(4, 'big'),
                port.to_bytes(2, 'big')
            ])
        except Exception as e:
            reply = self.generate_failed_reply(address_type, 5)
        connection.sendall(reply)
        if reply[1] == 0 and cmd == 1:
            self.exchange_loop(connection, remote)
        connection.close()
    def squad_rom_invisible(self):
         packet_invisible = "0503000001d01fb578313150905babcef51dd24ed75fd0a24b024bd1429646114bc22e604afd35a96fbc48710b2d9cfec4378287ec829e33a78608fd2dd138d4d24a19c00fbfdc9f15c77ff86d638b34de95bd886e3075e82d3f4a3888f9b6943463022c43fb90e229f0eaf8a788f6f766d891d99eb2c37b277144923212810b3c80d1c521790154ed270f5241adc136f2a22816e0bc84fcaf79386b27559de966aa788c184d35bbbfaa03a5f08746f8db0e73b2c91ec4515d61f689a0cad30a7cbd6c325151e879dabc43d506b3240abe41bc0d6b4416c18f68ef4af2d04c381be6bf586f6b25727c0c85c03a579137e4a6c602ef6d833dabdab3eba3a5266e5a4731fbfb1720b60f124cd8fd4fa26cc7a9fb6e0a218d8809f57b204d22fa97520aeb99007c7b71c709e53ecc688c9963e0786909152fa93f06dc93085468dae34e1609f33f7dee228fb058c6efd6846b50ac54db0aebb8f5bc2f6751f9e2886dbab41cbaf5a1d8cd88e6c13a2a2a56b613a2d32179dc3f781493a5027322ac0cb1a2d3c79d49fb12ed26230e1561df43d315a27be17b5debdba757803305252b5443f3d77cd319dde9c49a72c636d93d02bdd9597168f378aa6e41d0fd545abf8bc0883f3dac11ea27166683c7111a0f329bf6b6a5"
         self.client0500.send(bytes.fromhex(packet_invisible))
    def gen_squad_6(self):
        packet_6 = f'050000032708{self.EncryptedPlayerid}100520082a9a0608dbdcd7cb251a910608{self.EncryptedPlayerid}12024d4518012005329d0508{self.EncryptedPlayerid}121ee28094cd9ecd9fcd9ee29885efbcb6efbca5efbcaeefbcafefbcade385a41a024d4520ebdd88b90628363087cbd1303832421880c38566949be061e1cea561b793e66080a89763e5bfce64480150d60158991468b7db8dae037a05ab93c5b00382011f08d1daf1eb0412054f75656973180420d487d4f0042a0808cc9d85f304100392010b0107090a0b12191a1e20229801db01a0014fc00101d001ada48aaf03e80101880203920208c205d628ae2db202aa02050801109c44aa0208080210ea3018c413aa0208080f10d836188827aa0205081710bd33aa0205082b10e432aa0205083910a070aa0205083d10c16faa02050849108439aa0205081810d836aa0205081a10d836aa0205081c10d836aa0205082010d836aa0205082210d836aa0205082110d836aa0205082310d836aa0205083110e432aa0205084110d836aa0205084d10e432aa0205081b10d836aa0205083410d836aa0205082810e432aa0205082910e432c202cd0112041a0201041a730848121301040506070203f1a802f4a802f2a802f3a8021a0b080110031886032086ac021a0b0802100418810420c59a081a0b0803100418da0620ecb4051a06080520f5ec021a0d08f1a802100318b80320def0041a0d08f2a802100318bc0520d0e90a1a0d08f3a802100318ef032092c9051a1208501201631a0b0863100e188f0420eeba0d1a1b0851120265661a09086520a6910128e7021a08086620822d289e05221f121d65ed0e890ed9049103f503ad02f90abd05e907a1068507cd08950ab109d802a6a38daf03ea020410011801f202080885cab5ee01105c8a0300920300980398e0b3af0ba20319efbca334e385a4eaa884e385a4efbcb4efbca5efbca1efbcada80368b00301c2030a081c100f180320052801e203014fea03003a011a403e50056801721e313733303239333438313635343436323834305f6c646a72387477723378880180909beaf3d18fd919a20100b001e201ea010449444331fa011e313733303239333438313635343436363239355f6f747735637831756c6d050000031e08{self.EncryptedPlayerid}1005203a2a910608{self.EncryptedPlayerid}12024d4518012005329d0508{self.EncryptedPlayerid}121ee28094cd9ecd9fcd9ee29885efbcb6efbca5efbcaeefbcafefbcade385a41a024d4520ebdd88b90628363087cbd1303832421880c38566949be061e1cea561b793e66080a89763e5bfce64480150d60158991468b7db8dae037a05ab93c5b00382011f08d1daf1eb0412054f75656973180420d487d4f0042a0808cc9d85f304100392010b0107090a0b12191a1e20229801db01a0014fc00101d001ada48aaf03e80101880203920208c205d628ae2db202aa02050801109c44aa0208080210ea3018c413aa0208080f10d836188827aa0205081710bd33aa0205082b10e432aa0205083910a070aa0205083d10c16faa02050849108439aa0205081810d836aa0205081a10d836aa0205081c10d836aa0205082010d836aa0205082210d836aa0205082110d836aa0205082310d836aa0205083110e432aa0205084110d836aa0205084d10e432aa0205081b10d836aa0205083410d836aa0205082810e432aa0205082910e432c202cd0112041a0201041a730848121301040506070203f1a802f4a802f2a802f3a8021a0b080110031886032086ac021a0b0802100418810420c59a081a0b0803100418da0620ecb4051a06080520f5ec021a0d08f1a802100318b80320def0041a0d08f2a802100318bc0520d0e90a1a0d08f3a802100318ef032092c9051a1208501201631a0b0863100e188f0420eeba0d1a1b0851120265661a09086520a6910128e7021a08086620822d289e05221f121d65ed0e890ed9049103f503ad02f90abd05e907a1068507cd08950ab109d802a6a38daf03ea020410011801f202080885cab5ee01105c8a0300920300980398e0b3af0ba20319efbca334e385a4eaa884e385a4efbcb4efbca5efbca1efbcada80368b00301c2030a081c100f180320052801e203014fea03003a011a403e50056801721e313733303239333438313635343436323834305f6c646a72387477723378880180909beaf3d18fd919a20100b001e201ea010449444331fa011e313733303239333438313635343436363239355f6f747735637831756c6d'
        self.client0500.send(bytes.fromhex(packet_6))
    def gen_squad_5(self):
         packet_5 = f"05000001ff08{self.EncryptedPlayerid}1005203a2af20308{self.EncryptedPlayerid}12024d451801200432f70208{self.EncryptedPlayerid}1209424c52585f4d6f642b1a024d4520d78aa5b40628023085cbd1303832421880c38566fa96e660c19de061d998a36180a89763aab9ce64480150c90158e80792010801090a12191a1e209801c901c00101e801018802039202029603aa0208080110e43218807daa0207080f10e4322001aa0205080210e432aa0205081810e432aa0205081a10e432aa0205081c10e432aa0205082010e432aa0205082210e432aa0205082110e432aa0205081710e432aa0205082310e432aa0205082b10e432aa0205083110e432aa0205083910e432aa0205083d10e432aa0205084110e432aa0205084910e432aa0205084d10e432aa0205081b10e432aa0205083410e432aa0205082810e432aa0205082910e432c2022812041a0201041a0508501201631a060851120265661a0f0848120b0104050607f1a802f4a8022200ea0204100118018a03009203009803b7919db30ba20319c2b27854e19687e197a95fe191ade192aae197a95945e19687e20301523a011a403e50056801721e313732303237323231313638373535353930315f736f3278687a61366e347801820103303b30880180e0aecdacceba8e19a20100b00114ea010449444332fa011e313732303237323231313638373535383330335f71356f79736b3934716d"
         self.client0500.send(bytes.fromhex(packet_5))
    def adding_1mG_16kD(self):
        packet_1m_16k_GD = "080000001608edaae28710100820022a0a08bfda5b10fe7d18c801"
        self.client0500.send(bytes.fromhex(packet_1m_16k_GD))
    def adding_gold(self):
         packet_gold = f"080000001308{self.EncryptedPlayerid}100820022a0708a6b10318fa01"
         self.client0500.send(bytes.fromhex(packet_gold))
    def adding_daimond(self):
         packet_diamond = f"080000001608edaae28710100820022a0a08e7be0110b24f18c801"
         self.client0500.send(bytes.fromhex(packet_diamond))
    def adding_youtoubrs(self):
                    yout1 = b"\x06\x00\x00\x00{\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*o\x08\x81\x80\x83\xb6\x01\x1a)[f50057]\xd8\xb5\xd8\xa7\xd8\xa6\xd8\xaf\xe3\x85\xa4\xd8\xa7\xd9\x84\xd8\xa8\xd9\x87\xd8\xa7\xd8\xa6\xd9\x85[f50057]2\x02ME@N\xb0\x01\x13\xb8\x01\xdc)\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\tAO'-'TEAM\xf0\x01\x01\xf8\x01\xdc\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x11\xd8\x02F";yout2 = b'\x06\x00\x00\x00|\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*p\x08\xd6\xd1\xb9(\x1a![f50057]\xef\xbc\xa8\xef\xbc\xac\xe3\x85\xa4Hassone.[f50057]2\x02ME@G\xb0\x01\x13\xb8\x01\xcf\x1e\xd8\x01\xcc\xd6\xd0\xad\x03\xe0\x01\xed\xdc\x8d\xae\x03\xea\x01\x1d\xef\xbc\xb4\xef\xbc\xa8\xef\xbc\xa5\xe3\x85\xa4\xef\xbc\xa8\xef\xbc\xa5\xef\xbc\xac\xef\xbc\xac\xe0\xbf\x90\xc2\xb9\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01';yout3 = b'\x06\x00\x00\x00x\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*l\x08\xe9\xa7\xe9\x1b\x1a [ff00ff]DS\xe3\x85\xa4WAJIHANO\xe3\x85\xa4[ff00ff]2\x02ME@Q\xb0\x01\x14\xb8\x01\xca2\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x10.DICTATORS\xe3\x85\xa4\xe2\x88\x9a\xf0\x01\x01\xf8\x01\xc4\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02+';yout4 = b'\x06\x00\x00\x00z\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*n\x08\xed\xd4\xa7\xa2\x02\x1a\x1f[f50057]M8N\xe3\x85\xa4y\xe3\x85\xa4Fouad[f50057]2\x02ME@O\xb0\x01\x13\xb8\x01\xa9#\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xdb\xdb\x8d\xae\x03\xea\x01\x0cGREAT\xe2\x80\xbfWALL\xf0\x01\x01\xf8\x01b\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\r\xd8\x023\xe0\x02\xc1\xb7\xf8\xb1\x03';yout5 = b"\x06\x00\x00\x00\x84\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*x\x08\xb6\xc0\xf1\xcc\x01\x1a'[f50057]\xd9\x85\xd9\x84\xd9\x83\xd8\xa9*\xd9\x84\xd9\x85\xd8\xb9\xd9\x88\xd9\x82\xd9\x8a\xd9\x86[f50057]2\x02ME@G\xb0\x01\x05\xb8\x01\x82\x0b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x15\xe9\xbf\x84\xef\xbc\xac\xef\xbc\xaf\xef\xbc\xb2\xef\xbc\xa4\xef\xbc\xb3\xe9\xbf\x84\xf0\x01\x01\xf8\x01>\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x05\xd8\x02\x0e";yout6 = b'\x06\x00\x00\x00\x8e\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x81\x01\x08\xeb\x98\x88\x8e\x01\x1a"[f50057]OP\xe3\x85\xa4BNL\xe3\x85\xa4\xe2\x9a\xa1\xe3\x85\xa4*[f50057]2\x02ME@R\xb0\x01\x10\xb8\x01\xce\x16\xd8\x01\x84\xf0\xd2\xad\x03\xe0\x01\xa8\xdb\x8d\xae\x03\xea\x01\x1f\xe1\xb4\x8f\xe1\xb4\xa0\xe1\xb4\x87\xca\x80\xe3\x85\xa4\xe1\xb4\x98\xe1\xb4\x8f\xe1\xb4\xa1\xe1\xb4\x87\xca\x80\xe2\x9a\xa1\xf0\x01\x01\xf8\x01A\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01\xe0\x02\xf3\x94\xf6\xb1\x03';yout7 = b"\x06\x00\x00\x00\x8e\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x81\x01\x08\xb0\xa4\xdb\x80\x01\x1a'[f50057]\xd9\x85\xd9\x83\xd8\xa7\xd9\x81\xd8\xad\xd8\xa9.\xe2\x84\x93\xca\x99\xe3\x80\xb5..[f50057]2\x02ME@T\xb0\x01\x13\xb8\x01\xfc$\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xc1\xdb\x8d\xae\x03\xea\x01\x1d\xef\xbc\xad\xef\xbc\xa1\xef\xbc\xa6\xef\xbc\xa9\xef\xbc\xa1\xe3\x85\xa4\xe2\x8e\xb0\xe2\x84\x93\xca\x99\xe2\x8e\xb1\xf0\x01\x01\xf8\x01\xdb\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0f\xd8\x02>";yout8 = b'\x06\x00\x00\x00y\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*m\x08\xfd\x8a\xde\xb4\x02\x1a\x1f[f50057]ITZ\xe4\xb8\xb6MOHA\xe3\x85\xa42M[f50057]2\x02ME@C\xb0\x01\n\xb8\x01\xdf\x0f\xd8\x01\xac\xd8\xd0\xad\x03\xe0\x01\xf2\xdc\x8d\xae\x03\xea\x01\x15\xe3\x80\x9dITZ\xe3\x80\x9e\xe1\xb5\x97\xe1\xb5\x89\xe1\xb5\x83\xe1\xb5\x90\xf8\x01\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0e\xd8\x026';yout9 = b'\x06\x00\x00\x00w\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*k\x08\xc6\x99\xddp\x1a\x1b[f50057]HEROSHIIMA1[f50057]2\x02ME@I\xb0\x01\x01\xb8\x01\xe8\x07\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1e\xef\xbc\xa8\xef\xbc\xa5\xef\xbc\xb2\xef\xbc\xaf\xef\xbc\xb3\xef\xbc\xa8\xef\xbc\xa9\xef\xbc\xad\xef\xbc\xa1\xef\xa3\xbf\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01';yout10 = b'\x06\x00\x00\x00p\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*d\x08\xde\x91\xb7Q\x1a\x1c[f50057]SH\xe3\x85\xa4SHIMA|M[f50057]2\x02ME@R\xb0\x01\x14\xb8\x01\xe7C\xd8\x01\xdd\xd6\xd0\xad\x03\xe0\x01\xca\xdb\x8d\xae\x03\xea\x01\tSH\xe3\x85\xa4Team\xf8\x014\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x11\xd8\x02G\xe0\x02\x89\xa0\xf8\xb1\x03';yout11 = b'\x06\x00\x00\x00h\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\\\x08\xa1\x9f\xb3\xf4\x01\x1a\x1b[f50057]2JZ\xe3\x85\xa4POWER[f50057]2\x02ME@M\xb0\x01\x13\xb8\x01\xa5(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xec\xdb\x8d\xae\x03\xf0\x01\x01\xf8\x01\x9a\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02.\xe0\x02\xb2\xe9\xf7\xb1\x03';yout12 = b'\x06\x00\x00\x00\x8f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x82\x01\x08\xaa\xe5\xa4\xe3\x01\x1a-[f50057]\xe3\x85\xa4\xd8\xb4\xd9\x83\xd8\xa7\xd9\x8e\xd9\x83\xd9\x80\xd9\x8a\xe3\x80\x8e\xe2\x85\xb5\xe1\xb4\x98\xe3\x80\x8f[f50057]2\x02ME@Q\xb0\x01\x13\xb8\x01\xf2*\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xaf\xdb\x8d\xae\x03\xea\x01\x15\xe2\x80\xa2\xe3\x85\xa4\xe2\x93\x8b\xe2\x92\xbe\xe2\x93\x85\xe3\x85\xa4\xe2\x80\xa2\xf8\x01q\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02e\xe0\x02\xa0\xf1\xf7\xb1\x03';yout13 = b'\x06\x00\x00\x00`\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*T\x08\xd2\xbc\xae\x07\x1a%[f50057]SYBLUS\xe3\x85\xa4\xe4\xba\x97\xe3\x85\xa4\xe3\x85\xa4\xe3\x85\xa4[f50057]2\x02ME@E\xb0\x01\x01\xb8\x01\xe8\x07\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01';yout14 = b'\x06\x00\x00\x00\x86\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*z\x08\xfd\x8b\xf4\xfa\x01\x1a$[f50057]"\xd8\xaf\xd8\xb1\xd8\xa7\xd8\xba\xd9\x88\xd9\x86\xd9\x80\xd9\x88\xd9\x81"[f50057]2\x02ME@F\xb0\x01\x13\xb8\x01\xec \xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x12\xe1\xb4\x98\xe1\xb4\x84\xe1\xb5\x80\xe1\xb5\x89\xe1\xb5\x83\xe1\xb5\x90\xf0\x01\x01\xf8\x01\xb0\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x04\xd8\x02\t\xe0\x02\xf2\x94\xf6\xb1\x03';yout15 = b'\x06\x00\x00\x00\x7f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*s\x08\x90\xf6\x87\x15\x1a"[f50057]V4\xe3\x85\xa4RIO\xe3\x85\xa46%\xe3\x85\xa4zt[f50057]2\x02ME@M\xb0\x01\x13\xb8\x01\x95&\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb1\xdd\x8d\xae\x03\xea\x01\x0e\xe1\xb4\xa0\xe1\xb4\x80\xe1\xb4\x8d\xe1\xb4\x8f\xd1\x95\xf0\x01\x01\xf8\x01\xe2\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02^\xe0\x02\x85\xff\xf5\xb1\x03';yout16 = b'\x06\x00\x00\x00s\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*g\x08\xaa\x84\xc1r\x1a\x1f[f50057]SA777RAWI\xe3\x85\xa4\xe3\x85\xa4[f50057]2\x02ME@N\xb0\x01\x13\xb8\x01\xc8\x1b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x0cSA7RAWI\xe3\x85\xa4TM\xf0\x01\x01\xf8\x01\xfe\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\t\xd8\x02 ';yout17 = b'\x06\x00\x00\x00y\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*m\x08\xe7\xbf\xb6\x8f\x01\x1a\x1c[f50057]SVG.NINJA\xe2\xbc\xbd[f50057]2\x02ME@I\xb0\x01\x13\xb8\x01\x94\x1b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x85\xdb\x8d\xae\x03\xea\x01\x15\xe3\x85\xa4\xe3\x85\xa4\xe3\x85\xa4\xe3\x85\xa4???\xe3\x85\xa4\xe3\x85\xa4\xf0\x01\x01\xf8\x01o\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x10\xd8\x02?';yout18 = b"\x06\x00\x00\x00\x9d\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x90\x01\x08\xa8\xe8\x91\xd7\x01\x1a.[f50057]\xef\xbc\xa1\xef\xbc\xac\xef\xbc\x93\xef\xbc\xab\xef\xbc\xa5\xef\xbc\xa4\xe4\xba\x97\xef\xbc\xb9\xef\xbc\xb4\xe3\x85\xa4[f50057]2\x02ME@N\xb0\x01\x13\xb8\x01\x97'\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1e\xef\xbc\xa1\xef\xbc\xac\xef\xbc\x93\xef\xbc\xab\xef\xbc\xa5\xef\xbc\xa4\xe2\x80\xa2\xef\xbc\xb9\xef\xbc\xb4\xe2\x9c\x93\xf0\x01\x01\xf8\x01\xab\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x10\xd8\x02@\xe0\x02\xe9\x80\xf8\xb1\x03";yout19 = b'\x06\x00\x00\x00r\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*f\x08\x9b\x94\xaa\r\x1a\x1c[f50057]FARAMAWY_1M.[f50057]2\x02ME@I\xb0\x01\x01\xb8\x01\xe8\x07\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x12\xe2\x80\xa2\xe3\x85\xa4STRONG\xe3\x85\xa4\xe2\x80\xa2\xf0\x01\x01\xf8\x01X\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01';yout20 = b'\x06\x00\x00\x00p\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*d\x08\xde\x91\xb7Q\x1a\x1c[f50057]SH\xe3\x85\xa4SHIMA|M[f50057]2\x02ME@R\xb0\x01\x14\xb8\x01\xe7C\xd8\x01\xdd\xd6\xd0\xad\x03\xe0\x01\xca\xdb\x8d\xae\x03\xea\x01\tSH\xe3\x85\xa4Team\xf8\x014\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x11\xd8\x02G\xe0\x02\x89\xa0\xf8\xb1\x03';yout21 = b'\x06\x00\x00\x00h\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\\\x08\xa1\x9f\xb3\xf4\x01\x1a\x1b[f50057]2JZ\xe3\x85\xa4POWER[f50057]2\x02ME@M\xb0\x01\x13\xb8\x01\xa5(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xec\xdb\x8d\xae\x03\xf0\x01\x01\xf8\x01\x9a\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02.\xe0\x02\xb2\xe9\xf7\xb1\x03';yout22 = b'\x06\x00\x00\x00\x8f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x82\x01\x08\xaa\xe5\xa4\xe3\x01\x1a-[f50057]\xe3\x85\xa4\xd8\xb4\xd9\x83\xd8\xa7\xd9\x8e\xd9\x83\xd9\x80\xd9\x8a\xe3\x80\x8e\xe2\x85\xb5\xe1\xb4\x98\xe3\x80\x8f[f50057]2\x02ME@Q\xb0\x01\x13\xb8\x01\xf2*\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xaf\xdb\x8d\xae\x03\xea\x01\x15\xe2\x80\xa2\xe3\x85\xa4\xe2\x93\x8b\xe2\x92\xbe\xe2\x93\x85\xe3\x85\xa4\xe2\x80\xa2\xf8\x01q\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02e\xe0\x02\xa0\xf1\xf7\xb1\x03';yout23 = b'\x06\x00\x00\x00\x86\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*z\x08\xfd\x8b\xf4\xfa\x01\x1a$[f50057]"\xd8\xaf\xd8\xb1\xd8\xa7\xd8\xba\xd9\x88\xd9\x86\xd9\x80\xd9\x88\xd9\x81"[f50057]2\x02ME@F\xb0\x01\x13\xb8\x01\xec \xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x12\xe1\xb4\x98\xe1\xb4\x84\xe1\xb5\x80\xe1\xb5\x89\xe1\xb5\x83\xe1\xb5\x90\xf0\x01\x01\xf8\x01\xb0\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x04\xd8\x02\t\xe0\x02\xf2\x94\xf6\xb1\x03';yout24 = b'\x06\x00\x00\x00s\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*g\x08\xaa\x84\xc1r\x1a\x1f[f50057]SA777RAWI\xe3\x85\xa4\xe3\x85\xa4[f50057]2\x02ME@N\xb0\x01\x13\xb8\x01\xc8\x1b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x0cSA7RAWI\xe3\x85\xa4TM\xf0\x01\x01\xf8\x01\xfe\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\t\xd8\x02 ';yout25 = b'\x06\x00\x00\x00y\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*m\x08\xe7\xbf\xb6\x8f\x01\x1a\x1c[f50057]SVG.NINJA\xe2\xbc\xbd[f50057]2\x02ME@I\xb0\x01\x13\xb8\x01\x94\x1b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x85\xdb\x8d\xae\x03\xea\x01\x15\xe3\x85\xa4\xe3\x85\xa4\xe3\x85\xa4\xe3\x85\xa4???\xe3\x85\xa4\xe3\x85\xa4\xf0\x01\x01\xf8\x01o\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x10\xd8\x02?';yout26 = b"\x06\x00\x00\x00\x9d\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x90\x01\x08\xa8\xe8\x91\xd7\x01\x1a.[f50057]\xef\xbc\xa1\xef\xbc\xac\xef\xbc\x93\xef\xbc\xab\xef\xbc\xa5\xef\xbc\xa4\xe4\xba\x97\xef\xbc\xb9\xef\xbc\xb4\xe3\x85\xa4[f50057]2\x02ME@N\xb0\x01\x13\xb8\x01\x97'\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1e\xef\xbc\xa1\xef\xbc\xac\xef\xbc\x93\xef\xbc\xab\xef\xbc\xa5\xef\xbc\xa4\xe2\x80\xa2\xef\xbc\xb9\xef\xbc\xb4\xe2\x9c\x93\xf0\x01\x01\xf8\x01\xab\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x10\xd8\x02@\xe0\x02\xe9\x80\xf8\xb1\x03";yout27 = b'\x06\x00\x00\x00r\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*f\x08\x9b\x94\xaa\r\x1a\x1c[f50057]FARAMAWY_1M.[f50057]2\x02ME@I\xb0\x01\x01\xb8\x01\xe8\x07\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x12\xe2\x80\xa2\xe3\x85\xa4STRONG\xe3\x85\xa4\xe2\x80\xa2\xf0\x01\x01\xf8\x01X\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01';yout28 = b"\x06\x00\x00\x00\x82\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*v\x08\xaa\xdd\xf1'\x1a\x1d[f50057]BM\xe3\x85\xa4ABDOU_YT[f50057]2\x02ME@G\xb0\x01\x13\xb8\x01\xd4$\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1d\xe2\x80\xa2\xc9\xae\xe1\xb4\x87\xca\x9f\xca\x9f\xe1\xb4\x80\xca\x8d\xe1\xb4\x80\xd2\x93\xc9\xaa\xe1\xb4\x80\xc2\xb0\xf0\x01\x01\xf8\x01\x8e\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x07\xd8\x02\x16";yout29 = b'\x06\x00\x00\x00r\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*f\x08\x9a\xd6\xdcL\x1a-[f50057]\xe1\xb4\x8d\xcd\xa1\xcd\x9co\xe3\x85\xa4\xef\xbc\xa8\xef\xbc\xa1\xef\xbc\xa6\xef\xbc\xa9\xef\xbc\xa4\xef\xbc\xa9[f50057]2\x02ME@H\xb0\x01\x01\xb8\x01\xe8\x07\xea\x01\x15\xe1\xb4\x8d\xcd\xa1\xcd\x9co\xc9\xb4\xef\xbd\x93\xe1\xb4\x9b\xe1\xb4\x87\xca\x80\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01';yout30 = b'\x06\x00\x00\x00v\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*j\x08\xb6\x92\xa9\xc8\x01\x1a [f50057]\xef\xbc\xaa\xef\xbc\xad\xef\xbc\xb2\xe3\x85\xa4200K[f50057]2\x02ME@R\xb0\x01\x13\xb8\x01\xc3(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\n3KASH-TEAM\xf8\x012\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x06\xd8\x02\x13\xe0\x02\x89\xa0\xf8\xb1\x03';yout31 = b"\x06\x00\x00\x00\x92\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x85\x01\x08\xa2\xd3\xf4\x81\x07\x1a'[f50057]\xd8\xb3\xd9\x80\xd9\x86\xd9\x80\xd8\xaf\xd8\xb1\xd9\x8a\xd9\x84\xd8\xa71M\xe3\x85\xa4[f50057]2\x02ME@K\xb0\x01\x13\xb8\x01\xc1 \xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1a\xef\xbc\xad\xef\xbc\xa6\xef\xbc\x95\xef\xbc\xb2\xef\xbc\xa8\xe3\x85\xa4\xe1\xb4\xa0\xc9\xaa\xe1\xb4\x98\xf0\x01\x01\xf8\x01\x8c\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0e\xd8\x024\xe0\x02\x87\xff\xf5\xb1\x03";yout32 = b'\x06\x00\x00\x00|\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*p\x08\xe0\xe1\xdeu\x1a\x1a[f50057]P1\xe3\x85\xa4Fahad[f50057]2\x02ME@N\xb0\x01\x13\xb8\x01\xd0&\xd8\x01\xea\xd6\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1a\xe3\x85\xa4\xef\xbc\xb0\xef\xbc\xa8\xef\xbc\xaf\xef\xbc\xa5\xef\xbc\xae\xef\xbc\xa9\xef\xbc\xb8\xc2\xb9\xf0\x01\x01\xf8\x01\x9e\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0b\xd8\x02*';yout33 = b'\x06\x00\x00\x00\x82\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*v\x08\xc5\xcf\x94\x8b\x02\x1a\x18[f50057]@EL9YSAR[f50057]2\x02ME@P\xb0\x01\x13\xb8\x01\x86+\xd8\x01\xa2\xd7\xd0\xad\x03\xe0\x01\x89\xae\x8f\xae\x03\xea\x01\x1d-\xc9\xaa\xe1\xb4\x8d\xe1\xb4\x8d\xe1\xb4\x8f\xca\x80\xe1\xb4\x9b\xe1\xb4\x80\xca\x9fs\xe2\xac\x86\xef\xb8\x8f\xf8\x01j\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x14\xd8\x02\xe2\x02\xe0\x02\x9f\xf1\xf7\xb1\x03';yout34 = b'\x06\x00\x00\x00x\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*l\x08\xa9\x81\xe6^\x1a\x1e[f50057]STRONG\xe3\x85\xa4CRONA[f50057]2\x02ME@J\xb0\x01\x13\xb8\x01\xd8$\xd8\x01\xd8\xd6\xd0\xad\x03\xe0\x01\x92\xdb\x8d\xae\x03\xea\x01\x12\xe2\x80\xa2\xe3\x85\xa4STRONG\xe3\x85\xa4\xe2\x80\xa2\xf0\x01\x01\xf8\x01q\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x14\xd8\x02\xbc\x01';yout35 = b'\x06\x00\x00\x00\x7f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*s\x08\xeb\x8d\x97\xec\x01\x1a&[f50057]\xd8\xb9\xd9\x80\xd9\x85\xd9\x80\xd8\xaf\xd9\x86\xd9\x8a\xd9\x80\xd8\xaa\xd9\x80\xd9\x88[f50057]2\x02ME@F\xb0\x01\x13\xb8\x01\xd3\x1a\xd8\x01\xaf\xd7\xd0\xad\x03\xe0\x01\xf4\xdc\x8d\xae\x03\xea\x01\rOSIRIS\xe3\x85\xa4MASR\xf8\x01o\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02\\\xe0\x02\xf4\x94\xf6\xb1\x03';yout36 = b'\x06\x00\x00\x00\x7f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*s\x08\xb4\xff\xa3\xef\x01\x1a\x1c[f50057]ZAIN_YT_500K[f50057]2\x02ME@K\xb0\x01\x13\xb8\x01\xa3#\xd8\x01\xa2\xd7\xd0\xad\x03\xe0\x01\xbb\xdb\x8d\xae\x03\xea\x01\x1b\xe1\xb6\xbb\xe1\xb5\x83\xe1\xb6\xa4\xe1\xb6\xb0\xe3\x85\xa4\xe1\xb5\x97\xe1\xb5\x89\xe1\xb5\x83\xe1\xb5\x90\xf0\x01\x01\xf8\x01\\\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0b\xd8\x02(';yout37 = b'\x06\x00\x00\x00\x8f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x82\x01\x08\x86\xa7\x9e\xa7\x0b\x1a([f50057]\xe2\x80\x94\xcd\x9e\xcd\x9f\xcd\x9e\xe2\x98\x85\xef\xbc\xa2\xef\xbc\xac\xef\xbc\xb2\xef\xbc\xb8[f50057]2\x02ME@d\xb0\x01\x13\xb8\x01\xe3\x1c\xe0\x01\xf2\x83\x90\xae\x03\xea\x01!\xe3\x85\xa4\xef\xbc\xa2\xef\xbc\xac\xef\xbc\xb2\xef\xbc\xb8\xe3\x85\xa4\xef\xbc\xb4\xef\xbc\xa5\xef\xbc\xa1\xef\xbc\xad\xe3\x85\xa4\xf8\x01u\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02Y\xe0\x02\xc1\xb7\xf8\xb1\x03';yout38 = b'\x06\x00\x00\x00\x85\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*y\x08\xc3\xcf\xe5H\x1a([f50057]\xe3\x85\xa4BEE\xe2\x9c\xbfSTO\xe3\x85\xa4\xe1\xb5\x80\xe1\xb4\xb5\xe1\xb4\xb7[f50057]2\x02ME@Q\xb0\x01\x14\xb8\x01\xffP\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xc1\xdb\x8d\xae\x03\xea\x01\x15TIK\xe2\x9c\xbfTOK\xe1\xb5\x80\xe1\xb4\xb1\xe1\xb4\xac\xe1\xb4\xb9\xf0\x01\x01\xf8\x01\xc8\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02q';yout39 = b'\x06\x00\x00\x00\x94\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x87\x01\x08\x97\xd5\x9a.\x1a%[f50057]\xd8\xb9\xd9\x86\xd9\x83\xd9\x88\xd8\xb4\xe1\xb4\x80\xc9\xb4\xe1\xb4\x8b\xe3\x85\xa4[f50057]2\x02ME@P\xb0\x01\x13\xb8\x01\xe8(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1f\xe1\xb4\x80\xc9\xb4\xe1\xb4\x8b\xe1\xb4\x9c\xea\x9c\xb1\xca\x9c\xe3\x85\xa4\xe1\xb4\x9b\xe1\xb4\x87\xe1\xb4\x80\xe1\xb4\x8d\xf0\x01\x01\xf8\x01\xb6\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\n\xd8\x02"\xe0\x02\xf2\x94\xf6\xb1\x03';yout40 = b'\x06\x00\x00\x00\x8a\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*~\x08\xf7\xdf\xda\\\x1a/[f50057]\xef\xbc\xa1\xef\xbc\xac\xef\xbc\xa8\xef\xbc\xaf\xef\xbc\xad\xef\xbc\xb3\xef\xbc\xa9_\xef\xbc\xb9\xef\xbc\xb4\xe2\x9c\x93[f50057]2\x02ME@P\xb0\x01\x13\xb8\x01\xb9*\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xc1\xdb\x8d\xae\x03\xea\x01\x0cALHOMSI~TEAM\xf0\x01\x01\xf8\x01\x8e\x0e\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02S\xe0\x02\xc3\xb7\xf8\xb1\x03';yout41 = b'\x06\x00\x00\x00\x86\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*z\x08\xb5\xdd\xec\x8e\x01\x1a%[f50057]\xd8\xa7\xd9\x88\xd9\x81\xe3\x80\x80\xd9\x85\xd9\x86\xd9\x83\xe3\x85\xa4\xe2\x9c\x93[f50057]2\x02ME@K\xb0\x01\x13\xb8\x01\xdd#\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x18\xef\xbc\xaf\xef\xbc\xa6\xe3\x85\xa4\xef\xbc\xb4\xef\xbc\xa5\xef\xbc\xa1\xef\xbc\xad\xe3\x85\xa4\xf0\x01\x01\xf8\x01\xe8\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02Q';yout42 = b'\x06\x00\x00\x00\x8b\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x7f\x08\x81\xf4\xba\xf8\x01\x1a%[f50057]\xef\xbc\xa7\xef\xbc\xa2\xe3\x85\xa4\xef\xbc\xae\xef\xbc\xaf\xef\xbc\x91\xe3\x81\x95[f50057]2\x02ME@N\xb0\x01\x0c\xb8\x01\xbd\x11\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb1\xdd\x8d\xae\x03\xea\x01\x1a\xef\xbc\xa7\xef\xbc\xb2\xef\xbc\xa5\xef\xbc\xa1\xef\xbc\xb4__\xef\xbc\xa2\xef\xbc\xaf\xef\xbc\xb9\xf8\x018\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02-\xe0\x02\x85\xff\xf5\xb1\x03';yout43 = b'\x06\x00\x00\x00o\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*c\x08\xfb\x9d\xb9\xae\x06\x1a\x1c[f50057]BT\xe3\x85\xa4BadroTV[f50057]2\x02ME@@\xb0\x01\x13\xb8\x01\xe7\x1c\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x91\xdb\x8d\xae\x03\xea\x01\nBadro_TV_F\xf0\x01\x01\xf8\x01\x91\x1a\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\n\xd8\x02!';yout44 = b"\x06\x00\x00\x00s\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*g\x08\xc4\xe5\xe1>\x1a'[f50057]\xd8\xb5\xd8\xa7\xd8\xa6\xd8\xaf~\xd8\xa7\xd9\x84\xd8\xba\xd9\x86\xd8\xa7\xd8\xa6\xd9\x85[f50057]2\x02ME@J\xb0\x01\x14\xb8\x01\xceP\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x03Z7F\xf0\x01\x01\xf8\x01\xd0\x19\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x14\xd8\x02\x9c\x01";yout45 = b'\x06\x00\x00\x00\x85\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*y\x08\xfd\xa4\xa6i\x1a$[f50057]\xd8\xb2\xd9\x8a\xd9\x80\xd8\xb1\xc9\xb4\xcc\xb67\xcc\xb6\xca\x80\xe3\x85\xa4[f50057]2\x02ME@M\xb0\x01\x13\xb8\x01\xe1(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x19\xc2\xb7\xe3\x85\xa4\xe3\x85\xa4N\xe3\x85\xa47\xe3\x85\xa4R\xe3\x85\xa4\xe3\x85\xa4\xc2\xb7\xf0\x01\x01\xf8\x01\x8f\t\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02k';yout46 = b'\x06\x00\x00\x00y\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*m\x08\xcc\xb9\xcc\xd4\x06\x1a"[f50057]\xd8\xa8\xd9\x88\xd8\xad\xd8\xa7\xd9\x83\xd9\x80\xd9\x80\xd9\x80\xd9\x85[f50057]2\x02ME@9\xb0\x01\x07\xb8\x01\xca\x0c\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x11*\xef\xbc\x97\xef\xbc\xaf\xef\xbc\xab\xef\xbc\xa1\xef\xbc\xad*\xf0\x01\x01\xf8\x01\xad\x05\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01';yout47 = b'\x06\x00\x00\x00e\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*Y\x08\xe8\xbd\xc9b\x1a [f50057]\xe3\x80\x8cvip\xe3\x80\x8dDR999FF[f50057]2\x02ME@Q\xb0\x01\x10\xb8\x01\x94\x16\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xf0\x01\x01\xf8\x01\xa0\x04\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02+';yout48 = b'\x06\x00\x00\x00\x82\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*v\x08\x86\xb7\x84\xf1\x01\x1a&[f50057]\xd8\xa2\xd9\x86\xd9\x8a\xd9\x80\xd9\x80\xd9\x84\xd8\xa7\xce\x92\xe2\x92\x91\xe3\x85\xa4[f50057]2\x02ME@Q\xb0\x01\x13\xb8\x01\x82)\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x13\xce\x92\xe2\x92\x91\xe3\x85\xa4MAFIA\xe3\x85\xa4\xef\xa3\xbf\xf0\x01\x01\xf8\x01\x95\x04\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02W';yout49 = b'\x06\x00\x00\x00u\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*i\x08\xb4\xbe\xde\x83\x02\x1a [f50057]SPONGEBOB!\xe3\x85\xa4\xe4\xba\x97[f50057]2\x02ME@N\xb0\x01\x14\xb8\x01\x842\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x96\xdb\x8d\xae\x03\xea\x01\x0cALHOMSI~TEAM\xf0\x01\x01\xf8\x01\xbd\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02{';yout50 = b'\x06\x00\x00\x00u\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*i\x08\xb4\xbe\xde\x83\x02\x1a [f50057]SPONGEBOB!\xe3\x85\xa4\xe4\xba\x97[f50057]2\x02ME@N\xb0\x01\x14\xb8\x01\x842\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x96\xdb\x8d\xae\x03\xea\x01\x0cALHOMSI~TEAM\xf0\x01\x01\xf8\x01\xbd\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02{'
                    yout_list = [yout1,yout2,yout3,yout4,yout5,yout6,yout7,yout8,yout9,yout10,yout11,yout12,yout13,yout14,yout15,yout16,yout17,yout18,yout19,yout20,yout21,yout22,yout23,yout24,yout25,yout26,yout27,yout28,yout29,yout30,yout31,yout32,yout33,yout34,yout35,yout36,yout37,yout38,yout39,yout40,yout41,yout42,yout43,yout44,yout45,yout46,yout47,yout48,yout49,yout50]
                    for y in yout_list:
                    		self.client0500.send(y)
                    
    def Msg_Help_En(self):
        message_en = f"1200000eae08{self.EncryptedPlayerid}101220022aa11d08{self.EncryptedPlayerid}10{self.EncryptedPlayerid}22f91b0a5b3837434545425d5b635d5b625d435b3030424646465d5b635d5b625d4f5b3145393046465d5b635d5b625d445b3030303046465d5b635d5b625d455b3030303038425d5b635d5b625d58205b3837434545425d5b635d5b625d545b3030424646465d5b635d5b625d455b3145393046465d5b635d5b625d415b3030303046465d5b635d5b625d4d0a5b3837434545425d5b635d5b625d3d2d3d2d3d2d3d2d3d2d3d2d3d2d3d2d3d2d3d2d3d2d3d2d3d2d3d2d0a0a5b4646464646465d5b625d4669727374204d656e753a0a0a5b3145393046465d5b625d506c6179657220496e666f726d6174696f6e3a0a5b3837434545425d5b635d5b625d202020e2949ce29480e29480205b3837434545425d5b635d5b625d466f726d61743a202f696e666f203c7569643e0a5b3837434545425d5b635d5b625d202020e29494e29480e29480205b3837434545425d5b635d5b625d4578616d706c653a202f696e666f2b31323334353637380a0a5b3145393046465d5b625d436865636b20506c617965722773205365727665723a0a5b3837434545425d5b635d5b625d202020e2949ce29480e29480205b3837434545425d5b635d5b625d466f726d61743a202f726567696f6e203c7569643e0a5b3837434545425d5b635d5b625d202020e29494e29480e29480205b3837434545425d5b635d5b625d4578616d706c653a202f726567696f6e2b31323334353637380a0a5b4646464646465d5b625d5365636f6e64204d656e753a0a0a5b3145393046465d5b625d466f726365204a6f696e3a0a5b3837434545425d5b635d5b625d202020e2949ce29480e29480205b3837434545425d5b635d5b625d466f726d61743a202f7265636f72640a5b3837434545425d5b635d5b625d202020e2949ce29480e29480205b3837434545425d5b635d5b625d466f726d61743a202f73746172740a5b3837434545425d5b635d5b625d202020e29494e29480e29480205b3837434545425d5b635d5b625d4578616d706c653a202f73746172740a0a5b4646464646465d5b625d5468697264204d656e753a0a5b3145393046465d5b635d5b625d46657463682044616e63652062792049443a0a2020e2949ce29480e29480205b3837434545425d5b635d5b625d4578616d706c653a2040454d545b69645d0a5b3145393046465d5b635d5b625d44616e636520776974682048616e64733a0a2020e2949ce29480e294805b3837434545425d5b635d5b625d4578616d706c653a202f64732f5b69645d0a5b3145393046465d5b635d5b625d53717561642044616e636520776974682048616e64733a0a2020e2949ce29480e294805b3837434545425d5b635d5b625d4578616d706c653a202f64732f5b69645d2f5b69645d2f5b69645d2f5b69645d0a5b3145393046465d5b635d5b625d3730204e65772044616e6365733a0a2020e2949ce29480e294805b3837434545425d5b635d5b625d4578616d706c653a202f656d6f74657331202d3e202f656d6f74657337300a0a5b3145393046465d5b625d52657065617420596f7572204d65737361676520576974686f75742042616e3a0a5b3837434545425d5b635d5b625d202020e2949ce29480e29480205b3837434545425d5b635d5b625d466f726d61743a202f73706d203c6d6573736167653e0a5b3837434545425d5b635d5b625d202020e29494e29480e29480205b3837434545425d5b635d5b625d4578616d706c653a202f73706d206869690a0a5b3145393046465d5b625d41646420596f755475626572733a0a5b3837434545425d5b635d5b625d202020e2949ce29480e29480205b3837434545425d5b635d5b625d466f726d61743a202f464f582d59540a5b3837434545425d5b635d5b625d202020e29494e29480e29480205b3837434545425d5b635d5b625d4578616d706c653a202f464f582d59540a0a5b3145393046465d5b625d4164642046616b6520467269656e64205573696e672049443a0a5b3837434545425d5b635d5b625d202020e2949ce29480e29480205b3837434545425d5b635d5b625d466f726d61743a202f616464203c7569643e0a5b3837434545425d5b635d5b625d202020e29494e29480e29480205b3837434545425d5b635d5b625d4578616d706c653a202f6164642031323334353637380a0a5b3145393046465d5b625d4164642031204d696c6c696f6e20476f6c6420616e642031364b2047656d733a0a5b3837434545425d5b635d5b625d202020e2949ce29480e29480205b3837434545425d5b635d5b625d466f726d61743a202f47440a5b3837434545425d5b635d5b625d202020e29494e29480e29480205b3837434545425d5b635d5b625d4578616d706c653a202f47440a0a5b3145393046465d5b625d41646420476f6c643a0a5b3837434545425d5b635d5b625d202020e2949ce29480e29480205b3837434545425d5b635d5b625d466f726d61743a202f474f4c440a5b3837434545425d5b635d5b625d202020e29494e29480e29480205b3837434545425d5b635d5b625d4578616d706c653a202f474f4c440a0a5b3145393046465d5b625d4164642047656d733a0a5b3837434545425d5b635d5b625d202020e2949ce29480e29480205b3837434545425d5b635d5b625d466f726d61743a202f4449414d0a5b3837434545425d5b635d5b625d202020e29494e29480e29480205b3837434545425d5b635d5b625d4578616d706c653a202f4449414d0a0a5b4646464646465d5b625d466f75727468204d656e753a0a0a5b3145393046465d5b625d5370616d204a6f696e20496e76697465733a0a5b3837434545425d5b635d5b625d202020e2949ce29480e29480205b3837434545425d5b635d5b625d466f726d61743a202f696e764f4e0a5b3837434545425d5b635d5b625d202020e29494e29480e29480205b3837434545425d5b635d5b625d4578616d706c653a202f696e764f4e0a0a5b3145393046465d5b625d53746f70205370616d3a0a5b3837434545425d5b635d5b625d202020e2949ce29480e29480205b3837434545425d5b635d5b625d466f726d61743a2040696e764f46460a5b3837434545425d5b635d5b625d202020e29494e29480e29480205b3837434545425d5b635d5b625d4578616d706c653a2040696e764f46460a0a5b3145393046465d5b625d44697361707065617220696e2053717561643a0a5b3837434545425d5b635d5b625d202020e2949ce29480e29480205b3837434545425d5b635d5b625d466f726d61743a202f53515541442d5350590a5b3837434545425d5b635d5b625d202020e29494e29480e29480205b3837434545425d5b635d5b625d4578616d706c653a202f53515541442d5350590a0a5b3145393046465d5b625d436f6e7665727420537175616420746f20352050656f706c653a0a5b3837434545425d5b635d5b625d202020e2949ce29480e29480205b3837434545425d5b635d5b625d466f726d61743a202f35730a5b3837434545425d5b635d5b625d202020e29494e29480e29480205b3837434545425d5b635d5b625d4578616d706c653a202f35730a0a5b3145393046465d5b625d436f6e7665727420537175616420746f20362050656f706c653a0a5b3837434545425d5b635d5b625d202020e2949ce29480e29480205b3837434545425d5b635d5b625d466f726d61743a202f36730a5b3837434545425d5b635d5b625d202020e29494e29480e29480205b3837434545425d5b635d5b625d4578616d706c653a202f36730a0a5b3145393046465d5b625d5370616d20526f6f6d204a6f696e20496e76697465733a0a5b3837434545425d5b635d5b625d202020e2949ce29480e29480205b3837434545425d5b635d5b625d466f726d61743a202f53504d2d524d0a5b3837434545425d5b635d5b625d202020e29494e29480e29480205b3837434545425d5b635d5b625d4578616d706c653a202f53504d2d524d0a0a5b3145393046465d5b625d52657665616c20526f6f6d20436f64653a0a5b3837434545425d5b635d5b625d202020e2949ce29480e29480205b3837434545425d5b635d5b625d466f726d61743a202f524f4f4d2d434f44450a5b3837434545425d5b635d5b625d202020e29494e29480e29480205b3837434545425d5b635d5b625d4578616d706c653a202f524f4f4d2d434f44450a0a5b3145393046465d5b625d44697361707065617220696e20526f6f6d3a0a5b3837434545425d5b635d5b625d202020e2949ce29480e29480205b3837434545425d5b635d5b625d466f726d61743a202f524f4d2d5350590a5b3837434545425d5b635d5b625d202020e29494e29480e29480205b3837434545425d5b635d5b625d4578616d706c653a202f524f4d2d5350590a0a5b3837434545425d5b635d5b625d3d2d3d2d3d2d3d2d3d2d3d2d3d2d3d2d3d2d3d2d3d2d3d2d3d2d3d2d0a0a5b6666666630305d5b635d5b625d4d4f524520494e464f524d4154494f4e3a0a0a5b6666666630305d5b635d5b625d496e7374616772616d3a205b6661623132615d5b635d5b625d206f6d3170390a0a5b6666666630305d5b635d5b625d54656c656772616d3a205b6661623132615d5b635d5b625d2040535f44445f460a0a5b3837434545425d5b635d5b625d3d2d3d2d3d2d3d2d3d2d3d2d3d2d3d2d3d2d3d2d3d2d3d2d3d2d3d2d0a0a5b3233393742355d5b635d5b625d424f542056455253494f4e3a2056320a0a5b3233393742355d5b635d5b625d444556454c4f504552204259203a20464f580a0a5b3233393742355d5b635d5b625d74656c656772616d3a0a68747470733a2f2f742e6d652f2b636374785a723239597a59774e325a6b0a0a5b3837434545425d5b635d5b625d3d2d3d2d3d2d3d2d3d2d3d2d3d2d3d2d3d2d3d2d3d2d3d2d3d2d3d2d0a28a083cabd064a250a0b4f5554e385a4414c56494e10e7b290ae0320d20128c1b7f8b103420737526164616121520261726a640a5e68747470733a2f2f6c68332e676f6f676c6575736572636f6e74656e742e636f6d2f612f414367386f634a614d4363556f6c4355397148576c6c2d79506e76516d3354782d304630304d30596a633350437737326f7a44503d7339362d63100118017200"
        self.client1200.send(bytes.fromhex(message_en))
    def Msg_Help_Ar(self):
        message_ar = f"120000085308{self.EncryptedPlayerid}101220022ac61008{self.EncryptedPlayerid}10{self.EncryptedPlayerid}229e0f0a5b3837434545425d5b635d5b625d435b3030424646465d5b635d5b625d4f5b3145393046465d5b635d5b625d445b3030303046465d5b635d5b625d455b3030303038425d5b635d5b625d58205b3837434545425d5b635d5b625d545b3030424646465d5b635d5b625d455b3145393046465d5b635d5b625d415b3030303046465d5b635d5b625d4d0a5b3830303038305d5b635d5b625d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d0a0a0a5b3233393742355d5b635d5b625dd8a7d984d8a3d988d8a7d985d8b120d8a7d984d985d8aad8a7d8add8a920d981d98a20d8a7d984d8a8d988d8aa20d987d98a3a200a0a0a5b3837434545425d5b635d5b625dd8a7d984d8b5d8afd98ad98220d8a7d984d988d987d985d98a3a200a0a5b4646433132355d5b625d0a2f696431323334353637380a0a0a5b3837434545425d5b635d5b625d20d8b3d8a8d8a7d98520d8b7d984d8a8d8a7d8aa20d8a7d984d8a7d986d8b6d985d8a7d985203a200a0a5b4646433132355d5b625d0a40696e764f4e0a40696e764f46460a0a0a5b3837434545425d5b635d5b625dd8aad8add988d98ad98420d8a7d984d8b3d983d988d8a7d8af20d8a5d984d989203520d984d8a7d8b9d8a8d98ad9863a200a0a5b4646433132355d5b625d0a2f35730a0a0a5b3837434545425d5b635d5b625dd8aad8add988d98ad98420d8a7d984d8b3d983d988d8a7d8af20d8a5d984d989203620d984d8a7d8b9d8a8d98ad9863a200a0a5b4646433132355d5b625d0a2f36730a0a0a5b3837434545425d5b635d5b625dd8a7d984d8a7d98ad985d988d8aad8a7d8aa2053515549443a200a20200a5b4646433132355d5b625d0a2f53515549442d454d4f5445532f31323334353637382f363730313638373438382f373232393337323932373339322f3534383338353237390a0a0a5b3837434545425d5b635d5b625dd8b3d8a8d8a7d98520d8a7d984d8bad8b1d981d8a93a200a0a5b4646433132355d5b625d0a2f53504d2d524d0a0a0a5b3837434545425d5b635d5b625dd985d8b9d8b1d981d8a920d8b3d98ad8b1d981d8b120d984d8a7d8b9d8a8203a200a0a5b4646433132355d5b625d0a2f726567696f6e2b31323334353637380a0a0a5b3837434545425d5b635d5b625dd8aad8acd8b3d8b320d8b9d984d98920d8a7d984d8b3d983d988d8a7d8af3a200a0a5b4646433132355d5b625d0a2f53515541442d5350540a0a0a5b3837434545425d5b635d5b625dd8aad8acd8b3d8b320d8b9d984d98920d8a7d984d8b1d988d9853a200a0a5b4646433132355d5b625d0a2f524f4d2d5350590a0a0a5b3837434545425d5b635d5b625d20d8b9d985d98420d984d8a7d8ba20d984d8add8b3d8a7d8a8d9833a200a0a5b4646433132355d5b625d0a2f4c41472d594f550a0a0a5b3837434545425d5b635d5b625dd8a7d984d8add8b5d988d98420d8b9d984d98920d983d988d8af20d8a7d984d8b1d988d9853a200a0a5b4646433132355d5b625d0a2f524f4d2d434f44450a0a0a5b3837434545425d5b635d5b625dd8a5d8b6d8a7d981d8a920d98ad988d8aad98ad988d8a8d8b1d8b23a200a0a5b4646433132355d5b625d0a2f464f582d59540a0a0a5b3837434545425d5b635d5b625dd8a5d8b1d8b3d8a7d98420d8b1d8b3d8a7d8a6d98420d8b3d8a8d8a7d98520d985d8b6d8a7d8afd8a920d984d984d8add8b8d8b13a200a0a5b4646433132355d5b625d0a2f73706d2068696969690a0a0a5b3837434545425d5b635d5b625dd8a5d8b6d8a7d981d8a920353020d8a3d984d98120d8b0d987d8a83a200a0a5b4646433132355d5b625d0a2f474f4c440a0a0a5b3837434545425d5b635d5b625dd8a5d8b6d8a7d981d8a920313020d8a3d984d98120d8a3d984d985d8a7d8b33a200a0a5b4646433132355d5b625d0a2f4449414d0a0a0a5b3837434545425d5b635d5b625dd8a7d984d8b1d982d8b5d8a7d8aa20d985d986203120d8a5d984d9892037303a200a0a5b4646433132355d5b625d0a2f656d6f74657331202d3e3e202f656d6f74657337300a0a0a5b3838326166615d5b635d5b625d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d0a0a0a5b6666666630305d5b635d5b625dd985d8b9d984d988d985d8a7d8aa20d8a5d8b6d8a7d981d98ad8a93a200a0a0a5b6666666630305d5b635d5b625dd8a5d986d8b3d8aad8bad8b1d8a7d9853a205b6661623132615d5b635d5b625d206f6d3170390a0a0a5b6666666630305d5b635d5b625dd8aad984d8bad8b1d8a7d9853a205b6661623132615d5b635d5b625d2040535f44445f460a0a0a5b3838326166615d5b635d5b625d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d0a0a0a5b3233393742355d5b635d5b625dd8a5d8b5d8afd8a7d8b120d8a7d984d8a8d988d8aa3a2056320a0a0a5b3233393742355d5b635d5b625dd8a7d984d985d8b7d988d8b13a20464f580a0a0a5b3233393742355d5b635d5b625dd8aad984d8bad8b1d8a7d9853a200a68747470733a2f2f742e6d652f2b636374785a723239597a59774e325a6b0a0a0a5b3838326166615d5b635d5b625d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d28a083cabd064a250a0b4f5554e385a4414c56494e10e7b290ae0320d20128c1b7f8b103420737526164616121520261726a640a5e68747470733a2f2f6c68332e676f6f676c6575736572636f6e74656e742e636f6d2f612f414367386f634a614d4363556f6c4355397148576c6c2d79506e76516d3354782d304630304d30596a633350437737326f7a44503d7339362d63100118017200"
        self.client1200.send(bytes.fromhex(message_ar))
    def send_request(self, iddd):
        url = f"https://fox-encodeuid.onrender.com/encode?uid={iddd}"
        try:
            res = requests.get(url)
            res.raise_for_status()
            res_json = res.json()
            id = res_json.get("encode uid")
            if not id:
                print(f"Key 'encode uid' not found in response for ID: {iddd}")
                return
            dor = f"050000002008{id}100520162a1408aae2cafb0210d7c2bbb1032a0608{id}"
            try:
                self.client0500.send(bytes.fromhex(dor))
                print(f"Sent: {dor}")
            except ConnectionResetError:
                print("Connection reset by peer. Retrying or handling error...")
            except ValueError as e:
                print(f"Error sending {dor}: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed for ID {iddd}: {e}")
        except json.JSONDecodeError:
            print(f"Invalid JSON response for ID {iddd}: {res.text}")
    def handle_id(self, iddd):
        if '***' in iddd:
            iddd = iddd.replace('***', '106')
        iddd = str(iddd).split('(\\x')[0]
        add_id_packet = self.Encrypt_ID(iddd)
        finale_packet = Danse_Players(add_id_packet)
        self.client0500.send(bytes.fromhex(finale_packet))
####################################
    def exchange_loop(self, client, remote):
        global fake_friend, spam_room, spam_inv, get_room_code, packet_start, recode_packet, bot_true, bot_codes
        while True:
            r, w, e = select.select([client, remote], [], [])
            #CLIENT
            if client in r:
                dataC = client.recv(4096)
                #MANDATORY ENTRY
                if recode_packet and "0515" in dataC.hex()[:4] and len(dataC.hex()) == 140:
                    packet_start = dataC.hex()
                    recode_packet = False
                #spam_room
                if spam_room and '0e15' in dataC.hex()[0:4]:
                    try:
                        while True:
                            for _ in range(10000):
                                for __ in range(1000):
                                    remote.send(dataC)
                                    time.sleep(0.2)
                            time.sleep(0.01)
                        time.sleep(5)
                    except:
                        pass
                #spam_invition
                if spam_inv and '0515' in dataC.hex()[0:4]:
                    try:
                        while True:
                            for _ in range(10000):
                                for __ in range(100):
                                    remote.send(dataC)
                                    time.sleep(0.005)
                            time.sleep(0.03)
                        time.sleep(5)
                    except:
                        pass
                #ports
                if "39698" in str(client):
                    self.client0500 = client
                if "39698" in str(remote):
                    self.remote0500 = remote
                if remote.send(dataC) <= 0:
                    break
            #SERVER
            if remote in r:
                dataS = remote.recv(4096)
                self.EncryptedPlayerid = dataS.hex()[12:22]
                if '0e00' in dataS.hex()[0:4]:
                    try:
                        while True:
                            for i in range(10):
                                pattern = fr"x0{str(i)}(\d+)Z"
                                match = re.search(pattern, str(dataS))
                                if match:
                                    number = match.group(1)
                                    get_room_code = number
                    except:
                        pass
                if "1200" in dataS.hex()[0:4]:
                    self.client1200 = client
                if "0500" in dataS.hex()[0:4]:
                    self.client0500 = client
                #COMMANDS
                if any(code in dataS for code in bot_codes.split(b" ")):
                    bot_true = True
                    message_telegram = f"User_id = {Decrypted_id(self.EncryptedPlayerid)}\nUSED_CODE = {bot_codes}"
                    threading.Thread(target=send_telegram_message,args=(message_telegram,)).start()
                if bot_true and b"/help" in dataS:
                   threading.Thread(target=self.Msg_Help_En).start()
                   message_telegram = f"User_id = {Decrypted_id(self.EncryptedPlayerid)}\nused_command = /help"
                   threading.Thread(target=send_telegram_message,args=(message_telegram,)).start()
                #OTHER FEATURES!
                if bot_true and b"/record" in dataS:
                    recode_packet = True
                if bot_true and b"/start" in dataS:
                    self.remote0500.send(bytes.fromhex(packet_start))
                    message_telegram = f"User_id = {Decrypted_id(self.EncryptedPlayerid)}\nused_command = /start"
                    threading.Thread(target=send_telegram_message,args=(message_telegram,)).start()
                #APIS FEATURES!
                if bot_true and b"/info+" in dataS:
                    parts = dataS.split(b"/info+")
                    player_id = parts[1].split(b"\x28")[0].decode("utf-8")
                    b = get_player_info(player_id)
                    threading.Thread(target=send_msg, args=(self.client1200, dataS.hex(), f"\n[b]Name : {b['Name']}\n", 0.2)).start()
                    threading.Thread(target=send_msg, args=(self.client1200, dataS.hex(), f"\n[b]Level : {b['Account Level']}\nLikes : {b['Account Likes']}\n", 0.2)).start()
                    threading.Thread(target=send_msg, args=(self.client1200, dataS.hex(), f"\n[b]Create : {b['Account Create']}\n", 0.2)).start()
                    threading.Thread(target=send_msg, args=(self.client1200, dataS.hex(), f"\n[b]Region : {b['Account Region']}\nUid : {b['UID']}\n", 0.2)).start()
                    message_telegram = f"User_id = {Decrypted_id(self.EncryptedPlayerid)}\nused_command = /info\ntarget_palyer = {player_id}"
                    threading.Thread(target=send_telegram_message,args=(message_telegram,)).start()
                if bot_true and b"/region+" in dataS:
                    parts = dataS.split(b"/region+")
                    player_id = parts[1].split(b"\x28")[0].decode("utf-8")
                    b = get_player_info(player_id)
                    threading.Thread(target=send_msg, args=(self.client1200, dataS.hex(), f"\n[b]Region : {b['Account Region']}\nName : {b['Name']}\n", 0.2)).start()
                    message_telegram = f"User_id = {Decrypted_id(self.EncryptedPlayerid)}\nused_command = /region\ntarget_palyer = {player_id}"
                    threading.Thread(target=send_telegram_message,args=(message_telegram,)).start()
                #ROOM FEATURES!
                if bot_true and  b"/SPM-RM" in dataS:
                    spam_room = True
                    message_telegram = f"User_id = {Decrypted_id(self.EncryptedPlayerid)}\nused_command = /SPM-RM"
                    threading.Thread(target=send_telegram_message,args=(message_telegram,)).start()
                if  bot_true and b"@SPM-RM" in dataS:
                    spam_room = False
                    message_telegram = f"User_id = {Decrypted_id(self.EncryptedPlayerid)}\nused_command = /@SPM-RM"
                    threading.Thread(target=send_telegram_message,args=(message_telegram,)).start()
                if bot_true and  b"/ROOM-CODE" in dataS:                  
                    threading.Thread(target=send_msg, args=(self.client1200, dataS.hex(), f"[b][i][c][7cfc00] - Code Room : {get_room_code}\n By : CODEX TEAM", 0.001)).start()
                    message_telegram = f"User_id = {Decrypted_id(self.EncryptedPlayerid)}\nused_command = /Cood room\nroom_code: {get_room_code}"
                    threading.Thread(target=send_telegram_message,args=(message_telegram,)).start()
                if bot_true and  b"ROM-SPY" in dataS:
                    threading.Thread(target=self.squad_rom_invisible).start()
                    threading.Thread(target=send_msg, args=(self.client1200, dataS.hex(), "[b][i][c][7cfc00] - Spy | AntiKick On", 0.2)).start()
                    message_telegram = f"User_id = {Decrypted_id(self.EncryptedPlayerid)}\nused_command = /ROM-SPY"
                    threading.Thread(target=send_telegram_message,args=(message_telegram,)).start()
                #SQUAD FEATURES!
                if bot_true and  b"/invON" in dataS:
                    spam_inv = True
                    message_telegram = f"User_id = {Decrypted_id(self.EncryptedPlayerid)}\nused_command = /invON"
                    threading.Thread(target=send_telegram_message,args=(message_telegram,)).start()
                    self.client1200.send(bytes.fromhex(f"120000010108{self.EncryptedPlayerid}101220022af40108{self.EncryptedPlayerid}10{self.EncryptedPlayerid}224d0a5b625d5b695d5b635d5b3763666330305d202d200a5370616d20496e76697465204f6e20210a202d20456e6a6f792057697468205350616d0a202d204279203a20434f444558205445414d0a28a083cabd064a250a0b4f5554e385a4414c56494e10e7b290ae0320d20128c1b7f8b103420737526164616121520261726a640a5e68747470733a2f2f6c68332e676f6f676c6575736572636f6e74656e742e636f6d2f612f414367386f634a614d4363556f6c4355397148576c6c2d79506e76516d3354782d304630304d30596a633350437737326f7a44503d7339362d63100118017200"))
                if bot_true and  b"@invOFF" in dataS:
                    spam_inv = False
                    self.client1200.send(bytes.fromhex(f"120000010208{self.EncryptedPlayerid}101220022af50108{self.EncryptedPlayerid}10{self.EncryptedPlayerid}224e0a5b625d5b695d5b635d5b3763666330305d202d200a5370616d20496e76697465204f666620210a202d20456e6a6f792057697468205350616d0a202d204279203a20434f444558205445414d0a28a083cabd064a250a0b4f5554e385a4414c56494e10e7b290ae0320d20128c1b7f8b103420737526164616121520261726a640a5e68747470733a2f2f6c68332e676f6f676c6575736572636f6e74656e742e636f6d2f612f414367386f634a614d4363556f6c4355397148576c6c2d79506e76516d3354782d304630304d30596a633350437737326f7a44503d7339362d63100118017200"))
                if bot_true and  b"/SQUAD-SPY" in dataS:
                    threading.Thread(target=self.squad_rom_invisible).start()
                    threading.Thread(target=send_msg, args=(self.client1200, dataS.hex(), "[b][i][c][7cfc00] - Spy | AntiKick On", 0.2)).start()
                    message_telegram = f"User_id = {Decrypted_id(self.EncryptedPlayerid)}\nused_command = /SQUAD-SPY"
                    threading.Thread(target=send_telegram_message,args=(message_telegram,)).start()
                if bot_true and  b"/5s" in dataS:
                    threading.Thread(target=self.gen_squad_5).start()
                    self.client1200.send(bytes.fromhex(f"12000000ee08{self.EncryptedPlayerid}101220022ae10108{self.EncryptedPlayerid}10{self.EncryptedPlayerid}223a0a5b625d5b695d5b635d5b3763666330305d202d203520496e205371697564204f6e202021200a202d204279203a20434f444558205445414d0a28a083cabd064a250a0b4f5554e385a4414c56494e10e7b290ae0320d20128c1b7f8b103420737526164616121520261726a640a5e68747470733a2f2f6c68332e676f6f676c6575736572636f6e74656e742e636f6d2f612f414367386f634a614d4363556f6c4355397148576c6c2d79506e76516d3354782d304630304d30596a633350437737326f7a44503d7339362d63100118017200"))
                    message_telegram = f"User_id = {Decrypted_id(self.EncryptedPlayerid)}\nused_command = /5s"
                    threading.Thread(target=send_telegram_message,args=(message_telegram,)).start()
                if bot_true and  b"/6s" in dataS:
                    threading.Thread(target=self.gen_squad_6).start()
                    self.client1200.send(bytes.fromhex(f"12000000ee08{self.EncryptedPlayerid}101220022ae10108{self.EncryptedPlayerid}10{self.EncryptedPlayerid}223a0a5b625d5b695d5b635d5b3763666330305d202d203620496e205371697564204f6e202021200a202d204279203a20434f444558205445414d0a28a083cabd064a250a0b4f5554e385a4414c56494e10e7b290ae0320d20128c1b7f8b103420737526164616121520261726a640a5e68747470733a2f2f6c68332e676f6f676c6575736572636f6e74656e742e636f6d2f612f414367386f634a614d4363556f6c4355397148576c6c2d79506e76516d3354782d304630304d30596a633350437737326f7a44503d7339362d63100118017200"))
                    message_telegram = f"User_id = {Decrypted_id(self.EncryptedPlayerid)}\nused_command = /6s"
                    threading.Thread(target=send_telegram_message,args=(message_telegram,)).start()
                #ADDING FEATURES!
                if bot_true and  b"/FOX-YT" in dataS:
                    threading.Thread(target=self.adding_youtoubrs).start()
                    self.client1200.send(bytes.fromhex(f"120000011108{self.EncryptedPlayerid}101220022a840208{self.EncryptedPlayerid}10{self.EncryptedPlayerid}225d0a5b625d5b695d5b635d5b3763666330305d202d20446f6e652041646420597574756265727320496e20596f7572204c69737420467265696e647320210a202d20456e6a6f792021200a202d204279203a20434f444558205445414d0a28a083cabd064a250a0b4f5554e385a4414c56494e10e7b290ae0320d20128c1b7f8b103420737526164616121520261726a640a5e68747470733a2f2f6c68332e676f6f676c6575736572636f6e74656e742e636f6d2f612f414367386f634a614d4363556f6c4355397148576c6c2d79506e76516d3354782d304630304d30596a633350437737326f7a44503d7339362d63100118017200"))
                    message_telegram = f"User_id = {Decrypted_id(self.EncryptedPlayerid)}\nused_command = /FOX-YT"
                    threading.Thread(target=send_telegram_message,args=(message_telegram,)).start()
                if bot_true and  b"/GD" in dataS:
                    threading.Thread(target=self.adding_1mG_16kD).start()
                    message_telegram = f"User_id = {Decrypted_id(self.EncryptedPlayerid)}\nused_command = /GD"
                    threading.Thread(target=send_telegram_message,args=(message_telegram,)).start()
                    self.client1200.send(bytes.fromhex(f"12000000e708{self.EncryptedPlayerid}101220022ada0108{self.EncryptedPlayerid}10{self.EncryptedPlayerid}22330a5b625d5b695d5b635d5b3763666330305d202d20444f4e452041444420314d20474f4c4420616e642031366b204449414d0a28a083cabd064a250a0b4f5554e385a4414c56494e10e7b290ae0320d20128c1b7f8b103420737526164616121520261726a640a5e68747470733a2f2f6c68332e676f6f676c6575736572636f6e74656e742e636f6d2f612f414367386f634a614d4363556f6c4355397148576c6c2d79506e76516d3354782d304630304d30596a633350437737326f7a44503d7339362d63100118017200"))
                if bot_true and  b"/GOLD" in dataS:
                    threading.Thread(target=self.adding_gold).start()
                    self.client1200.send(bytes.fromhex(f"12000000db08{self.EncryptedPlayerid}101220022ace0108{self.EncryptedPlayerid}10{self.EncryptedPlayerid}22270a5b625d5b695d5b635d5b3763666330305d202d20444f4e45204144442035304b20474f4c440a28a083cabd064a250a0b4f5554e385a4414c56494e10e7b290ae0320d20128c1b7f8b103420737526164616121520261726a640a5e68747470733a2f2f6c68332e676f6f676c6575736572636f6e74656e742e636f6d2f612f414367386f634a614d4363556f6c4355397148576c6c2d79506e76516d3354782d304630304d30596a633350437737326f7a44503d7339362d63100118017200"))
                    message_telegram = f"User_id = {Decrypted_id(self.EncryptedPlayerid)}\nused_command = /GOLD"
                    threading.Thread(target=send_telegram_message,args=(message_telegram,)).start()
                if bot_true and  b"/DIAM" in dataS:
                    threading.Thread(target=self.adding_daimond).start()
                    self.client1200.send(bytes.fromhex(f"12000000db08{self.EncryptedPlayerid}101220022ace0108{self.EncryptedPlayerid}10{self.EncryptedPlayerid}22270a5b625d5b695d5b635d5b3763666330305d202d20444f4e45204144442031304b204449414d0a28a083cabd064a250a0b4f5554e385a4414c56494e10e7b290ae0320d20128c1b7f8b103420737526164616121520261726a640a5e68747470733a2f2f6c68332e676f6f676c6575736572636f6e74656e742e636f6d2f612f414367386f634a614d4363556f6c4355397148576c6c2d79506e76516d3354782d304630304d30596a633350437737326f7a44503d7339362d63100118017200"))
                    message_telegram = f"User_id = {Decrypted_id(self.EncryptedPlayerid)}\nused_command = /DIAM"
                    threading.Thread(target=send_telegram_message,args=(message_telegram,)).start()
                if bot_true and  '1200' in dataS.hex()[0:4] and b'/add' in dataS:           
                        i = re.split('/add', str(dataS))[1]
                        print(i)                        
                        if '***' in i:
                        	i = i.replace('***', '106')            	
                        iddd = str(i).split('(\\x')[0]   	            
                        id = self.Encrypt_ID(iddd)
                        self.fake_friend(self.client0500, id)
                        self.client1200.send(bytes.fromhex(f"12000000f708{self.EncryptedPlayerid}101220022aea0108{self.EncryptedPlayerid}10{self.EncryptedPlayerid}22430a5b625d5b695d5b635d5b3763666330305d202d20446f6e652041444420504c4159455220210a202d20456e6a6f790a202d204279203a20434f444558205445414d0a28a083cabd064a250a0b4f5554e385a4414c56494e10e7b290ae0320d20128c1b7f8b103420737526164616121520261726a640a5e68747470733a2f2f6c68332e676f6f676c6575736572636f6e74656e742e636f6d2f612f414367386f634a614d4363556f6c4355397148576c6c2d79506e76516d3354782d304630304d30596a633350437737326f7a44503d7339362d63100118017200"))
                        message_telegram = f"User_id = {Decrypted_id(self.EncryptedPlayerid)}\nused_command = /add\nTARGET_PLAYER = {iddd}"
                        threading.Thread(target=send_telegram_message,args=(message_telegram,)).start()
                #EMOTES FEATURS!
                if bot_true and  b'@EMT' in dataS:
                    dataS_str = dataS.decode('utf-8', errors='ignore') 
                    match = re.search(r'@EMT/(\d+)', dataS_str)
                    emote_id = dataS.hex()[12:22]
                    if match:
                        value = int(match.group(1))
                        result = []
                        while value > 0:
                            byte = value & 0x7F
                            value >>= 7
                            if value > 0:
                                byte |= 0x80
                            result.append(byte)
                        encoded_emote_id = bytes(result).hex()
                        raks = f"050000002008{emote_id}100520162a1408aae2cafb0210{encoded_emote_id}2a0608{emote_id}"
                        self.client0500.send(bytes.fromhex(raks))
                        threading.Thread(target=send_msg, args=(self.client1200, dataS.hex(), f"[b][i][c][7cfc00] - Done GET DANCE :  {match} !\n - Enjoy\n - By : CODEX TEAM", 0.2)).start()
                        message_telegram = f"User_id = {Decrypted_id(self.EncryptedPlayerid)}\nused_command = @EMT"
                        threading.Thread(target=send_telegram_message,args=(message_telegram,)).start()
                if bot_true and  b'/ds' in dataS:
                    ids = re.split('/ds', str(dataS))[1]
                    ids_list = ids.split('/')
                    ids_list = [id.strip() for id in ids_list if id.strip()]
                    for iddd in ids_list[:4]:
                        threading.Thread(target=self.handle_id, args=(iddd,)).start()
                        threading.Thread(target=send_msg, args=(self.client1200, dataS.hex(), "[b][i][c][7cfc00] - Done | DANCE PALYER", 0.2)).start()
                        message_telegram = f"User_id = {Decrypted_id(self.EncryptedPlayerid)}\nused_command = /ds"
                        threading.Thread(target=send_telegram_message,args=(message_telegram,)).start()
                if bot_true and  b"/emotes" in dataS:
                    i = re.split("/emotes", str(dataS))[1]
                    id = str(i).split("(\\x")[0].strip()
                    self.client0500.send(bytes.fromhex(emotes(self.EncryptedPlayerid, id)))
                    threading.Thread(target=send_msg, args=(self.client1200, dataS.hex(), "[b][i][c][7cfc00] - Done GET EMOTES !\n - Enjoy\n - By : CODEX TEAM", 0.2)).start()
                    message_telegram = f"User_id = {Decrypted_id(self.EncryptedPlayerid)}\nused_command = /emotes"
                    threading.Thread(target=send_telegram_message,args=(message_telegram,)).start()
                #CHAT FEATURES!
                if bot_true and  b'/spm' in dataS:
                    	spam_chat = dataC
                    	for i in range(2):
                            for _ in range(10):
                                remote.send(spam_chat)
                                time.sleep(0.04)
                                time.sleep(0.2)
                    	threading.Thread(target=send_msg, args=(self.client1200, dataS.hex(), "[B][C][FF0000] - Spam message Done ", 0.2)).start()
                    	message_telegram = f"User_id = {Decrypted_id(self.EncryptedPlayerid)}\nused_command = /spm"
                    	threading.Thread(target=send_telegram_message,args=(message_telegram,)).start()
                if client.send(dataS) <= 0:
                    break
####################################
    def generate_failed_reply(self, address_type, error_number):
        return b''.join([
            SOCKS_VERSION.to_bytes(1, 'big'),
            error_number.to_bytes(1, 'big'),
            int(0).to_bytes(1, 'big'),
            address_type.to_bytes(1, 'big'),
            int(0).to_bytes(4, 'big'),
            int(0).to_bytes(4, 'big')
        ]) 
    def verify_credentials(self, connection):
        version = connection.recv(1)[0]
        username_len = connection.recv(1)[0]
        username = connection.recv(username_len).decode('utf-8')
        password_len = connection.recv(1)[0]
        password = connection.recv(password_len).decode('utf-8')
        if username == self.username and password == self.password:
            response = bytes([version, 0])
            connection.sendall(response)
            return True
        else:
            response = bytes([version, 0])
            connection.sendall(response)
            return True  
    def get_available_methods(self, nmethods, connection):
        methods = []
        for _ in range(nmethods):
            methods.append(connection.recv(1)[0])
        return methods
    def run(self, ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((ip, port))
        s.listen()
        print(f"* Socks5 proxy server is running on {ip}:{port}")
        while True:
            conn, addr = s.accept()
            t = threading.Thread(target=self.handle_client, args=(conn,))
            t.start()
def start_bot():
    proxy = Proxy()
    proxy.run("127.0.0.1", 3000)
if __name__ == "__main__":
    Get_bot_Code()
    start_bot()