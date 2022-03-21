# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Holding Resolution",
    "summary": """
        Add holding_check_account_id field in res.config""",
    "author": "Milton Guzman",
    "category": "Custom",
    "version": "1.0.0",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "depends": ['account_check'],
    "data": [
        "view/template.xml",
    ],
}
