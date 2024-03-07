from .models import asset, metric

def individual_serial_assets(asset) -> dict:
    return {
        "id": str(asset["_id"]),
        "asset_name": asset["asset_name"],
        "asset_type": asset["asset_type"],
        "location": asset["location"],
        "purchase_date": asset["purchase_date"],
        "initial_cose": asset["initial_cost"],
        "operational_cost": asset["operational_cost"]
    }

def individual_serial_metrics(metric) -> dict:
    return {
        "id": str(metric["_id"]),
        "uptime": metric["uptime"],
        "downtime": metric["downtime"],
        "maintenance_cost": metric["maintenance_cost"],
        "failure_rate": metric["failure_rate"],
        "efficiency": metric["efficiency"]
    }

def list_serial_assets(asset) -> list:
    return [individual_serial_assets(asset) for asset in asset]

def list_serial_metrics(metrics) ->list:
    return [individual_serial_metrics(metric) for metric in metrics]