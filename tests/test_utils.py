import json
from unittest.mock import mock_open, patch

from src.utils import list_from_json


def test_list_from_json_valid_file(transactions):
    with patch(
            "builtins.open",
            new_callable=mock_open,
            read_data=json.dumps(transactions)
    ):
        result = list_from_json("test_path.json")
        assert result == transactions
        assert len(transactions) == 3
