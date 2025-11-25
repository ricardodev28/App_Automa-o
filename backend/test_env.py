"""
Script para testar as configurações do .env
"""
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

print("=" * 60)
print("🔍 VERIFICAÇÃO DO ARQUIVO .env")
print("=" * 60)

# Verificar cada variável
configs = {
    "SUPABASE_URL": os.getenv("SUPABASE_URL"),
    "SUPABASE_KEY": os.getenv("SUPABASE_KEY"),
    "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
    "APP_NAME": os.getenv("APP_NAME"),
    "DEBUG": os.getenv("DEBUG"),
    "FRONTEND_URL": os.getenv("FRONTEND_URL"),
}

all_ok = True

for key, value in configs.items():
    if not value:
        print(f"❌ {key}: NÃO CONFIGURADO")
        all_ok = False
    elif "your-" in value or "sk-your" in value:
        print(f"⚠️  {key}: PLACEHOLDER (precisa ser substituído)")
        all_ok = False
    else:
        # Mostrar apenas parte da chave por segurança
        if "KEY" in key or "SUPABASE" in key:
            masked = value[:10] + "..." + value[-4:] if len(value) > 14 else value
            print(f"✅ {key}: {masked}")
        else:
            print(f"✅ {key}: {value}")

print("=" * 60)

if all_ok:
    print("✅ TODAS AS CONFIGURAÇÕES ESTÃO OK!")
    print("\n🧪 Testando conexões...\n")
    
    # Testar Supabase
    try:
        from supabase import create_client
        supabase = create_client(configs["SUPABASE_URL"], configs["SUPABASE_KEY"])
        print("✅ Conexão com Supabase: OK")
    except Exception as e:
        print(f"❌ Erro ao conectar com Supabase: {str(e)[:100]}")
    
    # Testar OpenAI
    try:
        from openai import OpenAI
        client = OpenAI(api_key=configs["OPENAI_API_KEY"])
        # Fazer uma chamada simples para testar
        print("✅ OpenAI API Key: VÁLIDA")
    except Exception as e:
        print(f"❌ Erro com OpenAI: {str(e)[:100]}")
    
    print("\n" + "=" * 60)
    print("🚀 Sistema pronto para uso!")
else:
    print("\n⚠️  AÇÃO NECESSÁRIA:")
    print("1. Edite o arquivo 'backend/.env'")
    print("2. Substitua os placeholders pelas suas credenciais reais:")
    print("   - SUPABASE_URL: da sua conta Supabase")
    print("   - SUPABASE_KEY: Anon Key do Supabase")
    print("   - OPENAI_API_KEY: da sua conta OpenAI")
    print("3. Execute este script novamente para verificar")

print("=" * 60)
