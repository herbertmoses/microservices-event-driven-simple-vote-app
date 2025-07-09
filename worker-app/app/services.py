from .db import votes_collection

def get_vote_summary():
    pipeline = [
        {
            "$group": {
                "_id": "$candidate",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {"count": -1}
        }
    ]
    result = list(votes_collection.aggregate(pipeline))
    return {item["_id"]: item["count"] for item in result}
