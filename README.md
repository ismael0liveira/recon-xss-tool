# recon-xss-tool
Automação em Python para busca de Cross Site Scripting - XSS refletido. A ideia deste código é buscar inputs do tipo hidden e transformar em parâmetros do tipo GET, com isto pode ter sucesso caso o parâmetro seja válido.

Contexto: É normal encontrar inputs do tipo Hidden serem enviadas via requisição HTTP do tipo POST, então a lógica desta ferramenta é pegar estes parâmetros, transformar em parâmetros do tipo GET e enviar payloads tentando uma falta de limpeza de entrada, trazendo assim um XSS ou outro tipo de problema de segurança.

Aproveite este código para desenvolver novas ideias! :)
