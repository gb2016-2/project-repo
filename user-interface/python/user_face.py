import pymysql

cnx = pymysql.connect(user='root',
                      password='123qwe_+',
                      database='ark',
                      charset='utf8')
cur = cnx.cursor()


persons = []
sql_persons = "SELECT name FROM coriander_persons;"
cur.execute(sql_persons)
for row in cur:
    persons.append(row[0])

dates_year = {}
sql_pages = "SELECT id, found_date_time FROM coriander_pages;"
cur.execute(sql_pages)
for row in cur:
    dates_year[row[0]] = str(row[1].year)


from collections import Counter
count_years = Counter(dates_year.values())


ranks = {}
union_ranks = {}
sql_persons = "SELECT id FROM coriander_persons;"
cur.execute(sql_persons)
for row in cur:
    ranks[row[0]] = {}
    union_ranks[row[0]] = {}

for person in ranks.keys():
    sql_ranks = "SELECT page_id, rank FROM coriander_personpagerank WHERE person_id={};".format(person)
    cur.execute(sql_ranks)
    for row in cur:
        ranks[person][row[0]] = row[1]
        if row[0] == 0:
            union_ranks[person][row[0]] = 0
        else:
            union_ranks[person][row[0]] = 1


from collections import defaultdict

year_ranks = {}
year_union_ranks = {}
for person in ranks.keys():
    year_ranks[person] = defaultdict(int)
    year_union_ranks[person] = defaultdict(int)
    for k, v in ranks[person].items():
        year_ranks[person][dates_year.get(k)] += v
        if v == 0:
            year_union_ranks[person][dates_year.get(k)] += 0
        else:
            year_union_ranks[person][dates_year.get(k)] += 1


import pandas as pd

# 1. Абсолютные точные значения
ranks_year_df = pd.DataFrame(year_ranks)
ranks_year_df.columns = persons
ranks_year_df = ranks_year_df.sort_index()

# 2. Нормализованные точные значения
norm_abs_rank_year_df = pd.DataFrame(columns=persons)
for year, count in count_years.items():
    year_df = pd.DataFrame(ranks_year_df.ix[year].copy() / count)
    norm_abs_rank_year_df = pd.concat([norm_abs_rank_year_df, year_df.T])
norm_abs_rank_year_df = norm_abs_rank_year_df.sort_index()

# 3. Абсолютные единичные значения
ranks_union_year_df = pd.DataFrame(year_union_ranks)
ranks_union_year_df.columns = persons
ranks_union_year_df = ranks_union_year_df.sort_index()

# 4. Нормализованные единичные значения
norm_abs_rank_union_year_df = pd.DataFrame(columns=persons)
for year, count in count_years.items():
    union_year_df = pd.DataFrame(ranks_union_year_df.ix[year].copy() / count)
    norm_abs_rank_union_year_df = pd.concat([norm_abs_rank_union_year_df, union_year_df.T])
norm_abs_rank_union_year_df = norm_abs_rank_union_year_df.sort_index()


if __name__ == "__main__":
    # tests
    pass
