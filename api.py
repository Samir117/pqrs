
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pqrs'
mysql = MySQL(app)

app.secret_key = "mysecretkey"


@app.route('/insertUsuario', methods=['POST'])
def insertusuario():
    try:
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        id_tipo_usuario = request.json['id_tipo_usuario']
        numero_identificacion = request.json['numero_identificacion']
        numero_telefono = request.json['numero_telefono']
        correo = request.json['correo']
        direccion = request.json['dirrecion']
        contraseña = request.json['contraseña']
        usuario = request.json['usuario']
        tipo_documento = request.json['tipo_documento']
        fecha_registro = request.json['fecha_registro']
        estado = request.json['estado']
        cur = mysql.connection.cursor()
        cur.execute("insert into usuario(nombre,apellido,id_tipo_usuario,numero_identificacion,numero_telefono,correo,direccion,contraseña,usuario,tipo_documento,fecha_registro,estado) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (nombre, apellido, id_tipo_usuario, numero_identificacion, numero_telefono, correo, direccion, contraseña, usuario, tipo_documento, fecha_registro, estado))
        mysql.connection.commit()
        return jsonify({"Informacion": "Registro exitoso!!"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/updateUsuario/<numero_identificacion>', methods=['PUT'])
def update_usuario(numero_identificacion):
    try:
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        id_tipo_usuario = request.json['id_tipo_usuario']
        numero_telefono = request.json['numero_telefono']
        correo = request.json['correo']
        direccion = request.json['direccion']
        contraseña = request.json['contraseña']
        tipo_documento = request.json['tipo_documento']
        fecha_registro = request.json['fecha_registro']
        estado = request.json['estado']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE usuario
            SET nombre = %s,
                apellido = %s,
                id_tipo_usuario = %s,
                numero_telefono = %s,
                correo = %s,
                direccion = %s,
                contraseña = %s,
                tipo_documento = %s,
                fecha_registro =%s,
                estado = %s
            WHERE numero_identificacion = %s
            """, (nombre, apellido, id_tipo_usuario, numero_telefono,
                  correo, direccion, contraseña, tipo_documento, fecha_registro, numero_identificacion,estado))
        mysql.connection.commit()
        return jsonify({"informacion": "Registro actualizado!"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/updateSolicitud/<id_solicitudes>', methods=['PUT'])
def updatesolicitud(id_solicitudes):
    try:
        id_tipo_prioridad = request.json['id_tipo_prioridad']
        id_estado_solicitud = request.json['id_estado_solicitud']
        cur = mysql.connection.cursor()
        cur.execute("""UPDATE solicitudes
            SET id_tipo_prioridad =%s,
                id_estado_solicitud = %s
            WHERE id_solicitudes=%s
                """, (id_tipo_prioridad, id_estado_solicitud, id_solicitudes))
        mysql.connection.commit()
        return jsonify({"Informacion": "Registro Actualizado"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/getAllUsuario', methods=['GET'])
def getAllUsuario():
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT usuario.nombre, usuario.apellido, tipo_usuario.tipo_usuario, usuario.numero_identificacion, usuario.numero_telefono, usuario.correo, usuario.direccion, usuario.contraseña, usuario.usuario, tipo_documento.descripcion FROM usuario, tipo_documento, tipo_usuario WHERE usuario.id_tipo_usuario=tipo_usuario.id_tipo_usuario and usuario.tipo_documento=tipo_documento.id_tipo_documento')
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'nombre': result[0], 'apellido': result[1], 'id_tipo_usuario': result[2],
                       'numero_identificacion': result[3], 'numero_telefono': result[4], 'correo': result[5],
                       'direccion': result[6], 'contraseña': result[7], 'usuario': result[8],
                       'tipo_documento': result[9]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/getUsuarioById/<numId>', methods=['GET'])
def getUsuarioById(numId):
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT usuario.nombre, usuario.apellido, tipo_usuario.tipo_usuario, usuario.numero_identificacion, usuario.numero_telefono, usuario.correo, usuario.direccion, usuario.contraseña, usuario.usuario, tipo_documento.descripcion FROM usuario, tipo_documento, tipo_usuario WHERE usuario.id_tipo_usuario=tipo_usuario.id_tipo_usuario and usuario.tipo_documento=tipo_documento.id_tipo_documento and usuario.numero_identificacion = %s', (numId,))
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'nombre': result[0], 'apellido': result[1], 'id_tipo_usuario': result[2],
                       'numero_identificacion': result[3], 'numero_telefono': result[4], 'correo': result[5],
                       'direccion': result[6], 'contraseña': result[7], 'usuario': result[8],
                       'tipo_documento': result[9]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/insertSolicitudes', methods=['POST'])
def insertsolicitudes():
    try:
        descripcion = request.json['descripcion']
        id_tipo_solicitud = request.json['id_tipo_solicitud']
        id_tipo_prioridad = request.json['id_tipo_prioridad']
        id_estado_solicitud = request.json['id_estado_solicitud']
        fecha = request.json['fecha']
        n_asesor = request.json['n_asesor']
        n_usuario = request.json['n_usuario']
        codigo = request.json['codigo']

        cur = mysql.connection.cursor()
        cur.execute("insert into solicitudes(descripcion,id_tipo_solicitud,id_tipo_prioridad,id_estado_solicitud,fecha,n_asesor,n_usuario,codigo) values (%s,%s,%s,%s,%s,%s,%s)",
                    (descripcion, id_tipo_solicitud, id_tipo_prioridad, id_estado_solicitud, fecha, n_asesor, n_usuario, codigo))
        mysql.connection.commit()
        return jsonify({"Informacion": "Registro exitoso!!"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/insertRespuesta', methods=['POST'])
def insertrespuesta():
    try:
        id_solicitudes = request.json['id_solicitudes']
        respuesta = request.json['respuesta']
        fecha = request.json['fecha']
        asesor = request.json['asesor']
        codigo_rad = request.json['codigo_rad']

        cur = mysql.connection.cursor()
        cur.execute("insert into respuesta(id_solicitudes,respuesta,fecha,asesor,codigo_rad) values (%s,%s,%s,%s)",
                    (id_solicitudes, respuesta, fecha, asesor, codigo_rad))
        mysql.connection.commit()
        return jsonify({"Informacion": "Registro exitoso!!"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/getAllSolicitudById/<Id>', methods=['GET'])
def getAllSolicitudById(Id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('select descripcion,id_tipo_solicitud,id_tipo_prioridad,id_estado_solicitud,fecha,n_asesor,n_usuario from solicitudes where id_solicitudes = %s', (Id,))
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'descripcion': result[0], 'id_tipo_solicitud': result[1], 'id_tipo_prioridad': result[2],
                       'id_estado_solicitud': result[3], 'fecha': result[4], 'n_asesor': result[5], 'n_usuario': result[6]}

            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/getAllSolicitud', methods=['GET'])
def getAllSolicitud():
    try:
        cur = mysql.connection.cursor()
        cur.execute(
            'select descripcion,id_tipo_solicitud,id_tipo_prioridad,id_estado_solicitud,fecha,n_asesor,n_usuario from solicitudes')
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'descripcion': result[0], 'id_tipo_solicitud': result[1], 'id_tipo_prioridad': result[2],
                       'id_estado_solicitud': result[3], 'fecha': result[4], 'n_asesor': result[5], 'n_usuario': result[6]}

            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/getAllRespuesta', methods=['GET'])
def getAllRespuesta():
    try:
        cur = mysql.connection.cursor()
        cur.execute(
            'select id_solicitudes,respuesta,fecha,asesor from respuesta')
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {
                'id_solicitudes': result[0], 'respuesta': result[1], 'fecha': result[2], 'asesor': result[3]}

            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/getAllRespuestaById/<Id>', methods=['GET'])
def getAllRespuestaById(Id):
    try:
        cur = mysql.connection.cursor()
        cur.execute(
            'SELECT id_solicitudes, respuesta, fecha, usuario.nombre from respuesta, usuario where asesor=usuario.id_usuario and id_solicitudes=%s', (Id))
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {
                'id_solicitudes': result[0], 'respuesta': result[1], 'fecha': result[2], 'asesor': result[3]}

            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/deleteUsuarioById/<Id>', methods=['DELETE'])
def DeleteUsuario(Id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('delete from usuario where numero_identificacion=%s', (Id,))
        mysql.connection.commit()
        return jsonify({"informacion": "Registro eliminado"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/insertTipoUsuario', methods=['POST'])
def insertTipoUsuario():
    try:
        tipo_usuario = request.json['tipo_usuario']

        cur = mysql.connection.cursor()
        cur.execute("insert into tipo_usuario (tipo_usuario) values (%s)",
                    (tipo_usuario,))
        mysql.connection.commit()
        return jsonify({"Informacion": "Registro exitoso!!"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/insertTipoDocumento', methods=['POST'])
def insertTipoDocumento():
    try:
        id_tipo_documento = request.json['id_tipo_documento']
        descripcion = request.json['descripcion']
        cur = mysql.connection.cursor()
        cur.execute("insert into tipo_documento (descripcion,id_tipo_documento) values (%s,%s)",
                    (descripcion, id_tipo_documento))
        mysql.connection.commit()
        return jsonify({"Informacion": "Registro exitoso!!"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/insertEstadoSolicitud', methods=['POST'])
def insertEstadoSolicitud():
    try:
        id_estado_solicitud = request.json['id_estado_solicitud']
        estado_solicitud = request.json['estado_solicitud']
        cur = mysql.connection.cursor()
        cur.execute("insert into estado_solicitud(id_estado_solicitud,estado_solicitud) values (%s,%s)",
                    (id_estado_solicitud, estado_solicitud))
        mysql.connection.commit()
        return jsonify({"Informacion": "Registro exitoso!!"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/insertTipoSolicitud', methods=['POST'])
def insertTipoSolicitud():
    try:
        id_tipo_solicitud = request.json['id_tipo_solicitud']
        tipo_solicitud = request.json['tipo_solicitud']
        cur = mysql.connection.cursor()
        cur.execute("INSERT into tipo_solicitud(id_tipo_solicitud,tipo_solicitud) VALUES (%s,%s)",
                    (id_tipo_solicitud, tipo_solicitud))
        mysql.connection.commit()
        return jsonify({"Informacion": "Registro exitoso!!"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/insertTipoPrioridad', methods=['POST'])
def insertTipoPrioridad():
    try:
        id_tipo_prioridad = request.json['id_tipo_prioridad']
        tipo_prioridad = request.json['tipo_prioridad']
        cur = mysql.connection.cursor()
        cur.execute("insert into tipo_prioridad (id_tipo_prioridad,tipo_prioridad) values (%s,%s)",
                    (id_tipo_prioridad, tipo_prioridad))
        mysql.connection.commit()
        return jsonify({"Informacion": "Registro exitoso!!"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/deleteTipoUsuarioById/<Id>', methods=['DELETE'])
def DeleteTipoUsuario(Id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('delete from tipo_usuario where id_tipo_usuario=%s', (Id,))
        mysql.connection.commit()
        return jsonify({"informacion": "Registro eliminado"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/deleteTipoDocumentoById/<Id>', methods=['DELETE'])
def deleteTipoDocumentoById(Id):
    try:
        cur = mysql.connection.cursor()
        cur.execute(
            'delete from tipo_documento where id_tipo_documento=%s', (Id,))
        mysql.connection.commit()
        return jsonify({"informacion": "Registro eliminado"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/deleteEstadoSolicitudById/<Id>', methods=['DELETE'])
def deleteEstadoSolicitudById(Id):
    try:
        cur = mysql.connection.cursor()
        cur.execute(
            'delete from estado_solicitud where id_estado_solicitud=%s', (Id,))
        mysql.connection.commit()
        return jsonify({"informacion": "Registro eliminado"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/deleteTipoSolicitudById/<Id>', methods=['DELETE'])
def deleteTipoSolicitudById(Id):
    try:
        cur = mysql.connection.cursor()
        cur.execute(
            'delete from tipo_solicitud where id_tipo_solicitud=%s', (Id,))
        mysql.connection.commit()
        return jsonify({"informacion": "Registro eliminado"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/deleteTipoPrioridadById/<Id>', methods=['DELETE'])
def deleteTipoPrioridadById(Id):
    try:
        cur = mysql.connection.cursor()
        cur.execute(
            'delete from tipo_prioridad where id_tipo_prioridad=%s', (Id,))
        mysql.connection.commit()
        return jsonify({"informacion": "Registro eliminado"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


if __name__ == "__main__":
    app.run(port=3000, debug=True)
