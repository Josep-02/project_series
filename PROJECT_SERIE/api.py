from flask import Flask, request
from flask_restful import Resource, Api
from models import get_all_personas, get_persona_by_id, create_persona, update_persona, delete_persona

class PersonaList(Resource):
    def get(self):
        personas = get_all_personas()
        return [dict(p) for p in personas]

    def post(self):
        data = request.get_json()
        nombre = data.get('nombre')
        apellido = data.get('apellido')
        edad = data.get('edad')
        if not all([nombre, apellido, edad]):
            return {'message': 'Faltan datos requeridos'}, 400
        persona_id = create_persona(nombre, apellido, edad)
        return {'id': persona_id, 'message': 'Persona creada exitosamente'}, 201

class Persona(Resource):
    def get(self, persona_id):
        persona = get_persona_by_id(persona_id)
        if persona:
            return dict(persona)
        return {'message': 'Persona no encontrada'}, 404

    def put(self, persona_id):
        data = request.get_json()
        nombre = data.get('nombre')
        apellido = data.get('apellido')
        edad = data.get('edad')
        if not all([nombre, apellido, edad]):
            return {'message': 'Faltan datos requeridos'}, 400
        update_persona(persona_id, nombre, apellido, edad)
        return {'message': 'Persona actualizada exitosamente'}

    def delete(self, persona_id):
        delete_persona(persona_id)
        return {'message': 'Persona eliminada exitosamente'}

def init_api(app):
    api = Api(app)
    api.add_resource(PersonaList, '/api/personas')
    api.add_resource(Persona, '/api/personas/<int:persona_id>')