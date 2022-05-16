import psycopg2

conn = psycopg2.connect(database="yolo_db", user="postgres", password="123", host="localhost", port="5432")
cursor = conn.cursor()


def add_to_db(info, all_id):
    for i in all_id:
        info['accuracy%s' % i] = info['accuracy%s' % i] / (info['time%s' % i])
        number = str(i)
        name = str(info['name%s' % i])
        accuracy = str(info['accuracy%s' % i])
        time_ent = str(info['time_ent_%s' % i])
        time_out = str(info['time_out_%s' % i])
        print(number, name, time_ent, time_out, accuracy)
        print(info)
        #        cursor.execute('INSERT INTO main.info (number, fight_fall, time_ent, time_out, average_accuracy) '
        #                       'VALUES (%s, %s, %s, %s, %s);', (number, name, time_ent, time_out, accuracy))
        #        conn.commit()
