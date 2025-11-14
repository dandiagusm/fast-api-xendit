import requests
from app.config import settings

class XenditClient:

    def create_invoice(self, external_id: str, amount: float):
        url = "https://api.xendit.co/v2/invoices"

        headers = {"Content-Type": "application/json"}
        auth = (settings.XENDIT_API_KEY, "")

        payload = {
            "external_id": external_id,
            "amount": amount,
            "description": f"Payment for {external_id}",
        }

        response = requests.post(url, json=payload, auth=auth, headers=headers)

        try:
            response.raise_for_status()
        except Exception:
            print("XENDIT ERROR:", response.text)
            raise

        return response.json()
