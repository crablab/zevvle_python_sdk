from dotenv import load_dotenv
import os
import zevvle

if __name__ == "__main__":
    # Load .env vars
    load_dotenv()
    zevvle_key = os.getenv("ZEVVLE_KEY")
    zevvle_url = os.getenv("ZEVVLE_URL")

    zev = zevvle.zevvle(zevvle_key, zevvle_url)

    print(zev.get_account("acc_sdKB6nVYKoMAgvJb5DsbHk17"))
    print(zev.get_user("user_X5JFTB6KMiEyQjJNM51RDhrt"))
    print(zev.get_sim("sim_vOGFa9SfJ2QaNBHMjiFqRbMy"))
    print(zev.list_sim_cards())
    print(zev.list_call_records("sim_vOGFa9SfJ2QaNBHMjiFqRbMy", "data"))