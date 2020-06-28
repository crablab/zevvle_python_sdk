from dotenv import load_dotenv
import os, argparse
from zevvle import zevvle

if __name__ == "__main__":
    # Load .env vars
    load_dotenv()
    zevvle_key = os.getenv("ZEVVLE_KEY")
    zevvle_url = os.getenv("ZEVVLE_URL")

    # Initialize library
    zev = zevvle.zevvle(zevvle_key, zevvle_url)

    # Set up argparse 
    parser = argparse.ArgumentParser(description="A Python interface to the Zevvle API")
    parser.add_argument("--get-account", help="Get details for a Zevvle account ID.")
    parser.add_argument("--get-user", help="Get details for a Zevvle user ID.")
    parser.add_argument("--get-sim", help="Get details for a Zevvle SIM card ID.")
    parser.add_argument("--list-sim-cards", help="List Zevvle SIM cards for the API key.")
    args = parser.parse_args()

    result = {}

    if(args.get_account):
        result['account'] = zev.get_account(args.get_account)
    
    if(args.get_user):
        result['user'] = zev.get_user(args.get_user)
    
    if(args.get_sim):
        result['sim'] = zev.get_sim(args.get_sim)
    
    if(args.list_sim_cards):
        result['sim_cards'] = zev.list_sim_cards()

    #TODO: add call records
    # print(zev.list_call_records("sim_vOGFa9SfJ2QaNBHMjiFqRbMy", "data"))
    
    if(len(result) == 0):
        parser.print_help()
    else:
        print(result)
    