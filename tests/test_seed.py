from db.seed import seed_db
from db.connection import connect_to_db
import pytest

@pytest.fixture
def re_seed():
    return seed_db('test')




class TestRikishiTable:
    def test_seed_creates_rikishi_table(self, re_seed):
        query = connect_to_db().run('SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = \'rikishi\');')
        exists = query[0][0]
        assert exists == True
    
    def test_rikishi_table_has_id_serial_primary_key_column(self, re_seed):
        query = connect_to_db().run('SELECT column_name, data_type, column_default FROM information_schema.columns WHERE table_name = \'rikishi\' AND column_name = \'id\';')
        print(query)
        column = query[0][0]
        data_type = query[0][1]
        column_default = query[0][2]
        assert column == 'id'
        assert data_type == 'integer'
        assert column_default == 'nextval(\'rikishi_id_seq\'::regclass)'

    def test_rikishi_table_has_sumoapi_id_int(self, re_seed):
        query = connect_to_db().run('SELECT column_name, data_type FROM information_schema.columns WHERE table_name = \'rikishi\' AND column_name = \'sumoapi_id\';')
        column = query[0][0]
        data_type = query[0][1]
        assert column == 'sumoapi_id'
        assert data_type == 'integer'

    def test_rikishi_table_has_sumodb_id_int(self, re_seed):
        query = connect_to_db().run('SELECT column_name, data_type FROM information_schema.columns WHERE table_name = \'rikishi\' AND column_name = \'sumodb_id\';')
        column = query[0][0]
        data_type = query[0][1]
        assert column == 'sumodb_id'
        assert data_type == 'integer'

    def test_rikishi_table_has_nsk_id_int(self, re_seed):
        query = connect_to_db().run('SELECT column_name, data_type FROM information_schema.columns WHERE table_name = \'rikishi\' AND column_name = \'nsk_id\';')
        column = query[0][0]
        data_type = query[0][1]
        assert column == 'nsk_id'
        assert data_type == 'integer'

    def test_rikishi_table_has_shikona_en_varchar(self, re_seed):
        query = connect_to_db().run('SELECT column_name, data_type FROM information_schema.columns WHERE table_name = \'rikishi\' AND column_name = \'shikona_en\';')
        column = query[0][0]
        data_type = query[0][1]
        assert column == 'shikona_en'
        assert data_type == 'character varying'

    def test_rikishi_table_has_shikona_jp_varchar(self, re_seed):
        query = connect_to_db().run('SELECT column_name, data_type FROM information_schema.columns WHERE table_name = \'rikishi\' AND column_name = \'shikona_jp\';')
        column = query[0][0]
        data_type = query[0][1]
        assert column == 'shikona_jp'
        assert data_type == 'character varying'

    def test_rikishi_table_has_current_rank_varchar(self, re_seed):
        query = connect_to_db().run('SELECT column_name, data_type FROM information_schema.columns WHERE table_name = \'rikishi\' AND column_name = \'current_rank\';')
        column = query[0][0]
        data_type = query[0][1]
        assert column == 'current_rank'
        assert data_type == 'character varying'

    def test_rikishi_table_has_heya_varchar(self, re_seed):
        query = connect_to_db().run('SELECT column_name, data_type FROM information_schema.columns WHERE table_name = \'rikishi\' AND column_name = \'heya\';')
        column = query[0][0]
        data_type = query[0][1]
        assert column == 'heya'
        assert data_type == 'character varying'

    def test_rikishi_table_has_birth_date_varchar(self, re_seed):
        query = connect_to_db().run('SELECT column_name, data_type FROM information_schema.columns WHERE table_name = \'rikishi\' AND column_name = \'birth_date\';')
        column = query[0][0]
        data_type = query[0][1]
        assert column == 'birth_date'
        assert data_type == 'character varying'

    def test_rikishi_table_has_shusshin_varchar(self, re_seed):
        query = connect_to_db().run('SELECT column_name, data_type FROM information_schema.columns WHERE table_name = \'rikishi\' AND column_name = \'shusshin\';')
        column = query[0][0]
        data_type = query[0][1]
        assert column == 'shusshin'
        assert data_type == 'character varying'

    def test_rikishi_table_has_height_decimal(self, re_seed):
        query = connect_to_db().run('SELECT column_name, data_type FROM information_schema.columns WHERE table_name = \'rikishi\' AND column_name = \'height\';')
        column = query[0][0]
        data_type = query[0][1]
        assert column == 'height'
        assert data_type == 'numeric'

    def test_rikishi_table_has_weight_decimal(self, re_seed):
        query = connect_to_db().run('SELECT column_name, data_type FROM information_schema.columns WHERE table_name = \'rikishi\' AND column_name = \'weight\';')
        column = query[0][0]
        data_type = query[0][1]
        assert column == 'weight'
        assert data_type == 'numeric'

    def test_rikishi_table_has_debut_varchar(self, re_seed):
        query = connect_to_db().run('SELECT column_name, data_type FROM information_schema.columns WHERE table_name = \'rikishi\' AND column_name = \'debut\';')
        column = query[0][0]
        data_type = query[0][1]
        assert column == 'debut'
        assert data_type == 'character varying'

