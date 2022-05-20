# import psycopg2
#
# conn = psycopg2.connect(database="yolo_db", user="postgres", password="123", host="localhost", port="5432")
# cursor = conn.cursor()

add = []


def add_to_db(inf, all_id):
    for i in all_id:
        print(inf['accuracy%s' % i])
        print(inf['time%s' % i])
        inf['accuracy%s' % i] = round(inf['accuracy%s' % i] / (inf['time%s' % i]), 2)
        print(inf['accuracy%s' % i])
        number = str(i)
        name = str(inf['name%s' % i])
        accuracy = str(inf['accuracy%s' % i])
        time_ent = str(inf['time_ent_%s' % i])
        time_out = str(inf['time_out_%s' % i])
        print(number, name, time_ent, time_out, accuracy)
        add.append([number, name, time_ent, time_out, accuracy])
        print(add)

        try:
            cursor.execute('INSERT INTO main.info (number, fight_fall, time_ent, time_out, average_accuracy) '
                              'VALUES (%s, %s, %s, %s, %s);', (number, name, time_ent, time_out, accuracy))
            conn.commit()
        except:
            pass

    return add
