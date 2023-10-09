from project import get_data_segmentos, get_data_online, save_data

def main():
    test_get_data_segmentos()
    test_get_data_online()
    test_save_data()


def test_get_data_segmentos():
    data = get_data_segmentos()
    assert len(data) > 0


def test_get_data_online():
    data = get_data_online("acoes", "PETR4", "OIL AND GAS")
    assert len(data) == 9


def test_save_data():
    database = [['PETR4', 'OIL AND GAS', 'Petrobras', '28,49', '11,64%', '24/08/21', '16/09/21', '0,23', '2023-02-20 17:12:13']]
    save_data(database)
    try:
        with open('online_action.csv', 'r', encoding='utf8') as f:
            content = f.read()
            assert len(content) > 0
    except FileNotFoundError:
        assert False


if __name__ == "__main__":
    main()