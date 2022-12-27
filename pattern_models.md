## Project models

Abstract:
    datetime_joined
    datetime_deleted
    datetime_updated

Athor
    user_id
    date_start
    followrs: int

Gange
    title

Music
    id
    title: str
    duration: TimeField
    author_id (<Author class: 2>) > (<Lil Peep>)
    ganre_id
    status ('Предрелиз', 'Релиз', 'Удалена')
    