class TestStablesTable:
    def test_seed_creates_stables_table(self, re_seed):
        query = connect_to_db().run('SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = \'stables\');')
        exists = query[0][0]
        assert exists == True
    
    def test_stable_table_has_stable_id_serial_primary_key_column(self, re_seed):
        query = connect_to_db().run('SELECT column_name, data_type, column_default FROM information_schema.columns WHERE table_name = \'stables\' AND column_name = \'stable_id\';')
        print(query)
        column = query[0][0]
        data_type = query[0][1]
        column_default = query[0][2]
        assert column == 'stable_id'
        assert data_type == 'integer'
        assert column_default == 'nextval(\'stables_stable_id_seq\'::regclass)'

    def test_stable_table_has_stable_name_varchar(self, re_seed):
        query = connect_to_db().run('SELECT column_name, data_type FROM information_schema.columns WHERE table_name = \'stables\' AND column_name = \'stable_name\';')
        column = query[0][0]
        data_type = query[0][1]
        assert column == 'stable_name'
        assert data_type == 'character varying'

    def test_stables_table_has_ranking_int(self, re_seed):
        query = connect_to_db().run('SELECT column_name, data_type FROM information_schema.columns WHERE table_name = \'stables\' AND column_name = \'ranking\';')
        column = query[0][0]
        data_type = query[0][1]
        assert column == 'ranking'
        assert data_type == 'integer'

    def test_stables_table_has_rikishi_reference(self, re_seed):
        query = connect_to_db().run('SELECT column_name, data_type FROM information_schema.columns WHERE table_name = \'stables\' AND column_name = \'rikishi\';')
        column = query[0][0]
        data_type = query[0][1]
        assert column == 'rikishi'
        assert data_type == 'integer'

class TestUsersTable:
    def test_seed_creates_users_table(self, re_seed):
        query = connect_to_db().run('SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = \'stables\');')
        exists = query[0][0]
        assert exists == True

    def test_users_table_has_user_id_serial_primary_key_column(self, re_seed):
        query = connect_to_db().run('SELECT column_name, data_type, column_default FROM information_schema.columns WHERE table_name = \'users\' AND column_name = \'user_id\';')
        column = query[0][0]
        data_type = query[0][1]
        column_default = query[0][2]
        assert column == 'user_id'
        assert data_type == 'integer'
        assert column_default == 'nextval(\'users_user_id_seq\'::regclass)'

    def test_users_table_has_stable_name_reference(self, re_seed):
        query = connect_to_db().run('SELECT column_name, data_type FROM information_schema.columns WHERE table_name = \'users\' AND column_name = \'stable_name\';')
        column = query[0][0]
        data_type = query[0][1]
        assert column == 'stable_name'
        assert data_type == 'character varying'

    def test_users_table_has_username_varchar(self, re_seed):
        query = connect_to_db().run('SELECT column_name, data_type FROM information_schema.columns WHERE table_name = \'users\' AND column_name = \'username\';')
        column = query[0][0]
        data_type = query[0][1]
        assert column == 'username'
        assert data_type == 'character varying'

class TestRikishiStableTable:
    def test_seed_creates_rikishi_stable_table(self, re_seed):
        query = connect_to_db().run('SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = \'rikishi_stable\');')
        exists = query[0][0]
        assert exists == True

    def test_rikishi_stable_table_has_user_id_serial_primary_key_column(self, re_seed):
        query = connect_to_db().run('SELECT column_name, data_type, column_default FROM information_schema.columns WHERE table_name = \'rikishi_stable\' AND column_name = \'rikishi_stable_id\';')
        column = query[0][0]
        data_type = query[0][1]
        column_default = query[0][2]
        assert column == 'rikishi_stable_id'
        assert data_type == 'integer'
        assert column_default == 'nextval(\'rikishi_stable_rikishi_stable_id_seq\'::regclass)'

    def test_rikishi_stable_table_has_makuuchi_int_reference(self, re_seed):
        query = connect_to_db().run('SELECT column_name, data_type FROM information_schema.columns WHERE table_name = \'rikishi_stable\' AND column_name = \'makuuchi\';')
        column = query[0][0]
        data_type = query[0][1]
        assert column == 'makuuchi'
        assert data_type == 'integer'

    def test_rikishi_stable_table_has_juryo_int_reference(self, re_seed):
        query = connect_to_db().run('SELECT column_name, data_type FROM information_schema.columns WHERE table_name = \'rikishi_stable\' AND column_name = \'juryo\';')
        column = query[0][0]
        data_type = query[0][1]
        assert column == 'juryo'
        assert data_type == 'integer'

    def test_rikishi_stable_table_has_makushita_int_reference(self, re_seed):
        query = connect_to_db().run('SELECT column_name, data_type FROM information_schema.columns WHERE table_name = \'rikishi_stable\' AND column_name = \'makushita\';')
        column = query[0][0]
        data_type = query[0][1]
        assert column == 'makushita'
        assert data_type == 'integer'


    def test_rikishi_stable_table_has_sandanme_int_reference(self, re_seed):
        query = connect_to_db().run('SELECT column_name, data_type FROM information_schema.columns WHERE table_name = \'rikishi_stable\' AND column_name = \'sandanme\';')
        column = query[0][0]
        data_type = query[0][1]
        assert column == 'sandanme'
        assert data_type == 'integer'


    def test_rikishi_stable_table_has_jonidan_int_reference(self, re_seed):
        query = connect_to_db().run('SELECT column_name, data_type FROM information_schema.columns WHERE table_name = \'rikishi_stable\' AND column_name = \'jonidan\';')
        column = query[0][0]
        data_type = query[0][1]
        assert column == 'jonidan'
        assert data_type == 'integer'


    def test_rikishi_stable_table_has_jonokuchi_int_reference(self, re_seed):
        query = connect_to_db().run('SELECT column_name, data_type FROM information_schema.columns WHERE table_name = \'rikishi_stable\' AND column_name = \'jonokuchi\';')
        column = query[0][0]
        data_type = query[0][1]
        assert column == 'jonokuchi'
        assert data_type == 'integer'